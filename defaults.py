PLUGINS = [
    'rbac',
    'manage',
    'insights',
    'orchestration',
    'auth',
    'pricing'
]
UGLY_RBAC = """window.rbac={checkPerm:function(t,n,r,e,o){var s=document.querySelector("mist-app").model,e=e||s&&s.org,o=o||s&&s.user,i={rename:"edit",tag:"edit_tags",shell:"open_shell"};if(i[t=t||""]&&(t=i[t]),"s"===n.charAt(n.length-1)&&(n=n.slice(0,-1)),e){if(e.is_owner)return!0;console.log("check perm",t,n,r);var c,a,l,u=this,d=[];if(n&&r&&(i=!1,"location"!=n&&"zone"!=n?s[n+"s"]&&s[n+"s"][r]&&(i=s[n+"s"][r].owned_by==o.id):"zone"==n?(s.zones&&(c=Object.values(s.zones).find(function(e){return e.records&&e.records[r]})),c&&(i=c.owned_by==o.id)):"location"==n&&(s.clouds&&(a=Object.values(s.clouds).find(function(e){return e.locations&&e.locations[r]})),a&&(i=a.owned_by==o.id)),i&&(e.owner_policy?(i="ALLOW"==e.owner_policy.operator,e.owner_policy.rules&&(l=e.owner_policy.rules.filter(function(e){return!(e.rtype!=n&&e.rtype||e.action!=t&&e.action||e.rid!=r&&e.rid)})).length&&(i=f="ALLOW"==(h=l[0]).operator,f&&(0<Object.keys(h.rtags).length&&(y={tags:h.rtags},h.constraints&&(y.constraints=h.constraints),i=y),0<Object.keys(h.constraints).length&&(i=h.constraints))),d.push(i)):d.push(!0))),!d.length)for(var p=Object.values(s.teams).filter(function(e){return u.isMember(o.id,e)}),g=0;g<p.length;g++){var h,f,y,b=p[g],O=[],m=[];(O=b.policy.rules).length?(m=O.filter(function(e){return!(e.rtype!=n&&e.rtype||e.action!=t&&e.action&&""!==t||e.rid!=r&&e.rid&&r)})).length?(m=f="ALLOW"==(h=m[0]).operator,f&&(0<Object.keys(h.rtags).length&&(y={tags:h.rtags},h.constraints&&(y.constraints=h.constraints),m=y),0<Object.keys(h.constraints).length&&(m=h.constraints)),d.push(m)):d.push("ALLOW"==b.policy.operator):d.push("ALLOW"==b.policy.operator)}s=d.findIndex(function(e){return 0!=e});return-1<s&&d[s]}return console.warn("no org found"),!1},isMember:function(e,t){return-1<t.members.indexOf(e)}};"""


