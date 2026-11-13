# -*- coding: utf-8 -*-
"""Pagina interna /alberatura: mappa del sito da mostrare al cliente.
Non è linkata da nessuna pagina ed è esclusa dai motori (noindex).
Uso (dopo build.py, dalla cartella src):  python3 alberatura.py  → ../alberatura.html"""
import re, os

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(HERE)

# font del sito, presi dalla home già generata
home = open(os.path.join(ROOT, 'index.html')).read()
FONTS = '\n'.join(re.findall(r'@font-face\{[^}]*\}', home))
LOGO = open(os.path.join(HERE, 'logo.svg')).read()

# ------------------------------------------------------------------ dati
# nodo: (titolo, tipo, sezioni, figli)   tipo: page | menu | tpl:N | ext
TREE = [
    ('Chi siamo', 'page', ['Hero', 'Dove persone e professionisti si incontrano', 'Le persone che ti accompagnano', 'Dicono di noi', 'Mediazione, formazione, informazione'], []),
    ('Mediazione', 'menu', [], [
        ('Civile e commerciale', 'page', ['Che cos’è la mediazione', 'Quando si fa', 'Come si svolge', 'Avvia una mediazione', 'Costi e agevolazioni', 'Modulistica'], []),
        ('Familiare', 'page', ['A chi si rivolge', 'Il percorso', 'Come iniziare', 'Domande frequenti'], []),
        ('Sanitaria, penale e lavorativa', 'page', ['Dove interveniamo', 'In collaborazione con Me.Dia.Re.'], []),
    ]),
    ('Formazione', 'menu', [], [
        ('Corsi civile e commerciale', 'page', ['Corsi e incontri, con filtri e ricerca', 'Su DPL Accademy'], []),
        ('DPL Accademy', 'ext', ['Familiare', 'Coordinazione genitoriale', 'Seminari e aggiornamenti', 'Area corsisti'], []),
    ]),
    ('Le nostre sedi', 'menu', [], [
        ('Tutte le sedi', 'page', ['Mappa d’Italia', 'Trova la sede più vicina'], [
            ('Pagina regione', 'tpl:20', ['Sedi della regione'], []),
            ('Pagina sede', 'tpl:20', ['Contatti e orari', 'Corsi della sede', 'Professionisti della sede'], []),
        ]),
        ('Sede di Milano', 'page', ['Sede principale, scorciatoia dal menu'], []),
        ('Sedi convenzionate ex art. 6', 'page', ['Regione per regione'], []),
    ]),
    ('Modulistica', 'page', ['Moduli da scaricare', 'Accesso all’area riservata'], []),
    ('News & eventi', 'menu', [], [
        ('Rassegna stampa', 'page', ['In evidenza', 'Articoli, interviste, video'], [
            ('Articolo · intervista · video', 'tpl:7', ['Contenuto', 'Altri articoli'], []),
        ]),
        ('Media e magazine', 'ext', ['dplmagazine.it'], []),
        ('Eventi', 'page', ['Prossimi eventi'], [
            ('Pagina evento', 'tpl:6', ['Programma e dettagli', 'Altri eventi'], []),
        ]),
    ]),
    ('Contatti', 'page', ['Scrivici: modulo e sedi', 'Lavora con noi: aprire una sede, diventare mediatore'], []),
]
HOME_SECTIONS = ['Hero', 'Le sedi in scorrimento', 'Un punto di riferimento', 'I numeri', 'Aree di intervento', 'Come funziona', 'La parola a chi ci ha scelto']
SERVICE = [('Privacy e cookie', 'Dal footer'), ('Pagina 404', 'Quando un indirizzo non esiste')]
ALWAYS = [('Header', 'Logo, menu con tendine, bottone Contatti. Su mobile: barra con logo e menu a pannello.'),
          ('Chiusura', 'Invito all’azione della pagina, poi il footer con sedi, contatti e link.')]
JOURNEYS = [
    ('Avviare una mediazione', ['Home', 'Mediazione civile e commerciale', 'Avvia una mediazione', 'Area riservata o modulo']),
    ('Trovare una sede', ['Home', 'Le nostre sedi', 'Regione', 'Sede']),
    ('Iscriversi a un corso', ['Home', 'Formazione', 'Card del corso', 'Contatti, già compilato']),
]

TOTAL = 67
TPL = 20 + 20 + 7 + 6

# ------------------------------------------------------------------ markup
ARROW_UR = '<svg class="ur" viewBox="0 0 12 12" aria-hidden="true"><path d="M3 9 9 3M4 3h5v5" fill="none" stroke="currentColor" stroke-width="1.2"/></svg>'

