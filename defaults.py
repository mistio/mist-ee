PLUGINS = [
    'rbac',
    'manage',
    'insights',
    'orchestration',
    'auth',
    'pricing'
]

UGLY_RBAC = """window.rbac = {
    checkPerm: function (rtype, action, rid, org, user) {
        // rtype is required
        if (!rtype) {
            console.error('checkPerm: no resource type defined');
            return false;
        }// Singularize if necessary
        if (rtype.charAt(rtype.length - 1) === 's') {
            rtype = rtype.slice(0, -1);
        }
        const model = document.querySelector('mist-app').model
        org = org || (model && model.org);
        user = user || (model && model.user);
        action = action.replace(/ /g, "_");
        const actionsMap = {
            "rename": "edit",
            "tag": "edit_tags",
            "shell": "open_shell"
        };
        if (actionsMap[action]) action = actionsMap[action];

        if (!org) {
            console.warn('no org found');
            return false;
        }
        const returnValue = {tags:{}, constraints:{}};
        const teamsMemberIsIn = Object.values(model.teams).filter( t => {
            return this.isMember(user.id, t);
        });
        // The user wants to know if there is any allowing rule
        if (rid === "*") {
            const matchingRules = this.getAllMatchingRules(rtype, action, teamsMemberIsIn);
            // Ignore DENY rules if they have rid or rtags
            // Return operator of the any other first rule
            for (const rule of matchingRules){
                if (rule.operator === 'DENY' && rule.rid === "" && Object.keys(rule.rtags).length === 0)
                    return false;  // encountered a general rule first with DENY
                if (rule.operator === 'ALLOW') return true;
            }
        }
        if(this.isOwner(user, teamsMemberIsIn)) return returnValue;
        // fetch rtags
        let rtags = {};
        let constraints = {};
        // first in the case an rid is given
        if (rid && rid != null && rid !== ""){
            let ownedBy = false;
            if (rtype != 'location' && rtype != 'zone') {
                // get resource and check ownership
                if (model[rtype + 's'] && model[rtype + 's'][rid]) {
                    ownedBy = model[rtype + 's'][rid].owned_by === user.id;
                }
            } else if (rtype == 'zone') {
                // policy may apply to record, found only in model.zones.XXX.records
                let zoneOfRecord;
                if (model.zones)
                    zoneOfRecord = Object.values(model.zones).find((z) => {
                        return z.records && z.records[rid]
                    });
                if (zoneOfRecord) {
                    ownedBy = zoneOfRecord.owned_by == user.id;
                }
            } else if (rtype == 'location') {
                // policy may apply to locations, found only in model.clouds.XXX.locations
                // locations inherit ownership from their cloud.
                let locationCloud;
                if (model.clouds) {
                    locationCloud = Object.values(model.clouds).find((c) => {
                        return c.locations && c.locations[rid]
                    });
                }
                if (locationCloud) {
                    ownedBy = locationCloud.owned_by == user.id;
                }
            }
            // user owns the resource and has full access on it return immediately
            if(org.ownership_enabled && ownedBy){
                // Evaluate the default org policy for resource owners before returning
                if (org.owner_policy) {
                    ownerRules = org.owner_policy.rules.filter((rule) => {
                        return (rule.rtype === rtype || rule.rtype === "") &&
                               (rule.action === action || rule.action === "") &&
                               (rule.rid === rid || rule.rid === "");
                    });

                    // Relevant rule, one mathing rid ideally otherwise first matching
                    let rule = ownerRules.find(r => {r.rid === rid;});
                    rule = rule != null ? rule : ownerRules[0];
                    // if rule.operator is DENY return False
                    if(rule.operator !== "ALLOW") return false;
                    // if rule.operator is ALLOW return tags and constraints
                    returnValue.tags = rule.rtags;
                    returnValue.constraints = rule.constraints
                    return returnValue;
                }
                return returnValue;
            }
            // user is not owner or ownership is disabled, continue with getting tags
            if (model[rtype + 's'] && model[rtype + 's'][rid].tags) {
                rtags = model[rtype + 's'][rid].tags;
            }

        } else {
            const firstMatchingTagsConstraints = this.getMatchingTagsCstr(rtype, action, teamsMemberIsIn);
            if (firstMatchingTagsConstraints === false) return false;
            [rtags, constraints] = firstMatchingTagsConstraints;
        }
        let foundAllowing = false;
        // check if there is an allowing rule
        for(const team of teamsMemberIsIn) {
            // if no matching rule keep default operator
            if (team.policy.operator === 'ALLOW'){
                foundAllowing = true;
            }
            for(const rule of team.policy.rules){
                if(rule.rtype !== "" && rule.rtype !== rtype) continue;
                if(rule.action !== "" && rule.action !== action) continue;
                if(rule.rid !== "" && rule.rid !== rid) continue;
                if(Object.keys(rule.rtags).length > 0) {
                    if(Object.keys(rtags).length === 0) continue;
                    let rtagsMatch = true;
                    for(const key of Object.keys(rule.rtags)){
                        if(rtags[key] === undefined) {
                            rtagsMatch = false;
                            break;
                        }
                        if((rule.rtags[key] !== null && rule.rtags[key] !== "") || (rtags[key] !== null && rtags[key] !== "")){
                            if(rule.rtags[key] !== rtags[key]){
                                rtagsMatch = false;
                                break;
                            }
                        }
                    }
                    if(rtagsMatch === false) continue;
                }
                // rule is a match
                if (rule.operator === 'ALLOW'){
                    if (Object.keys(constraints).length === 0) constraints = rule.constraints;
                }
                foundAllowing = rule.operator === 'ALLOW';
                break;
            }
        }
        if (foundAllowing){
            return {tags: rtags, constraints: constraints}
        }
        return false;
    },

    getMatchingTagsCstr: (rtype, action, teamsMemberIsIn) => {
        // Like in api this will search for the first ALLOWing rule
        // that matches the given input and return the tags.
        // This will also return the constraints with that rule (unlike api)
        // If there is no rule, either an Array with 2 empty objects or False
        // will be returned, depending on default operator.
        // Return type Array [tags, constraints] or False

        for (const team of teamsMemberIsIn){
            const matches = team.policy.rules.filter(rule => {
                if (rule.rtype !== "" && rule.rtype !== rtype) return false;
                if (rule.action !== "" && rule.action !== action) return false;
                return rule.operator === 'ALLOW';
            });
            if (matches.length > 0) {
                return [matches[0].rtags, matches[0].constraints];
            }
            // no matches in this team but maybe has allowing operator
            if (team.policy.operator === "ALLOW") return [{}, {}];
        }
        // nothing allowing found..
        return false

    },
    getAllMatchingRules: (rtype, action, teamsMemberIsIn) => {
        const matchingRules = []
        for (const team of teamsMemberIsIn){
            const matches = team.policy.rules.filter(rule => {
                if (rule.rtype !== "" && rule.rtype !== rtype) return false;
                if (rule.action !== "" && rule.action !== action) return false;
                return true;
            });
            matchingRules.push(...matches);
        }
        return matchingRules;
    },
    isMember: function (userId, team) {
        return team.members.indexOf(userId) > -1;
    },
    isOwner: (user, teams) => {
        for(const team of teams){
            if (team.name === "Owners"){
                if (team.members.indexOf(user.id) > -1) return true;
            }
        }
        return false;
    },
};
"""



