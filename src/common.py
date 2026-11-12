# Shared building blocks for inner pages (Chi siamo, Mediazione civile…): page skeleton from the home source + common CSS.
import re

CSS = r'''
/* ================= INNER PAGES · shared ================= */
.cs-hero{height:U(516);background:var(--navy-deep)}
.cs-hero .rings{height:U(516)}
.cs-hero .title{position:absolute;left:U(40);top:U(210);width:U(620);margin:0;font:400 U(60)/U(62) var(--serif);letter-spacing:U(-2.4);text-transform:uppercase;color:var(--title-light);z-index:2}
.cs-hero .intro{position:absolute;left:U(953);top:U(218);width:U(447);display:flex;flex-direction:column;align-items:flex-start;gap:U(28);z-index:2}
.cs-hero .intro p{margin:0;font:400 U(18)/U(27) var(--sans);color:var(--title-light)}
.cs-sec{background:#fff;padding:U(120) 0}
.cs-sec.flush{padding-top:0}
.cs-sec .in{height:auto;padding:0 U(40);box-sizing:border-box}
.cs-head{display:flex;justify-content:space-between;align-items:flex-end;gap:U(40)}
.cs-head .h2{width:U(760)}
.cs-head p{margin:0;width:U(447);font:400 U(18)/U(27) var(--sans);color:rgba(25,35,75,.8)}
.pills{margin-top:U(4);display:flex;flex-wrap:wrap;gap:U(8)}
.pills a{padding:U(7) U(14);border:1px solid rgba(25,35,75,.25);border-radius:999px;font:400 U(14)/U(18) var(--sans);color:var(--navy);transition:background-color .4s var(--osmo),color .4s var(--osmo),border-color .4s var(--osmo)}
.pills a:hover{background:var(--navy);border-color:var(--navy);color:#fff}
@media (max-width: 899px){
  .cs-hero{height:auto}
  .cs-hero .in{height:auto}
  .cs-hero .rings{height:100%}
  .cs-hero .title{position:relative;left:auto;top:auto;width:auto;padding-top:130px;font-size:38px;line-height:38px;letter-spacing:-1.4px}
  .cs-hero .intro{position:relative;left:auto;top:auto;width:auto;margin:24px 0 0;padding-bottom:56px;gap:24px}
  .cs-hero .intro p{font-size:17px;line-height:26px}
  .cs-sec{padding:64px 0}.cs-sec.flush{padding-top:0}
  .cs-sec .in{padding:0 max(16px,env(safe-area-inset-left,0px))}
  .cs-head{flex-direction:column;align-items:flex-start;gap:20px}
  .cs-head .h2,.cs-head p{width:auto}
  .cs-head p{font-size:17px;line-height:26px}
}
'''

def page(src, title, body, css='', js='', header_fix=None, self_href=None):
    """Build an inner page: no logo splash, home header (optionally adjusted), given body between header-hero and the closing section."""
    s = re.sub(r'<title>[^<]*</title>', f'<title>{title}</title>', src, count=1)
    a = s.index('<!-- splash'); b = s.index('<div class="pill"', a); s = s[:a] + s[b:]
    h0 = s.index('    <header class="hdr">'); h1 = s.index('</header>', h0) + len('</header>')
    header = s[h0:h1]
    if header_fix: header = header_fix(header)
    a = s.index('<!-- HERO 613:2295 -->'); b = s.index('<!-- CTA + FOOTER')
    s = s[:a] + body.replace('__HEADER__', header) + s[b:]
    s = s.replace('</style>', CSS + css + '</style>', 1)
    if js: s = s.replace("  /* ---- splash (logo intro) ---- */", js + "\n  /* ---- splash (logo intro) ---- */", 1)
    s = s.replace('__HREF_HOME__', 'dpl-home.html').replace('__HREF_CHI__', 'chi-siamo.html').replace('__HREF_MC__', 'mediazione-civile.html')
    if self_href: s = s.replace(f'href="{self_href}"', 'href="#top"')
    ids = set(re.findall(r'id="([^"]+)"', s))
    s = re.sub(r'href="#([A-Za-z][\w-]*)"', lambda m: m.group(0) if m.group(1) in ids else f'href="dpl-home.html#{m.group(1)}"', s)
    return s
