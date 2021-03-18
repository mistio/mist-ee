"""
Default configuration options for Avvan
"""
PORTAL_NAME = "Avvan"
EMAIL_LOGO = "static/CTI-logo2.png"
THEME = "computrade"
EMAIL_FROM = "Avvan <cmp@avvan.id>"
EMAIL_ALERTS = "alert@avvan.id"
EMAIL_INFO = "info@avvan.id"
EMAIL_SALES = "sales@avvan.id"
EMAIL_SUPPORT = "support@avvan.id"
EMAIL_NOTIFICATIONS = "notifications@avvan.id"
#CURRENCY = {
#    "sign": "Rp",
#    "rate": 13720.5
#}
ENABLE_MONITORING = True
DOCS_URI = SUPPORT_URI = ''

PLUGINS = [
    'rbac',
    'manage',
    'insights',
    'orchestration',
    'auth',
    'pricing'
]

EC2_SECURITYGROUP = {
    'name': 'avvan',
    'description': 'Security group created by Avvan'
}


CONFIRMATION_EMAIL_SUBJECT = "[Avvan] Confirm your registration"

CONFIRMATION_EMAIL_BODY = \
"""Hi %s,

we received a registration request to Avvan from this email address.

To activate your account, please click on the following link:

%s/confirm?key=%s

This request originated from the IP address %s. If it wasn't you, simply ignore
this message.

Best regards,
The Avvan team

--
%s
"""


RESET_PASSWORD_EMAIL_SUBJECT = "[Avvan] Password reset request"

RESET_PASSWORD_EMAIL_BODY = \
"""Hi %s,

We have received a request to change your password.
Please click on the following link:

%s/reset-password?key=%s

This request originated from the IP address %s. If it wasn't you, simply ignore
this message. Your password has not been changed.


Best regards,
The Avvan team

--
%s
"""


WHITELIST_IP_EMAIL_SUBJECT = "[Avvan] Account IP whitelist request"

WHITELIST_IP_EMAIL_BODY = \
"""Hi %s,

We have received a request to whitelist the IP you just tried to login with.
Please click on the following link to finish this action:

%s/confirm-whitelist?key=%s

This request originated from the IP address %s. If it wasn't you, simply ignore
this message. The above IP will not be whitelisted.


Best regards,
The Avvan team

--
%s
Govern the clouds
"""


FAILED_LOGIN_ATTEMPTS_EMAIL_SUBJECT = "[Avvan] Failed login attempts warning"


ORG_NOTIFICATION_EMAIL_SUBJECT = "[Avvan] Subscribed to team"

USER_NOTIFY_ORG_TEAM_ADDITION = \
"""Hi

You have been added to the team "%s" of organization %s.

Best regards,
The Avvan team

--
%s
"""

USER_CONFIRM_ORG_INVITATION_EMAIL_BODY = \
"""Hi

You have been invited by %s to join the %s organization
as a member of the %s.

To confirm your invitation, please click on the following link:

%s/confirm-invitation?invitoken=%s

Once you are done with the confirmation process,
you will be able to login to your Avvan user account
as a member of the team%s.

Best regards,
The Avvan team

--
%s
"""

ORG_INVITATION_EMAIL_SUBJECT = "[Avvan] Confirm your invitation"

REGISTRATION_AND_ORG_INVITATION_EMAIL_BODY = \
"""Hi

You have been invited by %s to join the %s organization
as a member of the %s.

Before joining the team you must also activate your account in  Avvan and set
a password. To activate your account and join the team, please click on the
following link:

%s/confirm?key=%s&invitoken=%s

Once you are done with the registration process,
you will be able to login to your Avvan user account
as a member of the team%s.

Best regards,
The Avvan team

--
%s
"""

NOTIFY_REMOVED_FROM_TEAM = \
"""Hi

You have been removed from team %s of organization %s by the
administrator %s.

Best regards,
The Avvan team

--
%s
"""

NOTIFY_REMOVED_FROM_ORG = \
"""Hi

You are no longer a member of the organization %s.

Best regards,
The Avvan team

--
%s
"""

