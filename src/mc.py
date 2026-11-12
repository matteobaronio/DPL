# Mediazione civile e commerciale — built directly in code (no Figma frame yet), on the home + Chi siamo system.
# Content: dplmediazione.it/mediazione-civile.html (facts kept, copy rewritten in the DPL voice: "noi", "tu").
import re, common

DOCS = 'docs/'
MATERIE = ['Affitto di azienda','Condominio','Contratti assicurativi, bancari e finanziari','Contratti di associazione in partecipazione',
  'Contratti di franchising','Contratti di consorzio','Contratti d’opera','Contratti di rete','Contratti di somministrazione',
  'Contratti di subfornitura','Diritti reali','Divisione','Locazione e comodato','Opposizione a decreto ingiuntivo','Patti di famiglia',
  'Risarcimento danni da responsabilità medica e sanitaria','Risarcimento danni da diffamazione a mezzo stampa o con altri mezzi di informazione',
  'Società di persone','Successioni ereditarie']
MODULI = [('Domanda di mediazione','domanda_di_mediazione_v07.pdf'),('Domanda di mediazione congiunta','domanda_di_mediazione_congiunta_v07.pdf'),
  ('Allegato A · Adeguata verifica','ALLEGATO_A_ADEGUATA_VERIFICA_v07.pdf'),('Allegato B · Ulteriori parti','ALLEGATO_B_ULTERIORI_PARTI_v07.pdf'),
  ('Allegato C · Ulteriori difensori','ALLEGATO_C_ULTERIORI_DIFENSORI_v07.pdf'),('Regolamento','regolamento_DPL_2025.pdf'),
  ('Modulo di adesione','modulo_adesione_primo_incontro_v07.pdf'),('Delega all’assistenza in mediazione','delega_assistenza_mediazione_v06.pdf'),
  ('Procura speciale sostanziale (se non puoi partecipare di persona)','procura_speciale_sostanziale_mediazione_v06.pdf')]

