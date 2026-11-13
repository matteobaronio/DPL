# Section kit for inner pages — DPL brand (Zodiak/Switzer, navy/azzurro, osmo easing), clarity of Maisa/Stripe sections.
import html as H

ICONS = {  # DPL icon set (Figma «Iconografia» 400:74), drawn from the brand circles
 'persona': '<svg viewBox="0 0 314 377"><path d="M304.317 376.863C310.45 360.074 313.797 341.943 313.797 323.031C313.797 236.379 243.551 166.133 156.898 166.133C70.2458 166.133 0 236.379 0 323.031C0 341.943 3.34608 360.074 9.47852 376.863C31.4441 316.726 89.1579 273.797 156.898 273.797C224.639 273.797 282.352 316.726 304.317 376.863Z"/><circle cx="156.898" cy="70.8825" r="70.8825"/></svg>',
 'ascolto': '<svg viewBox="0 0 314 377"><path d="M209.184 175.056C270.13 196.59 313.797 254.711 313.797 323.031C313.797 341.943 310.45 360.074 304.317 376.863C282.352 316.726 224.639 273.797 156.898 273.797C89.1579 273.797 31.4441 316.726 9.47852 376.863C3.34608 360.074 0 341.943 0 323.031C0 254.712 43.6658 196.591 104.611 175.056C117.57 189.207 136.198 198.081 156.898 198.081C177.599 198.081 196.225 189.206 209.184 175.056Z"/><circle cx="156.898" cy="70.8825" r="70.8825"/></svg>',
 'accoglienza': '<svg viewBox="0 0 251 323"><path d="M199.77 97.2529C230.322 120.053 250.104 156.485 250.104 197.538C250.104 266.603 194.117 322.591 125.053 322.591C55.9882 322.591 0 266.603 0 197.538C0 156.485 19.7823 120.053 50.334 97.2529C59.1268 130.29 89.247 154.63 125.053 154.63C160.858 154.63 190.978 130.29 199.77 97.2529ZM125.053 0C167.752 0 202.367 34.6157 202.367 77.3154C202.367 84.2093 201.463 90.8921 199.77 97.2529C178.924 81.6961 153.064 72.4854 125.053 72.4853C97.0411 72.4853 71.1804 81.6959 50.334 97.2529C48.641 90.8922 47.7373 84.2093 47.7373 77.3154C47.7373 34.6156 82.3529 0 125.053 0Z"/></svg>',
 'ricerca': '<svg viewBox="0 0 309 310"><path d="M45.8084 301.633C35.3291 312.112 18.3387 312.112 7.85942 301.633C-2.61973 291.153 -2.61983 274.163 7.85942 263.684L101.49 170.053C106.032 177.501 111.523 184.534 117.964 190.975C124.604 197.615 131.873 203.244 139.576 207.865L45.8084 301.633ZM276.173 32.7664C319.861 76.4546 319.861 147.286 276.173 190.975C239.125 228.023 182.558 233.652 139.576 207.865L184.404 163.037C194.883 152.558 194.883 135.567 184.404 125.088C173.925 114.609 156.934 114.609 146.455 125.088L101.49 170.053C75.2274 126.988 80.7177 70.0124 117.964 32.7657C161.653 -10.9223 232.485 -10.9218 276.173 32.7664Z"/></svg>',
 'gruppo': '<svg viewBox="0 0 335 313"><path d="M96.9355 103.1C107.925 131.309 135.353 151.299 167.45 151.299C199.546 151.299 226.972 131.309 237.962 103.101C295.208 129.716 334.899 187.734 334.899 255.022C334.899 275.206 331.327 294.556 324.782 312.474C301.34 248.293 239.745 202.476 167.449 202.476C95.1534 202.476 33.5588 248.292 10.1162 312.474C3.57162 294.556 0 275.206 0 255.022C0 187.734 39.6896 129.715 96.9355 103.1ZM167.45 0C209.23 0 243.099 33.8697 243.099 75.6494C243.099 85.3327 241.277 94.5903 237.962 103.101C216.531 93.1368 192.64 87.5733 167.449 87.5732C142.258 87.5733 118.367 93.1357 96.9355 103.1C93.6203 94.5898 91.8008 85.3322 91.8008 75.6494C91.8008 33.8695 125.67 0 167.45 0Z"/></svg>',
 'dialogo': '<svg viewBox="0 0 251 401"><path d="M224.956 200.269C240.743 221.202 250.104 247.253 250.104 275.492C250.104 344.557 194.117 400.545 125.053 400.545C55.9882 400.545 0 344.557 0 275.492C0 247.254 9.36115 221.203 25.1475 200.27C47.9703 230.534 84.2257 250.099 125.052 250.1C165.878 250.1 202.133 230.534 224.956 200.269ZM125.052 0C194.115 0 250.102 55.9867 250.103 125.05C250.103 153.287 240.741 179.336 224.956 200.269C202.133 170.005 165.878 150.44 125.053 150.439C84.2265 150.439 47.9709 170.005 25.1475 200.27C9.36229 179.337 0.00195074 153.287 0.00195312 125.05C0.00205888 55.9868 55.9888 0 125.052 0Z"/></svg>',
}
DL = '<svg class="dl" viewBox="0 0 16 16" fill="none" aria-hidden="true"><path d="M8 2.5v8m-3.5-3.5L8 10.5l3.5-3.5M3 13.5h10" stroke="currentColor" stroke-width="1.4" stroke-linecap="round" stroke-linejoin="round"/></svg>'
UR = '<svg class="ur" viewBox="0 0 16 16" fill="none" aria-hidden="true"><path d="M5 11l6-6m-5 0h5v5" stroke="currentColor" stroke-width="1.4" stroke-linecap="round" stroke-linejoin="round"/></svg>'
SEARCH = '<svg viewBox="0 0 20 20" fill="none" aria-hidden="true"><circle cx="9" cy="9" r="6" stroke="currentColor" stroke-width="1.5"/><path d="M13.5 13.5L17 17" stroke="currentColor" stroke-width="1.5" stroke-linecap="round"/></svg>'

