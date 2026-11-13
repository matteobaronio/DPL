# News & eventi: rassegna stampa and eventi listings (zaro-like), article and event detail pages, and the 404 page (Figma 715:144).
import json
from urllib.parse import quote
from kit import hero, band, sec, head, ctab, btn, UR, SEARCH

# slug, category, title, excerpt, date, image
RS = [('rassegna-in-evidenza', 'In evidenza', '[Titolo dell’articolo in evidenza]', '[Testata · estratto dell’articolo più recente o più importante.]', '[Data]', 'mb12'),
      ('rassegna-articolo-1', 'Stampa', '[Titolo dell’articolo]', '[Testata · breve estratto dell’articolo su DPL Mediazione.]', '[Data]', 'mb2'),
      ('rassegna-articolo-2', 'Stampa', '[Titolo dell’articolo]', '[Testata · breve estratto dell’articolo.]', '[Data]', 'mb4'),
      ('rassegna-intervista-1', 'Intervista', '[Titolo dell’intervista]', '[Testata · chi parla e di cosa.]', '[Data]', 'mb8'),
      ('rassegna-video-1', 'Video', '[Titolo del video]', '[Canale · breve descrizione.]', '[Data]', 'mb10'),
      ('rassegna-articolo-3', 'Stampa', '[Titolo dell’articolo]', '[Testata · breve estratto.]', '[Data]', 'mb6'),
      ('rassegna-intervista-2', 'Intervista', '[Titolo dell’intervista]', '[Testata · breve estratto.]', '[Data]', 'mb3')]

# slug, category, title, excerpt, date shown, image, iso date, start, end
# Eventi ricavati dal calendario corsi (fonte: https://www.dplmediazione.it/formazione-civcom.html, letta il 12/11/2026)
EV = [('evento-mediazione-4-0', 'Incontri', 'Mediazione 4.0', 'L’appuntamento mensile per mediatori e avvocati: tre ore, il quarto lunedì del mese, in sede a Milano e online. Gratuito.', '23 novembre 2026 · 15:30', 'mb5', '2026-11-23', '15:30', '18:30'),
      ('evento-gestione-emozioni', 'Convegni', 'La gestione delle emozioni in mediazione', 'Profili deontologici e disciplinari. Accreditato dal COA di Milano: 3 crediti.', '23 novembre 2026', 'mb8', '2026-11-23', '15:30', '18:30'),
      ('evento-disturbi-personalita', 'Aggiornamenti', 'Relazioniamoci · Disturbi di personalità', 'Una giornata di aggiornamento per mediatori, a Milano.', '16 dicembre 2026', 'mb1', '2026-12-16', '09:00', '19:00'),
      ('evento-successioni-ereditarie', 'Aggiornamenti', 'Il conflitto nelle successioni ereditarie', 'Giornata di approfondimento a Milano e online.', '20 gennaio 2027', 'mb9', '2027-01-20', '09:00', '19:00'),
      ('evento-conflitto-condominiale', 'Aggiornamenti', 'Il conflitto condominiale', 'Giornata di approfondimento a Milano e online.', '17 marzo 2027', 'mb10', '2027-03-17', '09:00', '19:00'),
      ('evento-canoni-locazione', 'Aggiornamenti', 'Il conflitto per i canoni di locazione', 'Giornata di approfondimento a Milano e online.', '14 aprile 2027', 'mb2', '2027-04-14', '09:00', '19:00')]

NEWS_DD = 'News &amp; eventi'
UR_ICO = UR.replace('class="ur"', 'class="ico"')
SHARE = '<button class="btn-ghost copy-l" type="button" data-copy=""><span>Copia il link</span></button>'


def ccat(c):
    return c.lower().replace(' ', '-')


def card(slug, c, t, d, m, img, end='', more='Leggi'):
    de = f' data-end="{end}"' if end else ''
    return (f'<a class="post" href="{slug}.html"{de} data-cat="{ccat(c)}"><div class="ph"><img src="__IMG_{img}__" alt=""></div>'
            f'<div class="meta"><b>{c}</b><span>{m}</span></div><h3>{t}</h3><p>{d}</p><span class="go">{more} __ARROW_N__</span></a>')


def listing(mk, src, fname, title_a, title_b, intro, items, feat, more, events=False):
    cats = sorted({x[1] for x in items})
    chips = '<button data-chip="all" aria-pressed="true">Tutti</button>' + ''.join(f'<button data-chip="{ccat(c)}" aria-pressed="false">{c}</button>' for c in cats)
    fs, fc, ft, fd, fm, fimg = feat[:6]
    b = hero(title_a, title_b, intro, btn('DPL Magazine', 'https://www.dplmagazine.it/', 'glass', True, UR_ICO), ['News & eventi'])
    grid = ''.join(card(*x[:6], x[6] if events else '', more) for x in items)
    b += sec(f'<a class="post-feat" href="{fs}.html"><div class="ph"><img src="__IMG_{fimg}__" alt=""></div><div><div class="meta"><b>{fc}</b><span>{fm}</span></div>'
             f'<h2>{ft}</h2><p>{fd}</p><span class="go">{more} __ARROW_N__</span></div></a>'
             f'<div class="tools" data-filter=".post"><div class="chips-f">{chips}</div><label class="search">{SEARCH}<input type="search" placeholder="Cerca" aria-label="Cerca"></label></div>'
             f'<div class="posts">{grid}</div>', '')
    return mk(src, fname, title_a + ' ' + title_b if title_b else title_a, b, active_dd=NEWS_DD)