CSS = r'''
/* ================= MEDIAZIONE CIVILE E COMMERCIALE (codice, nessun frame Figma) ================= */
.mc-hero .title{width:U(700)}
.mc-hero .btns{display:flex;gap:U(16);flex-wrap:wrap}
.facts{margin-top:U(72);display:grid;grid-template-columns:repeat(3,1fr);gap:U(24)}
.fact{border-left:1px solid rgba(25,35,75,.15);padding-left:U(23)}
.fact .fnum{margin:0;font:400 U(96)/U(88) var(--serif);letter-spacing:U(-6);color:var(--navy);white-space:nowrap}
.fact .fnum small{font-size:U(32);letter-spacing:U(-1);margin-left:U(6)}
.fact p{margin:U(28) 0 0;width:U(330);font:400 U(16)/U(24) var(--sans);color:rgba(25,35,75,.7)}
/* tipi: foto + accordion */
.tipi .grid{margin-top:U(64);display:grid;grid-template-columns:U(560) 1fr;gap:U(80);align-items:start}
.tipi .pic{position:sticky;top:U(110);height:U(700);overflow:hidden}
.tipi .pic img{display:block;width:100%;height:100%;object-fit:cover}
.acc{border-top:1px solid rgba(25,35,75,.12)}
.acc-item{border-bottom:1px solid rgba(25,35,75,.12)}
.acc-head{width:100%;display:flex;align-items:center;gap:U(20);padding:U(28) 0;text-align:left;color:var(--navy)}
.acc-n{flex:none;width:U(28);font:400 U(16)/1 var(--serif);letter-spacing:U(-.96);color:rgba(25,35,75,.5);transition:color .5s var(--osmo)}
.acc-t{flex:1;font:400 U(26)/U(32) var(--sans);letter-spacing:U(-.26);transition:color .5s var(--osmo)}
.acc-head .ico{width:U(20);height:U(20);transition:transform .6s var(--osmo)}
.acc-item.open .acc-head .ico{transform:rotate(180deg)}
.acc-item.open .acc-n{color:var(--navy)}
.acc-body{display:grid;grid-template-rows:0fr;transition:grid-template-rows .7s var(--osmo)}
.acc-item.open .acc-body{grid-template-rows:1fr}
.acc-body>div{overflow:hidden;min-height:0}
.acc-body p{margin:0;padding:0 0 U(16) U(48);font:400 U(16)/U(24) var(--sans);color:rgba(25,35,75,.75);max-width:U(620)}
.acc-body .chips{display:flex;flex-wrap:wrap;gap:U(8);padding:U(4) 0 U(32) U(48)}
.acc-body .chips span{padding:U(7) U(14);border:1px solid rgba(25,35,75,.2);border-radius:999px;font:400 U(14)/U(18) var(--sans);color:var(--navy)}
.acc-body p:last-child{padding-bottom:U(32)}
/* come si svolge */
.steps4{margin-top:U(64);display:grid;grid-template-columns:repeat(4,1fr);gap:U(16)}
.s4{background:#F3F5FC;padding:U(28);min-height:U(300);box-sizing:border-box;display:flex;flex-direction:column;transition:background-color .5s var(--osmo)}
.s4:hover{background:#EBEFFB}
.s4 .n{font:400 U(40)/1 var(--serif);letter-spacing:U(-2);color:var(--navy)}
.s4 h3{margin:auto 0 0;padding-top:U(40);font:400 U(22)/U(28) var(--sans);color:var(--navy)}
.s4 p{margin:U(10) 0 0;font:400 U(16)/U(24) var(--sans);color:rgba(25,35,75,.7)}
.notes{margin-top:U(56);display:grid;grid-template-columns:repeat(3,1fr);gap:U(24)}
.note{border-top:1px solid rgba(25,35,75,.15);padding-top:U(20)}
.note h3{margin:0;font:500 U(16)/U(22) var(--sans);color:var(--navy)}
.note p{margin:U(8) 0 0;font:400 U(16)/U(24) var(--sans);color:rgba(25,35,75,.7)}
/* avvia */
.avvia .block{background:var(--azzurro);padding:U(56) U(44) U(44)}
.avvia .h2{width:U(760)}
.avvia .two{margin-top:U(44);display:grid;grid-template-columns:1fr 1fr;gap:U(16)}
.opt{background:#fff;padding:U(36) U(32) U(32);display:flex;flex-direction:column;gap:U(16)}
.opt h3{margin:0;font:400 U(28)/U(34) var(--sans);letter-spacing:U(-.28);color:var(--navy)}
.opt p{margin:0;font:400 U(16)/U(24) var(--sans);color:rgba(25,35,75,.8)}
.opt .acts{margin-top:auto;padding-top:U(16);display:flex;flex-wrap:wrap;gap:U(8)}
.btn-navy{display:inline-flex;align-items:center;gap:U(10);padding:U(13) U(16) U(13) U(20);border-radius:U(5);background:var(--navy);font:500 U(15)/normal var(--sans);color:#fff;transition:background-color .4s var(--osmo)}
.btn-navy:hover{background:var(--navy-deep)}
.btn-navy .ico{width:U(18);height:U(18);transition:transform .5s var(--osmo)}
.btn-navy:hover .ico{transform:translateX(U(3))}
.opt .pills a{display:inline-flex;align-items:center;gap:U(6)}
.pills .dl,.docs .dl{width:U(14);height:U(14);flex:none}
/* costi */
.costi .links{margin-top:U(40);display:flex;flex-wrap:wrap;gap:U(8)}
.costi .cols{margin-top:U(64);display:grid;grid-template-columns:1fr 1fr;gap:U(80)}
.costi h3.col-t{margin:0 0 U(8);font:400 U(26)/U(32) var(--sans);letter-spacing:U(-.26);color:var(--navy)}
.costi .col-sub{margin:0 0 U(24);font:400 U(14)/U(20) var(--sans);color:rgba(25,35,75,.6)}
.row{border-top:1px solid rgba(25,35,75,.12);padding:U(20) 0 U(24);display:grid;grid-template-columns:U(200) 1fr;gap:U(24)}
.row h4{margin:0;font:500 U(16)/U(24) var(--sans);color:var(--navy)}
.row p{margin:0;font:400 U(16)/U(24) var(--sans);color:rgba(25,35,75,.75)}
/* modulistica */
.docs{margin-top:U(56);display:grid;grid-template-columns:1fr 1fr;column-gap:U(80)}
.docs a{display:flex;align-items:center;gap:U(14);padding:U(20) 0;border-top:1px solid rgba(25,35,75,.12);font:400 U(18)/U(26) var(--sans);color:var(--navy);transition:color .4s var(--osmo)}
.docs a .ic{width:U(20);height:U(20);flex:none}
.docs a span{flex:1}
.docs a .dl{transition:transform .5s var(--osmo)}
.docs a:hover{color:#3B4A8C}
.docs a:hover .dl{transform:translateY(U(2))}
@media (max-width: 899px){
  .mc-hero .title{width:auto}
  .facts,.steps4,.notes,.avvia .two,.costi .cols,.docs{grid-template-columns:1fr}
  .facts{gap:32px;margin-top:40px}
  .fact .fnum{font-size:72px;line-height:68px;letter-spacing:-4px}
  .fact p{width:auto;margin-top:16px}
  .tipi .grid{grid-template-columns:1fr;gap:32px;margin-top:32px}
  .tipi .pic{position:relative;top:auto;height:100vw;max-height:520px}
  .acc-head{padding:22px 0}
  .acc-t{font-size:21px;line-height:27px}
  .acc-body p,.acc-body .chips{padding-left:0}
  .steps4{margin-top:32px}
  .s4{min-height:0}
  .s4 h3{padding-top:28px}
  .notes{margin-top:32px}
  .avvia .block{padding:32px 16px 16px}
  .avvia .h2{width:auto}
  .avvia .two{margin-top:28px}
  .opt{padding:24px 20px}
  .costi .cols{gap:48px;margin-top:40px}
  .row{grid-template-columns:1fr;gap:6px}
  .docs{margin-top:32px}
}
'''