CSS = r'''
/* ================= KIT · inner pages ================= */
.px-hero{height:auto;background:var(--navy-deep)}
.px-hero .in{min-height:U(700);display:flex;flex-direction:column;padding:U(196) U(40) U(64);box-sizing:border-box}
.px-hero .rings{height:U(700)}
.px-hero h1{position:relative;margin:0 0 U(40);width:U(1060);font:400 U(88)/U(82) var(--serif);letter-spacing:U(-3.4);text-transform:uppercase;z-index:2}
.px-hero h1 .a{display:block;color:var(--title-light)}.px-hero h1 .b{display:block;color:var(--azzurro)}
.px-hero .rule{position:relative;flex-shrink:0;margin-top:auto;height:1px;background:rgba(255,255,255,.12);z-index:2}
.px-hero .foot-row{position:relative;min-height:U(167);padding-top:U(32);box-sizing:border-box;display:flex;justify-content:space-between;align-items:flex-end;gap:U(40);z-index:2}
.px-hero .facts{display:flex;flex-wrap:wrap;gap:U(12) U(28);max-width:U(700);font:500 U(14)/U(20) var(--sans);letter-spacing:U(.84);text-transform:uppercase;color:var(--azzurro)}
.px-hero .facts span{display:flex;align-items:center;gap:U(28)}
.px-hero .facts span+span::before{content:"";width:U(4);height:U(4);border-radius:50%;background:var(--azzurro);opacity:.6}
.px-hero .intro{width:U(447);display:flex;flex-direction:column;align-items:flex-start;gap:U(26)}
.px-hero .intro p{margin:0;font:400 U(18)/U(27) var(--sans);color:var(--title-light)}
.px-hero .btns{display:flex;gap:U(12);flex-wrap:wrap}
.px-sec{background:#fff;padding:U(120) 0}
.px-sec.tint{background:#F3F5FC}
.px-sec.flush{padding-top:0}
.px-sec .in{height:auto;padding:0 U(40);box-sizing:border-box}
.px-body{margin-top:U(64)}
/* photo band with parallax */
.px-band{position:relative;height:U(600);overflow:hidden;background:#F3F5FC}
.px-band img{position:absolute;left:0;top:-10%;width:100%;height:120%;object-fit:cover;will-change:transform}
/* feature rows (text + live visual) */
.feat{display:grid;grid-template-columns:1fr 1fr;gap:U(80);align-items:center}
.feat+.feat{margin-top:U(96)}
.feat.rev .ft{order:2}
.feat .ft h3{margin:0;font:400 U(34)/U(40) var(--sans);letter-spacing:U(-.6);color:var(--navy)}
.feat .ft p{margin:U(18) 0 0;font:400 U(17)/U(26) var(--sans);color:rgba(25,35,75,.75);max-width:U(520)}
.feat .ft ul{list-style:none;margin:U(28) 0 0;padding:0;border-top:1px solid rgba(25,35,75,.12);max-width:U(560)}
.feat .ft li{display:flex;gap:U(14);padding:U(14) 0;border-bottom:1px solid rgba(25,35,75,.12);font:400 U(16)/U(24) var(--sans);color:var(--navy)}
.feat .ft li::before{content:"";flex:none;margin-top:U(9);width:U(6);height:U(6);border-radius:50%;background:var(--azzurro);box-shadow:0 0 0 U(3) rgba(186,199,249,.35)}
.vis{position:relative;height:U(520);overflow:hidden;background:var(--navy-deep);isolation:isolate}
.vis.light{background:#F3F5FC}
.vis .glow{position:absolute;inset:-20%;background:radial-gradient(closest-side at 70% 30%,rgba(186,199,249,.22),transparent 70%),radial-gradient(closest-side at 20% 80%,rgba(186,199,249,.12),transparent 70%);animation:drift 22s var(--osmo) infinite alternate;z-index:-1}
/* icon cards */
.icards{display:grid;grid-template-columns:repeat(var(--cols,3),minmax(0,1fr));gap:U(16)}
.icard{background:#F3F5FC;padding:U(32) U(28);min-height:U(260);box-sizing:border-box;display:flex;flex-direction:column;transition:background-color .5s var(--osmo)}
.px-sec.tint .icard{background:#fff}
.icard:hover{background:#EBEFFB}
.icard .ic{width:U(40);height:U(48)}
.icard .ic svg{width:100%;height:100%;fill:var(--azzurro);display:block}
.icard h3{margin:auto 0 0;padding-top:U(40);font:400 U(22)/U(28) var(--sans);color:var(--navy)}
.icard p{margin:U(10) 0 0;font:400 U(16)/U(24) var(--sans);color:rgba(25,35,75,.7)}
/* steps */
.steps-x{display:grid;grid-template-columns:repeat(var(--cols,4),1fr);gap:U(16);counter-reset:s}
.sx{border-top:1px solid var(--navy);padding-top:U(20)}
.sx .n{font:400 U(40)/1 var(--serif);letter-spacing:U(-2);color:var(--navy)}
.sx h3{margin:U(28) 0 0;font:400 U(22)/U(28) var(--sans);color:var(--navy)}
.sx p{margin:U(10) 0 0;font:400 U(16)/U(24) var(--sans);color:rgba(25,35,75,.7)}
/* quote band */
.qband{background:var(--azzurro);padding:U(110) 0}
.qband .in{height:auto;padding:0 U(40);box-sizing:border-box}
.qband blockquote{margin:0 auto;max-width:U(1000);text-align:center;font:400 U(52)/U(56) var(--serif);letter-spacing:U(-2);text-transform:uppercase;color:var(--navy)}
.qband p{margin:U(28) 0 0;text-align:center;font:500 U(14)/U(20) var(--sans);letter-spacing:U(.84);text-transform:uppercase;color:rgba(25,35,75,.6)}
/* faq */
.faq{border-top:1px solid rgba(25,35,75,.12)}
.faq details{border-bottom:1px solid rgba(25,35,75,.12)}
.faq summary{list-style:none;cursor:pointer;display:flex;justify-content:space-between;align-items:center;gap:U(20);padding:U(26) 0;font:400 U(22)/U(28) var(--sans);color:var(--navy)}
.faq summary::-webkit-details-marker{display:none}
.faq summary::after{content:"";flex:none;width:U(12);height:U(12);border-right:1.5px solid currentColor;border-bottom:1.5px solid currentColor;transform:translateY(-25%) rotate(45deg);transition:transform .5s var(--osmo)}
.faq details[open] summary::after{transform:translateY(25%) rotate(-135deg)}
.faq .a{padding:0 0 U(26);max-width:U(760);font:400 U(16)/U(24) var(--sans);color:rgba(25,35,75,.75)}
.faq .a p{margin:0 0 U(10)}
.two-col{display:grid;grid-template-columns:U(447) 1fr;gap:U(120)}
.two-col .side h2{margin:0}
.two-col .side p{margin:U(20) 0 0;font:400 U(17)/U(26) var(--sans);color:rgba(25,35,75,.75)}
/* cta band */
.ctab{display:flex;justify-content:space-between;align-items:center;gap:U(40);background:var(--navy-deep);padding:U(56) U(56);color:#fff;position:relative;overflow:hidden}
.ctab h2{margin:0;max-width:U(760);font:400 U(44)/U(46) var(--serif);letter-spacing:U(-1.6);text-transform:uppercase;color:var(--title-light)}
.ctab p{margin:U(14) 0 0;font:400 U(17)/U(26) var(--sans);color:rgba(255,255,255,.75)}
.ctab .btns{display:flex;gap:U(12);flex-wrap:wrap;flex:none}
/* rows list (documents, regions…) */
.lst{border-top:1px solid rgba(25,35,75,.12)}
.lst a,.lst .row{display:flex;align-items:center;gap:U(16);padding:U(20) 0;border-bottom:1px solid rgba(25,35,75,.12);font:400 U(18)/U(26) var(--sans);color:var(--navy);transition:color .4s var(--osmo),padding .5s var(--osmo)}
.lst a:hover{color:#3B4A8C;padding-left:U(8)}
.lst .t{flex:1;min-width:0}
.lst .m{font:400 max(13px,U(16))/1.4 var(--sans);color:rgba(25,35,75,.7);white-space:nowrap}
.lst .dl,.lst .ur{width:U(16);height:U(16);flex:none}
.lst .ic{width:U(20);height:U(20);flex:none}
.lst-2{display:grid;grid-template-columns:1fr 1fr;column-gap:U(80)}
/* search + chips */
.tools{display:flex;justify-content:space-between;align-items:center;gap:U(24);flex-wrap:wrap;margin-bottom:U(32)}
.search{display:flex;align-items:center;gap:U(10);width:U(360);max-width:100%;padding:U(12) U(16);border:1px solid rgba(25,35,75,.2);border-radius:999px;color:var(--navy);transition:border-color .4s var(--osmo)}
.search:focus-within{border-color:var(--navy)}
.search svg{width:U(18);height:U(18);flex:none}
.search input{flex:1;min-width:0;border:0;outline:0;background:none;font:400 U(16)/U(22) var(--sans);color:var(--navy)}
.chips-f{display:flex;flex-wrap:wrap;gap:U(8)}
.chips-f button{padding:U(10) U(16);border:1px solid rgba(25,35,75,.28);border-radius:U(5);font:500 U(14)/U(18) var(--sans);color:var(--navy);transition:background-color .4s var(--osmo),border-color .4s var(--osmo),color .4s var(--osmo)}
.chips-f button:hover{border-color:var(--navy)}
.chips-f button[aria-pressed="true"]{background:var(--navy);border-color:var(--navy);color:#fff}
/* course cards (DPL Accademy) */
.courses{display:grid;grid-template-columns:repeat(3,minmax(0,1fr));gap:U(20)}
.course{display:flex;flex-direction:column;background:#fff;border:1px solid rgba(90,28,48,.14);transition:border-color .5s var(--osmo),transform .6s var(--osmo),box-shadow .6s var(--osmo)}
.course:hover{border-color:var(--bordeaux);transform:translateY(U(-4));box-shadow:0 U(20) U(44) rgba(90,28,48,.08)}
.course .tag{align-self:flex-start;margin:U(32) U(32) 0;padding:U(6) U(10) U(5);border-radius:U(4);font:500 U(13)/U(16) var(--sans);letter-spacing:0;text-transform:none;white-space:nowrap}
.course .tag.t-corso{background:var(--bordeaux);color:#fff}
.course .tag.t-incontro{background:var(--rosa);color:var(--bordeaux)}
.course .tag.t-aggiornamento{background:#fff;color:var(--bordeaux);box-shadow:inset 0 0 0 1px var(--bordeaux)}
.course h3{margin:U(20) U(32) 0;min-height:U(56);font:400 U(22)/U(28) var(--sans);letter-spacing:U(-.2);color:var(--bordeaux)}
.course dl{margin:U(24) U(32) U(28);display:flex;flex-direction:column;gap:U(12)}
.course .m{display:grid;grid-template-columns:U(20) minmax(0,1fr);gap:U(12);align-items:start}
.course dt{display:flex;padding-top:U(1)}
.course dt .ph{width:U(20);height:U(20);color:rgba(90,28,48,.55)}
.course dd{margin:0;font:400 U(15)/U(22) var(--sans);color:rgba(90,28,48,.85)}
.course .go{display:flex;align-items:center;justify-content:space-between;gap:U(12);margin-top:auto;padding:U(18) U(32) U(20);border-top:1px solid rgba(90,28,48,.12);font:500 U(15)/U(20) var(--sans);color:var(--bordeaux);transition:background-color .5s var(--osmo),color .5s var(--osmo)}
.course .go .ar{width:U(20);height:U(20);transition:transform .5s var(--osmo)}
.course .go:hover{background:var(--bordeaux);color:#fff}
.course .go:hover .ar{transform:translateX(U(4))}
.more-c{display:none}
/* blog (zaro-like) */
.post-feat{display:grid;grid-template-columns:1.3fr 1fr;gap:U(48);align-items:center;margin-bottom:U(72)}
.post-feat .ph{height:U(460);overflow:hidden;background:#F3F5FC}
.post-feat .ph img{width:100%;height:100%;object-fit:cover;display:block;transition:transform 1.4s var(--osmo)}
.post-feat:hover .ph img{transform:scale(1.03)}
.post-feat h2{margin:U(16) 0 0;font:400 U(44)/U(46) var(--serif);letter-spacing:U(-1.6);text-transform:uppercase;color:var(--navy)}
.post-feat p{margin:U(18) 0 0;font:400 U(17)/U(26) var(--sans);color:rgba(25,35,75,.75)}
.meta{display:flex;gap:U(12);align-items:center;font:500 U(13)/U(18) var(--sans);letter-spacing:U(.7);text-transform:uppercase;color:rgba(25,35,75,.55)}
.meta b{font-weight:500;color:var(--navy)}
.posts{display:grid;grid-template-columns:repeat(3,minmax(0,1fr));gap:U(48) U(24)}
.post .ph{height:U(260);overflow:hidden;background:#F3F5FC;margin-bottom:U(20);display:grid;place-items:center}
.post .ph img{width:100%;height:100%;object-fit:cover;display:block;transition:transform 1.4s var(--osmo)}
.post:hover .ph img{transform:scale(1.04)}
.post .ph .ic{width:U(56);height:U(64)}.post .ph .ic svg{width:100%;height:100%;fill:var(--azzurro)}
.post h3{margin:U(12) 0 0;font:400 U(22)/U(28) var(--sans);color:var(--navy)}
.post p{margin:U(10) 0 0;font:400 U(15)/U(22) var(--sans);color:rgba(25,35,75,.7)}
/* legal (maisa-like) */
.legal{display:grid;grid-template-columns:U(300) 1fr;gap:U(120);align-items:start}
.toc{position:sticky;top:U(110);display:flex;flex-direction:column;border-left:1px solid rgba(25,35,75,.12)}
.toc a{padding:U(8) 0 U(8) U(18);margin-left:-1px;border-left:1px solid transparent;font:400 U(14)/U(20) var(--sans);color:rgba(25,35,75,.55);transition:color .3s var(--osmo),border-color .3s var(--osmo)}
.toc a:hover,.toc a.on{color:var(--navy);border-left-color:var(--navy)}
.prose{max-width:U(760);font:400 U(17)/U(28) var(--sans);color:rgba(25,35,75,.85)}
.prose h2{margin:U(64) 0 U(18);font:400 U(30)/U(36) var(--sans);letter-spacing:U(-.4);color:var(--navy);scroll-margin-top:U(110)}
.prose h2:first-child{margin-top:0}
.prose h3{margin:U(32) 0 U(10);font:500 U(17)/U(26) var(--sans);color:var(--navy)}
.prose p{margin:0 0 U(16)}
.prose ul{margin:0 0 U(16);padding-left:U(20)}
.prose li{margin-bottom:U(6)}
.prose a{color:var(--navy);text-decoration:underline;text-underline-offset:3px;word-break:break-word}
.prose table{width:100%;border-collapse:collapse;margin:U(8) 0 U(24);font-size:U(15);line-height:U(22)}
.prose th,.prose td{text-align:left;vertical-align:top;padding:U(14) U(12);border-bottom:1px solid rgba(25,35,75,.12)}
.prose th{font-weight:500;color:var(--navy);border-bottom-color:var(--navy)}
.prose .lead{font-size:U(20);line-height:U(30);color:var(--navy)}
.prose .upd{font:500 U(13)/U(18) var(--sans);letter-spacing:U(.7);text-transform:uppercase;color:rgba(25,35,75,.5)}
/* form */
.form{display:grid;grid-template-columns:1fr 1fr;gap:U(16)}
.form .full{grid-column:1/-1}
.form label{display:flex;flex-direction:column;gap:U(8);font:500 U(13)/U(18) var(--sans);letter-spacing:U(.4);color:rgba(25,35,75,.7)}
.form input,.form select,.form textarea{font:400 U(16)/U(22) var(--sans);color:var(--navy);background:#fff;border:1px solid rgba(25,35,75,.2);border-radius:U(5);padding:U(14) U(16);outline:0;transition:border-color .4s var(--osmo),box-shadow .4s var(--osmo)}
.form textarea{min-height:U(140);resize:vertical}
.form input:focus,.form select:focus,.form textarea:focus{border-color:var(--navy);box-shadow:0 0 0 U(3) rgba(186,199,249,.45)}
.form .check{flex-direction:row;align-items:flex-start;gap:U(10);font:400 U(14)/U(20) var(--sans);letter-spacing:0;color:rgba(25,35,75,.75)}
.form .check input{width:U(18);height:U(18);margin:U(1) 0 0;padding:0;flex:none;accent-color:var(--navy)}
.form .check a{text-decoration:underline}
.form button{justify-self:start;border:0;cursor:pointer}
.btn-navy{display:inline-flex;align-items:center;gap:U(10);padding:U(13) U(16) U(13) U(20);border-radius:U(5);background:var(--navy);font:500 U(15)/normal var(--sans);color:#fff;transition:background-color .4s var(--osmo)}
.btn-navy:hover{background:var(--navy-deep)}
.btn-navy .ico{width:U(18);height:U(18);transition:transform .5s var(--osmo)}
.btn-navy:hover .ico{transform:translateX(U(3))}
.btn-ghost{display:inline-flex;align-items:center;gap:U(10);padding:U(12) U(15) U(12) U(19);border-radius:U(5);border:1px solid rgba(25,35,75,.25);font:500 U(15)/normal var(--sans);color:var(--navy);transition:border-color .4s var(--osmo)}
.btn-ghost:hover{border-color:var(--navy)}
.btn-ghost .ico,.btn-ghost .ur{width:U(16);height:U(16)}
/* contact cards */
.ccards{display:grid;grid-template-columns:repeat(4,1fr);gap:U(16)}
.ccard{background:#F3F5FC;padding:U(28);display:flex;flex-direction:column;gap:U(8);min-height:U(180);box-sizing:border-box}
.ccard .k{font:500 U(13)/U(18) var(--sans);letter-spacing:U(.7);text-transform:uppercase;color:rgba(25,35,75,.55)}
.ccard .v{margin-top:auto;font:400 U(22)/U(28) var(--sans);color:var(--navy)}
.ccard a.v:hover{color:#3B4A8C}
/* cities grid */
.cities{display:grid;grid-template-columns:repeat(4,minmax(0,1fr));gap:U(16)}
.city{position:relative;display:flex;flex-direction:column;justify-content:space-between;min-height:U(168);padding:U(24);background:#F3F5FC;color:var(--navy);transition:background-color .5s var(--osmo),color .5s var(--osmo)}
.city .rg{font:500 U(12)/U(16) var(--sans);letter-spacing:U(.7);text-transform:uppercase;color:rgba(25,35,75,.5);transition:color .5s var(--osmo)}
.city .c{font:400 U(30)/U(32) var(--serif);letter-spacing:U(-1);text-transform:uppercase;overflow-wrap:anywhere;padding-right:U(36)}
.city .go{position:absolute;right:U(24);top:U(24);width:U(32);height:U(32);border-radius:50%;border:1px solid rgba(25,35,75,.25);display:grid;place-items:center;transition:all .5s var(--osmo)}
.city .go .ico{width:U(14);height:U(14)}
.city:hover{background:var(--navy);color:#fff}
.city:hover .rg{color:var(--azzurro)}
.city:hover .go{background:var(--azzurro);border-color:var(--azzurro)}
.city.hq{background:var(--azzurro)}
.city[hidden]{display:none}
/* names list */
.names{columns:4;column-gap:U(32);font:400 U(15)/U(30) var(--sans);color:var(--navy)}
.names span{display:block;break-inside:avoid;border-bottom:1px solid rgba(25,35,75,.08)}
.names span[hidden]{display:none}
/* ===== live visuals ===== */
.v-chat{position:absolute;left:50%;top:50%;width:U(380);transform:translate(-50%,-50%);display:flex;flex-direction:column;gap:U(12)}
.v-chat .b{max-width:82%;padding:U(14) U(16);border-radius:U(14);font:400 U(15)/U(21) var(--sans);opacity:0;transform:translateY(U(14)) scale(.98);animation:vchat 12s var(--osmo) infinite}
.v-chat .b.me{align-self:flex-end;background:var(--azzurro);color:var(--navy);border-bottom-right-radius:U(4)}
.v-chat .b.us{align-self:flex-start;background:rgba(255,255,255,.12);color:#fff;border:1px solid rgba(255,255,255,.18);border-bottom-left-radius:U(4);-webkit-backdrop-filter:blur(8px);backdrop-filter:blur(8px)}
.v-chat .b small{display:block;margin-top:U(6);font-size:U(11);opacity:.6}
.v-chat .typing{align-self:flex-start;display:flex;gap:U(5);padding:U(14) U(16);border-radius:U(14);background:rgba(255,255,255,.12);opacity:0;animation:vtype 12s var(--osmo) infinite}
.v-chat .typing i{width:U(6);height:U(6);border-radius:50%;background:#fff;animation:vdot 1s ease-in-out infinite}
.v-chat .typing i:nth-child(2){animation-delay:.15s}.v-chat .typing i:nth-child(3){animation-delay:.3s}
.v-chat .b:nth-child(1){animation-delay:0s}.v-chat .typing{animation-delay:1.2s}.v-chat .b:nth-child(3){animation-delay:2.6s}.v-chat .b:nth-child(4){animation-delay:4.4s}.v-chat .b:nth-child(5){animation-delay:6s}
@keyframes vchat{0%,2%{opacity:0;transform:translateY(U(14)) scale(.98)}6%,86%{opacity:1;transform:none}94%,100%{opacity:0;transform:translateY(U(-8))}}
@keyframes vtype{0%,2%{opacity:0}5%,10%{opacity:1}12%,100%{opacity:0;height:0;padding:0;margin:0}}
@keyframes vdot{0%,100%{transform:translateY(0);opacity:.4}50%{transform:translateY(-3px);opacity:1}}
.v-path{position:absolute;left:U(48);right:U(48);top:50%;transform:translateY(-50%)}
.v-path .track{position:relative;display:grid;grid-template-columns:repeat(12,1fr);gap:U(8)}
.v-path .d{height:U(56);border-radius:U(28);background:rgba(255,255,255,.08);border:1px solid rgba(255,255,255,.14);position:relative;overflow:hidden}
.v-path .d::after{content:"";position:absolute;inset:0;background:var(--azzurro);transform:scaleY(0);transform-origin:50% 100%;animation:vfill 10s var(--osmo) infinite}
.v-path .lbls{display:flex;justify-content:space-between;margin-top:U(18);font:500 U(12)/U(16) var(--sans);letter-spacing:U(.7);text-transform:uppercase;color:var(--azzurro)}
.v-path .ttl{margin-bottom:U(22);font:400 U(26)/U(32) var(--sans);color:#fff}
.v-path .ttl b{font-weight:400;color:var(--azzurro)}
@keyframes vfill{0%,3%{transform:scaleY(0)}12%,85%{transform:scaleY(1)}95%,100%{transform:scaleY(0)}}
.v-italy{position:absolute;left:50%;top:50%;height:92%;width:auto;max-width:92%;transform:translate(-50%,-50%);overflow:visible}
.v-italy .grid circle{fill:rgba(186,199,249,.32);opacity:0;animation:vgrid 1.6s var(--osmo) forwards}
.in-view .v-italy .grid circle,.vis .v-italy .grid circle{animation-play-state:running}
@keyframes vgrid{from{opacity:0;transform:translateY(6px)}to{opacity:1;transform:none}}
.v-italy .arcs path{fill:none;stroke:url(#arcg);stroke:var(--azzurro);stroke-width:2;stroke-linecap:round;stroke-dasharray:1;stroke-dashoffset:1;opacity:.9;animation:varc 9s var(--osmo) infinite}
@keyframes varc{0%{stroke-dashoffset:1;opacity:0}6%{opacity:.9}22%{stroke-dashoffset:0;opacity:.9}70%{stroke-dashoffset:0;opacity:.35}86%,100%{stroke-dashoffset:-1;opacity:0}}
.v-italy .pin .dot{fill:var(--azzurro)}
.v-italy .pin.hq .dot{fill:#fff}
.v-italy .pin .halo{fill:rgba(186,199,249,.25);transform-box:fill-box;transform-origin:center;animation:vhalo 3s var(--osmo) infinite}
.v-italy .pin.hq .halo{fill:rgba(255,255,255,.22)}
@keyframes vhalo{0%{transform:scale(.3);opacity:.9}70%,100%{transform:scale(1.6);opacity:0}}
.v-italy text{font:500 22px/1 var(--sans);letter-spacing:1px;text-transform:uppercase;fill:rgba(255,255,255,.75)}
.v-italy .pin.hq text{fill:#fff;font-size:26px}
.v-map .mp{position:absolute;width:U(10);height:U(10);margin:U(-5) 0 0 U(-5);border-radius:50%;background:var(--azzurro);box-shadow:0 0 0 0 rgba(186,199,249,.6);animation:vping 6s var(--osmo) infinite}
.v-map .mp.hq{width:U(16);height:U(16);margin:U(-8) 0 0 U(-8);background:#fff}
.v-map .mp span{position:absolute;left:U(14);top:U(-5);font:500 U(11)/U(14) var(--sans);letter-spacing:U(.5);text-transform:uppercase;color:rgba(255,255,255,.7);white-space:nowrap}
@keyframes vping{0%{box-shadow:0 0 0 0 rgba(186,199,249,.55)}30%{box-shadow:0 0 0 U(14) rgba(186,199,249,0)}100%{box-shadow:0 0 0 0 rgba(186,199,249,0)}}
.v-docs{position:absolute;left:50%;top:50%;width:U(400);transform:translate(-50%,-50%);display:flex;flex-direction:column;gap:U(10)}
.v-docs .f{position:relative;display:flex;align-items:center;gap:U(12);padding:U(16) U(18);border-radius:U(10);background:rgba(255,255,255,.92);color:var(--navy);font:500 U(14)/U(20) var(--sans);overflow:hidden;opacity:0;animation:vdoc 9s var(--osmo) infinite}
.v-docs .f .ic{width:U(20);height:U(20);flex:none}
.v-docs .f .s{margin-left:auto;font:400 U(12)/U(16) var(--sans);color:rgba(25,35,75,.55)}
.v-docs .f::after{content:"";position:absolute;left:0;bottom:0;height:2px;width:100%;background:var(--azzurro);transform:scaleX(0);transform-origin:0 50%;animation:vbar 9s var(--osmo) infinite;animation-delay:inherit}
.v-docs .f:nth-child(2){animation-delay:.5s}.v-docs .f:nth-child(3){animation-delay:1s}.v-docs .f:nth-child(4){animation-delay:1.5s}
@keyframes vdoc{0%{opacity:0;transform:translateY(U(16))}7%,88%{opacity:1;transform:none}96%,100%{opacity:0;transform:translateY(U(-8))}}
@keyframes vbar{0%,12%{transform:scaleX(0)}30%,88%{transform:scaleX(1)}96%,100%{transform:scaleX(1);opacity:0}}
.v-stack{position:absolute;left:50%;top:50%;width:U(360);height:U(300);transform:translate(-50%,-50%)}
.v-stack .c{position:absolute;inset:0;padding:U(24);border-radius:U(12);background:#fff;box-shadow:0 U(20) U(50) rgba(5,8,30,.35);display:flex;flex-direction:column;gap:U(10);animation:vstack 12s var(--osmo) infinite;color:var(--navy)}
.v-stack .c .tag{align-self:flex-start;padding:U(4) U(10);border-radius:999px;background:var(--azzurro);font:500 U(11)/U(16) var(--sans);letter-spacing:U(.6);text-transform:uppercase}
.v-stack .c b{font:400 U(22)/U(28) var(--sans)}
.v-stack .c span{font:400 U(13)/U(18) var(--sans);color:rgba(25,35,75,.6)}
.v-stack .c:nth-child(1){animation-delay:-8s}.v-stack .c:nth-child(2){animation-delay:-4s}.v-stack .c:nth-child(3){animation-delay:0s}
@keyframes vstack{0%{transform:translateY(U(36)) scale(.9);opacity:0;z-index:1}10%{transform:translateY(U(24)) scale(.92);opacity:.5}33%{transform:translateY(U(12)) scale(.96);opacity:.8;z-index:2}43%,63%{transform:none;opacity:1;z-index:3}72%,100%{transform:translateY(U(-60)) scale(1.02);opacity:0;z-index:4}}
.v-orbit{position:absolute;left:50%;top:50%;width:U(360);height:U(360);transform:translate(-50%,-50%)}
.v-orbit .ring{position:absolute;inset:0;border:1px solid rgba(186,199,249,.25);border-radius:50%}
.v-orbit .core{position:absolute;left:50%;top:50%;width:U(90);height:U(108);transform:translate(-50%,-50%)}
.v-orbit .core svg{width:100%;height:100%;fill:var(--azzurro)}
.v-orbit .o{position:absolute;left:50%;top:50%;width:0;height:0;animation:vorb 24s linear infinite}
.v-orbit .o span{position:absolute;left:U(180);top:0;transform:translate(-50%,-50%);padding:U(8) U(14);border-radius:999px;background:rgba(255,255,255,.1);border:1px solid rgba(255,255,255,.2);font:500 U(13)/U(16) var(--sans);color:#fff;white-space:nowrap;animation:vorbr 24s linear infinite}
@keyframes vorb{to{transform:rotate(360deg)}}
@keyframes vorbr{to{transform:translate(-50%,-50%) rotate(-360deg)}}
@media (max-width: 899px){
  .px-hero{height:auto}
  .px-hero .in{height:auto;min-height:0;display:block;padding:0 max(16px,env(safe-area-inset-left,0px));box-sizing:border-box}
  .px-hero .rings{height:100%}
  .px-hero h1{position:relative;left:auto;top:auto;margin:0;width:auto;padding-top:132px;font-size:44px;line-height:42px;letter-spacing:-1.6px}
  .px-hero .rule{position:relative;left:auto;right:auto;bottom:auto;margin:36px 0 22px}
  .px-hero .foot-row{position:relative;left:auto;right:auto;bottom:auto;min-height:0;padding-top:0;flex-direction:column-reverse;align-items:flex-start;gap:28px;padding-bottom:48px}
  .px-hero .intro{width:auto;gap:22px}
  .px-hero .intro p{font-size:17px;line-height:26px}
  .px-hero .btns{flex-wrap:nowrap;gap:8px;width:100%}
  .px-hero .btns .btn{font-size:14px;gap:6px;padding:12px 12px 12px 14px}
  .px-hero .btns .btn .ico{width:16px;height:16px}
  .px-hero .facts{gap:8px 16px;font-size:12px;letter-spacing:.7px}
  .px-hero .facts span{gap:16px}
  .px-band{height:68vw}
  .px-sec{padding:64px 0}.px-sec.flush{padding-top:0}
  .px-sec .in,.qband .in{padding:0 max(16px,env(safe-area-inset-left,0px))}
  .px-body{margin-top:32px}
  .feat{grid-template-columns:1fr;gap:24px}
  .feat+.feat{margin-top:56px}
  .feat.rev .ft{order:0}
  .feat .ft h3{font-size:26px;line-height:32px}
  .feat .ft p{font-size:16px;line-height:24px}
  .vis{height:110vw;max-height:460px;margin:0 calc(-1*max(16px,env(safe-area-inset-left,0px)))}
  .icards,.steps-x,.courses,.posts,.ccards{grid-template-columns:minmax(0,1fr);gap:12px}
  .icard{min-height:0;padding:24px}
  .icard h3{padding-top:28px}
  .steps-x{gap:28px}
  .qband{padding:64px 0}
  .qband blockquote{font-size:30px;line-height:32px;letter-spacing:-1px}
  .faq summary{font-size:18px;line-height:24px;padding:20px 0}
  .two-col{grid-template-columns:1fr;gap:32px}
  .ctab{flex-direction:column;align-items:flex-start;padding:32px 20px;margin:0 calc(-1*max(16px,env(safe-area-inset-left,0px)))}
  .ctab h2{font-size:30px;line-height:32px;letter-spacing:-1px}
  .lst a,.lst .row{font-size:16px;line-height:22px;gap:12px}
  .lst .m{display:none}
  .lst-2{grid-template-columns:1fr}
  .search{width:100%}
  .tools{margin-bottom:20px}
  .post-feat{grid-template-columns:1fr;gap:20px;margin-bottom:48px}
  .post-feat .ph{height:62vw}
  .post-feat h2{font-size:30px;line-height:32px;letter-spacing:-1px}
  .posts{gap:36px}
  .post .ph{height:58vw}
  .legal{grid-template-columns:1fr;gap:24px}
  .toc{position:relative;top:auto;flex-direction:row;overflow-x:auto;border-left:0;border-bottom:1px solid rgba(25,35,75,.12);margin:0 calc(-1*max(16px,env(safe-area-inset-left,0px)));padding:0 16px;scrollbar-width:none}
  .toc a{flex:none;padding:12px 14px;border-left:0;margin:0;border-bottom:1px solid transparent;margin-bottom:-1px;white-space:nowrap}
  .toc a:hover,.toc a.on{border-bottom-color:var(--navy)}
  .prose{font-size:16px;line-height:26px}
  .prose h2{font-size:24px;line-height:30px;margin-top:48px}
  .prose table{display:block;overflow-x:auto}
  .form{grid-template-columns:1fr}
  .cities{grid-template-columns:repeat(2,minmax(0,1fr));gap:8px}
  .city{min-height:120px;padding:16px}
  .city .c{font-size:22px;line-height:24px}
  .city .go{right:14px;top:14px;width:28px;height:28px}
  .names{columns:1}
  .ccards{grid-template-columns:repeat(2,minmax(0,1fr));gap:8px}
  .ccard{min-height:0;padding:16px;gap:4px}
  .ccard .v{margin-top:14px;font-size:16px;line-height:22px;overflow-wrap:anywhere}
  .courses:not(.all) .course:nth-child(n+5){display:none}
  .more-c{display:flex!important;justify-content:center;margin-top:20px}
  .v-chat{width:86%}
  .v-path{left:20px;right:20px}
  .v-path .track{gap:5px}
  .v-path .d{height:44px}
  .v-path .ttl{font-size:20px;line-height:26px}
  .v-docs{width:88%}
  .v-stack{width:80%;height:260px}
  .v-orbit{width:290px;height:290px}
  .v-orbit .o span{left:145px;font-size:12px}
}
'''