NOTIFY_INVITATION_REVOKED_SUBJECT = "Invitation for organization revoked"

NOTIFY_INVITATION_REVOKED = \
"""Hi

Your invitation to the organization %s has been revoked.

Best regards,
The Avvan team

--
%s
"""

UGLY_RBAC = """window.rbac={checkPerm:function(e,t,r,o,n){if(!e)return console.error("checkPerm: no resource type defined"),!1;"s"===e.charAt(e.length-1)&&(e=e.slice(0,-1));const s=document.querySelector("mist-app").model;o=o||s&&s.org,n=n||s&&s.user;const i={rename:"edit",tag:"edit_tags",shell:"open_shell"};if(i[t=t.replace(/ /g,"_")]&&(t=i[t]),!o)return console.warn("no org found"),!1;const c={tags:{},constraints:{}},l=Object.values(s.teams).filter((e=>this.isMember(n.id,e)));if("*"===r){const r=this.getAllMatchingRules(e,t,l);for(const e of r){if("DENY"===e.operator&&""===e.rid&&0===Object.keys(e.rtags).length)return!1;if("ALLOW"===e.operator)return!0}}if(o.is_owner)return c;let a={},f={};if(r&&null!=r&&""!==r){let i=!1;if("location"!=e&&"zone"!=e)s[e+"s"]&&s[e+"s"][r]&&(i=s[e+"s"][r].owned_by===n.id);else if("zone"==e){let e;s.zones&&(e=Object.values(s.zones).find((e=>e.records&&e.records[r]))),e&&(i=e.owned_by==n.id)}else if("location"==e){let e;s.clouds&&(e=Object.values(s.clouds).find((e=>e.locations&&e.locations[r]))),e&&(i=e.owned_by==n.id)}if(o.ownership_enabled&&i){if(o.owner_policy){if(ownerRules=o.owner_policy.rules.filter((o=>!(o.rtype!==e&&""!==o.rtype||o.action!==t&&""!==o.action||o.rid!==r&&""!==o.rid))),ownerRules.length>0){let e=ownerRules.find((e=>{e.rid}));return e=null!=e?e:ownerRules[0],"ALLOW"!==e.operator?!1:(c.tags=e.rtags,c.constraints=e.constraints,c)}return"ALLOW"===o.owner_policy.operator&&c}return c}s[e+"s"]&&s[e+"s"][r]&&s[e+"s"][r].tags&&(a=s[e+"s"][r].tags)}else{const r=this.getMatchingTagsCstr(e,t,l);if(!1===r)return!1;[a,f]=r}let u=!1;for(const o of l){"ALLOW"===o.policy.operator&&(u=!0);for(const n of o.policy.rules)if((""===n.rtype||n.rtype===e)&&!(""!==n.action&&n.action!==t||""!==n.rid&&n.rid!==r)){if(Object.keys(n.rtags).length>0){if(0===Object.keys(a).length)continue;let e=!0;for(const t of Object.keys(n.rtags)){if(void 0===a[t]){e=!1;break}if((null!==n.rtags[t]&&""!==n.rtags[t]||null!==a[t]&&""!==a[t])&&n.rtags[t]!==a[t]){e=!1;break}}if(!1===e)continue}"ALLOW"===n.operator&&0===Object.keys(f).length&&(f=n.constraints),u="ALLOW"===n.operator;break}}return!!u&&{tags:a,constraints:f}},getMatchingTagsCstr:(e,t,r)=>{for(const o of r){const r=o.policy.rules.filter((r=>(""===r.rtype||r.rtype===e)&&((""===r.action||r.action===t)&&"ALLOW"===r.operator)));if(r.length>0)return[r[0].rtags,r[0].constraints];if("ALLOW"===o.policy.operator)return[{},{}]}return!1},getAllMatchingRules:(e,t,r)=>{const o=[];for(const n of r){const r=n.policy.rules.filter((r=>(""===r.rtype||r.rtype===e)&&(""===r.action||r.action===t)));o.push(...r)}return o},isMember:function(e,t){return t.members.indexOf(e)>-1}};"""



