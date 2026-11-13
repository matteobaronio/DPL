# Chi siamo — v2, interpreted (not copied from the Figma frame): editorial hero, scroll-lit manifesto,
# full-bleed photo band, three rows "how we're here", team carousel, navy index of the three areas.
import common

CSS = r'''
/* ================= CHI SIAMO v2 ================= */
.ab-hero{height:U(860);background:var(--navy-deep)}
.ab-hero .rings{height:U(860)}
.ab-hero h1{position:absolute;left:U(40);top:U(200);margin:0;width:U(1100);font:400 U(104)/U(94) var(--serif);letter-spacing:U(-4.2);text-transform:uppercase;z-index:2}
.ab-hero h1 .a{display:block;color:var(--title-light)}.ab-hero h1 .b{display:block;color:var(--azzurro)}
.ab-hero .foot-row{position:absolute;left:U(40);right:U(40);bottom:U(72);display:flex;justify-content:space-between;align-items:flex-end;gap:U(40);z-index:2}
.ab-hero .facts{display:flex;gap:U(28);font:500 U(14)/U(20) var(--sans);letter-spacing:U(.84);text-transform:uppercase;color:var(--azzurro)}
.ab-hero .facts span{display:flex;align-items:center;gap:U(28)}
.ab-hero .facts span+span::before{content:"";width:U(4);height:U(4);border-radius:50%;background:var(--azzurro);opacity:.6}
.ab-hero .intro{width:U(447);display:flex;flex-direction:column;align-items:flex-start;gap:U(28)}
.ab-hero .intro p{margin:0;font:400 U(18)/U(27) var(--sans);color:var(--title-light)}
.ab-hero .rule{position:absolute;left:U(40);right:U(40);bottom:U(250);height:1px;background:rgba(255,255,255,.12);z-index:2}
/* manifesto: words light up while scrolling */
.manifesto{background:#fff;padding:U(160) 0 U(150)}
.manifesto .in{height:auto;padding:0 U(40);box-sizing:border-box}
.manifesto p{margin:0 0 0 U(240);width:U(1000);font:400 U(44)/U(56) var(--sans);letter-spacing:U(-.88);color:var(--navy)}
.manifesto .w{color:rgba(25,35,75,.16);transition:color .5s var(--osmo)}
.manifesto .w.lit{color:var(--navy)}
/* photo band with parallax */
.band{position:relative;height:U(640);overflow:hidden}
.band img{position:absolute;left:0;top:-10%;width:100%;height:120%;object-fit:cover;will-change:transform}
/* three rows */
.rows{margin-top:U(72);border-top:1px solid rgba(25,35,75,.12)}
.rowx{display:grid;grid-template-columns:U(80) U(420) 1fr U(300);gap:U(32);align-items:start;padding:U(32) 0;border-bottom:1px solid rgba(25,35,75,.12)}
.rowx .n{font:400 U(16)/U(32) var(--serif);letter-spacing:U(-.96);color:rgba(25,35,75,.5)}
.rowx h3{margin:0;font:400 U(30)/U(36) var(--sans);letter-spacing:U(-.3);color:var(--navy)}
.rowx p{margin:0;max-width:U(440);font:400 U(17)/U(26) var(--sans);color:rgba(25,35,75,.75)}
.rowx .ph{height:U(200);overflow:hidden}
.rowx .ph img{display:block;width:100%;height:100%;object-fit:cover;transform:scale(1.001);transition:transform 1.4s var(--osmo)}
.rowx:hover .ph img{transform:scale(1.04)}
/* team */
.ab-team .cs-head{align-items:flex-end}
.ab-team .ctrl{display:flex;gap:U(12)}
.ab-team .car-view{margin-top:U(56);margin-right:calc(-1*(50vw - U(680)));overflow:hidden;cursor:grab;touch-action:pan-y}
.ab-team .car-view.drag{cursor:grabbing}
.ab-team .track{display:flex;gap:U(20);width:max-content;transition:transform 1s var(--osmo);will-change:transform}
.ab-team .car-view.drag .track{transition:none}
.mate{flex:none;width:U(320);user-select:none}
.mate .pic{height:U(400);display:grid;place-items:center;background:#F3F5FC;font:400 U(13)/1 var(--sans);color:rgba(25,35,75,.45);transition:background-color .5s var(--osmo)}
.mate:hover .pic{background:#EBEFFB}
.mate .nm{margin:U(20) 0 0;font:400 U(22)/U(28) var(--sans);color:var(--navy)}
.mate .role{margin:U(4) 0 0;font:400 U(15)/U(22) var(--sans);color:rgba(25,35,75,.55)}
/* areas index (navy) */
.ab-areas{background:#F3F5FC;color:var(--navy);padding:U(120) 0}
.ab-areas .in{height:auto;padding:0 U(40);box-sizing:border-box}
.idx{margin-top:U(64);border-top:1px solid rgba(25,35,75,.14)}
.idx a{display:grid;grid-template-columns:U(80) 1fr U(447) U(40);gap:U(32);align-items:center;padding:U(36) 0;border-bottom:1px solid rgba(25,35,75,.14);color:var(--navy);transition:color .5s var(--osmo)}
.idx .n{font:400 U(16)/1 var(--serif);color:rgba(25,35,75,.45)}
.idx .t{font:400 U(64)/U(60) var(--serif);letter-spacing:U(-2.6);text-transform:uppercase;transition:transform .8s var(--osmo)}
.idx .d{font:400 U(16)/U(24) var(--sans);color:rgba(25,35,75,.7)}
.idx .ar{width:U(40);height:U(40);border-radius:50%;border:1px solid rgba(25,35,75,.25);display:grid;place-items:center;transition:background-color .5s var(--osmo),border-color .5s var(--osmo)}
.idx .ar .ico{width:U(18);height:U(18)}
.idx a:hover{color:#3B4A8C}
.idx a:hover .t{transform:translateX(U(16))}
.idx a:hover .ar{background:var(--navy);border-color:var(--navy)}
.idx a:hover .ar path{stroke:#fff}
/* recensioni */
.ab-rev{background:#fff;padding:0 0 U(120)}
.ab-rev .in{height:auto;padding:0 U(40);box-sizing:border-box}
.revs{margin-top:U(56);display:grid;grid-template-columns:repeat(3,1fr);gap:U(16)}
.revs figure{margin:0;padding:U(32) U(28);background:#F3F5FC;display:flex;flex-direction:column;gap:U(24);min-height:U(300);box-sizing:border-box}
.revs blockquote{margin:0;font:400 U(22)/U(30) var(--serif);letter-spacing:U(-.2);color:var(--navy)}
.revs figcaption{margin-top:auto;padding-top:U(18);border-top:1px solid rgba(25,35,75,.12);font:500 U(15)/U(22) var(--sans);color:var(--navy)}
.revs figcaption span{display:block;font-weight:400;color:rgba(25,35,75,.6)}
.ab-rev .more{margin-top:U(32)}
@media (max-width: 899px){
  .ab-rev{padding-bottom:64px}
  .ab-rev .in{padding:0 max(16px,env(safe-area-inset-left,0px))}
  .revs{grid-template-columns:1fr;gap:12px;margin-top:28px}
  .revs figure{min-height:0;padding:24px}
  .revs blockquote{font-size:20px;line-height:27px}
  .ab-hero{height:auto}
  .ab-hero .in{height:auto;padding:0 max(16px,env(safe-area-inset-left,0px));box-sizing:border-box}
  .ab-hero .rings{height:100%}
  .ab-hero h1{position:relative;left:auto;top:auto;width:auto;padding-top:132px;font-size:46px;line-height:44px;letter-spacing:-1.8px}
  .ab-hero .rule{position:relative;left:auto;right:auto;bottom:auto;margin:40px 0 24px}
  .ab-hero .foot-row{position:relative;left:auto;right:auto;bottom:auto;flex-direction:column-reverse;align-items:flex-start;gap:32px;padding-bottom:48px}
  .ab-hero .intro{width:auto;gap:24px}
  .ab-hero .intro p{font-size:17px;line-height:26px}
  .ab-hero .facts{flex-wrap:wrap;gap:10px 16px;font-size:12px;letter-spacing:.7px}
  .ab-hero .facts span{gap:16px}
  .manifesto{padding:80px 0 72px}
  .manifesto .in{padding:0 max(16px,env(safe-area-inset-left,0px))}
  .manifesto p{margin:0;width:auto;font-size:27px;line-height:36px;letter-spacing:-.5px}
  .band{height:72vw}
  .rows{margin-top:32px}
  .rowx{grid-template-columns:36px 1fr;gap:6px 12px;padding:24px 0 28px}
  .rowx .ph{grid-column:1 / -1;grid-row:1;height:58vw;margin-bottom:18px}
  .rowx .n{grid-column:1;grid-row:2;line-height:30px}
  .rowx h3{grid-column:2;grid-row:2;font-size:24px;line-height:30px}
  .rowx p{grid-column:2;grid-row:3;font-size:16px;line-height:24px}
  .ab-team .car-view{margin-top:28px;margin-right:calc(-1*max(16px,env(safe-area-inset-right,0px)))}
  .ab-team .cs-head{gap:20px}
  .ab-team .ctrl{gap:8px;align-self:flex-end}
  .mate{width:68vw;max-width:300px}
  .mate .pic{height:86vw;max-height:380px}
  .ab-areas{padding:64px 0}
  .ab-areas .in{padding:0 max(16px,env(safe-area-inset-left,0px))}
  .idx{margin-top:32px}
  .idx a{grid-template-columns:28px 1fr 36px;gap:8px 12px;padding:24px 0}
  .idx .n{grid-row:1}
  .idx .t{font-size:32px;line-height:32px;letter-spacing:-1.2px}
  .idx .d{grid-column:2 / 4;grid-row:2;font-size:15px;line-height:22px}
  .idx .ar{grid-column:3;grid-row:1;width:36px;height:36px}
}
'''