CSS += r'''
/* ---- UX pass (12/11) ---- */
.px-hero .crumb{position:absolute;left:U(40);top:U(150);z-index:3;display:inline-flex;align-items:center;gap:U(8);font:500 U(13)/U(18) var(--sans);letter-spacing:U(.78);text-transform:uppercase;color:var(--azzurro);transition:color .4s var(--osmo)}
.px-hero .crumb:hover{color:#fff}
.px-hero .crumb .ar{display:inline-block;transition:transform .5s var(--osmo)}
.px-hero .crumb:hover .ar{transform:translateX(U(-3))}
.course.past{opacity:.62}
.course.past:hover{opacity:1}
.post .go,.post-feat .go{display:inline-flex;align-items:center;gap:U(8);margin-top:U(14);font:500 U(15)/U(20) var(--sans);color:var(--navy)}
.post .go .ico,.post-feat .go .ico{width:U(16);height:U(16);transition:transform .5s var(--osmo)}
.post .go:hover .ico,.post-feat .go:hover .ico{transform:translateX(U(3))}
.post.past .meta span::after{content:" · concluso"}
.post.past .go{display:none}
/* lavora con noi: e-mail only */
.job{display:grid;grid-template-columns:minmax(0,1fr) minmax(0,1fr);gap:U(24);margin-top:U(56)}
.roles{border-top:1px solid rgba(25,35,75,.12)}
.role{display:grid;grid-template-columns:U(44) minmax(0,1fr) U(32);gap:U(20);align-items:start;padding:U(26) 0;border-bottom:1px solid rgba(25,35,75,.12);color:var(--navy);transition:padding .5s var(--osmo)}
.role:hover{padding-left:U(8)}
.role .ic{width:U(44);height:U(44)}
.role .ic svg{width:100%;height:100%;display:block;fill:var(--navy)}
.role h3{margin:0;font:400 U(22)/U(28) var(--sans)}
.role p{margin:U(6) 0 0;font:400 U(15)/U(22) var(--sans);color:rgba(25,35,75,.7)}
.role .go{width:U(32);height:U(32);border-radius:50%;border:1px solid rgba(25,35,75,.25);display:grid;place-items:center;transition:all .5s var(--osmo)}
.role .go .ico,.role .go .ur{width:U(14);height:U(14)}
.role:hover .go{background:var(--navy);border-color:var(--navy);color:#fff}
.mailbox{background:var(--navy-deep);color:#fff;padding:U(44);display:flex;flex-direction:column;gap:U(22);position:relative;overflow:hidden}
.mailbox .k{font:500 U(13)/U(18) var(--sans);letter-spacing:U(.78);text-transform:uppercase;color:var(--azzurro)}
.mailbox .addr{font:400 U(40)/U(44) var(--serif);letter-spacing:U(-1.2);color:#fff;overflow-wrap:anywhere}
.mailbox ul{list-style:none;margin:0;padding:0;border-top:1px solid rgba(255,255,255,.14)}
.mailbox li{display:flex;align-items:center;gap:U(14);padding:U(14) 0;border-bottom:1px solid rgba(255,255,255,.14);font:400 U(16)/U(22) var(--sans);color:rgba(255,255,255,.85)}
.mailbox li b{font:500 U(12)/U(16) var(--sans);color:var(--azzurro);letter-spacing:U(.6)}
.mailbox .btns{display:flex;gap:U(12);flex-wrap:wrap;margin-top:U(6)}
.mailbox .copy{cursor:pointer;background:none}
.mailbox .copy.ok{border-color:var(--azzurro);color:var(--azzurro)}
.mailbox .note{margin:0;font:400 U(14)/U(20) var(--sans);color:rgba(255,255,255,.6)}
.inline-link{color:inherit;text-decoration:underline;text-underline-offset:.2em;text-decoration-color:rgba(186,199,249,.6)}
.inline-link:hover{text-decoration-color:currentColor}
.rnav{display:flex;flex-wrap:wrap;gap:U(8);margin-top:U(24)}
.rnav a{padding:U(8) U(16);border:1px solid rgba(25,35,75,.2);border-radius:999px;font:400 U(14)/U(18) var(--sans);color:var(--navy);transition:all .4s var(--osmo)}
.rnav a:hover{background:var(--navy);border-color:var(--navy);color:#fff}
.pn{display:flex;justify-content:space-between;gap:U(16);margin-top:U(56);padding-top:U(24);border-top:1px solid rgba(25,35,75,.12)}
.pn a{display:flex;flex-direction:column;gap:U(4);font:400 U(22)/U(28) var(--sans);color:var(--navy)}
.pn a small{font:500 U(12)/U(16) var(--sans);letter-spacing:U(.7);text-transform:uppercase;color:rgba(25,35,75,.5)}
.pn a.nx{text-align:right;margin-left:auto}
.closing.short{height:U(600)}
.closing.short .foot{top:U(20)}
.cta-block .btns{display:flex;gap:U(12);flex-wrap:wrap;justify-content:center}
@media (max-width: 899px){
  .px-hero .crumb{left:max(16px,env(safe-area-inset-left,0px));top:96px;font-size:12px}
  .ccards{grid-template-columns:minmax(0,1fr)!important;gap:0!important;border-top:1px solid rgba(25,35,75,.12)}
  .ccard{flex-direction:row;justify-content:space-between;align-items:baseline;gap:16px!important;padding:16px 0!important;background:none;border-bottom:1px solid rgba(25,35,75,.12)}
  .ccard .v{margin:0!important;text-align:right;font-size:16px;line-height:22px;overflow-wrap:normal!important}
  .city{min-height:92px;padding:14px}
  .city .c{font-size:18px;line-height:20px;padding-right:0;overflow-wrap:normal;word-break:normal;hyphens:none}
  .names{columns:1}
  .names:not(.all):not(.q) span:nth-child(n+13){display:none}
  .courses:not(.all):not(.q) .course:nth-child(n+4){display:none}
  .more-c[data-n="0"]{display:none!important}
  .job{grid-template-columns:minmax(0,1fr);gap:24px;margin-top:32px}
  .role{grid-template-columns:36px minmax(0,1fr) 28px;gap:14px;padding:20px 0}
  .role .ic{width:36px;height:36px}
  .role h3{font-size:19px;line-height:24px}
  .role .go{width:28px;height:28px}
  .mailbox{padding:28px 20px;margin:0 calc(-1*max(16px,env(safe-area-inset-left,0px)))}
  .mailbox .addr{font-size:28px;line-height:32px}
  .rtab thead{display:none}
  .rtab,.rtab tbody{display:block}
  .rtab tr{display:grid;grid-template-columns:1fr auto;gap:2px 12px;padding:16px 0;border-bottom:1px solid rgba(25,35,75,.12)}
  .rtab td{border:0!important;padding:0!important;font-size:14px;line-height:20px}
  .rtab td:nth-child(1){font-size:17px;line-height:24px;color:var(--navy)}
  .rtab td:nth-child(5){grid-column:2;grid-row:1;color:rgba(25,35,75,.55);font-size:13px}
  .rtab td:nth-child(2),.rtab td:nth-child(3),.rtab td:nth-child(4){grid-column:1/-1;color:rgba(25,35,75,.75)}
  .pn{flex-direction:column;margin-top:40px}
  .pn a{font-size:18px;line-height:24px}
  .closing.short{height:auto;padding-top:0}
  .cta-block .btns{flex-direction:column;align-items:center}
}
'''


