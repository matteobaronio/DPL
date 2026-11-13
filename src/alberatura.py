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
# pagina: dict(t=titolo, s=[sezioni], n=ripetizioni del modello, ext=True se sito esterno, kids=[pagine figlie])
HOME = dict(t='Home', s=['Hero', 'Sedi in scorrimento', 'Un punto di riferimento', 'I numeri', 'Aree di intervento', 'Come funziona', 'Testimonianze'])
# colonne del menu: (voce, gruppo?, [pagine])  — gruppo=True: la voce apre una tendina e non è una pagina
MENU = [
    ('Chi siamo', False, [dict(t='Chi siamo', s=['Hero', 'Dove persone e professionisti si incontrano', 'Il team', 'Dicono di noi', 'Mediazione, formazione, informazione'])]),
    ('Mediazione', True, [
        dict(t='Civile e commerciale', s=['Hero', 'Che cos’è', 'Quando si fa', 'Come si svolge', 'Avvia una mediazione', 'Costi e agevolazioni', 'Modulistica']),
        dict(t='Familiare', s=['Hero', 'A chi si rivolge', 'Il percorso', 'Come iniziare', 'Domande frequenti']),
        dict(t='Sanitaria, penale e lavorativa', s=['Hero', 'Dove interveniamo']),
    ]),
    ('Formazione', True, [
        dict(t='Corsi civile e commerciale', s=['Hero', 'Corsi e incontri', 'Su DPL Accademy']),
        dict(t='DPL Accademy', ext=True, s=['Familiare', 'Coordinazione genitoriale', 'Seminari e aggiornamenti', 'Area corsisti']),
    ]),
    ('Le nostre sedi', True, [
        dict(t='Tutte le sedi', s=['Hero', 'Mappa d’Italia', 'Trova la sede, filtri per regione'], kids=[
            dict(t='Sede', n=20, s=['Hero', 'Contatti e orari', 'Corsi della sede', 'Professionisti']),
        ]),
        dict(t='Sedi convenzionate ex art. 6', s=['Hero', 'Regione per regione']),
    ]),
    ('Modulistica', False, [dict(t='Modulistica', s=['Hero', 'Moduli da scaricare', 'Area riservata'])]),
    ('News & eventi', True, [
        dict(t='DPL Magazine', ext=True, s=['Media e magazine']),
        dict(t='Rassegna stampa', note='Da discutere', s=['Hero', 'In evidenza', 'Articoli, interviste, video'], kids=[
            dict(t='Articolo', n=7, s=['Contenuto', 'Altri articoli']),
        ]),
        dict(t='Eventi', note='Da discutere', s=['Hero', 'Prossimi eventi'], kids=[
            dict(t='Evento', n=6, s=['Programma', 'Altri eventi']),
        ]),
    ]),
    ('Contatti', False, [dict(t='Contatti', s=['Hero', 'Scrivici', 'Lavora con noi'])]),
]
OTHER = [dict(t='Privacy e cookie', s=['Informativa', 'Cookie policy']), dict(t='Pagina 404', s=['Messaggio', 'Link utili'])]
JOURNEYS = [
    ('Avviare una mediazione', ['Home', 'Mediazione civile e commerciale', 'Avvia una mediazione', 'Area riservata o modulo']),
    ('Trovare una sede', ['Home', 'Le nostre sedi', 'Regione', 'Sede']),
    ('Iscriversi a un corso', ['Home', 'Formazione', 'Card del corso', 'Contatti, già compilato']),
]
TOTAL, TPL = 47, 20 + 7 + 6

# ------------------------------------------------------------------ markup
UR = '<svg viewBox="0 0 12 12" aria-hidden="true"><path d="M3 9 9 3M4 3h5v5" fill="none" stroke="currentColor" stroke-width="1.2"/></svg>'

def card(p, cls=''):
    ext = p.get('ext'); n = p.get('n')
    k = 'card' + (' ext' if ext else '') + (' tpl' if n else '') + (' flag' if p.get('note') else '') + (' ' + cls if cls else '')
    meta = []
    if n: meta.append(f'<span class="m">{n} pagine, stesso modello</span>')
    if ext: meta.append(f'<span class="m">Sito esterno {UR}</span>')
    if p.get('note'): meta.append(f'<span class="m note">{p["note"]}</span>')
    tag = '<span class="meta">' + ''.join(meta) + '</span>' if meta else ''
    rows = ''
    if not ext: rows += '<li class="hd">Header</li>'
    rows += ''.join(f'<li>{x}</li>' for x in p['s'])
    if not ext: rows += '<li class="ft">Footer</li>'
    out = f'<div class="{k}"><div class="ttl"><span>{p["t"]}</span>{tag}</div><ul>{rows}</ul></div>'
    if p.get('kids'):
        out += '<div class="sub">' + ''.join(f'<div class="link"></div>{card(c)}' for c in p['kids']) + '</div>'
    return out

def column(label, group, pages):
    head = f'<div class="grp">{label}<span>menu</span></div>' if group else ''
    body = ''.join((f'<div class="link"></div>' if (group or i) else '') + f'<div class="unit">{card(p)}</div>' for i, p in enumerate(pages))
    return f'<div class="col">{head}{body}</div>'

