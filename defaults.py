PLUGINS = [
    'rbac',
    'manage',
    'insights',
    'orchestration',
    'auth',
    'pricing'
]
UGLY_RBAC = """window.rbac={actionsMap:{rename:"edit",tag:"edit_tags",shell:"open_shell"},checkPerm:function(n,e,r,t,o){var s=document.querySelector("mist-app").model,t=t||s&&s.org,o=o||s&&s.user,n=n||"";if(this.actionsMap(n)&&(n=actionsMap(n)),"s"===e.charAt(e.length-1)&&(e=e.slice(0,-1)),t){if(t.is_owner)return!0;console.log("check perm",n,e,r);var i,c,a,l,u=this,p=[];if(e&&r&&(l=!1,"location"!=e&&"zone"!=e?s[e+"s"]&&s[e+"s"][r]&&(l=s[e+"s"][r].owned_by==o.id):"zone"==e?(s.zones&&(i=Object.values(s.zones).find(function(t){return t.records&&t.records[r]})),i&&(l=i.owned_by==o.id)):"location"==e&&(s.clouds&&(c=Object.values(s.clouds).find(function(t){return t.locations&&t.locations[r]})),c&&(l=c.owned_by==o.id)),l&&(t.owner_policy?(l="ALLOW"==t.owner_policy.operator,t.owner_policy.rules&&(a=t.owner_policy.rules.filter(function(t){return!(t.rtype!=e&&t.rtype||t.action!=n&&t.action||t.rid!=r&&t.rid)})).length&&(l=f="ALLOW"==(g=a[0]).operator,f&&(0<Object.keys(g.rtags).length&&(y={tags:g.rtags},g.constraints&&(y.constraints=g.constraints),l=y),0<Object.keys(g.constraints).length&&(l=g.constraints))),p.push(l)):p.push(!0))),!p.length)for(var d=Object.values(s.teams).filter(function(t){return u.isMember(o.id,t)}),h=0;h<d.length;h++){var g,f,y,b=d[h],O=[],m=[];(O=b.policy.rules).length?(m=O.filter(function(t){return!(t.rtype!=e&&t.rtype||t.action!=n&&t.action&&""!==n||t.rid!=r&&t.rid&&r)})).length?(m=f="ALLOW"==(g=m[0]).operator,f&&(0<Object.keys(g.rtags).length&&(y={tags:g.rtags},g.constraints&&(y.constraints=g.constraints),m=y),0<Object.keys(g.constraints).length&&(m=g.constraints)),p.push(m)):p.push("ALLOW"==b.policy.operator):p.push("ALLOW"==b.policy.operator)}s=p.findIndex(function(t){return 0!=t});return-1<s&&p[s]}return console.warn("no org found"),!1},isMember:function(t,n){return-1<n.members.indexOf(t)}};"""