def badge(kind):
    if kind == 'menu': return '<span class="b b-menu">Voce di menu</span>'
    if kind == 'ext': return f'<span class="b b-ext">Sito esterno {ARROW_UR}</span>'
    if kind.startswith('tpl:'): return f'<span class="b b-tpl">Modello ×{kind[4:]}</span>'
    return ''

def node(t, kind, secs, kids, lvl):
    cls = {'menu': 'menu', 'ext': 'ext'}.get(kind, 'tpl' if kind.startswith('tpl') else 'page')
    s = ''.join(f'<li>{x}</li>' for x in secs)
    out = f'<div class="nd l{lvl} {cls}"><div class="nh"><span class="t">{t}</span>{badge(kind)}</div>'
    if s: out += f'<ul class="secs">{s}</ul>'
    out += '</div>'
    if kids:
        out += '<div class="kids">' + ''.join(f'<div class="kid">{node(*k, lvl + 1)}</div>' for k in kids) + '</div>'
    return out

cols = ''.join(f'<div class="col"><span class="num">{i:02d}</span>{node(*n, 1)}</div>' for i, n in enumerate(TREE, 1))
home_secs = ''.join(f'<li>{x}</li>' for x in HOME_SECTIONS)
service = ''.join(f'<div class="row"><span class="t">{t}</span><span class="d">{d}</span></div>' for t, d in SERVICE)
always = ''.join(f'<div class="row"><span class="t">{t}</span><span class="d">{d}</span></div>' for t, d in ALWAYS)
journeys = ''.join(
    f'<div class="jr"><h3>{t}</h3><ol>' + ''.join(f'<li>{x}</li>' for x in steps) + '</ol></div>' for t, steps in JOURNEYS)