cols = ''.join(column(*m) for m in MENU)
others = ''.join(card(p) for p in OTHER)
journeys = ''.join(f'<div class="jr"><h3>{t}</h3><ol>' + ''.join(f'<li>{x}</li>' for x in steps) + '</ol></div>' for t, steps in JOURNEYS)
N = len(MENU)

HTML = f'''<!doctype html>
<html lang="it">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<meta name="robots" content="noindex, nofollow">
<title>Alberatura · DPL Mediazione</title>
<style>
{FONTS}
:root{{--navy:#19234B;--navy-deep:#11174A;--azzurro:#BAC7F9;--title-light:#D9E5F6;
  --hd:#DCE5F8;--sec:#F2F4FB;--ft:#E7E4F5;--bd:rgba(25,35,75,.18);
  --serif:"Zodiak","Playfair Display",Georgia,serif;--sans:"Switzer","Inter",system-ui,-apple-system,"Segoe UI",sans-serif}}
*{{box-sizing:border-box}}
html{{-webkit-text-size-adjust:100%}}
body{{margin:0;font:400 16px/1.5 var(--sans);color:var(--navy);background:#fff;-webkit-font-smoothing:antialiased}}
.in{{width:min(1440px,100% - 48px);margin:0 auto}}
h1,h2{{font-family:var(--serif);font-weight:400;text-transform:uppercase;letter-spacing:-.02em;margin:0}}
/* testata */
.top{{background:var(--navy-deep);color:#fff;padding:32px 0 64px}}
.top .logo{{width:120px;height:40px;display:block}}
.top .logo svg{{width:100%;height:100%}}
.top .kick{{margin:80px 0 0;font:500 13px/1 var(--sans);letter-spacing:.06em;text-transform:uppercase;color:var(--azzurro)}}
.top h1{{margin-top:16px;font-size:clamp(44px,7vw,96px);line-height:.95;color:var(--title-light)}}
.top h1 span{{color:var(--azzurro)}}
.top .lead{{margin:24px 0 0;max-width:600px;font-size:18px;line-height:1.55;color:rgba(255,255,255,.82)}}
.stats{{display:grid;grid-template-columns:repeat(4,minmax(0,1fr));gap:16px;margin-top:56px;border-top:1px solid rgba(255,255,255,.18);padding-top:28px}}
.stats b{{display:block;font:400 clamp(36px,4vw,56px)/1 var(--serif);color:#fff}}
.stats span{{display:block;margin-top:10px;font-size:14px;line-height:1.4;color:rgba(255,255,255,.7)}}
/* sezioni */
.sec{{padding:72px 0 96px}}
.sh{{display:flex;justify-content:space-between;align-items:flex-start;gap:40px;margin-bottom:36px}}
.sh h2{{font-size:clamp(32px,4vw,52px);line-height:1}}
.sh p{{margin:0;max-width:440px;font-size:17px;color:rgba(25,35,75,.75)}}
.legend{{display:flex;flex-wrap:wrap;gap:10px 24px;margin:0 0 48px;padding:0;list-style:none;font-size:14px;color:rgba(25,35,75,.8)}}
.legend li{{display:flex;align-items:center;gap:8px}}
.sw{{width:28px;height:14px;border-radius:3px;flex:none}}
.sw.hd{{background:var(--hd)}}.sw.sc{{background:var(--sec);box-shadow:inset 0 0 0 1px rgba(25,35,75,.08)}}.sw.ft{{background:var(--ft)}}
.sw.tpl{{width:20px;height:16px;background:#fff;box-shadow:inset 0 0 0 1.5px var(--bd),3px 3px 0 -1px #fff,3px 3px 0 0 var(--bd)}}
.sw.ext{{width:20px;height:16px;border:1.5px dashed rgba(25,35,75,.45)}}
/* card pagina */
.card{{position:relative;width:100%;background:#fff;border:1.5px solid var(--bd);border-radius:10px;padding:10px}}
.card .ttl{{display:flex;flex-direction:column;align-items:center;justify-content:center;gap:4px;min-height:40px;padding:4px 4px 10px;text-align:center;font:500 15px/1.25 var(--sans)}}
.card ul{{list-style:none;margin:0;padding:0;display:flex;flex-direction:column;gap:4px}}
.card li{{padding:7px 10px;border-radius:5px;background:var(--sec);font-size:13px;line-height:1.3;color:rgba(25,35,75,.85)}}
.card li.hd{{background:var(--hd);color:var(--navy);font-weight:500}}
.card li.ft{{background:var(--ft);color:var(--navy);font-weight:500}}
.card.tpl{{box-shadow:5px 5px 0 -1.5px #fff,5px 5px 0 0 var(--bd)}}
.card.ext{{border-style:dashed;border-color:rgba(25,35,75,.4)}}
.card.ext li{{background:transparent;padding:4px 6px;color:rgba(25,35,75,.7)}}
.meta{{display:flex;flex-direction:column;align-items:center;gap:2px}}
.meta .m{{display:inline-flex;align-items:center;gap:4px;font:400 12px/1.3 var(--sans);color:rgba(25,35,75,.6)}}
.meta .m svg{{width:9px;height:9px}}
.meta .note{{font-weight:500;color:#C2570C}}
.meta .note::before{{content:"";width:6px;height:6px;background:#E8762B}}
.card.flag{{border-color:#E8762B}}
/* albero */
.tree{{overflow-x:auto;padding:4px 4px 16px;-webkit-overflow-scrolling:touch}}
.tree-in{{min-width:1280px}}
.root{{display:flex;justify-content:center}}
.root .card{{width:260px;border-color:var(--navy)}}
.root .card .ttl{{font:400 22px/1 var(--serif);text-transform:uppercase}}
.stem{{width:1.5px;height:32px;margin:0 auto;background:var(--navy)}}
.cols{{position:relative;display:grid;grid-template-columns:repeat({N},minmax(0,1fr));gap:16px;padding-top:32px}}
.cols::before{{content:"";position:absolute;top:0;height:1.5px;background:var(--navy);left:calc((100% - {16*(N-1)}px) / {N} / 2);right:calc((100% - {16*(N-1)}px) / {N} / 2)}}
.col{{position:relative;display:flex;flex-direction:column;align-items:stretch}}
.col::before{{content:"";position:absolute;top:-32px;left:50%;width:1.5px;height:32px;background:var(--navy);transform:translateX(-50%)}}
.grp{{display:flex;flex-direction:column;align-items:center;gap:2px;padding:10px 8px;border-radius:10px;background:var(--navy);color:#fff;text-align:center;font:500 15px/1.2 var(--sans)}}
.grp span{{font-size:11px;letter-spacing:.06em;text-transform:uppercase;color:var(--azzurro)}}
.link{{width:1.5px;height:20px;margin:0 auto;background:var(--bd)}}
.sub{{display:flex;flex-direction:column;padding:0 10px}}
.sub .card{{background:#FBFCFE}}
/* altre pagine + percorsi */
.others{{display:grid;grid-template-columns:repeat(4,minmax(0,1fr));gap:16px}}
.jrs{{display:grid;grid-template-columns:repeat(3,minmax(0,1fr));gap:16px}}
.jr{{border-top:1.5px solid var(--navy);padding-top:20px}}
.jr h3{{margin:0;font:400 22px/1.25 var(--sans)}}
.jr ol{{list-style:none;margin:20px 0 0;padding:0;counter-reset:s}}
.jr li{{counter-increment:s;position:relative;padding:0 0 18px 36px;font-size:15px;line-height:1.4;color:rgba(25,35,75,.8)}}
.jr li::before{{content:counter(s);position:absolute;left:0;top:-1px;width:22px;height:22px;border-radius:50%;display:grid;place-items:center;font:500 11px/1 var(--sans);background:var(--navy);color:#fff}}
.jr li:not(:last-child)::after{{content:"";position:absolute;left:11px;top:24px;bottom:2px;width:1px;background:rgba(25,35,75,.25)}}
.foot{{margin-top:112px;padding:28px 0 40px;border-top:1px solid rgba(25,35,75,.14);font-size:13px;color:rgba(25,35,75,.6);display:flex;justify-content:space-between;gap:24px;flex-wrap:wrap}}
@media (max-width: 899px){{
  .in{{width:calc(100% - 32px)}}
  .top{{padding:20px 0 48px}}
  .top .kick{{margin-top:56px}}
  .stats{{grid-template-columns:repeat(2,minmax(0,1fr));gap:24px 16px;margin-top:40px}}
  .sec{{padding:40px 0 64px}}
  .sh{{flex-direction:column;gap:16px;margin-bottom:24px}}
  .legend{{margin-bottom:32px}}
  .tree-in{{min-width:0}}
  .root .card{{width:100%}}
  .stem{{height:24px}}
  .cols{{grid-template-columns:1fr;gap:28px;padding-top:0}}
  .cols::before,.col::before{{display:none}}
  .others,.jrs{{grid-template-columns:1fr;gap:16px}}
  .jrs{{gap:40px}}
}}
</style>
</head>
<body>
<main>
  <section class="sec">
    <div class="in">
      <div class="sh"><h2>Mappa del sito</h2></div>
      <ul class="legend">
        <li><span class="sw hd"></span>Header</li>
        <li><span class="sw sc"></span>Sezione della pagina</li>
        <li><span class="sw ft"></span>Footer</li>
        <li><span class="sw tpl"></span>Più pagine con lo stesso modello</li>
        <li><span class="sw ext"></span>Sito esterno</li>
      </ul>
      <div class="tree"><div class="tree-in">
        <div class="root">{card(HOME)}</div>
        <div class="stem"></div>
        <div class="cols">{cols}</div>
      </div></div>
    </div>
  </section>

</main>

</body>
</html>
'''

open(os.path.join(ROOT, 'alberatura.html'), 'w').write(HTML)
print('alberatura.html scritta')
