# Chi siamo page (Figma 689:121) built from the homepage source: same head, tokens, header, menu, footer, JS.
import re

CSS = r'''
/* ================= CHI SIAMO (Figma 689:121) ================= */
.cs-hero{height:U(516);background:var(--navy-deep)}
.cs-hero .rings{height:U(516)}
.cs-hero .title{position:absolute;left:U(40);top:U(210);width:U(620);margin:0;font:400 U(60)/U(62) var(--serif);letter-spacing:U(-2.4);text-transform:uppercase;color:var(--title-light);z-index:2}
.cs-hero .intro{position:absolute;left:U(953);top:U(218);width:U(447);display:flex;flex-direction:column;align-items:flex-start;gap:U(28);z-index:2}
.cs-hero .intro p{margin:0;font:400 U(18)/U(27) var(--sans);color:var(--title-light)}
.cs-photo{display:block;width:100%;height:U(640);object-fit:cover}
.cs-sec{background:#fff;padding:U(120) 0}
.cs-sec.flush{padding-top:0}
.cs-sec .in{height:auto;padding:0 U(40);box-sizing:border-box}
.cs-head{display:flex;justify-content:space-between;align-items:flex-end;gap:U(40)}
.cs-head .h2{width:U(760)}
.cs-head p{margin:0;width:U(447);font:400 U(18)/U(27) var(--sans);color:rgba(25,35,75,.8)}
/* L'idea */
.idea .cols{margin-top:U(72);display:grid;grid-template-columns:repeat(3,1fr);gap:U(24)}
.idea figure{margin:0}
.idea .ph{overflow:hidden;height:U(520)}
.idea .ph img{display:block;width:100%;height:100%;object-fit:cover;transition:transform 1.6s var(--osmo)}
.idea figure:hover .ph img{transform:scale(1.02)}
.idea h3{margin:U(24) 0 0;font:400 U(22)/U(28) var(--sans);color:var(--navy)}
.idea figure p{margin:U(10) 0 0;font:400 U(16)/U(24) var(--sans);color:rgba(25,35,75,.7)}
/* Team */
.team .h2{width:U(640)}
.sq-ctrl{display:flex;gap:U(8)}
.sq-btn{width:U(40);height:U(40);display:grid;place-items:center;border:1px solid rgba(25,35,75,.5);color:var(--navy);transition:background-color .4s var(--osmo),border-color .4s var(--osmo),opacity .4s var(--osmo)}
.sq-btn .ico{width:U(16);height:U(16)}
.sq-btn.car-prev .ico{transform:scaleX(-1)}
.sq-btn:disabled{border-color:rgba(25,35,75,.15);cursor:default}
.sq-btn:disabled .ico{opacity:.4}
.sq-btn:hover:not(:disabled){background:var(--navy);border-color:var(--navy)}
.sq-btn:hover:not(:disabled) path{stroke:#fff}
.team .car-view{margin-top:U(56);margin-right:calc(-1*(50vw - U(680)));overflow:hidden;cursor:grab;touch-action:pan-y}
.team .car-view.drag{cursor:grabbing}
.team .track{display:flex;gap:U(16);width:max-content;transition:transform 1s var(--osmo);will-change:transform}
.team .car-view.drag .track{transition:none}
.person{flex:none;width:U(380);height:U(440);box-sizing:border-box;padding:U(28);display:flex;flex-direction:column;justify-content:space-between;background:#F3F5FC;color:var(--navy);user-select:none;transition:background-color .5s var(--osmo)}
.person:hover{background:#EBEFFB}
.person .pic{width:U(88);height:U(88);display:grid;place-items:center;background:var(--azzurro);font:400 U(12)/1 var(--sans);color:rgba(25,35,75,.6)}
.person .nm{margin:U(20) 0 0;font:400 U(24)/U(31) var(--sans)}
.person .role{margin:U(4) 0 0;font:400 U(16)/U(22) var(--sans);color:rgba(25,35,75,.55)}
.person .bio{margin:0;font:400 U(16)/U(24) var(--sans);color:rgba(25,35,75,.55)}
.person .more{margin-top:U(20);display:inline-flex;align-items:center;gap:U(6);font:500 U(15)/U(19) var(--sans);color:var(--navy)}
.person .more .ico{width:U(16);height:U(16);transition:transform .5s var(--osmo)}
.person .more:hover .ico{transform:translateX(U(3))}
/* Aree */
.cs-areas .cards{margin-top:U(64);display:grid;grid-template-columns:repeat(3,1fr);gap:U(24);align-items:stretch}
.acard{border:1px solid rgba(25,35,75,.12);background:#fff;display:flex;flex-direction:column}
.acard .ph{height:U(260);overflow:hidden}
.acard .ph img{display:block;width:100%;height:100%;object-fit:cover;transition:transform 1.6s var(--osmo)}
.acard:hover .ph img{transform:scale(1.02)}
.acard .body{padding:U(32) U(32) U(36);display:flex;flex-direction:column;gap:U(16)}
.acard h3{margin:0;font:400 U(28)/U(34) var(--sans);letter-spacing:U(-.28);color:var(--navy)}
.acard p{margin:0;font:400 U(16)/U(24) var(--sans);color:rgba(25,35,75,.8)}
.pills{margin-top:U(4);display:flex;flex-wrap:wrap;gap:U(8)}
.pills a{padding:U(7) U(14);border:1px solid rgba(25,35,75,.25);border-radius:999px;font:400 U(14)/U(18) var(--sans);color:var(--navy);transition:background-color .4s var(--osmo),color .4s var(--osmo),border-color .4s var(--osmo)}
.pills a:hover{background:var(--navy);border-color:var(--navy);color:#fff}
.acard--acc h3{color:#5A1C30}
.acard--acc .pills a{border-color:rgba(90,28,48,.25);color:#5A1C30}
.acard--acc .pills a:hover{background:#5A1C30;border-color:#5A1C30;color:#fff}
/* Recensione */
.cs-rev .block{display:flex;gap:U(24);padding:U(12);background:var(--azzurro)}
.cs-rev .txt{flex:1;min-width:0;padding:U(52) U(32);display:flex;flex-direction:column;justify-content:space-between}
.cs-rev blockquote{margin:0;font:400 U(34)/U(42) var(--serif);letter-spacing:U(-.34);color:var(--navy)}
.cs-rev .who{margin:U(20) 0 0;font:400 U(16)/U(24) var(--sans);color:rgba(25,35,75,.7)}
.cs-rev .btn-solid{display:flex;align-items:center;justify-content:center;gap:U(10);padding:U(14) U(18);border-radius:U(4);background:var(--navy);font:500 U(15)/U(20) var(--sans);color:#fff;transition:background-color .4s var(--osmo)}
.cs-rev .btn-solid:hover{background:var(--navy-deep)}
.cs-rev .btn-solid .ico{width:U(16);height:U(16);transition:transform .5s var(--osmo)}
.cs-rev .btn-solid:hover .ico{transform:translateX(U(3))}
.cs-rev .pic{flex:none;width:U(660);height:U(460);object-fit:cover;display:block}
@media (max-width: 899px){
  .cs-hero{height:auto}
  .cs-hero .in{height:auto}
  .cs-hero .rings{height:100%}
  .cs-hero .title{position:relative;left:auto;top:auto;width:auto;padding-top:130px;font-size:38px;line-height:38px;letter-spacing:-1.4px}
  .cs-hero .intro{position:relative;left:auto;top:auto;width:auto;margin:24px 0 0;padding-bottom:56px;gap:24px}
  .cs-hero .intro p{font-size:17px;line-height:26px}
  .cs-photo{height:70vw}
  .cs-sec{padding:64px 0}.cs-sec.flush{padding-top:0}
  .cs-sec .in{padding:0 max(16px,env(safe-area-inset-left,0px))}
  .cs-head{flex-direction:column;align-items:flex-start;gap:20px}
  .cs-head .h2,.cs-head p,.team .h2{width:auto}
  .cs-head p{font-size:17px;line-height:26px}
  .idea .cols,.cs-areas .cards{grid-template-columns:1fr;gap:40px;margin-top:32px}
  .idea .ph{height:110vw;max-height:520px}
  .team .car-view{margin-top:28px;margin-right:calc(-1*max(16px,env(safe-area-inset-right,0px)))}
  .person{width:calc(100vw - 72px);max-width:380px;height:400px}
  .cs-rev .block{flex-direction:column}
  .cs-rev .txt{padding:28px 16px 16px;gap:32px}
  .cs-rev blockquote{font-size:24px;line-height:31px}
  .cs-rev .pic{width:100%;height:70vw}
  .sq-btn{width:40px;height:40px}
}
'''