CSS += r'''
/* ---- news: clickable cards, article & event pages ---- */
a.post{display:block;color:inherit}
a.post h3{transition:color .4s var(--osmo)}
a.post:hover h3{color:#3B4A8C}
a.post-feat{color:inherit}
.post-feat .go,.post .go{white-space:nowrap}
.art-hero{background:var(--navy-deep)}
.art-hero .rings{height:100%}
.art-hero .in{height:auto;padding:U(168) U(40) U(88);box-sizing:border-box}
.art-hero .ah{position:relative;z-index:2;max-width:U(1040)}
.art-hero .crumb{display:inline-flex;align-items:center;gap:U(8);font:500 U(13)/U(18) var(--sans);letter-spacing:U(.78);text-transform:uppercase;color:var(--azzurro);transition:color .4s var(--osmo)}
.art-hero .crumb:hover{color:#fff}
.art-hero .crumb .ar{display:inline-block;transition:transform .5s var(--osmo)}
.art-hero .crumb:hover .ar{transform:translateX(U(-3))}
.art-hero .meta{margin-top:U(40);color:rgba(255,255,255,.6)}
.art-hero .meta b{color:var(--azzurro)}
.art-hero h1{margin:U(18) 0 0;font:400 U(60)/U(62) var(--serif);letter-spacing:U(-2.2);text-transform:uppercase;color:var(--title-light)}
.art-hero .lead{margin:U(28) 0 0;max-width:U(680);font:400 U(20)/U(30) var(--sans);color:rgba(255,255,255,.8)}
.art-hero .btns{display:flex;gap:U(12);flex-wrap:wrap;margin-top:U(36)}
.art{display:grid;grid-template-columns:U(320) minmax(0,1fr);gap:U(120);align-items:start}
.art aside{position:sticky;top:U(110);display:flex;flex-direction:column;gap:U(28)}
.ainfo{margin:0;display:grid;grid-template-columns:auto 1fr;gap:U(12) U(20);padding:U(24) 0;border-top:1px solid rgba(25,35,75,.12);border-bottom:1px solid rgba(25,35,75,.12);font:400 U(15)/U(22) var(--sans)}
.ainfo dt{color:rgba(25,35,75,.5)}
.ainfo dd{margin:0;color:var(--navy)}
.abtn{display:flex;flex-direction:column;align-items:flex-start;gap:U(10)}
.copy-l{cursor:pointer;background:none}
.copy-l.ok{border-color:var(--navy)}
.ended{display:none;margin:0;padding:U(12) U(16);background:#F3F5FC;font:500 U(14)/U(20) var(--sans);color:var(--navy)}
.art.past .ended{display:block}
.art.past .abtn>a:not(.btn-ghost){display:none}
.prose blockquote{margin:U(36) 0;padding-left:U(28);border-left:2px solid var(--azzurro);font:400 U(30)/U(36) var(--serif);letter-spacing:U(-.6);color:var(--navy)}
.prose .upd{margin-top:U(32);font-size:U(14);color:rgba(25,35,75,.55)}
/* ---- 404 (Figma 715:144) ---- */
.nf{min-height:100vh;min-height:100svh;background:#11174A}
.nf .rings{height:100%}
.nf .in{height:auto}
.nf-c{position:relative;z-index:2;min-height:100vh;min-height:100svh;box-sizing:border-box;display:flex;flex-direction:column;align-items:center;justify-content:center;text-align:center;padding:U(120) 0 U(72)}
.nf-n{margin:0;font:400 U(192)/U(173) var(--serif);letter-spacing:U(-4.8);text-transform:uppercase;color:#D9E5F6}
.nf-m{margin:U(44) 0 0;width:U(460);display:flex;flex-direction:column;gap:U(8);font:400 U(18)/U(27) var(--sans);color:#fff;animation:nfIn 1.1s var(--osmo) both .15s}
.nf-m b{font-weight:400;color:#fff}
.nf-m span{color:rgba(255,255,255,.7)}
@keyframes nfIn{from{opacity:0;filter:blur(10px);transform:translateY(8px)}to{opacity:1;filter:none;transform:none}}
.nf .btns{display:flex;gap:U(12);flex-wrap:wrap;justify-content:center;margin-top:U(36)}
.nf-l{display:flex;flex-wrap:wrap;justify-content:center;gap:U(8) U(24);margin-top:U(56);padding-top:U(24);border-top:1px solid rgba(255,255,255,.14)}
.nf-l a{font:400 U(15)/U(22) var(--sans);color:rgba(255,255,255,.75);transition:color .3s var(--osmo)}
.nf-l a:hover{color:#fff}
.sr{position:absolute;width:1px;height:1px;overflow:hidden;clip:rect(0 0 0 0);white-space:nowrap}
@media (prefers-reduced-motion: reduce){.nf-m{animation:none}}
@media (max-width: 899px){
  .art-hero .in{padding:112px max(16px,env(safe-area-inset-left,0px)) 48px}
  .art-hero .meta{margin-top:28px;flex-wrap:wrap;gap:6px 12px}
  .art-hero h1{font-size:32px;line-height:34px;letter-spacing:-1px}
  .art-hero .lead{font-size:17px;line-height:26px}
  .art{grid-template-columns:minmax(0,1fr);gap:32px}
  .art aside{position:relative;top:auto}
  .abtn{flex-direction:row;flex-wrap:wrap}
  .prose blockquote{font-size:22px;line-height:28px;padding-left:18px}
  .nf-c{padding:120px 0 64px}
  .nf-n{font-size:120px;line-height:110px;letter-spacing:-3px}
  .nf-m{width:auto;max-width:340px;font-size:17px;line-height:26px}
  .nf .btns{flex-direction:column;align-items:center}
  .nf-l{gap:8px 18px;margin-top:40px}
}
'''