def rassegna(mk, src):
    return listing(mk, src, 'rassegna-stampa.html', 'Rassegna', 'stampa', 'Cosa scrivono di noi: articoli, interviste e video su DPL Mediazione e sulla mediazione in Italia.', RS[1:], RS[0], 'Leggi')


def eventi(mk, src):
    return listing(mk, src, 'eventi.html', 'Eventi', '', 'Incontri, convegni e giornate di aggiornamento aperti a mediatori, avvocati e professionisti.', EV[1:], EV[0], 'Dettagli e iscrizione', True)


def art_hero(crumb, meta, title, lead, btns=''):
    bt = f'<div class="btns">{btns}</div>' if btns else ''
    return (f'<section class="sec art-hero" id="top">\n  <div class="in">\n    <div class="rings" data-parallax="0.1"><div class="art">__DEVICE_CS__</div></div>\n__HEADER__\n'
            f'    <div class="ah"><a class="crumb" href="{crumb[1]}"><span class="ar">←</span>{crumb[0]}</a><div class="meta">{meta}</div>'
            f'<h1>{title}</h1><p class="lead blurin">{lead}</p>{bt}</div>\n  </div>\n</section>\n')


def pn_nav(items, i, label, kind):
    pv = items[i - 1] if i else None
    nx = items[i + 1] if i + 1 < len(items) else None
    return (f'<nav class="pn" aria-label="{label}">'
            + (f'<a href="{pv[0]}.html"><small>← {kind} precedente</small>{pv[2]}</a>' if pv else '')
            + (f'<a class="nx" href="{nx[0]}.html"><small>{kind} successivo →</small>{nx[2]}</a>' if nx else '') + '</nav>')


def articolo(mk, src, i):
    sl, c, t, d, m, img = RS[i]
    b = art_hero(('Rassegna stampa', '__HREF_RS__'), f'<b>{c}</b><span>{m}</span><span>[Testata]</span>', t, d)
    b += band(img, '')
    body = ('<p>[Primo paragrafo dell’articolo: chi, cosa, dove, quando.]</p><p>[Secondo paragrafo: il contesto e il ruolo di DPL Mediazione.]</p>'
            '<blockquote>[Una citazione significativa dall’articolo.]</blockquote><p>[Terzo paragrafo: i dati, le opinioni, le conclusioni.]</p>'
            '<p class="upd">Estratto. Il testo completo è sul sito della testata.</p>')
    src_btn = btn('Guarda il video' if c == 'Video' else 'Leggi l’originale', '#', 'navy', True, UR_ICO)
    aside = f'<dl class="ainfo"><dt>Fonte</dt><dd>[Testata]</dd><dt>Data</dt><dd>{m}</dd><dt>Tipo</dt><dd>{c}</dd></dl><div class="abtn">{src_btn}{SHARE}</div>'
    others = [x for j, x in enumerate(RS) if j != i][:3]
    b += sec(f'<div class="art"><aside>{aside}</aside><article class="prose">{body}</article></div>' + pn_nav(RS, i, 'Altri articoli', 'Articolo'), '')
    b += sec(head('Altri articoli') + '<div class="posts px-body">' + ''.join(card(*x, '', 'Leggi') for x in others) + '</div>', 'tint')
    return mk(src, f'{sl}.html', f'{t} · Rassegna stampa', b, active_dd=NEWS_DD)


def ics(t, day, h0, h1, where):
    d = day.replace('-', '')
    a, z = h0.replace(':', '') + '00', h1.replace(':', '') + '00'
    txt = ('BEGIN:VCALENDAR\r\nVERSION:2.0\r\nPRODID:-//DPL Mediazione//IT\r\nBEGIN:VEVENT\r\n'
           f'UID:{d}-{sum(map(ord, t))}@dplmediazione.it\r\nDTSTAMP:{d}T000000Z\r\nDTSTART;TZID=Europe/Rome:{d}T{a}\r\nDTEND;TZID=Europe/Rome:{d}T{z}\r\n'
           f'SUMMARY:{t} · DPL Mediazione\r\nLOCATION:{where}\r\nEND:VEVENT\r\nEND:VCALENDAR\r\n')
    return 'data:text/calendar;charset=utf-8,' + quote(txt)