HERO = '''<!-- HERO Chi siamo 689:170 -->
<section class="sec hero cs-hero" id="top">
  <div class="in">
    <div class="rings" data-parallax="0.1"><div class="art">__DEVICE_CS__</div></div>
__HEADER__
    <h1 class="title">Diffondiamo una cultura del dialogo</h1>
    <div class="intro">
      <p class="blurin">Aiutiamo le persone ad affrontare i conflitti con maggiore consapevolezza e a trovare soluzioni condivise e durature. In 20 sedi in Italia.</p>
      <a class="btn btn--glass" href="#contatti">Avvia una mediazione __ARROW_W__</a>
    </div>
  </div>
</section>
<img class="cs-photo" src="__IMG_cs_hero__" alt="Un mediatore parla con le parti durante un incontro">
'''

IDEA = [("cs_idea1","Uno spazio per le persone","Ti offriamo uno spazio riservato e confidenziale, in cui sentirti accolto e trovare il professionista più adatto a te."),
        ("cs_idea2","Un alleato per i professionisti","Agli avvocati e ai professionisti del settore legale offriamo servizi pensati per il loro lavoro: dall’analisi del caso alla strategia, dalla conduzione della procedura alla scelta del mediatore."),
        ("cs_idea3","L’esperienza di un gruppo","Competenza e affidabilità nascono da anni di lavoro di un gruppo di professionisti: mediatori civili e commerciali, familiari, sanitari e penali, counselor, coach, psicologi e psicoterapeuti.")]