CSS += r'''
/* ---- DPL Accademy: tonalità rosse (D-054, D-128) — bordeaux #5A1C30, rosa #E1BED2; mai bordeaux attaccato al blu notte (D-142), niente gradienti ---- */
:root{--bordeaux:#5A1C30;--rosa:#E1BED2;--rosa-t:#FAF5F8}
.px-hero.acc{background:var(--bordeaux)}
/* pagine DPL Accademy: solo rosa o bianco, mai l'azzurro */
.px-hero.acc{--azzurro:var(--rosa);--title-light:#fff}
.px-hero.acc h1 .a{color:var(--rosa)}
body:has(.px-hero.acc) .closing{--azzurro:var(--rosa);--title-light:#fff}
.px-hero.acc .device path{fill:var(--rosa)}
.px-hero.acc h1 .b{color:var(--rosa)}
.px-hero.acc .facts{color:var(--rosa)}
.px-hero.acc .facts span+span::before{background:var(--rosa)}
.px-sec.acc-t{background:var(--rosa-t)}
.acc .cs-head .h2{color:var(--bordeaux)}
.acc .vis{background:var(--bordeaux)}
.acc .vis .glow{display:none}
.acc .v-stack .c{color:var(--bordeaux);box-shadow:0 U(20) U(50) rgba(40,8,20,.35)}
.acc .v-stack .c .tag{background:var(--rosa)}
.acc .feat .ft h3{color:var(--bordeaux)}
.acc .feat .ft li{color:var(--bordeaux)}
.acc .feat .ft li::before{background:var(--rosa);box-shadow:0 0 0 U(3) rgba(225,190,210,.4)}
.acc .chips-f button{border-color:rgba(90,28,48,.3);color:var(--bordeaux)}
.acc .chips-f button:hover{border-color:var(--bordeaux)}
.acc .chips-f button[aria-pressed="true"]{background:var(--bordeaux);border-color:var(--bordeaux);color:#fff}
.acc .btn-ghost:hover{border-color:var(--bordeaux)}
.acc .lst a:hover{color:var(--bordeaux)}
.acc .lst .ur path{stroke:var(--bordeaux)}
.acc .lst .m{color:rgba(90,28,48,.75)}
/* course cards are DPL Accademy products everywhere they appear */
.course .tag.past{background:#fff;color:rgba(90,28,48,.75);box-shadow:inset 0 0 0 1px rgba(90,28,48,.35)}
'''

