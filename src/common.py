# Shared building blocks for inner pages (Chi siamo, Mediazione civile…): page skeleton from the home source + common CSS.
import re
HREFS = {'__HREF_HOME__': 'dpl-home.html', '__HREF_CHI__': 'chi-siamo.html', '__HREF_MC__': 'mediazione-civile.html', '__HREF_FAM__': 'mediazione-familiare.html',
         '__HREF_SAN__': 'mediazione-sanitaria.html', '__HREF_FORM__': 'formazione.html', '__HREF_SEDI__': 'sedi.html', '__HREF_MOD__': 'modulistica.html',
         '__HREF_RS__': 'rassegna-stampa.html', '__HREF_EV__': 'eventi.html', '__HREF_CON__': 'contatti.html', '__HREF_EX6__': 'sedi-convenzionate.html', '__HREF_PRIV__': 'privacy.html'}
def hrefs(s, home='dpl-home.html'):
    for k, v in HREFS.items(): s = s.replace(k, home if k == '__HREF_HOME__' else v)
    return s

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
.cs-head{display:flex;justify-content:space-between;align-items:flex-start;gap:U(40)}
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

def page(src, title, body, css='', js='', header_fix=None, self_href=None, cta=True):
    """Build an inner page: no logo splash, home header (optionally adjusted), given body between header-hero and the closing section."""
    s = re.sub(r'<title>[^<]*</title>', f'<title>{title}</title>', src, count=1)
    a = s.index('<!-- splash'); b = s.index('<div class="pill"', a); s = s[:a] + s[b:]
    h0 = s.index('    <header class="hdr">'); h1 = s.index('</header>', h0) + len('</header>')
    header = s[h0:h1]
    if header_fix: header = header_fix(header)
    a = s.index('<!-- HERO 613:2295 -->'); b = s.index('<!-- CTA + FOOTER')
    # One closing call to action per page: a page's own final CTA band replaces the generic one above the footer.
    m = list(re.finditer(r'<section class="px-sec[^"]*"[^>]*>\s*<div class="in">\s*<div class="ctab"><div><h2>(.*?)</h2><p>(.*?)</p></div><div class="btns">(.*?)</div></div>\s*</div>\s*</section>\s*', body, re.S))
    if m and not body[m[-1].end():].strip():
        h2, p, bt = m[-1].groups(); body = body[:m[-1].start()]
        s = s[:b] + re.sub(r'<h2>Hai un conflitto.*?</a></div>', lambda _: f'<h2>{h2}</h2>\n      <div class="intro"><p>{p}</p><div class="btns">{bt}</div></div>', s[b:], count=1, flags=re.S)
    else:
        s = s[:b] + s[b:].replace('href="mailto:info@dplmediazione.it">Avvia una mediazione', 'href="__HREF_CON__#modulo">Avvia una mediazione', 1)
    if cta is False:
        s = s[:b] + re.sub(r'\s*<div class="cta-block">.*?</div>\s*</div>', '', s[b:], count=1, flags=re.S).replace('<section class="sec closing"', '<section class="sec closing short"', 1)
    s = s[:a] + body.replace('__HEADER__', header) + s[b:]
    s = s.replace('</style>', CSS + css + '</style>', 1)
    if js: s = s.replace("  /* ---- splash (logo intro) ---- */", js + "\n  /* ---- splash (logo intro) ---- */", 1)
    s = hrefs(s)
    if self_href: s = s.replace(f'href="{self_href}"', 'href="#top"')
    ids = set(re.findall(r'id="([^"]+)"', s))
    s = re.sub(r'href="#([A-Za-z][\w-]*)"', lambda m: m.group(0) if m.group(1) in ids else f'href="dpl-home.html#{m.group(1)}"', s)
    return s