AREAS = [("cs_area1","","Mediazione","Civile e commerciale, familiare, sanitaria, penale e lavorativa: ti accompagniamo in ogni tipo di mediazione, in sede o online.",[("Civile e commerciale","mediazione-civile.html"),"Familiare","Sanitaria, penale e lavorativa"]),
         ("cs_area2"," acard--acc","DPL Accademy","Siamo ente di formazione accreditato presso il Ministero della Giustizia: corsi per diventare mediatori e percorsi specialistici.",["Civile e commerciale","Familiare","Coordinazione genitoriale","Seminari e aggiornamenti"]),
         ("cs_area3","","DPL Magazine","Notizie, approfondimenti ed eventi sul mondo della mediazione, su dplmagazine.it.",["Rassegna stampa","Eventi","Media e magazine"])]

def person(name, role):
    return (f'<article class="person"><div><div class="pic">[Foto]</div><p class="nm">{name}</p><p class="role">{role}</p></div>'
            f'<div><p class="bio">[Breve presentazione: esperienza, ambiti di mediazione, sede.]</p><a class="more" href="#">Vedi profilo __ARROW_N16__</a></div></article>')

def body():
    idea = '\n'.join(f'''      <figure><div class="ph"><img src="__IMG_{im}__" alt=""></div><h3 class="blurin">{t}</h3><p class="blurin">{p}</p></figure>''' for im,t,p in IDEA)
    people = '\n'.join('        '+person(*x) for x in [("Lucia Di Palermo","[Ruolo]")]+[("[Nome Cognome]","[Ruolo · Sede]")]*7)
    areas = '\n'.join(f'''      <article class="acard{cls}"><div class="ph"><img src="__IMG_{im}__" alt=""></div><div class="body"><h3>{t}</h3><p>{p}</p><div class="pills">{''.join((f'<a href="{x[1]}">{x[0]}</a>' if isinstance(x,tuple) else f'<a href="#">{x}</a>') for x in pills)}</div></div></article>''' for im,cls,t,p,pills in AREAS)
    return f'''<!-- L'IDEA 689:181 -->
<section class="cs-sec idea" id="idea">
  <div class="in">
    <div class="cs-head"><h2 class="h2 blurin">Dove le persone e i professionisti si incontrano</h2><p class="blurin">L’idea nasce dal desiderio di creare una realtà nuova, in cui far incontrare le esigenze delle persone e quelle dei professionisti.</p></div>
    <div class="cols">
{idea}
    </div>
  </div>
</section>

<!-- IL TEAM 689:201 -->
<section class="cs-sec flush team" id="team">
  <div class="in">
    <div class="cs-head head-row"><h2 class="h2 blurin">Le persone che ti accompagnano</h2>
      <div class="sq-ctrl"><button class="sq-btn car-prev" aria-label="Persona precedente" disabled>__ARROW_N16__</button><button class="sq-btn car-next" aria-label="Persona successiva">__ARROW_N16__</button></div></div>
    <div class="car-view" aria-roledescription="carosello" aria-label="Il team">
      <div class="track">
{people}
      </div>
    </div>
  </div>
</section>

<!-- LE NOSTRE AREE 689:306 -->
<section class="cs-sec flush cs-areas" id="aree">
  <div class="in">
    <div class="cs-head"><h2 class="h2 blurin">Mediazione, formazione, informazione</h2><p class="blurin">Tre aree con lo stesso modo di lavorare: ascolto, chiarezza e competenza.</p></div>
    <div class="cards">
{areas}
    </div>
  </div>
</section>

<!-- RECENSIONE 689:352 -->
<section class="cs-sec flush cs-rev" id="recensioni">
  <div class="in">
    <div class="block">
      <div class="txt">
        <div><blockquote>«…la cura, la professionalità e il calore con cui i mediatori DPL accolgono ed accompagnano i clienti nel loro percorso.»</blockquote><p class="who">Silvia B. · Corso biennale di mediazione familiare</p></div>
        <a class="btn-solid" href="https://www.dplmediazione.it/dicono-di-noi.html" target="_blank" rel="noopener">Leggi tutte le recensioni __ARROW_W16__</a>
      </div>
      <img class="pic" src="__IMG_cs_rev__" alt="">
    </div>
  </div>
</section>

'''