def esc(s): return H.escape(s, quote=True)

def hero(a, b, intro, btns, facts, device='__DEVICE_HERO__', crumb=None, cls=''):
    f = ''.join(f'<span>{x}</span>' for x in facts)
    cr = f'<a class="crumb" href="{crumb[1]}"><span class="ar">←</span>{crumb[0]}</a>' if crumb else ''
    return f'''<section class="sec hero px-hero {cls}" id="top">
  <div class="in">
    <div class="rings" data-parallax="0.1"><div class="art">{device}</div></div>
__HEADER__
    {cr}<h1><span class="a">{a}</span>{f'<span class="b">{b}</span>' if b else ''}</h1>
    <div class="rule"></div>
    <div class="foot-row">
      <div class="facts">{f}</div>
      <div class="intro"><p class="blurin">{intro}</p><div class="btns">{btns}</div></div>
    </div>
  </div>
</section>
'''

def band(img, alt=''):
    return f'<div class="px-band"><img src="__IMG_{img}__" alt="{alt}"></div>\n'

def sec(inner, cls='', sid=''):
    return f'<section class="px-sec {cls}"{f" id={chr(34)}{sid}{chr(34)}" if sid else ""}>\n  <div class="in">\n{inner}\n  </div>\n</section>\n'

def head(h2, p=''):
    return f'<div class="cs-head"><h2 class="h2 blurin">{h2}</h2>{f"<p class={chr(34)}blurin{chr(34)}>{p}</p>" if p else ""}</div>'