MANIFESTO = ('Aiutiamo le persone ad affrontare i conflitti con maggiore consapevolezza e a trovare soluzioni condivise e durature. '
             'Per questo abbiamo creato uno spazio in cui le esigenze delle persone e quelle dei professionisti si incontrano.')

ROWS = [('01', 'Uno spazio per le persone', 'Ti offriamo uno spazio riservato e confidenziale, in cui sentirti accolto e trovare il professionista più adatto a te.', 'cs_idea1'),
        ('02', 'Un alleato per i professionisti', 'Agli avvocati e ai professionisti del settore legale offriamo servizi pensati per il loro lavoro: dall’analisi del caso alla strategia, dalla conduzione della procedura alla scelta del mediatore.', 'cs_idea2'),
        ('03', 'L’esperienza di un gruppo', 'Competenza e affidabilità nascono da anni di lavoro di un gruppo di professionisti: mediatori civili e commerciali, familiari, sanitari e penali, counselor, coach, psicologi e psicoterapeuti.', 'cs_idea3')]

AREAS = [('01', 'Mediazione', 'Civile e commerciale, familiare, sanitaria, penale e lavorativa: ti accompagniamo in ogni tipo di mediazione, in sede o online.', '__HREF_MC__', ''),
         ('02', 'DPL Accademy', 'Siamo ente di formazione accreditato presso il Ministero della Giustizia: corsi per diventare mediatori e percorsi specialistici.', '__HREF_FORM__', ' data-acc'),
         ('03', 'DPL Magazine', 'Notizie, approfondimenti ed eventi sul mondo della mediazione, su dplmagazine.it.', 'https://www.dplmagazine.it/', ' target="_blank" rel="noopener"')]

