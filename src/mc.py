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
.s4{border-top:1px solid var(--navy);padding-top:U(20)}
.s4 .n{font:400 U(40)/1 var(--serif);letter-spacing:U(-2);color:var(--navy)}
.s4 h3{margin:U(28) 0 0;font:400 U(22)/U(28) var(--sans);color:var(--navy)}
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
  .steps4{gap:28px}
  .s4 h3{margin-top:22px}
  .notes{margin-top:32px}
  .avvia .block{padding:32px 16px 16px}
  .avvia .h2{width:auto}
  .avvia .two{margin-top:28px}
  .opt{padding:24px 20px}
  .costi .cols{gap:48px;margin-top:40px}
  .row{grid-template-columns:1fr;gap:6px}
  .docs{margin-top:32px}
}

/* card «quando» e «costi» (stile delle pagine interne) */
.mc-cards{display:grid;grid-template-columns:repeat(4,minmax(0,1fr));gap:U(56) U(16);margin-top:U(56)}
.mc-card{border-top:1px solid var(--navy);padding-top:U(20);display:flex;flex-direction:column}
.mc-card .ic{width:U(36);height:U(36)}
.mc-card .ic svg{width:100%;height:100%;fill:var(--navy);display:block}
.mc-card h3{margin:U(28) 0 0;font:400 U(22)/U(28) var(--sans);color:var(--navy)}
.mc-card p{margin:U(10) 0 0;font:400 max(14px,U(16))/1.5 var(--sans);color:rgba(25,35,75,.7)}
.mc-more{margin-top:U(16);border-top:1px solid rgba(25,35,75,.12);border-bottom:1px solid rgba(25,35,75,.12)}
.mc-more summary{list-style:none;cursor:pointer;display:flex;align-items:center;gap:U(12);padding:U(24) 0;font:400 U(20)/U(26) var(--sans);color:var(--navy)}
.mc-more summary::-webkit-details-marker{display:none}
.mc-more summary .n{display:inline-flex;align-items:center;justify-content:center;min-width:U(28);height:U(24);padding:0 U(6);border-radius:U(4);background:var(--navy);color:#fff;font:500 max(12px,U(13))/1 var(--sans)}
.mc-more summary::after{content:"";margin-left:auto;flex:none;width:U(12);height:U(12);border-right:1.5px solid currentColor;border-bottom:1.5px solid currentColor;transform:translateY(-25%) rotate(45deg);transition:transform .5s var(--osmo)}
.mc-more[open] summary::after{transform:translateY(25%) rotate(-135deg)}
.mc-mat{margin:0;padding:0 0 U(28);list-style:none;columns:3;column-gap:U(40)}
.mc-mat li{break-inside:avoid;padding:U(8) 0;font:400 max(14px,U(16))/1.4 var(--sans);color:rgba(25,35,75,.8)}
.mc-note{margin:U(20) 0 0;max-width:U(760);font:400 max(13px,U(14))/1.5 var(--sans);color:rgba(25,35,75,.6)}
.mc-dl{display:grid;grid-template-columns:U(447) 1fr;gap:U(120);margin-top:U(72)}
.mc-dl h3{margin:0;padding-top:U(18);font:400 U(22)/U(28) var(--sans);color:var(--navy)}
.mc-dl .lst{border-top:1px solid rgba(25,35,75,.12)}
.mc-dl .lst a{display:flex;align-items:center;gap:U(16);padding:U(20) 0;border-bottom:1px solid rgba(25,35,75,.12);font:400 U(18)/U(26) var(--sans);color:var(--navy);transition:color .4s var(--osmo),padding .5s var(--osmo)}
.mc-dl .lst a:hover{color:#3B4A8C;padding-left:U(8)}
.mc-dl .lst .ic{width:U(20);height:U(20);flex:none}
.mc-dl .lst .t{flex:1;min-width:0}
.mc-dl .lst .m{font:400 max(13px,U(14))/1.4 var(--sans);color:rgba(25,35,75,.6)}
.mc-dl .lst .dl{width:U(16);height:U(16);flex:none}
@media (max-width: 1100px) and (min-width: 900px){.mc-cards{grid-template-columns:repeat(2,minmax(0,1fr))}}
@media (max-width: 899px){
  .mc-cards{grid-template-columns:minmax(0,1fr);gap:28px;margin-top:32px}
  .mc-card h3{margin-top:22px;font-size:20px;line-height:26px}
  .mc-more summary{font-size:18px;line-height:24px;padding:20px 0}
  .mc-mat{columns:1;padding-bottom:20px}
  .mc-dl{grid-template-columns:1fr;gap:16px;margin-top:48px}
  .mc-dl h3{padding-top:0;font-size:20px}
  .mc-dl .lst a{font-size:16px;line-height:22px;gap:12px}
}
'''

DL = '<svg class="dl" viewBox="0 0 16 16" fill="none" aria-hidden="true"><path d="M8 2.5v8m-3.5-3.5L8 10.5l3.5-3.5M3 13.5h10" stroke="currentColor" stroke-width="1.4" stroke-linecap="round" stroke-linejoin="round"/></svg>'

def pdf(name, f, cls=''):
    return f'<a{cls} href="{DOCS}{f}" target="_blank" rel="noopener">{name} {DL}</a>'

def _hdr(h):
    h = h.replace('<button class="dd-btn" aria-expanded="false" aria-haspopup="true">Mediazione', '<button class="dd-btn is-active" aria-expanded="false" aria-haspopup="true">Mediazione', 1)
    return h.replace('<a href="__HREF_MC__">Civile e commerciale</a>', '<a href="__HREF_MC__" aria-current="page">Civile e commerciale</a>')

def make(src):
    tipi_cards = '      <article class="mc-card"><span class="ic"><svg viewBox="0 0 256 256" aria-hidden="true"><path d="M239.43,133l-32-80A8,8,0,0,0,200,48a8.27,8.27,0,0,0-1.73.21L136,62V40a8,8,0,0,0-16,0V65.58L54.27,80.21A8,8,0,0,0,48.57,85l-32,80a7.92,7.92,0,0,0-.57,3c0,23.31,24.54,32,40,32s40-8.69,40-32a7.92,7.92,0,0,0-.57-3L66.92,93.77,120,82V208H104a8,8,0,0,0,0,16h48a8,8,0,0,0,0-16H136V78.42L187,67.1,160.57,133a7.92,7.92,0,0,0-.57,3c0,23.31,24.54,32,40,32s40-8.69,40-32A7.92,7.92,0,0,0,239.43,133Zm-160,35H32.62L56,109.54Zm97.24-32L200,77.54,223.38,136Z"/></svg></span><h3>Obbligatoria</h3><p>Per alcune materie la legge chiede di tentarla prima di andare dal giudice.</p></article>\n      <article class="mc-card"><span class="ic"><svg viewBox="0 0 256 256" aria-hidden="true"><path d="M254.3,107.91,228.78,56.85a16,16,0,0,0-21.47-7.15L182.44,62.13,130.05,48.27a8.14,8.14,0,0,0-4.1,0L73.56,62.13,48.69,49.7a16,16,0,0,0-21.47,7.15L1.7,107.9a16,16,0,0,0,7.15,21.47l27,13.51,55.49,39.63a8.06,8.06,0,0,0,2.71,1.25l64,16a8,8,0,0,0,7.6-2.1l40-40,15.08-15.08,26.42-13.21a16,16,0,0,0,7.15-21.46Zm-54.89,33.37L165,113.72a8,8,0,0,0-10.68.61C136.51,132.27,116.66,130,104,122L147.24,80h31.81l27.21,54.41Zm-41.87,41.86L99.42,168.61l-49.2-35.14,28-56L128,64.28l9.8,2.59-45,43.68-.08.09a16,16,0,0,0,2.72,24.81c20.56,13.13,45.37,11,64.91-5L188,152.66Zm-25.72,34.8a8,8,0,0,1-7.75,6.06,8.13,8.13,0,0,1-1.95-.24L80.41,213.33a7.89,7.89,0,0,1-2.71-1.25L51.35,193.26a8,8,0,0,1,9.3-13l25.11,17.94L126,208.24A8,8,0,0,1,131.82,217.94Z"/></svg></span><h3>Volontaria</h3><p>Puoi sceglierla per qualsiasi controversia su diritti disponibili, anche senza avvocato.</p></article>\n      <article class="mc-card"><span class="ic"><svg viewBox="0 0 256 256" aria-hidden="true"><path d="M52.69,99.31a16,16,0,0,1,0-22.63l64-64a16,16,0,0,1,22.63,22.63l-64,64a16,16,0,0,1-22.63,0Zm190.63,17.37a16,16,0,0,0-22.63,0l-64,64a16,16,0,0,0,0,22.63h0a16,16,0,0,0,22.63,0l64-64A16,16,0,0,0,243.32,116.68Zm-35.11-15.8L155.12,47.79a4,4,0,0,0-5.66,0L87.8,109.45a4,4,0,0,0,0,5.66L103,130.34,28.69,204.69a16,16,0,0,0,22.62,22.62L125.66,153l15.23,15.23a4,4,0,0,0,5.66,0l61.66-61.66A4,4,0,0,0,208.21,100.88Z"/></svg></span><h3>Demandata dal giudice</h3><p>Durante una causa il giudice può invitare le parti a tentarla: il tentativo diventa obbligatorio.</p></article>\n      <article class="mc-card"><span class="ic"><svg viewBox="0 0 256 256" aria-hidden="true"><path d="M80.3,120.26A58.29,58.29,0,0,1,81,97.07C83.32,87,87.89,80,92.1,80c2.57,0,2.94.67,3.12,1,.88,1.61,4,10.93-12.63,46.52A28.87,28.87,0,0,1,80.3,120.26ZM232,56V200a16,16,0,0,1-16,16H40a16,16,0,0,1-16-16V56A16,16,0,0,1,40,40H216A16,16,0,0,1,232,56ZM84,160c2-3.59,3.94-7.32,5.9-11.14,10.34-.32,22.21-7.57,35.47-21.68,5,9.69,11.38,15.25,18.87,16.55,8,1.38,16-2.38,23.94-11.2,6,5.53,16.15,11.47,31.8,11.47a8,8,0,0,0,0-16c-17.91,0-24.3-10.88-24.84-11.86a7.83,7.83,0,0,0-6.54-4.51,8,8,0,0,0-7.25,3.6c-6.78,10-11.87,13.16-14.39,12.73-4-.69-9.15-10-11.23-18a8,8,0,0,0-14-3c-8.88,10.94-16.3,17.79-22.13,21.66,15.8-35.65,13.27-48.59,9.6-55.3C107.35,69.84,102.59,64,92.1,64,79.66,64,69.68,75,65.41,93.46a75,75,0,0,0-.83,29.81c1.7,8.9,5.17,15.73,10.16,20.12-3,5.81-6.09,11.43-9,16.61H56a8,8,0,0,0,0,16h.44c-4.26,7.12-7.11,11.59-7.18,11.69a8,8,0,0,0,13.48,8.62c.36-.55,5.47-8.57,12.29-20.31H200a8,8,0,0,0,0-16Z"/></svg></span><h3>Prevista da un contratto</h3><p>Una clausola del contratto o dello statuto può prevederla prima di ogni altra strada.</p></article>'
    costi_cards = '      <article class="mc-card"><span class="ic"><svg viewBox="0 0 256 256" aria-hidden="true"><path d="M184,89.57V84c0-25.08-37.83-44-88-44S8,58.92,8,84v40c0,20.89,26.25,37.49,64,42.46V172c0,25.08,37.83,44,88,44s88-18.92,88-44V132C248,111.3,222.58,94.68,184,89.57ZM56,146.87C36.41,141.4,24,132.39,24,124V109.93c8.16,5.78,19.09,10.44,32,13.57Zm80-23.37c12.91-3.13,23.84-7.79,32-13.57V124c0,8.39-12.41,17.4-32,22.87Zm-16,71.37C100.41,189.4,88,180.39,88,172v-4.17c2.63.1,5.29.17,8,.17,3.88,0,7.67-.13,11.39-.35A121.92,121.92,0,0,0,120,171.41Zm0-44.62A163,163,0,0,1,96,152a163,163,0,0,1-24-1.75V126.46A183.74,183.74,0,0,0,96,128a183.74,183.74,0,0,0,24-1.54Zm64,48a165.45,165.45,0,0,1-48,0V174.4a179.48,179.48,0,0,0,24,1.6,183.74,183.74,0,0,0,24-1.54ZM232,172c0,8.39-12.41,17.4-32,22.87V171.5c12.91-3.13,23.84-7.79,32-13.57Z"/></svg></span><h3>Credito d’imposta</h3><p>Con l’accordo recuperi l’indennità pagata fino a € 600, nelle obbligatorie anche il compenso dell’avvocato. Senza accordo, la metà.</p></article>\n      <article class="mc-card"><span class="ic"><svg viewBox="0 0 256 256" aria-hidden="true"><path d="M216,40H40A16,16,0,0,0,24,56V208a8,8,0,0,0,11.58,7.15L64,200.94l28.42,14.21a8,8,0,0,0,7.16,0L128,200.94l28.42,14.21a8,8,0,0,0,7.16,0L192,200.94l28.42,14.21A8,8,0,0,0,232,208V56A16,16,0,0,0,216,40ZM176,144H80a8,8,0,0,1,0-16h96a8,8,0,0,1,0,16Zm0-32H80a8,8,0,0,1,0-16h96a8,8,0,0,1,0,16Z"/></svg></span><h3>Contributo unificato</h3><p>Se una causa in corso si chiude con l’accordo, credito pari al contributo versato, fino a € 518.</p></article>\n      <article class="mc-card"><span class="ic"><svg viewBox="0 0 256 256" aria-hidden="true"><path d="M225.86,102.82c-3.77-3.94-7.67-8-9.14-11.57-1.36-3.27-1.44-8.69-1.52-13.94-.15-9.76-.31-20.82-8-28.51s-18.75-7.85-28.51-8c-5.25-.08-10.67-.16-13.94-1.52-3.56-1.47-7.63-5.37-11.57-9.14C146.28,23.51,138.44,16,128,16s-18.27,7.51-25.18,14.14c-3.94,3.77-8,7.67-11.57,9.14C88,40.64,82.56,40.72,77.31,40.8c-9.76.15-20.82.31-28.51,8S41,67.55,40.8,77.31c-.08,5.25-.16,10.67-1.52,13.94-1.47,3.56-5.37,7.63-9.14,11.57C23.51,109.72,16,117.56,16,128s7.51,18.27,14.14,25.18c3.77,3.94,7.67,8,9.14,11.57,1.36,3.27,1.44,8.69,1.52,13.94.15,9.76.31,20.82,8,28.51s18.75,7.85,28.51,8c5.25.08,10.67.16,13.94,1.52,3.56,1.47,7.63,5.37,11.57,9.14C109.72,232.49,117.56,240,128,240s18.27-7.51,25.18-14.14c3.94-3.77,8-7.67,11.57-9.14,3.27-1.36,8.69-1.44,13.94-1.52,9.76-.15,20.82-.31,28.51-8s7.85-18.75,8-28.51c.08-5.25.16-10.67,1.52-13.94,1.47-3.56,5.37-7.63,9.14-11.57C232.49,146.28,240,138.44,240,128S232.49,109.73,225.86,102.82Zm-52.2,6.84-56,56a8,8,0,0,1-11.32,0l-24-24a8,8,0,0,1,11.32-11.32L112,148.69l50.34-50.35a8,8,0,0,1,11.32,11.32Z"/></svg></span><h3>Bollo e registro</h3><p>Nessuna imposta di bollo. Il verbale è esente dall’imposta di registro fino a € 100.000.</p></article>\n      <article class="mc-card"><span class="ic"><svg viewBox="0 0 256 256" aria-hidden="true"><path d="M230.33,141.06a24.34,24.34,0,0,0-18.61-4.77C230.5,117.33,240,98.48,240,80c0-26.47-21.29-48-47.46-48A47.58,47.58,0,0,0,156,48.75,47.58,47.58,0,0,0,119.46,32C93.29,32,72,53.53,72,80c0,11,3.24,21.69,10.06,33a31.87,31.87,0,0,0-14.75,8.4L44.69,144H16A16,16,0,0,0,0,160v40a16,16,0,0,0,16,16H120a7.93,7.93,0,0,0,1.94-.24l64-16a6.94,6.94,0,0,0,1.19-.4L226,182.82l.44-.2a24.6,24.6,0,0,0,3.93-41.56Zm-10.9,27.15-38,16.18L119,200H56V155.31l22.63-22.62A15.86,15.86,0,0,1,89.94,128H140a12,12,0,0,1,0,24H112a8,8,0,0,0,0,16h32a8.32,8.32,0,0,0,1.79-.2l67-15.41.31-.08a8.6,8.6,0,0,1,6.3,15.9Z"/></svg></span><h3>Patrocinio a spese dello Stato</h3><p>Se hai i requisiti, chiedi l’ammissione al Consiglio dell’Ordine degli Avvocati e non paghi la mediazione.</p></article>'
    materie_li = ''.join(f'<li>{m}</li>' for m in MATERIE)
    n_materie = len(MATERIE)
    tabelle = ''.join(f'<a href="{DOCS}{f}" target="_blank" rel="noopener">__ICO_FILE__<span class="t">{n}</span><span class="m">PDF</span>{DL}</a>' for n, f in [('Indennità · mediazioni volontarie','INDENNITA_MEDIAZIONI_VOLONTARIE_DPL_2025.pdf'),('Indennità · materie obbligatorie','INDENNITA_MEDIAZIONI_OBBLIGATORIE_DPL_2025.pdf'),('Tabelle ministeriali','tabella_ministero_2024.pdf')])
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
<div class="px-band"><img src="__IMG_mb3__" alt="Una persona consulta i documenti dal portatile"></div>

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
    <div class="mc-cards">
{tipi_cards}
    </div>
    <details class="mc-more"><summary>Le materie per cui è obbligatoria <span class="n">{n_materie}</span></summary><ul class="mc-mat">{materie_li}</ul></details>
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
    <div class="mc-cards">
{costi_cards}
    </div>
    <p class="mc-note">Limite di € 600 per procedura e, ogni anno, di € 2.400 per le persone fisiche e di € 24.000 per le persone giuridiche. Riferimenti: D.M. 1 agosto 2023, artt. 15-ter, 15-quater e 20 del D.lgs. 28/2010.</p>
    <div class="mc-dl">
      <h3>Tabelle dei costi</h3>
      <div class="lst">{tabelle}</div>
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
    import kit
    band_css = '\n.px-band{position:relative;height:U(600);overflow:hidden;background:#F3F5FC}\n.px-band img{position:absolute;left:0;top:-10%;width:100%;height:120%;object-fit:cover;will-change:transform}\n@media (max-width: 899px){.px-band{height:68vw}}\n'
    band_js = kit.FILTER_JS[kit.FILTER_JS.index('  /* ---- kit: photo band parallax'):kit.FILTER_JS.index('  /* ---- kit: legal table')]
    return common.page(src, 'Mediazione civile e commerciale · DPL Mediazione', body, CSS + band_css, js + band_js, _hdr, 'mediazione-civile.html')