def feat(h3, p, bullets, visual, rev=False, light=False):
    ul = ('<ul>' + ''.join(f'<li>{b}</li>' for b in bullets) + '</ul>') if bullets else ''
    return f'<div class="feat{" rev" if rev else ""}"><div class="ft"><h3 class="blurin">{h3}</h3><p class="blurin">{p}</p>{ul}</div><div class="vis{" light" if light else ""}"><div class="glow"></div>{visual}</div></div>'

def icards(items, cols=3):
    return f'<div class="icards px-body" style="--cols:{cols}">' + ''.join(f'<article class="icard"><span class="ic">{ICONS[i]}</span><h3>{t}</h3><p>{p}</p></article>' for i, t, p in items) + '</div>'

def steps(items):
    return f'<div class="steps-x px-body" style="--cols:{len(items)}">' + ''.join(f'<div class="sx"><span class="n">{n:02d}</span><h3>{t}</h3><p>{p}</p></div>' for n, (t, p) in enumerate(items, 1)) + '</div>'

def faq(items):
    return '<div class="faq">' + ''.join(f'<details><summary>{q}</summary><div class="a">{a}</div></details>' for q, a in items) + '</div>'

def faq_sec(items, title='Domande frequenti', p='Le risposte alle domande che ci fate più spesso.'):
    return sec(f'<div class="two-col"><div class="side"><h2 class="h2 blurin">{title}</h2><p class="blurin">{p}</p></div>{faq(items)}</div>', 'flush')

def qband(q, who):
    return f'<section class="qband"><div class="in"><blockquote class="blurin">{q}</blockquote><p>{who}</p></div></section>\n'

def ctab(h2, p, btns):
    return f'<div class="ctab"><div><h2>{h2}</h2><p>{p}</p></div><div class="btns">{btns}</div></div>'

def btn(label, href, kind='glass', ext=False, icon='__ARROW_W__'):
    x = ' target="_blank" rel="noopener"' if ext else ''
    cls = {'glass': 'btn btn--glass', 'line': 'btn btn--line', 'navy': 'btn-navy', 'ghost': 'btn-ghost'}[kind]
    return f'<a class="{cls}" href="{href}"{x}>{label} {icon}</a>'

# live visuals
def v_chat(msgs):
    out = []
    for i, (who, t, meta) in enumerate(msgs):
        out.append(f'<div class="b {who}">{t}{f"<small>{meta}</small>" if meta else ""}</div>')
        if i == 0: out.append('<div class="typing"><i></i><i></i><i></i></div>')
    return '<div class="v-chat" aria-hidden="true">' + ''.join(out) + '</div>'

def v_path(title, left, right, n=12):
    ds = ''.join(f'<span class="d" style="--i:{i}"></span>' for i in range(n))
    return f'<div class="v-path" aria-hidden="true"><div class="ttl">{title}</div><div class="track">{ds}</div><div class="lbls"><span>{left}</span><span>{right}</span></div></div><style>.v-path .d::after{{animation-delay:calc(var(--i) * .35s)}}</style>'

def v_docs(items):
    return '<div class="v-docs" aria-hidden="true">' + ''.join(f'<div class="f">__ICO_FILE__<span>{n}</span><span class="s">{s}</span></div>' for n, s in items) + '</div>'