HTML = f'''<!doctype html>
<html lang="it">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<meta name="robots" content="noindex, nofollow">
<title>Alberatura · DPL Mediazione</title>
<style>
{FONTS}
:root{{--navy:#19234B;--navy-deep:#11174A;--azzurro:#BAC7F9;--title-light:#D9E5F6;--line:rgba(25,35,75,.14);
  --serif:"Zodiak","Playfair Display",Georgia,serif;--sans:"Switzer","Inter",system-ui,-apple-system,"Segoe UI",sans-serif}}
*{{box-sizing:border-box}}
html{{-webkit-text-size-adjust:100%}}
body{{margin:0;font:400 16px/1.5 var(--sans);color:var(--navy);background:#fff;-webkit-font-smoothing:antialiased}}
.in{{width:min(1360px,100% - 48px);margin:0 auto}}
h1,h2{{font-family:var(--serif);font-weight:400;text-transform:uppercase;letter-spacing:-.02em;margin:0}}
/* testata */
.top{{background:var(--navy-deep);color:#fff;padding:32px 0 72px}}
.top .logo{{width:120px;height:40px;display:block}}
.top .logo svg{{width:100%;height:100%}}
.top .kick{{margin:88px 0 0;font:500 13px/1 var(--sans);letter-spacing:.06em;text-transform:uppercase;color:var(--azzurro)}}
.top h1{{margin-top:16px;font-size:clamp(44px,7vw,96px);line-height:.95;color:var(--title-light)}}
.top h1 span{{color:var(--azzurro)}}
.top .lead{{margin:28px 0 0;max-width:620px;font-size:18px;line-height:1.55;color:rgba(255,255,255,.82)}}
.stats{{display:grid;grid-template-columns:repeat(4,minmax(0,1fr));gap:16px;margin-top:64px;border-top:1px solid rgba(255,255,255,.18);padding-top:28px}}
.stats b{{display:block;font:400 clamp(36px,4vw,56px)/1 var(--serif);color:#fff}}
.stats span{{display:block;margin-top:10px;font-size:14px;line-height:1.4;color:rgba(255,255,255,.7)}}
/* sezioni */
.sec{{padding:96px 0 0}}
.sh{{display:flex;justify-content:space-between;align-items:flex-start;gap:40px;margin-bottom:48px}}
.sh h2{{font-size:clamp(32px,4vw,52px);line-height:1}}
.sh p{{margin:0;max-width:440px;font-size:17px;color:rgba(25,35,75,.75)}}
/* legenda */
.legend{{display:flex;flex-wrap:wrap;gap:10px 28px;margin:0 0 36px;padding:0;list-style:none;font-size:14px;color:rgba(25,35,75,.8)}}
.legend li{{display:flex;align-items:center;gap:10px}}
.sw{{width:18px;height:18px;border-radius:3px;flex:none}}
.sw.page{{background:#fff;box-shadow:inset 0 0 0 1px var(--navy)}}
.sw.menu{{background:var(--navy)}}
.sw.tpl{{background:#F3F5FC;box-shadow:inset 0 0 0 1px rgba(25,35,75,.25)}}
.sw.ext{{background:#fff;box-shadow:inset 0 0 0 1px rgba(25,35,75,.35);border:1px dashed rgba(25,35,75,.6)}}
/* albero */
.tree{{overflow-x:auto;padding-bottom:12px;-webkit-overflow-scrolling:touch}}
.tree-in{{min-width:1180px}}
.root{{display:flex;justify-content:center}}
.root .nd{{width:min(560px,100%);background:var(--navy-deep);color:#fff;box-shadow:none}}
.root .nd .t{{font:400 30px/1 var(--serif);text-transform:uppercase;letter-spacing:-.02em}}
.root .secs{{columns:2;column-gap:24px}}
.root .secs li{{color:rgba(255,255,255,.72)}}
.root .secs li::before{{background:var(--azzurro)}}
.stem{{height:36px;width:1px;background:var(--navy);margin:0 auto}}
.cols{{display:grid;grid-template-columns:repeat({len(TREE)},minmax(0,1fr));gap:12px;position:relative;padding-top:36px}}
.cols::before{{content:"";position:absolute;top:0;left:calc(100% / {len(TREE)} / 2);right:calc(100% / {len(TREE)} / 2);height:1px;background:var(--navy)}}
.col{{position:relative;display:flex;flex-direction:column}}
.col::before{{content:"";position:absolute;top:-36px;left:50%;width:1px;height:36px;background:var(--navy)}}
.col .num{{position:absolute;top:-28px;left:calc(50% + 8px);font:500 11px/1 var(--sans);letter-spacing:.06em;color:rgba(25,35,75,.5)}}
.nd{{border-radius:6px;padding:14px 14px 16px;background:#fff;box-shadow:inset 0 0 0 1px var(--navy)}}
.nd.menu{{background:var(--navy);color:#fff;box-shadow:none}}
.nd.tpl{{background:#F3F5FC;box-shadow:inset 0 0 0 1px rgba(25,35,75,.22)}}
.nd.ext{{background:#fff;box-shadow:none;border:1px dashed rgba(25,35,75,.5)}}
.nh{{display:flex;flex-direction:column;align-items:flex-start;gap:8px}}
.nd .t{{font:500 16px/1.25 var(--sans)}}
.l1>.nh .t{{font-size:17px}}
.b{{display:inline-flex;align-items:center;gap:4px;padding:4px 7px 3px;border-radius:3px;font:500 11px/1.2 var(--sans);letter-spacing:.02em}}
.b-menu{{background:rgba(255,255,255,.14);color:var(--azzurro)}}
.b-tpl{{background:var(--navy);color:#fff}}
.b-ext{{background:#fff;color:var(--navy);box-shadow:inset 0 0 0 1px rgba(25,35,75,.35)}}
.b .ur{{width:10px;height:10px}}
.secs{{list-style:none;margin:12px 0 0;padding:0}}
.secs li{{position:relative;padding:3px 0 3px 12px;font-size:13px;line-height:1.35;color:rgba(25,35,75,.72);break-inside:avoid}}
.secs li::before{{content:"";position:absolute;left:0;top:10px;width:4px;height:4px;border-radius:50%;background:rgba(25,35,75,.4)}}
.nd.menu .secs li{{color:rgba(255,255,255,.75)}}
.kids{{position:relative;margin-left:12px;padding-left:12px;border-left:1px solid var(--navy)}}
.kid{{position:relative;padding-top:12px}}
.kid::before{{content:"";position:absolute;left:-12px;top:30px;width:12px;height:1px;background:var(--navy)}}
.kid:last-child::after{{content:"";position:absolute;left:-13px;top:31px;bottom:0;width:3px;background:#fff}}
.kids .kids .kid:last-child::after{{background:#fff}}
/* righe */
.two{{display:grid;grid-template-columns:repeat(2,minmax(0,1fr));gap:56px}}
.two h3{{margin:0 0 8px;font:500 18px/1.3 var(--sans)}}
.row{{display:grid;grid-template-columns:minmax(0,200px) minmax(0,1fr);gap:24px;padding:18px 0;border-bottom:1px solid var(--line)}}
.row:first-of-type{{border-top:1px solid var(--line)}}
.row .t{{font-weight:500}}
.row .d{{color:rgba(25,35,75,.72)}}
/* percorsi */
.jrs{{display:grid;grid-template-columns:repeat(3,minmax(0,1fr));gap:16px}}
.jr{{border-top:1px solid var(--navy);padding-top:20px}}
.jr h3{{margin:0;font:400 22px/1.25 var(--sans)}}
.jr ol{{list-style:none;margin:20px 0 0;padding:0;counter-reset:s}}
.jr li{{counter-increment:s;position:relative;padding:0 0 18px 36px;font-size:15px;line-height:1.4;color:rgba(25,35,75,.8)}}
.jr li::before{{content:counter(s);position:absolute;left:0;top:-1px;width:22px;height:22px;border-radius:50%;display:grid;place-items:center;font:500 11px/1 var(--sans);background:var(--navy);color:#fff}}
.jr li:not(:last-child)::after{{content:"";position:absolute;left:11px;top:24px;bottom:2px;width:1px;background:rgba(25,35,75,.25)}}
.foot{{margin-top:120px;padding:28px 0 40px;border-top:1px solid var(--line);font-size:13px;color:rgba(25,35,75,.6);display:flex;justify-content:space-between;gap:24px;flex-wrap:wrap}}
@media (max-width: 899px){{
  .in{{width:calc(100% - 32px)}}
  .top{{padding:20px 0 48px}}
  .top .kick{{margin-top:56px}}
  .stats{{grid-template-columns:repeat(2,minmax(0,1fr));gap:24px 16px;margin-top:40px}}
  .sec{{padding-top:64px}}
  .sh{{flex-direction:column;gap:16px;margin-bottom:28px}}
  .two,.jrs{{grid-template-columns:1fr;gap:40px}}
  .row{{grid-template-columns:1fr;gap:4px}}
  /* albero verticale */
  .tree-in{{min-width:0}}
  .root .secs{{columns:1}}
  .stem{{display:none}}
  .cols{{grid-template-columns:1fr;gap:0;padding:0 0 0 14px;margin-left:14px;border-left:1px solid var(--navy)}}
  .cols::before{{display:none}}
  .col{{padding-top:16px}}
  .col::before{{top:34px;left:-14px;width:14px;height:1px}}
  .col:last-child::after{{content:"";position:absolute;left:-15px;top:35px;bottom:0;width:3px;background:#fff}}
  .col .num{{position:static;margin:0 0 6px;display:block}}
  .col .num{{display:none}}
}}
</style>
</head>
<body>
<header class="top">
  <div class="in">
    <span class="logo" aria-label="DPL Mediazione">{LOGO}</span>
    <p class="kick">Documento di lavoro · non pubblico</p>
    <h1>Alberatura <span>del sito</span></h1>
    <p class="lead">Come è organizzato il nuovo dplmediazione.it: le voci di menu, le pagine che contengono, le sezioni di ogni pagina e i percorsi principali delle persone.</p>
    <div class="stats">
      <div><b>{len(TREE)}</b><span>voci nel menu principale</span></div>
      <div><b>{TOTAL}</b><span>pagine in tutto</span></div>
      <div><b>{TOTAL - TPL}</b><span>pagine uniche, più {TPL} generate da 4 modelli</span></div>
      <div><b>3</b><span>siti collegati: DPL Accademy, DPL Magazine, area riservata</span></div>
    </div>
  </div>
</header>

<main>
  <section class="sec">
    <div class="in">
      <div class="sh"><h2>La struttura</h2><p>Dalla home si raggiungono le sette voci del menu. Alcune voci aprono una tendina con più pagine; per ogni pagina sono indicate le sezioni principali.</p></div>
      <ul class="legend">
        <li><span class="sw page"></span>Pagina</li>
        <li><span class="sw menu"></span>Voce di menu che apre una tendina</li>
        <li><span class="sw tpl"></span>Modello ripetuto per più pagine</li>
        <li><span class="sw ext"></span>Sito esterno</li>
      </ul>
      <div class="tree"><div class="tree-in">
        <div class="root"><div class="nd l0"><div class="nh"><span class="t">Home</span></div><ul class="secs">{home_secs}</ul></div></div>
        <div class="stem"></div>
        <div class="cols">{cols}</div>
      </div></div>
    </div>
  </section>

  <section class="sec">
    <div class="in">
      <div class="sh"><h2>Percorsi principali</h2><p>I tre compiti più frequenti e quanti passaggi servono per completarli partendo dalla home.</p></div>
      <div class="jrs">{journeys}</div>
    </div>
  </section>

  <section class="sec">
    <div class="in two">
      <div><h3>In ogni pagina</h3>{always}</div>
      <div><h3>Pagine di servizio</h3>{service}</div>
    </div>
  </section>
</main>

<div class="in foot"><span>DPL Mediazione · alberatura del sito</span><span>Pagina riservata, non collegata al sito e non indicizzata</span></div>
</body>
</html>
'''

open(os.path.join(ROOT, 'alberatura.html'), 'w').write(HTML)
print('alberatura.html scritta')