JS = '''
  /* ---- Chi siamo: manifesto words light up with scroll; photo band parallax ---- */
  const mani = document.querySelector('.manifesto p');
  if (mani) {
    const words = [...mani.querySelectorAll('.w')], band = document.querySelector('.band img');
    const loop = () => {
      const vh = innerHeight, r = mani.getBoundingClientRect();
      const p = reduce ? 1 : Math.min(1, Math.max(0, (vh * .82 - r.top) / (r.height + vh * .35)));
      const n = Math.round(p * words.length); words.forEach((w, i) => w.classList.toggle('lit', i < n));
      if (band && !reduce) { const b = band.parentElement.getBoundingClientRect(); if (b.bottom > 0 && b.top < vh) band.style.transform = `translate3d(0,${(-(b.top + b.height / 2 - vh / 2) / vh * b.height * .14).toFixed(1)}px,0)`; }
      requestAnimationFrame(loop);
    };
    requestAnimationFrame(loop);
  }
'''

def make(src):
    words = ' '.join(f'<span class="w">{w}</span>' for w in MANIFESTO.split(' '))
    rows = '\n'.join(f'      <article class="rowx"><span class="n">{n}</span><h3>{t}</h3><p>{p}</p><div class="ph"><img src="__IMG_{im}__" alt=""></div></article>' for n, t, p, im in ROWS)
    mates = '\n'.join(f'        <article class="mate"><div class="pic">[Foto]</div><p class="nm">{n}</p><p class="role">{r}</p></article>'
                      for n, r in [('Lucia Di Palermo', '[Ruolo]')] + [('[Nome Cognome]', '[Ruolo · Sede]')] * 7)
    idx = '\n'.join(f'      <a href="{h}"{x}><span class="n">{n}</span><span class="t">{t}</span><span class="d">{d}</span><span class="ar">__ARROW_N__</span></a>' for n, t, d, h, x in AREAS)
    body = f'''<!-- HERO · Chi siamo v2 -->
<section class="sec hero ab-hero" id="top">
  <div class="in">
    <div class="rings" data-parallax="0.1"><div class="art">__DEVICE_HERO__</div></div>
__HEADER__
    <h1><span class="a">Diffondiamo una cultura</span><span class="b">del dialogo.</span></h1>
    <div class="rule"></div>
    <div class="foot-row">
      <div class="facts"><span>Organismo n. 1075</span><span>20 sedi in Italia</span><span>Mediazione e formazione</span></div>
      <div class="intro"><p class="blurin">Siamo mediatori, formatori e professionisti che lavorano insieme perché un conflitto possa diventare un dialogo.</p><a class="btn btn--glass" href="#contatti">Avvia una mediazione __ARROW_W__</a></div>
    </div>
  </div>
</section>

<!-- MANIFESTO -->
<section class="manifesto" id="idea">
  <div class="in">
    <p>{words}</p>
  </div>
</section>

<div class="band"><img src="__IMG_cs_hero__" alt="Un mediatore parla con le parti durante un incontro"></div>

<!-- COME CI SIAMO -->
<section class="cs-sec" id="come-ci-siamo">
  <div class="in">
    <div class="cs-head"><h2 class="h2 blurin">Dove le persone e i professionisti si incontrano</h2><p class="blurin">Tre modi di esserci, con lo stesso approccio: ascolto, chiarezza e competenza.</p></div>
    <div class="rows">
{rows}
    </div>
  </div>
</section>

<!-- TEAM -->
<section class="cs-sec flush ab-team" id="team">
  <div class="in">
    <div class="cs-head"><h2 class="h2 blurin">Le persone che ti accompagnano</h2>
      <div class="ctrl"><button class="rv-btn prev car-prev" aria-label="Persona precedente" disabled>__ARROW_N__</button><button class="rv-btn next car-next" aria-label="Persona successiva">__ARROW_N__</button></div></div>
    <div class="car-view" aria-roledescription="carosello" aria-label="Il team">
      <div class="track">
{mates}
      </div>
    </div>
  </div>
</section>

<!-- RECENSIONI -->
<section class="ab-rev" id="recensioni">
  <div class="in">
    <div class="cs-head"><h2 class="h2 blurin">Dicono di noi</h2><p class="blurin">Le parole di chi ha fatto un percorso con noi, in mediazione o in formazione.</p></div>
    <div class="revs">
      <figure><blockquote>«I mediatori hanno creato un ambiente sereno e rispettoso, dove tutti si sono sentiti ascoltati senza giudizio.»</blockquote><figcaption>Maria Cristina Paolillo<span>Mediazione civile e commerciale</span></figcaption></figure>
      <figure><blockquote>«…la cura, la professionalità e il calore con cui i mediatori DPL accolgono ed accompagnano i clienti nel loro percorso.»</blockquote><figcaption>Silvia B.<span>Corso biennale di mediazione familiare</span></figcaption></figure>
      <figure><blockquote>«Organismo ben organizzato e gestito sia sul piano tecnico sia umano.»</blockquote><figcaption>Stefano Saglimbeni<span>Mediazione</span></figcaption></figure>
    </div>
  </div>
</section>

<!-- AREE -->
<section class="ab-areas" id="aree">
  <div class="in">
    <div class="cs-head"><h2 class="h2 blurin">Mediazione, formazione, informazione</h2><p class="blurin">Tre aree con lo stesso modo di lavorare.</p></div>
    <nav class="idx" aria-label="Le nostre aree">
{idx}
    </nav>
  </div>
</section>

'''
    hdr = lambda h: h.replace('<a href="__HREF_CHI__">Chi siamo</a>', '<a class="is-active" href="__HREF_CHI__" aria-current="page">Chi siamo</a>')
    s = common.page(src, 'Chi siamo · DPL Mediazione', body, CSS, JS, hdr, 'chi-siamo.html')
    return s