def v_stack(cards):
    return '<div class="v-stack" aria-hidden="true">' + ''.join(f'<div class="c"><span class="tag">{t}</span><b>{h}</b><span>{m}</span></div>' for t, h, m in cards) + '</div>'

def v_orbit(icon, labels):
    n = len(labels)
    os_ = ''.join(f'<div class="o" style="animation-delay:{-24 * i / n:.2f}s"><span style="animation-delay:{-24 * i / n:.2f}s">{l}</span></div>' for i, l in enumerate(labels))
    return f'<div class="v-orbit" aria-hidden="true"><div class="ring"></div><div class="core">{ICONS[icon]}</div>{os_}</div>'

ITALY = [  # rough outlines (lat, lon): mainland, Sicily, Sardinia
 [(43.79,7.53),(44.15,7.65),(44.4,6.9),(45.1,6.6),(45.5,7.0),(45.9,6.8),(46.0,7.9),(46.45,8.45),(45.85,9.0),(46.3,9.25),(46.5,10.1),(46.6,10.45),(46.9,10.5),(46.8,11.0),(47.08,12.2),(46.65,13.7),(46.4,13.7),(45.8,13.6),(45.65,13.8),(45.75,13.2),(45.45,12.4),(45.2,12.3),(44.8,12.4),(44.2,12.4),(43.6,13.5),(43.0,13.9),(42.4,14.2),(41.9,15.2),(41.9,16.1),(41.6,15.9),(41.3,16.5),(40.6,17.9),(40.15,18.5),(39.8,18.35),(40.3,17.4),(40.1,16.6),(39.6,16.5),(39.4,17.1),(38.9,16.6),(38.4,16.6),(37.92,16.05),(38.25,15.65),(38.7,15.9),(39.3,16.0),(39.95,15.6),(40.05,15.3),(40.25,14.9),(40.6,14.4),(40.8,14.15),(41.2,13.6),(41.4,12.9),(41.75,12.2),(42.4,11.3),(43.0,10.5),(43.55,10.3),(44.05,10.0),(44.4,8.9),(44.1,8.2)],
 [(38.27,15.65),(37.6,15.15),(37.0,15.3),(36.65,15.1),(36.8,14.4),(37.1,13.7),(37.3,13.0),(37.6,12.45),(38.1,12.5),(38.15,13.4),(38.0,14.0)],
 [(41.25,9.2),(40.9,9.7),(40.0,9.75),(39.1,9.6),(38.9,8.85),(39.2,8.4),(39.9,8.5),(40.6,8.15),(40.95,8.25)]]

def _inside(pt, poly):
    y, x = pt; c = False; n = len(poly)
    for i in range(n):
        y1, x1 = poly[i]; y2, x2 = poly[(i + 1) % n]
        if (y1 > y) != (y2 > y) and x < (x2 - x1) * (y - y1) / (y2 - y1) + x1: c = not c
    return c

def v_map(cities):
    """Stripe-like dotted Italy: a dot matrix shaped like the country, city markers that pulse, arcs from Milano drawn in sequence."""
    import math
    k = math.cos(math.radians(42)); S = 100
    X = lambda lo: (lo - 6.4) * k * S; Y = lambda la: (47.3 - la) * S
    W, H = X(18.7), Y(36.5)
    dots = []; step = .15
    la = 47.2
    while la > 36.5:
        lo = 6.5
        while lo < 18.6:
            if any(_inside((la, lo), p) for p in ITALY):
                d = (47.2 - la) / 10.7
                dots.append(f'<circle cx="{X(lo):.0f}" cy="{Y(la):.0f}" r="3.4" style="animation-delay:{d * 1.6:.2f}s"/>')
            lo += step / k
        la -= step
    hq = next((la, lo) for n, la, lo, h in cities if h)
    arcs, pins = [], []
    for i, (n, la, lo, h) in enumerate(cities):
        x, y = X(lo), Y(la)
        if not h:
            hx, hy = X(hq[1]), Y(hq[0]); mx, my = (hx + x) / 2, (hy + y) / 2; dist = math.hypot(x - hx, y - hy)
            cx, cy = mx + (y - hy) * .18, my - dist * .28
            arcs.append(f'<path d="M{hx:.0f} {hy:.0f}Q{cx:.0f} {cy:.0f} {x:.0f} {y:.0f}" pathLength="1" style="animation-delay:{i * .45:.2f}s"/>')
        lbl = f'<text x="{x + 16:.0f}" y="{y + 5:.0f}">{n}</text>' if h or n in ('Torino', 'Roma', 'Salerno', 'Varese', 'Terni', 'Cuneo') else ''
        pins.append(f'<g class="pin{" hq" if h else ""}" style="animation-delay:{i * .45 + .9:.2f}s"><circle class="halo" cx="{x:.0f}" cy="{y:.0f}" r="18"/><circle class="dot" cx="{x:.0f}" cy="{y:.0f}" r="{9 if h else 6.5}"/>{lbl}</g>')
    return (f'<svg class="v-italy" viewBox="0 0 {W:.0f} {H:.0f}" aria-hidden="true"><g class="grid">{"".join(dots)}</g>'
            f'<g class="arcs">{"".join(arcs)}</g><g class="pins">{"".join(pins)}</g></svg>')

FILTER_JS = '''
  /* ---- kit: list filters (search + chips) ---- */
  document.querySelectorAll('[data-filter]').forEach(box => {
    const items = [...document.querySelectorAll(box.dataset.filter)], input = box.querySelector('input'), chips = [...box.querySelectorAll('[data-chip]')];
    let chip = 'all';
    const run = () => { const q = (input ? input.value : '').trim().toLowerCase();
      items.forEach(it => { const okq = !q || it.textContent.toLowerCase().includes(q); const okc = chip === 'all' || (it.dataset.cat || '').split(' ').includes(chip); it.hidden = !(okq && okc); }); if (items[0]) items[0].parentElement.classList.toggle('q', !!q || chip !== 'all'); };
    if (input) input.addEventListener('input', run);
    chips.forEach(c => c.addEventListener('click', () => { chip = c.dataset.chip; chips.forEach(x => x.setAttribute('aria-pressed', String(x === c))); run(); }));
  });
  document.querySelectorAll('.more-c button').forEach(b => b.addEventListener('click', () => { const c = b.closest('.px-body').querySelector('.courses,.names'); c.classList.add('all'); b.parentElement.remove(); }));
  /* ---- kit: past dates (courses, events) — marked at runtime so the static page never goes stale ---- */
  (() => { const now = new Date(); now.setHours(0, 0, 0, 0);
    document.querySelectorAll('[data-end]').forEach(el => { if (new Date(el.dataset.end + 'T23:59:59') >= now) return; el.classList.add('past');
      const t = el.querySelector('.tag'); if (t) { t.textContent = 'Edizione conclusa'; t.className = 'tag past'; }
      const g = el.querySelector('.course .go, .go'); if (g && el.classList.contains('course')) g.firstChild.textContent = 'Avvisami per la prossima edizione ';
      if (el.matches('.course,.post')) el.parentElement.appendChild(el); }); })();
  /* ---- kit: copy e-mail address ---- */
  document.querySelectorAll('[data-copy]').forEach(b => b.addEventListener('click', async () => { const v = b.dataset.copy || location.href, l = b.querySelector('span') || b;
    try { await navigator.clipboard.writeText(v); } catch (e) { const t = document.createElement('textarea'); t.value = v; document.body.appendChild(t); t.select(); try { document.execCommand('copy'); } catch (_) {} t.remove(); }
    const o = l.textContent; l.textContent = b.dataset.copy ? 'Indirizzo copiato' : 'Link copiato'; b.classList.add('ok'); setTimeout(() => { l.textContent = o; b.classList.remove('ok'); }, 2200); }));
  /* ---- kit: photo band parallax ---- */
  const bands = [...document.querySelectorAll('.px-band img')];
  if (bands.length && !reduce) { const bl = () => { const vh = innerHeight; bands.forEach(im => { const r = im.parentElement.getBoundingClientRect(); if (r.bottom > 0 && r.top < vh) im.style.transform = `translate3d(0,${(-(r.top + r.height / 2 - vh / 2) / vh * r.height * .14).toFixed(1)}px,0)`; }); requestAnimationFrame(bl); }; requestAnimationFrame(bl); }
  /* ---- kit: legal table of contents highlight ---- */
  const tocLinks = [...document.querySelectorAll('.toc a')];
  if (tocLinks.length) {
    const hs = tocLinks.map(a => document.querySelector(a.getAttribute('href')));
    const io = new IntersectionObserver(es => es.forEach(e => { if (e.isIntersecting) { const i = hs.indexOf(e.target); tocLinks.forEach((a, j) => a.classList.toggle('on', i === j)); } }), { rootMargin: '-20% 0px -70% 0px' });
    hs.forEach(h => h && io.observe(h));
  }
'''