DL = '<svg class="dl" viewBox="0 0 16 16" fill="none" aria-hidden="true"><path d="M8 2.5v8m-3.5-3.5L8 10.5l3.5-3.5M3 13.5h10" stroke="currentColor" stroke-width="1.4" stroke-linecap="round" stroke-linejoin="round"/></svg>'

def pdf(name, f, cls=''):
    return f'<a{cls} href="{DOCS}{f}" target="_blank" rel="noopener">{name} {DL}</a>'

def _hdr(h):
    h = h.replace('<button class="dd-btn" aria-expanded="false" aria-haspopup="true">Mediazione', '<button class="dd-btn is-active" aria-expanded="false" aria-haspopup="true">Mediazione', 1)
    return h.replace('<a href="__HREF_MC__">Civile e commerciale</a>', '<a href="__HREF_MC__" aria-current="page">Civile e commerciale</a>')

def make(src):
    chips = ''.join(f'<span>{m}</span>' for m in MATERIE)
    tipi = [
      ('01','Obbligatoria', f'<p>Per queste materie la legge chiede di tentare la mediazione prima di rivolgersi al giudice.</p><div class="chips">{chips}</div>'),
      ('02','Volontaria', '<p>Puoi sceglierla liberamente per qualsiasi controversia su diritti disponibili, anche senza avvocato o con l’assistenza di un altro professionista.</p><p>Per esempio: recupero crediti (commerciali, condominiali, privati), risarcimento danni, appalto, prestazione d’opera manuale e intellettuale, contestazione di lavori, contratti d’agenzia.</p>'),
      ('03','Demandata dal giudice', '<p>Durante una causa il giudice può invitare le parti a tentare la mediazione presso un organismo. In questo caso il tentativo è obbligatorio.</p>'),
      ('04','Prevista da un contratto', '<p>Un contratto o uno statuto può contenere una clausola che prevede la mediazione prima di ogni altra strada.</p>'),
    ]
    acc = '\n'.join(f'''        <div class="acc-item{' open' if i==0 else ''}"><button class="acc-head" aria-expanded="{'true' if i==0 else 'false'}"><span class="acc-n">{n}</span><span class="acc-t">{t}</span>__ACC__</button><div class="acc-body"><div>{b}</div></div></div>''' for i,(n,t,b) in enumerate(tipi))
    steps = [('01','Presenta la domanda','Online dall’area riservata, via e-mail o PEC. Bastano i dati delle parti e una breve descrizione della controversia.'),
             ('02','Informiamo le parti','Invitiamo le altre parti, nominiamo il mediatore e fissiamo la data del primo incontro.'),
             ('03','Vi incontrate','Il primo incontro si svolge in sede o in videoconferenza: il mediatore ascolta tutti e vi aiuta a trovare un terreno comune.'),
             ('04','Raggiungete l’accordo','Se trovate un’intesa, la mettiamo per iscritto. L’accordo firmato da voi e dai vostri avvocati ha valore di titolo esecutivo.')]
    s4 = '\n'.join(f'      <article class="s4"><span class="n">{n}</span><h3>{t}</h3><p>{p}</p></article>' for n,t,p in steps)
    docs = '\n'.join(f'      <a href="{DOCS}{f}" target="_blank" rel="noopener">__ICO_FILE__<span>{n}</span>{DL}</a>' for n,f in MODULI)
    body = f'''<!-- HERO -->
<section class="sec hero cs-hero mc-hero" id="top">
  <div class="in">
    <div class="rings" data-parallax="0.1"><div class="art">__DEVICE_CS__</div></div>
__HEADER__
    <h1 class="title">Mediazione civile e commerciale</h1>
    <div class="intro">
      <p class="blurin">Ti aiutiamo a risolvere una controversia senza andare in tribunale: in tempi brevi, con costi certi, in sede o in videoconferenza.</p>
      <div class="btns"><a class="btn btn--glass" href="https://www.dplmediazione.eu/" target="_blank" rel="noopener">Avvia una mediazione __ARROW_W__</a><a class="btn btn--line" href="#modulistica">Scarica la domanda __ARROW_W__</a></div>
    </div>
  </div>
</section>

<!-- CHE COS'È -->
<section class="cs-sec" id="cos-e">
  <div class="in">
    <div class="cs-head"><h2 class="h2 blurin">Che cos’è la mediazione</h2><p class="blurin">È un modo per risolvere una controversia senza passare dal giudice: un mediatore terzo e imparziale aiuta le parti a trovare un accordo che risponda davvero alle loro esigenze. La regola il D.lgs. 28/2010.</p></div>
    <div class="facts">
      <div class="fact"><p class="fnum">1075</p><p class="blurin">Il nostro numero di iscrizione al Registro degli Organismi di Mediazione del Ministero della Giustizia.</p></div>
      <div class="fact"><p class="fnum">3 <small>mesi</small></p><p class="blurin">La durata della procedura dal deposito della domanda, prorogabile di altri tre.</p></div>
      <div class="fact"><p class="fnum">€ 600</p><p class="blurin">Il credito d’imposta massimo per procedura se raggiungete l’accordo; la metà se non lo raggiungete.</p></div>
    </div>
  </div>
</section>

<!-- TIPI DI MEDIAZIONE -->
<section class="cs-sec flush tipi" id="tipi">
  <div class="in">
    <div class="cs-head"><h2 class="h2 blurin">Quando si fa la mediazione</h2><p class="blurin">Per alcune materie è obbligatoria prima di andare in tribunale. Negli altri casi puoi sceglierla tu, oppure la chiede il giudice o un contratto.</p></div>
    <div class="grid">
      <div class="pic"><img src="__IMG_card1w__" alt="Un uomo ascolta durante un incontro di mediazione"></div>
      <div class="acc" id="acc">
{acc}
      </div>
    </div>
  </div>
</section>

<!-- COME SI SVOLGE -->
<section class="cs-sec flush come" id="come-si-svolge">
  <div class="in">
    <div class="cs-head"><h2 class="h2 blurin">Come si svolge</h2><p class="blurin">Senza formalità, in tempi brevi e con costi certi. Ci occupiamo noi di ogni passaggio.</p></div>
    <div class="steps4">
{s4}
    </div>
    <div class="notes">
      <div class="note"><h3>Riservatezza</h3><p class="blurin">Chi partecipa è tenuto alla riservatezza. Salvo diverso accordo tra le parti, quello che viene detto non può essere usato in un futuro giudizio sulla stessa controversia.</p></div>
      <div class="note"><h3>Competenza territoriale</h3><p class="blurin">Come per una causa, la domanda va presentata a un organismo nel luogo del giudice competente per la controversia. Con 20 sedi in Italia, trovi quella giusta.</p></div>
      <div class="note"><h3>Anche a distanza</h3><p class="blurin">Puoi partecipare in videoconferenza, da dove ti trovi, con la stessa validità di un incontro in sede.</p></div>
    </div>
  </div>
</section>

<!-- AVVIA -->
<section class="cs-sec flush avvia" id="avvia">
  <div class="in">
    <div class="block">
      <h2 class="h2 blurin">Avvia una mediazione</h2>
      <div class="two">
        <article class="opt"><h3>Online, dall’area riservata</h3><p>Con le tue credenziali depositi la domanda in pochi minuti, scegli la data del primo incontro dal nostro calendario e segui lo stato della mediazione. L’area riservata è gratuita.</p>
          <div class="acts"><a class="btn-navy" href="https://www.dplmediazione.eu/" target="_blank" rel="noopener">Accedi all’area riservata __ARROW_W__</a></div></article>
        <article class="opt"><h3>Con il modulo</h3><p>Scarica la domanda, compilala e inviala per e-mail a <a href="mailto:info@dplmediazione.it">info@dplmediazione.it</a> o via PEC. Se ci sono più parti o più avvocati, aggiungi gli allegati.</p>
          <div class="acts pills">{pdf('Domanda di mediazione','domanda_di_mediazione_v07.pdf')}{pdf('Allegato A','ALLEGATO_A_ADEGUATA_VERIFICA_v07.pdf')}{pdf('Allegato B','ALLEGATO_B_ULTERIORI_PARTI_v07.pdf')}{pdf('Allegato C','ALLEGATO_C_ULTERIORI_DIFENSORI_v07.pdf')}</div></article>
      </div>
    </div>
  </div>
</section>

<!-- COSTI E AGEVOLAZIONI -->
<section class="cs-sec flush costi" id="costi">
  <div class="in">
    <div class="cs-head"><h2 class="h2 blurin">Costi e agevolazioni</h2><p class="blurin">Le tariffe sono predeterminate e contenute, secondo il D.M. 145/2011 e successive modifiche. In più, lo Stato riconosce crediti d’imposta ed esenzioni.</p></div>
    <div class="links pills">{pdf('Tabella costi · mediazioni volontarie','INDENNITA_MEDIAZIONI_VOLONTARIE_DPL_2025.pdf')}{pdf('Tabella costi · materie obbligatorie','INDENNITA_MEDIAZIONI_OBBLIGATORIE_DPL_2025.pdf')}{pdf('Tabelle ministeriali','tabella_ministero_2024.pdf')}</div>
    <div class="cols">
      <div><h3 class="col-t">Credito d’imposta</h3><p class="col-sub">D.M. 1 agosto 2023 · art. 20 D.lgs. 28/2010</p>
        <div class="row"><h4>Se raggiungete l’accordo</h4><p>Credito pari all’indennità pagata all’organismo, fino a € 600. Se la mediazione è obbligatoria, anche per il compenso dell’avvocato, fino a € 600. Limite di € 600 per procedura e, ogni anno, di € 2.400 per le persone fisiche e € 24.000 per le persone giuridiche.</p></div>
        <div class="row"><h4>Se l’accordo non arriva</h4><p>I crediti d’imposta sono ridotti della metà.</p></div>
        <div class="row"><h4>Se la causa si chiude con l’accordo</h4><p>Credito pari al contributo unificato versato per il giudizio, fino a € 518.</p></div>
      </div>
      <div><h3 class="col-t">Esenzioni e patrocinio</h3><p class="col-sub">Per tutte le mediazioni</p>
        <div class="row"><h4>Nessuna imposta di bollo</h4><p>Atti, documenti e provvedimenti della mediazione sono esenti da bollo e da ogni spesa, tassa o diritto.</p></div>
        <div class="row"><h4>Registro gratuito fino a € 100.000</h4><p>Il verbale con l’accordo è esente dall’imposta di registro fino a € 100.000 di valore; oltre, l’imposta si paga solo sulla parte eccedente.</p></div>
        <div class="row"><h4>Patrocinio a spese dello Stato</h4><p>Se hai i requisiti (art. 15-ter D.lgs. 28/2010), chiedi l’ammissione al Consiglio dell’Ordine degli Avvocati della città dell’organismo e non paghi le spese di mediazione. Nelle mediazioni obbligatorie puoi chiederla già prima della domanda (art. 15-quater).</p></div>
      </div>
    </div>
  </div>
</section>

<!-- MODULISTICA -->
<section class="cs-sec flush modulistica" id="modulistica">
  <div class="in">
    <div class="cs-head"><h2 class="h2 blurin">Modulistica</h2><p class="blurin">Tutti i documenti per avviare e seguire la mediazione, in PDF.</p></div>
    <div class="docs">
{docs}
    </div>
  </div>
</section>

'''
    # accordion behaviour (one open at a time)
    js = '''
  document.querySelectorAll('.acc').forEach(acc => acc.querySelectorAll('.acc-head').forEach(h => h.addEventListener('click', () => {
    const it = h.parentElement, o = !it.classList.contains('open');
    acc.querySelectorAll('.acc-item').forEach(x => { x.classList.remove('open'); x.querySelector('.acc-head').setAttribute('aria-expanded','false'); });
    if (o) { it.classList.add('open'); h.setAttribute('aria-expanded','true'); }
  })));
'''
    return common.page(src, 'Mediazione civile e commerciale · DPL Mediazione', body, CSS, js, _hdr, 'mediazione-civile.html')
