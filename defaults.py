PLUGINS = [
    'rbac',
    'manage',
    'insights',
    'orchestration',
    'auth',
    'pricing'
]

UGLY_RBAC = """window.rbac={properties:{},checkPerm:function(t,o,n,e,r){e=e||this.model&&this.model.org,r=r||this.model&&this.model.user,t=t||"";if(console.log("check perm plugin"),e){if(e.is_owner)return!0;console.log("check perm",t,o,n);var s,i,c,l,a=this,d=[];if(o&&n&&(s=!1,"location"!=o&&"zone"!=o?this.model[o+"s"]&&this.model[o+"s"][n]&&(s=this.model[o+"s"][n].owned_by==r.id):"zone"==o?(this.model.zones&&(i=Object.values(this.model.zones).find(function(e){return e.records&&e.records[n]})),i&&(s=i.owned_by==r.id)):"location"==o&&(this.model.clouds&&(c=Object.values(this.model.clouds).find(function(e){return e.locations&&e.locations[n]})),c&&(s=c.owned_by==r.id)),s&&(e.owner_policy?(O="ALLOW"==e.owner_policy.operator,e.owner_policy.rules&&(l=e.owner_policy.rules.filter(function(e){return!(e.rtype!=o&&e.rtype||e.action!=t&&e.action||e.rid!=n&&e.rid)})).length&&(O=f="ALLOW"==(p=l[0]).operator,f&&(0<Object.keys(p.rtags).length&&(g={tags:p.rtags},p.constraints&&(g.constraints=p.constraints),O=g),0<Object.keys(p.constraints).length&&(O=p.constraints))),d.push(O)):d.push(!0))),!d.length)for(var u=Object.values(this.model.teams).filter(function(e){return a.isMember(r.id,e)}),h=0;h<u.length;h++){var p,f,g,m=u[h],y=[],b=[];(y=m.policy.rules).length?(b=y.filter(function(e){return!(e.rtype!=o&&e.rtype||e.action!=t&&e.action||e.rid!=n&&e.rid)})).length?(b=f="ALLOW"==(p=b[0]).operator,f&&(0<Object.keys(p.rtags).length&&(g={tags:p.rtags},p.constraints&&(g.constraints=p.constraints),b=g),0<Object.keys(p.constraints).length&&(b=p.constraints)),d.push(b)):d.push("ALLOW"==m.policy.operator):d.push("ALLOW"==m.policy.operator)}var O=d.findIndex(function(e){return 0!=e});return-1<O&&d[O]}return console.warn("no org found"),!1},isMember:function(e,t){return-1<t.members.indexOf(e)}};"""