def make(src):
    s = src
    s = re.sub(r'<title>[^<]*</title>', '<title>Chi siamo · DPL Mediazione</title>', s, count=1)
    # no logo splash on inner pages
    a = s.index('<!-- splash'); b = s.index('<div class="pill"', a); s = s[:a] + s[b:]
    # header markup, reused from the homepage hero
    h0 = s.index('    <header class="hdr">'); h1 = s.index('</header>', h0) + len('</header>')
    header = s[h0:h1]
    header = header.replace('<a href="__HREF_CHI__">Chi siamo</a>', '<a class="is-active" href="__HREF_CHI__" aria-current="page">Chi siamo</a>')
    # replace everything from the home hero to the closing section
    a = s.index('<!-- HERO 613:2295 -->'); b = s.index('<!-- CTA + FOOTER')
    s = s[:a] + HERO.replace('__HEADER__', header) + body() + s[b:]
    s = s.replace('</style>', CSS + '</style>', 1)
    s = s.replace('__HREF_HOME__', 'dpl-home.html').replace('__HREF_CHI__', '#top')
    ids = set(re.findall(r'id="([^"]+)"', s))
    s = re.sub(r'href="#([A-Za-z][\w-]*)"', lambda m: m.group(0) if m.group(1) in ids else f'href="dpl-home.html#{m.group(1)}"', s)
    s = s.replace('__ARROW_N16__', '__ARROW_N__').replace('__ARROW_W16__', '__ARROW_W__')
    return s
