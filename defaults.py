PLUGINS = [
    'rbac',
    'manage',
    'insights',
    'orchestration',
    'auth',
    'pricing'
]

UGLY_RBAC = """window.rbac={checkPerm:function(e,o,n,t,r){t=t||this.model&&this.model.org,r=r||this.model&&this.model.user,e=e||"";if(console.log("check perm plugin"),t){if(t.is_owner)return!0;console.log("check perm",e,o,n);var s,i,c,l,a=this,d=[];if(o&&n&&(s=!1,"location"!=o&&"zone"!=o?this.model[o+"s"]&&this.model[o+"s"][n]&&(s=this.model[o+"s"][n].owned_by==r.id):"zone"==o?(this.model.zones&&(i=Object.values(this.model.zones).find(function(t){return t.records&&t.records[n]})),i&&(s=i.owned_by==r.id)):"location"==o&&(this.model.clouds&&(c=Object.values(this.model.clouds).find(function(t){return t.locations&&t.locations[n]})),c&&(s=c.owned_by==r.id)),s&&(t.owner_policy?(O="ALLOW"==t.owner_policy.operator,t.owner_policy.rules&&(l=t.owner_policy.rules.filter(function(t){return!(t.rtype!=o&&t.rtype||t.action!=e&&t.action||t.rid!=n&&t.rid)})).length&&(O=f="ALLOW"==(p=l[0]).operator,f&&(0<Object.keys(p.rtags).length&&(g={tags:p.rtags},p.constraints&&(g.constraints=p.constraints),O=g),0<Object.keys(p.constraints).length&&(O=p.constraints))),d.push(O)):d.push(!0))),!d.length)for(var u=Object.values(this.model.teams).filter(function(t){return a.isMember(r.id,t)}),h=0;h<u.length;h++){var p,f,g,m=u[h],y=[],b=[];(y=m.policy.rules).length?(b=y.filter(function(t){return!(t.rtype!=o&&t.rtype||t.action!=e&&t.action&&""!==e||t.rid!=n&&t.rid&&n)})).length?(b=f="ALLOW"==(p=b[0]).operator,f&&(0<Object.keys(p.rtags).length&&(g={tags:p.rtags},p.constraints&&(g.constraints=p.constraints),b=g),0<Object.keys(p.constraints).length&&(b=p.constraints)),d.push(b)):d.push("ALLOW"==m.policy.operator):d.push("ALLOW"==m.policy.operator)}var O=d.findIndex(function(t){return 0!=t});return-1<O&&d[O]}return console.warn("no org found"),!1},isMember:function(t,e){return-1<e.members.indexOf(t)}};"""