def evento(mk, src, i, courses):
    sl, c, t, d, m, img, day, h0, h1 = EV[i]
    co = next((x for x in courses if x[1] == t), None)
    where = co[2] if co else 'Milano'
    rows = [('Quando', co[3]), ('Dove', where), ('Costo', co[4]), ('Durata', co[5]), ('Crediti', co[6])] if co else [('Quando', m), ('Dove', where)]
    info = '<dl class="ainfo">' + ''.join(f'<dt>{k}</dt><dd>{v}</dd>' for k, v in rows if v) + '</dl>'
    reg = f'__HREF_CON__?argomento=Formazione&amp;corso={quote(t)}#modulo'
    cal = f'<a class="btn-ghost" href="{ics(t, day, h0, h1, "DPL Mediazione, Via Monte Bianco 8, Milano")}" download="{sl}.ics">Aggiungi al calendario</a>'
    b = art_hero(('Eventi', '__HREF_EV__'), f'<b>{c}</b><span>{m}</span><span>{where}</span>', t, d,
                 btn('Richiedi informazioni', reg) + btn('Tutti gli eventi', '__HREF_EV__', 'line'))
    b += band(img, '')
    body = (f'<p>{d}</p><p>Gli eventi DPL sono aperti a mediatori, avvocati e professionisti. Per partecipare o avere informazioni scrivici dal modulo contatti: '
            'il titolo dell’evento è già inserito, ti ricontattiamo noi.</p><p class="upd">Programma, relatori e modalità di iscrizione: [da completare con DPL].</p>')
    aside = info + f'<div class="abtn">{btn("Richiedi informazioni", reg, "navy")}{cal}{SHARE}</div>'
    others = [x for j, x in enumerate(EV) if j != i][:3]
    b += sec(f'<div class="art ev" data-end="{day}"><aside><p class="ended">Questo evento si è concluso.</p>{aside}</aside><article class="prose">{body}</article></div>'
             + pn_nav(EV, i, 'Altri eventi', 'Evento'), '')
    b += sec(head('Altri eventi') + '<div class="posts px-body">' + ''.join(card(*x[:6], x[6], 'Dettagli e iscrizione') for x in others) + '</div>', 'tint')
    b += sec(ctab('Vuoi partecipare?', 'Scrivici: ti mandiamo programma e modalità di iscrizione.', btn('Richiedi informazioni', reg) + btn('02 49717642', 'tel:+390249717642', 'line')), 'flush')
    return mk(src, f'{sl}.html', f'{t} · Eventi', b, active_dd=NEWS_DD)


# ---------------------------------------------------------------- 404 (Figma 715:144)
NF = [('Non ti preoccupare.', 'Ti accompagniamo anche in questo. La pagina che cerchi non c’è, ma la strada per tornare sì.'),
      ('Anche qui non ti sei perso.', 'Questa pagina non esiste più. Ripartiamo insieme da un punto chiaro.'),
      ('Ogni situazione ha un’altra strada.', 'Come in mediazione, si riparte da ciò che funziona. Torna alla home o scrivi alla nostra segreteria.')]

NF_JS = '''
  /* ---- 404: a different reassuring message at each reload (cycles through 3) ---- */
  (() => { const M = %s; let i = 0;
    try { i = (parseInt(localStorage.getItem('dpl-404'), 10) || 0) %% M.length; localStorage.setItem('dpl-404', String(i + 1)); } catch (e) { i = Math.floor(Math.random() * M.length); }
    const el = document.querySelector('.nf-m'); if (el) { el.querySelector('b').textContent = M[i][0]; el.querySelector('span').textContent = M[i][1]; } })();
''' % json.dumps(NF, ensure_ascii=False)


def notfound(mk, src):
    links = [('Mediazione', '__HREF_MC__'), ('Formazione', '__HREF_FORM__'), ('Le nostre sedi', '__HREF_SEDI__'), ('Modulistica', '__HREF_MOD__'), ('News & eventi', '__HREF_RS__')]
    b = ('<section class="sec nf" id="top">\n  <div class="in">\n    <div class="rings" data-parallax="0.06"><div class="art">__DEVICE_404__</div></div>\n__HEADER__\n'
         '    <div class="nf-c"><h1 class="nf-n"><span class="sr">Errore </span>404<span class="sr">, pagina non trovata</span></h1>'
         f'<p class="nf-m" aria-live="polite"><b>{NF[0][0]}</b><span>{NF[0][1]}</span></p>'
         f'<div class="btns">{btn("Torna alla home", "__HREF_HOME__")}{btn("Scrivici", "__HREF_CON__", "line")}</div>'
         '<nav class="nf-l" aria-label="Pagine principali">' + ''.join(f'<a href="{u}">{t}</a>' for t, u in links) + '</nav></div>\n  </div>\n</section>\n')
    return mk(src, '404.html', 'Pagina non trovata', b, js=NF_JS, cta=False)


def pages(mk, courses):
    out = [((lambda src: rassegna(mk, src)), 'rassegna-stampa.html'), ((lambda src: eventi(mk, src)), 'eventi.html'), ((lambda src: notfound(mk, src)), '404.html')]
    out += [((lambda src, i=i: articolo(mk, src, i)), f'{x[0]}.html') for i, x in enumerate(RS)]
    out += [((lambda src, i=i: evento(mk, src, i, courses)), f'{x[0]}.html') for i, x in enumerate(EV)]
    return out
