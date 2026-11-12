# All inner pages of the "Poldo's Proposal" architecture (Figma 481:37), built with kit.py in the homepage brand.
import common, kit, regions_data
from urllib.parse import quote
from kit import hero, band, sec, head, feat, icards, steps, faq_sec, qband, ctab, btn, v_chat, v_path, v_docs, v_stack, v_orbit, v_map, ICONS, DL, UR, SEARCH

TEL = '<a href="tel:+390249717642">02 49717642</a>'
DOCS = 'docs/'  # served on the new site (Netlify proxy to the current archive, see _redirects)
OLD = 'https://www.dplmediazione.it/'

def mk(src, fname, title, body, active_nav=None, active_dd=None, js='', cta=True):
    def hdr(h):
        if active_nav: h = h.replace(f'<a href="{active_nav}">', f'<a class="is-active" href="{active_nav}" aria-current="page">', 1)
        if active_dd: h = h.replace(f'<button class="dd-btn" aria-expanded="false" aria-haspopup="true">{active_dd}', f'<button class="dd-btn is-active" aria-expanded="false" aria-haspopup="true">{active_dd}', 1)
        return h
    return common.page(src, f'{title} · DPL Mediazione', body, kit.CSS, kit.FILTER_JS + js, hdr, fname, cta)

# ---------------------------------------------------------------- Mediazione familiare
def familiare(src):
    b = hero('Mediazione', 'familiare',
             'Un’opportunità per gestire la separazione in modo meno doloroso: uno spazio neutro e riservato, alternativo alle vie legali, in cui sono le parti a decidere per il loro futuro.',
             btn('Fissa il primo incontro', 'tel:+390249717642') + btn('Scrivici', '__HREF_CON__', 'line'),
             ['Primo appuntamento gratuito', 'Al massimo 12 incontri', 'In sede o online'])
    b += band('mb9', 'Persone a confronto durante un incontro')
    b += sec(head('A chi si rivolge', 'Alle coppie, con o senza figli, e a chi vive un conflitto in famiglia.') + icards([
        ('persona', 'Coppie in crisi', 'Coniugate o conviventi, con o senza figli, in crisi o in fase di separazione.'),
        ('gruppo', 'Coppie separate o divorziate', 'Per riorganizzare la vita familiare e rivedere gli accordi quando le cose cambiano.'),
        ('dialogo', 'Altri conflitti in famiglia', 'Tra genitori e figli, tra fratelli adulti, tra genitori davanti a scelte importanti per i figli.')]))
    b += sec(head('Il percorso', 'Breve e strutturato, con entrambi i membri della coppia.') + '<div class="px-body">' +
        feat('Un incontro alla volta, al massimo dodici',
             'Il mediatore, imparziale ed equiprossimo, aiuta la coppia a riorganizzare la vita familiare e a individuare insieme le soluzioni migliori per il benessere dei figli e dei genitori, senza vincitori né vinti.',
             ['La cura e l’educazione dei figli', 'Gli aspetti economici e patrimoniali', 'Il mediatore non decide: non è un giudice né un arbitro'],
             v_path('Primo incontro <b>gratuito</b>', 'Inizio', 'Accordo')) +
        feat('Ascolto e comunicazione, di nuovo',
             'Riattivare un ascolto reciproco è il primo passo. Accogliamo i bisogni e le emozioni di chi vive una relazione conflittuale, in uno spazio riservato.',
             [], v_chat([('me', 'Vorremmo capire come organizzarci con i bambini.', ''), ('us', 'Partiamo da quello che funziona già. Cosa è importante per ciascuno di voi?', 'Mediatrice'), ('me', 'Che possano vedere entrambi i genitori con regolarità.', ''), ('us', 'Bene: è un obiettivo comune. Lo mettiamo per primo.', 'Mediatrice')]), rev=True) + '</div>', 'flush')
    b += qband('La relazione di coppia può finire, ma genitori si rimane per sempre.', 'Il principio da cui partiamo')
    b += sec(head('Come iniziare') + steps([
        ('Chiamaci o scrivici', 'Al 02 49717642 o dal modulo contatti: ti ricontattiamo noi.'),
        ('Primo appuntamento', 'Gratuito: conosciamo la situazione e ti spieghiamo come funziona il percorso.'),
        ('Gli incontri', 'Con entrambi i membri della coppia, in sede o online, fino a un massimo di 12.'),
        ('L’accordo', 'Le soluzioni trovate insieme, per i figli e per la famiglia.')]), '')
    b += faq_sec([
        ('Il mediatore decide per noi?', '<p>No. Il mediatore non ha potere decisionale, non è un giudice e nemmeno un arbitro: sono le parti a decidere per il loro futuro.</p>'),
        ('Quanto dura il percorso?', '<p>È un percorso breve e strutturato, al massimo 12 incontri con entrambi i membri della coppia.</p>'),
        ('Il primo incontro è a pagamento?', '<p>No, il primo appuntamento è gratuito.</p>'),
        ('Possiamo parlare anche di questioni economiche?', '<p>Sì. Oltre alla cura e all’educazione dei figli, in mediazione familiare si possono affrontare gli aspetti economici e patrimoniali.</p>')])
    b += sec(ctab('Fissa il primo appuntamento gratuito', 'Ti rispondiamo con chiarezza, senza impegno.', btn('Chiama 02 49717642', 'tel:+390249717642') + btn('Scrivici', '__HREF_CON__', 'line')), 'flush')
    return mk(src, 'mediazione-familiare.html', 'Mediazione familiare', b, active_dd='Mediazione')

# ---------------------------------------------------------------- Mediazione sanitaria, penale e lavorativa
def sanitaria(src):
    b = hero('Mediazione sanitaria,', 'penale e lavorativa',
             'Con l’associazione Me.Dia.Re. di Torino offriamo servizi a chi sta vivendo un conflitto sul lavoro, in ambito sanitario o scolastico, tra vicini o nei rapporti professionali.',
             btn('Parla con noi', '__HREF_CON__') + btn('Chiama', 'tel:+390249717642', 'line'),
             ['In collaborazione con Me.Dia.Re.', 'Torino'])
    b += band('mb6', 'Una professionista durante un incontro')
    b += sec(head('Dove interveniamo', 'Conflitti diversi, lo stesso approccio: ascolto, chiarezza e competenza.') + icards([
        ('gruppo', 'Sul luogo di lavoro', 'Tensioni tra colleghi, con i responsabili o all’interno dei gruppi di lavoro.'),
        ('accoglienza', 'In ambito sanitario', 'Tra pazienti, familiari e strutture o professionisti della cura.'),
        ('persona', 'In ambito scolastico', 'Tra famiglie, studenti e scuola.'),
        ('dialogo', 'Nei rapporti di vicinato', 'Quando la convivenza quotidiana diventa difficile.'),
        ('ascolto', 'Nelle prestazioni professionali', 'Nei rapporti che nascono da un incarico o da un servizio professionale.'),
        ('ricerca', 'Penale', 'Percorsi di confronto tra le persone coinvolte, quando la legge lo prevede.')], 3), '')
    b += sec('<div class="px-body" style="margin-top:0">' + feat('La persona, prima del conflitto',
        'Chi arriva in mediazione non è soltanto «una parte di un conflitto»: se si sente riconosciuto nella propria complessità, supera le resistenze e comprende che la mediazione non è uno strumento di pacificazione ma di confronto, anche aspro.',
        ['Uno spazio riservato e neutrale', 'Mediatori formati sui contesti relazionali', 'Incontri in sede o online'],
        v_orbit('ascolto', ['Lavoro', 'Sanità', 'Scuola', 'Vicinato', 'Professioni', 'Penale'])) + '</div>', 'tint')
    b += qband('Non uno strumento di pacificazione, ma di confronto.', 'Il nostro modo di intendere la mediazione')
    b += sec(ctab('Raccontaci la situazione', 'Ti diciamo con chiarezza se e come la mediazione può aiutarti.', btn('Scrivici', '__HREF_CON__') + btn('02 49717642', 'tel:+390249717642', 'line')), '')
    return mk(src, 'mediazione-sanitaria.html', 'Mediazione sanitaria, penale e lavorativa', b, active_dd='Mediazione')

# ---------------------------------------------------------------- Formazione
COURSES = [
 ('corso', 'Corso di mediazione civile e commerciale · 41ª edizione', 'Milano e online', '24 febbraio – 12 marzo 2027', 'Consultare i dettagli', '80 ore (+14 approfondimento giuridico)', '18 CF corso · 10 CF aggiornamento'),
 ('corso', 'Corso di mediazione civile e commerciale · 42ª edizione', 'Milano e online', '9 – 25 giugno 2027', 'Consultare i dettagli', '80 ore (+14 approfondimento giuridico)', '18 CF corso · 10 CF aggiornamento'),
 ('corso', 'Corso biennale mediatori familiari · 5ª edizione', 'Milano', '14/03/2025 – 04/07/2026', '2.800 € + IVA, rateizzabile', 'Biennale', '20 CF Avv.'),
 ('incontro', 'Mediazione 4.0', 'Milano e online', 'Quarto lunedì del mese, 15:30–18:30', 'Gratuito', '3 ore al mese', 'In accreditamento'),
 ('incontro', 'La gestione delle emozioni in mediazione', 'Milano e online', '23 novembre 2026, 15:30–18:30', 'Gratuito, su prenotazione', '3 ore', '3 CF COA Milano'),
 ('aggiornamento', 'Relazioniamoci · Analisi transazionale in mediazione', 'Milano', '14 ottobre 2026, 9–19', '100 € IVA esente (mediatori DPL)', '10 ore', ''),
 ('aggiornamento', 'Relazioniamoci · Disturbi di personalità', 'Milano', '16 dicembre 2026, 9–19', '100 € IVA esente (mediatori DPL)', '10 ore', ''),
 ('aggiornamento', 'Il conflitto nelle successioni ereditarie', 'Milano e online', '20 gennaio 2027, 9–19', '125 € IVA esente', '', 'In accreditamento'),
 ('aggiornamento', 'Il conflitto nelle divisioni a seguito di separazione', 'Milano e online', '17 febbraio 2027, 9–19', '125 € IVA esente', '', 'In accreditamento'),
 ('aggiornamento', 'Il conflitto condominiale', 'Milano e online', '17 marzo 2027, 9–19', '125 € IVA esente', '', 'In accreditamento'),
 ('aggiornamento', 'Il conflitto per i canoni di locazione', 'Milano e online', '14 aprile 2027, 9–19', '125 € IVA esente', '', 'In accreditamento'),
]
MESI = {m: i for i, m in enumerate(['gennaio','febbraio','marzo','aprile','maggio','giugno','luglio','agosto','settembre','ottobre','novembre','dicembre'], 1)}
def end_iso(when):
    """Last date in a free-text period ('9 – 25 giugno 2027', '14/03/2025 – 04/07/2026') as YYYY-MM-DD, or '' for recurring dates."""
    import re
    d = re.findall(r'(\d{1,2})/(\d{1,2})/(\d{4})', when)
    if d: g, m, y = d[-1]; return f'{y}-{int(m):02d}-{int(g):02d}'
    d = re.findall(r'(\d{1,2})\s+(' + '|'.join(MESI) + r')\s+(\d{4})', when)
    if d: g, m, y = d[-1]; return f'{y}-{MESI[m]:02d}-{int(g):02d}'
    return ''
CATS = {'corso': 'Corso abilitante', 'incontro': 'Incontro gratuito', 'aggiornamento': 'Aggiornamento'}

def course_cards(items):
    out = []
    for cat, t, where, when, cost, dur, cf in items:
        rows = ''.join(f'<dt>{k}</dt><dd>{v}</dd>' for k, v in [('Dove', where), ('Quando', when), ('Costo', cost), ('Durata', dur), ('Crediti', cf)] if v)
        e = end_iso(when); de = f' data-end="{e}"' if e else ''
        out.append(f'<article class="course" data-cat="{cat}"{de}><span class="tag{" free" if cat == "incontro" else ""}">{CATS[cat]}</span><h3>{t}</h3><dl>{rows}</dl><a class="go" href="__HREF_CON__?argomento=Formazione&amp;corso={quote(t)}#modulo">Richiedi informazioni __ARROW_N__</a></article>')
    return '\n'.join(out)

def courses_block(items):
    """Course grid; on mobile the first three show, the rest behind «Mostra tutti»."""
    n = max(0, len(items) - 3)
    return f'<div class="courses">{course_cards(items)}</div><div class="more-c" data-n="{n}"><button class="btn-ghost" type="button">Mostra tutti i corsi ({len(items)})</button></div>'

def formazione(src):
    b = hero('Formazione', 'per mediatori',
             'Siamo ente di formazione accreditato presso il Ministero della Giustizia: corsi per diventare mediatori, aggiornamenti e incontri aperti a professionisti e avvocati.',
             btn('Vedi i corsi', '#corsi') + btn('DPL Accademy', 'https://www.dplaccademy.it/', 'line', True, UR.replace('class="ur"', 'class="ico"')),
             ['Ente accreditato', 'Milano e online', 'Crediti formativi per avvocati'])
    b += band('mb5', 'Un formatore spiega durante un corso')
    b += sec(head('Corsi e incontri', 'Civile e commerciale: il calendario dei prossimi appuntamenti.') +
        '<div class="px-body"><div class="tools" data-filter=".course"><div class="chips-f"><button data-chip="all" aria-pressed="true">Tutti</button><button data-chip="corso" aria-pressed="false">Corsi abilitanti</button><button data-chip="aggiornamento" aria-pressed="false">Aggiornamenti</button><button data-chip="incontro" aria-pressed="false">Incontri gratuiti</button></div>'
        f'<label class="search">{SEARCH}<input type="search" placeholder="Cerca un corso" aria-label="Cerca un corso"></label></div>'
        + courses_block(COURSES) + '</div>', '', 'corsi')
    b += sec('<div class="px-body" style="margin-top:0">' + feat('Diventare mediatore',
        'Il corso di mediazione civile e commerciale dura 80 ore, con un approfondimento giuridico di 14 ore per chi ha una laurea diversa da giurisprudenza, ed esame finale. Gli aggiornamenti valgono per la formazione continua dei mediatori.',
        ['Patrocinio EIMI e Ordine degli Avvocati di Milano', 'In aula a Milano o online', 'Aggiornamento da 18 ore per i mediatori'],
        v_stack([('Corso abilitante', 'Mediazione civile e commerciale', '80 ore · esame finale'), ('Aggiornamento', 'Il conflitto condominiale', '17 marzo 2027 · 9–19'), ('Incontro gratuito', 'Mediazione 4.0', 'Quarto lunedì del mese')])) + '</div>', 'tint')
    acc = [('Familiare', 'Corso biennale e percorsi per mediatori familiari.', 'https://www.dplaccademy.it/'),
           ('Coordinazione genitoriale', 'Formazione specialistica per professionisti.', 'https://www.dplaccademy.it/'),
           ('Seminari e aggiornamenti', 'Il calendario completo degli eventi formativi.', 'https://www.dplaccademy.it/'),
           ('Area corsisti', 'Materiali e accesso riservato per chi frequenta i corsi.', 'https://www.dplaccademy.it/login.html')]
    b += sec(head('Su DPL Accademy', 'La formazione familiare e specialistica vive sul sito di DPL Accademy.') +
        '<div class="lst px-body">' + ''.join(f'<a href="{u}" target="_blank" rel="noopener"><span class="t">{t}</span><span class="m">{d}</span>{UR}</a>' for t, d, u in acc) + '</div>', '')
    b += sec(ctab('Hai domande su un corso?', 'Ti aiutiamo a scegliere il percorso giusto.', btn('Scrivici', '__HREF_CON__') + btn('02 49717642', 'tel:+390249717642', 'line')), 'flush')
    return mk(src, 'formazione.html', 'Formazione', b, active_nav='__HREF_FORM__')

# ---------------------------------------------------------------- Le nostre sedi
CITIES = [('Avellino','Campania',40.91,14.79),('Busto Arsizio','Lombardia',45.61,8.85),('Como','Lombardia',45.81,9.09),('Cuneo','Piemonte',44.39,7.55),
 ('Ivrea','Piemonte',45.47,7.88),('Lecco','Lombardia',45.86,9.40),('Milano','Lombardia',45.46,9.19),('Monza','Lombardia',45.58,9.27),('Pavia','Lombardia',45.19,9.16),
 ('Piacenza','Emilia-Romagna',45.05,9.69),('Rieti','Lazio',42.40,12.86),('Roma','Lazio',41.90,12.50),('Salerno','Campania',40.68,14.77),('Sondrio','Lombardia',46.17,9.87),
 ('Terni','Umbria',42.56,12.65),('Tivoli','Lazio',41.96,12.80),('Torino','Piemonte',45.07,7.69),('Torre Annunziata','Campania',40.75,14.45),('Varese','Lombardia',45.82,8.83),('Velletri','Lazio',41.69,12.78)]
def slug(c): return c.lower().replace(' ', '-').replace('’', '').replace("'", '')

def sedi(src):
    regs = sorted({r for _, r, _, _ in CITIES})
    b = hero('Le nostre', 'sedi',
             'Venti sedi in Italia, da Torino a Salerno: la mediazione vicino a te. Ogni sede ha i suoi mediatori e i suoi corsi.',
             btn('Trova la sede', '#elenco') + btn('Sede di Milano', 'sede-milano.html', 'line'),
             ['20 sedi', '6 regioni', 'Sede principale a Milano'])
    b += band('mb11', 'Due professionisti camminano in città')
    b += sec('<div class="px-body" style="margin-top:0">' + feat('La rete DPL in Italia',
        'Per la mediazione vale la competenza territoriale: la domanda va presentata a un organismo nel luogo del giudice competente. Con venti sedi è più facile trovare quella giusta.',
        ['Milano, Via Monte Bianco 8: sede principale', 'Lombardia, Piemonte, Emilia-Romagna, Lazio, Umbria e Campania', 'Mediazioni anche in videoconferenza'],
        v_map([(c, la, lo, c == 'Milano') for c, _, la, lo in CITIES])) + '</div>', 'tint')
    chips = '<button data-chip="all" aria-pressed="true">Tutte</button>' + ''.join(f'<button data-chip="{r.lower()}" aria-pressed="false">{r}</button>' for r in regs)
    cards = ''.join(
        f'<a class="city{" hq" if c == "Milano" else ""}" data-cat="{r.lower()}" href="sede-{slug(c)}.html"><span class="rg">{r}</span><span class="c">{c}</span><span class="go">__ARROW_N__</span></a>'
        for c, r, _, _ in CITIES)
    b += sec(head('Trova la sede più vicina', 'Cerca per città o filtra per regione.') +
        f'<div class="px-body"><div class="tools" data-filter=".city"><div class="chips-f">{chips}</div><label class="search">{SEARCH}<input type="search" placeholder="Cerca una città" aria-label="Cerca una città"></label></div><div class="cities">{cards}</div></div>', '', 'elenco')
    b += sec(ctab('Cerchi un organismo convenzionato?', 'L’elenco delle sedi ex art. 6 D.M. 150/23, regione per regione.', btn('Sedi convenzionate', '__HREF_EX6__')), 'flush')
    return mk(src, 'sedi.html', 'Le nostre sedi', b, active_nav='__HREF_SEDI__')

PROS = '''AVV MARCO ACCOSSANO|Avv. MARIA CRISTINA AIELLO|AVV. ELENA ALIANI|Dott.ssa ELISA ALLEGRINI|AVV. FRANCESCA ARALDI|Avv. ELENA ARPINI|AVV. ANNA BANTERLA|Dott. MARIO BARLOCCO|DOTT. GIANFRANCO BAUDONE|dott.ssa MARIA BERTONE|AVV FEDERICA GIULIA BESOSTRI|Dott.ssa LAURA BIANCHI|AVV. FRANCO BIGOT|AVV. LUCIA BONANNI|Dott.ssa LUCIA ADELE BONOMETTI|Dott.ssa NADIA BORDONI|AVV. CHIARA BRAMBILLA|AVV. DAVIDE BRUNO BRESEGHELLO|AVV. SARA BRIOSCHI|dott. WALTER CAGNONI|Avv. MILENA CAIROLI|AVV. ROBERTA STEFANIA CASSANI|Avv. ALESSIA CASTELLANA|AVV. PIERA ROSALIA GIUSEPPINA CATRISANO|Dott.ssa FRANCESCA CAVALLERI|AVV. GIOVANNA CIANCI|AVV LUCIA COLITTI|Dott.ssa CHIARA CONCINA|Avv. SERENA CONTE|Avv. EMANUELA CONTIN|DOTT.SSA TIZIANA CORSI|Avv. EMANUELA CRIPPA|AVV GIANFRANCO CURCI|Dott.ssa GIOVANNA ROSARIA DEL BENE|Avv. LAURA DELL'ORO|AVV. ROSSELLA FEDERICA DI MURO|Dott.ssa LUCIA GIUSEPPA DI PALERMO|AVV. MARCO FALAPPI|AVV. SOLANGE FARRUGGIO|AVV. ANNAMARIA FEROLETO|DOTT.SSA LAURA FERRARIO|dott. EMANUELE FINALDI|Avv. SIMONA FORZANI|Dott. DAMIANO FRANGI|AVV ELENA FUSI|Avv. SUSANNA GALIMBERTI|AVV. LEONIERO PAOLO GALLEANI|Dott.ssa ANTONELLA GAROFALO|AVV. MILA GARUTI|Avv. SARA GIUGGIOLI|AVV. GUGLIELMINA GRASSI|AVV. LAURA GRINGERI|AVV MARIANNA ELISABETTA GURRADO|AVV. ALESSANDRA LIPPI|AVV. LUCA LODATO|Dott.ssa ELENA LOPRIORE|dott.ssa ANNA MARIA LUNGHI|AVV. VIVIANA MAGGIONI|Avv. MONICA MALAFOGLIA|dott.ssa CARMEN MANFREDDA|Avv. ANNA CARLA MANGIONE|Dott.ssa EMANUELA MARROCCO|AVV. MONICA MERONI|dott.ssa BELINDA MAARIA MINNECI|AVV. SABRINA MITA|DOTT. FEDERICO CARLO MOIA|DOTT.SSA MARIA NACCARATO|Dott.ssa STEFANIA NACCARELLA|AVV. ALESSIA NAPOLANO|Avv. CLAUDIA NAPOLI|Avv. DONATELLA MARIA PACIELLO|DOTT. ALESSANDRO ANDREA PAVIA|Avv. PAMELA PAVIOTTI|AVV. PAOLA PELLEGRINI|AVV. MASSIMO PIAZZOLI|Avv. GIUSEPPE PICCARDO|Avv. SILVIA PIRO|Dott.ssa GABRIELLA PONTI|Avv. PAOLO PONTIGGIA|DOTT.SSA LUCIA POZZI|AVV. VALERIA RAPPA|DOTT. REMO REDEGHIERI|Avv. FRANCESCA RESTA|Dott.ssa Sonia Riva|AVV. SANNITA ROVETTA|DOTT.SSA ELISA SALVATORE|Avv. MASSIMO SANGUINETI|Avv. LUCA SAULLE|Dott. FRANCESCO SCHINAIA|AVV. FEDERICA SIRONI|AVV MICHELA SIRONI|Dott.ssa ROSA TANGERINI|Avv. ALESSANDRA TOSELLI|Avv. VITTORIA ZANUSSO|Avv. LAURA ZECCHI'''

def nice_name(n):
    import re
    m = re.match(r'(?i)(avv\.?|dott\.ssa|dott\.?)\s+(.*)', n.strip())
    t, rest = (m.group(1), m.group(2)) if m else ('', n)
    t = {'avv': 'Avv.', 'avv.': 'Avv.', 'dott.ssa': 'Dott.ssa', 'dott': 'Dott.', 'dott.': 'Dott.'}.get(t.lower(), t)
    rest = ' '.join(w.capitalize() if not w.startswith("DELL'") else "Dell'" + w[5:].capitalize() for w in rest.split())
    return (t + ' ' + rest).strip()

def sede_milano(src):
    b = hero('Sede di', 'Milano',
             'La nostra sede principale, in Via Monte Bianco 8. Qui si svolgono gli incontri di mediazione e buona parte dei corsi, anche online.',
             btn('Chiama la sede', 'tel:+390249717642') + btn('Indicazioni', 'https://www.google.com/maps/search/?api=1&query=Via+Monte+Bianco+8+Milano', 'line', True, UR.replace('class="ur"', 'class="ico"')),
             ['Via Monte Bianco 8', '20149 Milano', 'Lun–ven 9–13 · 14–18'], crumb=('Le nostre sedi', '__HREF_SEDI__'))
    b += band('mb1', 'Accoglienza in sede')
    b += sec('<div class="ccards">' +
        '<div class="ccard"><span class="k">Indirizzo</span><span class="v">Via Monte Bianco 8<br>20149 Milano</span></div>'
        '<div class="ccard"><span class="k">Telefono</span><a class="v" href="tel:+390249717642">02 49717642</a></div>'
        '<div class="ccard"><span class="k">E-mail</span><a class="v" href="mailto:info@dplmediazione.it">info@dplmediazione.it</a></div>'
        '<div class="ccard"><span class="k">Segreteria</span><span class="v">Lun–ven<br>9–13 · 14–18</span></div></div>', '')
    mil = [c for c in COURSES]
    b += sec(head('Corsi della sede', 'Corsi, aggiornamenti e incontri in programma a Milano e online.') + f'<div class="px-body">{courses_block(mil[:6])}</div>', 'tint', 'corsi')
    names = [nice_name(n) for n in PROS.split('|')]
    b += sec(head('Professionisti della sede', f'{len(names)} mediatori e professionisti della sede di Milano.') +
        f'<div class="px-body"><div class="tools" data-filter=".names span"><label class="search">{SEARCH}<input type="search" placeholder="Cerca un professionista" aria-label="Cerca un professionista"></label></div><div class="names">' +
        ''.join(f'<span>{n}</span>' for n in names) + f'</div><div class="more-c" data-n="{len(names) - 12}"><button class="btn-ghost" type="button">Mostra tutti i {len(names)} professionisti</button></div></div>', '', 'professionisti')
    b += sec(ctab('Vuoi un incontro a Milano?', 'Chiamaci o scrivici: fissiamo il primo incontro in sede o online.', btn('02 49717642', 'tel:+390249717642') + btn('Scrivici', '__HREF_CON__', 'line')), 'flush')
    return mk(src, 'sede-milano.html', 'Sede di Milano', b, active_nav='__HREF_SEDI__')

def sede(src, c, r):
    b = hero('Sede di', c, f'La sede DPL di {c}, in {r}. Per fissare un incontro o avere informazioni, la nostra segreteria ti mette in contatto con la sede.',
             btn('Chiama la segreteria', 'tel:+390249717642') + btn('Scrivici', f'__HREF_CON__?sede={quote(c)}#modulo', 'line'), [r, 'Mediazione in sede e online'], crumb=('Le nostre sedi', '__HREF_SEDI__'))
    b += band('mb1', 'Accoglienza in sede')
    b += sec('<div class="ccards">'
        '<div class="ccard"><span class="k">Indirizzo</span><span class="v">[Indirizzo della sede]</span></div>'
        '<div class="ccard"><span class="k">Referente</span><span class="v">[Nome del referente]</span></div>'
        '<div class="ccard"><span class="k">Segreteria</span><a class="v" href="tel:+390249717642">02 49717642</a></div>'
        '<div class="ccard"><span class="k">E-mail</span><a class="v" href="mailto:info@dplmediazione.it">info@dplmediazione.it</a></div></div>', '')
    online = [x for x in COURSES if 'online' in x[2]]
    b += sec(head('Corsi disponibili', 'Corsi e incontri che puoi seguire online da qualsiasi sede.') + f'<div class="px-body">{courses_block(online[:6])}</div>', 'tint', 'corsi')
    b += sec(head('Professionisti della sede', 'I mediatori e i professionisti che lavorano a ' + c + '.') + '<div class="px-body"><div class="lst"><div class="row"><span class="t">[Elenco dei professionisti della sede]</span></div></div></div>', '', 'professionisti')
    b += sec(ctab(f'Vuoi un incontro a {c}?', 'Chiamaci o scrivici: fissiamo il primo incontro in sede o online.', btn('02 49717642', 'tel:+390249717642') + btn('Scrivici', f'__HREF_CON__?sede={quote(c)}#modulo', 'line')), 'flush')
    return mk(src, f'sede-{slug(c)}.html', f'Sede di {c}', b, active_nav='__HREF_SEDI__')

# ---------------------------------------------------------------- Modulistica
MODULI = [('mediazione', 'Domanda di mediazione', 'domanda_di_mediazione_v07.pdf'), ('mediazione', 'Domanda di mediazione congiunta', 'domanda_di_mediazione_congiunta_v07.pdf'),
  ('mediazione', 'Allegato A · Adeguata verifica', 'ALLEGATO_A_ADEGUATA_VERIFICA_v07.pdf'), ('mediazione', 'Allegato B · Ulteriori parti', 'ALLEGATO_B_ULTERIORI_PARTI_v07.pdf'),
  ('mediazione', 'Allegato C · Ulteriori difensori', 'ALLEGATO_C_ULTERIORI_DIFENSORI_v07.pdf'), ('procedura', 'Modulo di adesione', 'modulo_adesione_primo_incontro_v07.pdf'),
  ('procedura', 'Delega all’assistenza in mediazione', 'delega_assistenza_mediazione_v06.pdf'), ('procedura', 'Procura speciale sostanziale', 'procura_speciale_sostanziale_mediazione_v06.pdf'),
  ('procedura', 'Regolamento DPL', 'regolamento_DPL_2025.pdf'), ('costi', 'Tabella costi · mediazioni volontarie', 'INDENNITA_MEDIAZIONI_VOLONTARIE_DPL_2025.pdf'),
  ('costi', 'Tabella costi · materie obbligatorie', 'INDENNITA_MEDIAZIONI_OBBLIGATORIE_DPL_2025.pdf'), ('costi', 'Tabelle ministeriali', 'tabella_ministero_2024.pdf')]

def modulistica(src):
    b = hero('Modulistica', '',
             'Tutti i documenti per avviare e seguire una mediazione, in PDF. Compilali e inviali per e-mail o PEC, oppure deposita la domanda dall’area riservata.',
             btn('Area riservata', 'https://www.dplmediazione.eu/', 'glass', True) + btn('Come si avvia', '__HREF_MC__#avvia', 'line'),
             ['12 documenti', 'PDF', 'Aggiornati al 2025'])
    labels = {'mediazione': 'Domanda e allegati', 'procedura': 'Durante la procedura', 'costi': 'Costi'}
    rows = ''.join(f'<a data-cat="{c}" href="{DOCS}{f}" target="_blank" rel="noopener">__ICO_FILE__<span class="t">{n}</span><span class="m">{labels[c]} · PDF</span>{DL}</a>' for c, n, f in MODULI)
    b += band('mb7', 'Documenti su una scrivania')
    b += sec('<div class="px-body" style="margin-top:0"><div class="tools" data-filter=".lst a"><div class="chips-f"><button data-chip="all" aria-pressed="true">Tutti</button>' +
        ''.join(f'<button data-chip="{k}" aria-pressed="false">{v}</button>' for k, v in labels.items()) +
        f'</div><label class="search">{SEARCH}<input type="search" placeholder="Cerca un documento" aria-label="Cerca un documento"></label></div><div class="lst">{rows}</div></div>', '')
    b += sec('<div class="px-body" style="margin-top:0">' + feat('Preferisci farlo online?',
        'Dall’area riservata depositi la domanda in pochi minuti, scegli la data del primo incontro dal nostro calendario e segui lo stato della mediazione. È gratuita.',
        ['Deposito della domanda', 'Calendario del primo incontro', 'Stato della mediazione sempre aggiornato'],
        v_docs([('Domanda di mediazione.pdf', 'Caricata'), ('Allegato A.pdf', 'Caricata'), ('Delega.pdf', 'Caricata'), ('Primo incontro', 'Fissato')])) + '</div>', 'tint')
    return mk(src, 'modulistica.html', 'Modulistica', b, active_nav='__HREF_MOD__')

# ---------------------------------------------------------------- Contatti (+ Lavora con noi)
def contatti(src):
    b = hero('Parliamone', '',
             'Ti rispondiamo con chiarezza, senza impegno. Scrivici dal modulo, chiamaci o passa in sede a Milano. Vuoi lavorare con noi? <a class="inline-link" href="#lavora-con-noi">Scrivici una e-mail</a>.',
             btn('Chiama 02 49717642', 'tel:+390249717642') + btn('Scrivici', '#modulo', 'line'),
             ['Lun–ven 9–13 · 14–18', 'Via Monte Bianco 8, Milano'])
    b += band('mb12', 'Persone sorridenti durante un incontro')
    b += sec('<div class="ccards">'
        '<div class="ccard"><span class="k">Telefono</span><a class="v" href="tel:+390249717642">02 49717642</a></div>'
        '<div class="ccard"><span class="k">E-mail</span><a class="v" href="mailto:info@dplmediazione.it">info@dplmediazione.it</a></div>'
        '<div class="ccard"><span class="k">Sede principale</span><span class="v">Via Monte Bianco 8<br>20149 Milano</span></div>'
        '<div class="ccard"><span class="k">Segreteria</span><span class="v">Lun–ven<br>9–13 · 14–18</span></div></div>', '')
    opts = ''.join(f'<option>{c}</option>' for c, *_ in CITIES)
    form = (f'<form class="form" name="contatti" method="POST" data-netlify="true" netlify-honeypot="bot-field" action="__HREF_CON__#grazie"><input type="hidden" name="form-name" value="contatti"><p hidden><label>Non compilare <input name="bot-field"></label></p>'
            '<label>Nome e cognome<input name="nome" required autocomplete="name"></label><label>E-mail<input type="email" name="email" required autocomplete="email"></label>'
            '<label>Telefono<input type="tel" name="telefono" autocomplete="tel"></label>'
            '<label>Argomento<select name="argomento"><option>Mediazione civile e commerciale</option><option>Mediazione familiare</option><option>Mediazione sanitaria, penale e lavorativa</option><option>Formazione</option><option>Altro</option></select></label>'
            f'<label class="full">Sede di riferimento<select name="sede"><option>Non so</option>{opts}</select></label>'
            '<label class="full">Messaggio<textarea name="messaggio" required></textarea></label>'
            '<label class="check full"><input type="checkbox" name="privacy" required> <span>Ho letto l’<a href="__HREF_PRIV__">informativa privacy</a> e acconsento al trattamento dei dati per ricevere una risposta.</span></label>'
            '<button class="btn-navy" type="submit">Invia la richiesta __ARROW_W__</button></form>')
    b += sec('<div class="two-col"><div class="side"><h2 class="h2 blurin">Scrivici</h2><p class="blurin">Raccontaci in poche righe di cosa hai bisogno: ti ricontattiamo noi.</p></div>' + form + '</div>', 'flush', 'modulo')
    MAIL = 'info@dplmediazione.it'
    def mt(subj, body=''):
        return f'mailto:{MAIL}?subject=' + quote(subj) + ('&amp;body=' + quote(body) if body else '')
    tmpl = 'Buongiorno,\nmi chiamo … e sono …\n\nMi interessa: …\nCittà o zona: …\n\nAllego il mio CV.\n'
    roles = [('accoglienza', 'Aprire una sede DPL', 'Hai uno studio o una rete sul territorio? Porta la mediazione DPL nella tua città.', mt('Lavora con noi · Aprire una sede', tmpl), UR),
             ('persona', 'Diventare mediatore DPL', 'Sei mediatore abilitato e vuoi entrare nei nostri elenchi, in sede o online.', mt('Lavora con noi · Mediatore', tmpl), UR),
             ('ricerca', 'Non sei ancora mediatore?', 'Inizia dal corso abilitante di 80 ore: a Milano e online, con esame finale.', '__HREF_FORM__#corsi', '<span class="ico">__ARROW_N__</span>')]
    rl = ''.join(f'<a class="role" href="{u}"><span class="ic">{ICONS[ic]}</span><span><h3>{t}</h3><p>{d}</p></span><span class="go">{g}</span></a>' for ic, t, d, u, g in roles)
    box = (f'<div class="mailbox"><span class="k">Candidature</span><a class="addr" href="{mt("Lavora con noi · Candidatura", tmpl)}">{MAIL}</a>'
           '<ul><li><b>01</b>Chi sei e cosa fai</li><li><b>02</b>La città o la zona che ti interessa</li><li><b>03</b>Il tuo CV in PDF, in allegato</li></ul>'
           f'<div class="btns">{btn("Scrivi l’e-mail", mt("Lavora con noi · Candidatura", tmpl))}<button class="btn btn--line copy" type="button" data-copy="{MAIL}"><span>Copia l’indirizzo</span></button></div>'
           '<p class="note">Niente moduli da compilare: l’oggetto dell’e-mail è già pronto.</p></div>')
    b += sec(head('Lavora con noi', 'Cerchiamo mediatori, formatori e partner per aprire nuove sedi. Basta un’e-mail: ti rispondiamo noi.') + f'<div class="job"><div class="roles">{rl}</div>{box}</div>', 'tint', 'lavora-con-noi')
    js = '''
  /* ---- contatti: prefill from ?argomento=&corso=&sede= ---- */
  (() => { const q = new URLSearchParams(location.search), f = document.querySelector('form[name="contatti"]'); if (!f) return;
    const set = (n, v) => { const el = f.elements[n]; if (!el || !v) return; if (el.tagName === 'SELECT') { const o = [...el.options].find(o => o.text === v); if (o) el.value = o.text; } else el.value = v; };
    set('argomento', q.get('argomento')); set('sede', q.get('sede'));
    if (q.get('corso')) f.elements.messaggio.value = 'Vorrei informazioni sul corso «' + q.get('corso') + '».';
  })();
'''
    return mk(src, 'contatti.html', 'Contatti', b, js=js, cta=False)

# ---------------------------------------------------------------- Sedi ex art. 6 D.M. 150/23
REGIONS = [('Lombardia', 'lombardia'), ('Piemonte', 'piemonte'), ('Valle d’Aosta', 'aosta'), ('Liguria', 'liguria'), ('Veneto', 'veneto'), ('Trentino-Alto Adige', 'trentino'),
           ('Friuli-Venezia Giulia', 'friuli'), ('Emilia-Romagna', 'emiliaromagna'), ('Toscana', 'toscana'), ('Umbria', 'umbria'), ('Marche', 'marche'), ('Lazio', 'lazio'),
           ('Abruzzo', 'abruzzo'), ('Molise', 'molise'), ('Campania', 'campania'), ('Puglia', 'puglia'), ('Basilicata', 'basilicata'), ('Calabria', 'calabria'), ('Sicilia', 'sicilia'), ('Sardegna', 'sardegna')]

def acc(n): return f'{n} accordo' if n == 1 else f'{n} accordi'

def sedi_conv(src):
    b = hero('Sedi convenzionate', 'ex art. 6',
             'Gli organismi con cui abbiamo un accordo ai sensi dell’art. 6 del D.M. 150/2023, regione per regione: indirizzo, organismo e tipo di accordo.',
             btn('Cerca una regione', '#elenco') + btn('Le nostre sedi', '__HREF_SEDI__', 'line'), ['D.M. 150/2023', '20 regioni'])
    rows = ''.join(f'<a href="regione-{s}.html"><span class="t">{n}</span><span class="m">{acc(len(LOMB) if s == "lombardia" else len(regions_data.rows(s)))}</span>__ARROW_N__</a>' for n, s in REGIONS)
    b += band('mb11', 'Due professionisti camminano in città')
    b += sec(head('Regione per regione', 'Puoi svolgere la mediazione con DPL anche presso questi organismi, grazie agli accordi previsti dall’art. 6 del D.M. 150/2023.') +
             f'<div class="px-body"><div class="tools" data-filter=".lst a"><label class="search">{SEARCH}<input type="search" placeholder="Cerca una regione" aria-label="Cerca una regione"></label></div><div class="lst lst-2">{rows}</div></div>', '', 'elenco')
    return mk(src, 'sedi-convenzionate.html', 'Sedi convenzionate ex art. 6', b)

LOMB = [('Bergamo','Piazza G. Matteotti 20','Emediation srl n. 232','generico','05/06/2024'),('Bergamo (Capriate San Gervasio)','Vicolo Trieste 6','Me.co Srl n. 153','generico','28/03/2025'),
 ('Brescia','Via Cipro 1','101 Mediatori n. 294','generico','03/12/2025'),('Brescia','c/o Museo delle Mille Miglia, viale Bornata','Medyapro n. 1048','generico','01/03/2024'),
 ('Brescia','Via L. Gambara 87','Conciliando Med n. 1041','generico','04/03/2024'),('Brescia','Via Malta 8','Camera Nazionale per la Mediazione e l’Arbitrato','generico','19/07/2024'),
 ('Brescia (Cividate Camuno)','Via Cortiglione 7A','Emediation srl n. 232','generico','05/06/2024'),('Brescia (Moniga del Garda)','Via S. Michele snc','Italia Concilia srl n. 492','generico','17/05/2024'),
 ('Crema','Via Piacenza 34','Conciliando Med n. 1041','generico','04/03/2024'),('Cremona (Sesto ed Uniti)','Via Veneto 7','Italia Concilia srl n. 492','generico','17/05/2024'),
 ('Lecco (Oggiono)','Via XXV Aprile 8','Resolutia','singolo procedimento','03/02/2025'),('Lecco (Oggiono)','Via XXV Aprile 8','Resolutia','singolo procedimento','26/03/2025'),
 ('Lecco (Barzanò)','Via Monsignor Colli 4','Resolutia srl n. 1066','generico','27/05/2025'),('Lecco (Oggiono)','Via XXV Aprile 8','Resolutia','singolo procedimento','30/09/2024'),
 ('Lecco (Oggiono)','Via XXV Aprile 8','Resolutia','singolo procedimento','12/12/2024'),('Lecco (Oggiono)','Via XXV Aprile 8','Resolutia','singolo procedimento','13/02/2025'),
 ('Lecco (Oggiono)','Via XXV Aprile 8','Resolutia','singolo procedimento','22/04/2025'),('Lodi','Via Dante Alighieri 15','Fondazione Aequitas ADR n. 5','generico','05/06/2024'),
 ('Mantova','Via Oberdan 14','Camera Mantovana n. 413','singolo procedimento','22/11/2024'),('Mantova','Via Oberdan 14','Camera di Mediazione Mantovana n. 413','singolo procedimento','30/06/2025'),
 ('Mantova','Via L. Fancelli 4','Camera Mantovana di mediazione e conciliazione n. 413','generico','03/07/2025'),('Mantova (Castiglione delle Stiviere)','P.zza Dallò 23','Camera di Mediazione Mantovana n. 413','generico','03/07/2025'),
 ('Oggiono (Lecco)','Via XXV Aprile 8','Resolutia','singolo procedimento','04/11/2024'),('Pavia (Voghera)','Via Jacopo Dentici 19','Reconcilia ADR n. 1074','generico','27/03/2024')] + \
 [('Varese','Via Bernascone 19','Fondazione Aequitas ADR n. 5','singolo procedimento',d) for d in ['07/06/2024','14/06/2024','19/06/2024','27/06/2024','05/07/2024','08/07/2024','20/09/2024','09/10/2024','16/10/2024','17/10/2024']]

def regione(src, name, s):
    data = LOMB if s == 'lombardia' else regions_data.rows(s)
    b = hero(name, '', f'Le sedi convenzionate ex art. 6 del D.M. 150/2023 in {name}.', btn('Cerca un organismo', '#elenco') + btn('Le nostre sedi', '__HREF_SEDI__', 'line'), [acc(len(data)), 'D.M. 150/2023'], crumb=('Sedi convenzionate', '__HREF_EX6__'))
    k = [x for _, x in REGIONS].index(s); pv, nx = REGIONS[k - 1] if k else None, REGIONS[k + 1] if k + 1 < len(REGIONS) else None
    pn = '<nav class="pn" aria-label="Altre regioni">' + (f'<a href="regione-{pv[1]}.html"><small>← Regione precedente</small>{pv[0]}</a>' if pv else '') + (f'<a class="nx" href="regione-{nx[1]}.html"><small>Regione successiva →</small>{nx[0]}</a>' if nx else '') + '</nav>'
    trs = ''.join(f'<tr class="lr"><td>{c}</td><td>{a}</td><td>{o}</td><td>{"Accordo generico a durata indeterminata" if t == "generico" else "Accordo per singolo procedimento"}</td><td>{d}</td></tr>' for c, a, o, t, d in data)
    b += sec(f'<div class="tools" data-filter=".lr"><label class="search">{SEARCH}<input type="search" placeholder="Cerca città o organismo" aria-label="Cerca"></label></div>'
             f'<div class="prose" style="max-width:none"><table class="rtab"><thead><tr><th>Città</th><th>Indirizzo</th><th>Organismo</th><th>Accordo</th><th>Stipulato il</th></tr></thead><tbody>{trs}</tbody></table></div>' + pn, '', 'elenco')
    return mk(src, f'regione-{s}.html', f'Sedi convenzionate · {name}', b)

# ---------------------------------------------------------------- Privacy e cookie (legal, maisa-like)
PRIV = [
 ('informativa', 'Informativa sulla protezione dei dati personali', '''<p class="lead">Gentile visitatore, la navigazione sul nostro sito non comporta alcun conferimento di dati personali se si escludono i dati raccolti attraverso i cookie, per il dettaglio dei quali si rimanda alla specifica sezione.</p>
<p>Raccogliamo invece dati personali volontariamente conferiti attraverso le maschere appositamente predisposte, nel caso in cui Lei decidesse di contattarci per avere informazioni o ricevere materiale o per formulare richieste.</p>
<p>I seguenti paragrafi contengono una serie di informazioni utili a comprendere in che modo trattiamo i dati personali, nel rispetto delle disposizioni in materia di protezione dei dati personali e dei principi di liceità, correttezza, trasparenza, limitazione delle finalità e della conservazione, minimizzazione dei dati, esattezza, integrità e riservatezza.</p>
<p>La invitiamo pertanto a leggere attentamente la presente informativa.</p>'''),
 ('definizioni', 'Definizioni', '''<h3>Normativa Privacy</h3><p>Insieme di tutta la normativa riferita alla protezione dei dati personali: Regolamento EU 679/2016 (GDPR o RGPD), D.Lgs. 196/2003 (Codice), D.Lgs. 101/2018, D.Lgs. 51/2018, Linee Guida del EDPB (ex WP29), Regole deontologiche e autorizzazioni generali dell’Autorità Garante, Provvedimenti dell’Autorità Garante dove applicabili, Normativa internazionale di ambito.</p>
<h3>Trattamento</h3><p>Qualsiasi operazione o insieme di operazioni, compiute con o senza l'ausilio di processi automatizzati e applicate a dati personali o insiemi di dati personali, come la raccolta, la registrazione, l'organizzazione, la strutturazione, la conservazione, l'adattamento o la modifica, l'estrazione, la consultazione, l'uso, la comunicazione mediante trasmissione/diffusione o qualsiasi altra forma di messa a disposizione, il raffronto o l'interconnessione, la limitazione, la cancellazione o la distruzione.</p>
<h3>Titolare del trattamento</h3><p>La persona fisica o giuridica, l'autorità pubblica, il servizio o altro organismo che, singolarmente o insieme ad altri, determina le finalità e i mezzi del trattamento dei dati personali.</p>
<h3>Dati personali</h3><p>Qualsiasi informazione riguardante una persona fisica identificata o identificabile («interessato»); si considera identificabile la persona fisica che può essere identificata, direttamente o indirettamente, con particolare riferimento a un identificativo come il nome, un numero di identificazione, i dati relativi all'ubicazione, un identificativo online o a uno o più elementi caratteristici della sua identità: fisica, fisiologica, genetica, psichica, economica, culturale o sociale.</p>
<h3>Categorie particolari di dati personali</h3><p>Le informazioni personali relative a origine etnica, opinioni politiche, convinzioni religiose o filosofiche, appartenenza sindacale, stato di salute, vita o orientamento sessuale dell’interessato, nonché informazioni genetiche, biometriche e di geo-localizzazione.</p>
<h3>Dati relativi a condanne penali e reati</h3><p>Le informazioni personali relative a condanne penali, reati o a connesse misure di sicurezza.</p>'''),
 ('titolare', 'Titolare del trattamento', '''<p>Il Titolare del trattamento dei dati personali ivi descritto è DPL MEDIAZIONE &amp; Co. S.r.l. (in seguito DPL).</p><p>Può contattarlo attraverso l’indirizzo e-mail: <a href="mailto:news@dplmediazione.it">news@dplmediazione.it</a></p>'''),
 ('origine', 'Origine dei suoi dati e categorie di dati trattati', '''<p>I dati oggetto di trattamento sono quelli da Lei forniti al momento della compilazione delle maschere presenti sul sito per avere informazioni e/o ricevere materiale e/o richiedere l’accesso alla nostra area riservata. I dati raccolti sono nome, cognome, numero di cellulare e indirizzo e-mail.</p>
<h3>Informazioni raccolte durante la navigazione nel sito – Cookie</h3><p>Per una descrizione estesa dei cookie si rimanda a quanto contenuto nella Cookie Policy. A parte i cookie di sessione, la presenza di cookie Google Analytics ci permette di raccogliere informazioni in formato anonimo per statistiche aggregate che ci permettono di analizzare alcuni aspetti della navigazione sul nostro sito.</p>'''),
 ('finalita', 'Finalità del trattamento', '''<p>DPL tratta i suoi dati personali come sopra definiti e indicati per le finalità di seguito illustrate:</p><ul><li>Per rispondere a specifiche richieste dei visitatori del sito (RGPD, art. 6, comma 1, lett. b) e per il relativo invio di informazioni e/o materiale;</li><li>Per il perseguimento del legittimo interesse dei titolari (RGPD, art. 6, comma 1, lett. f). A titolo puramente esemplificativo e non esaustivo: la sicurezza e la salvaguardia dei propri sistemi informativi e del sito; l’analisi statistica delle visite effettuate e delle pagine più visitate; la gestione di eventuali contenziosi o controversie giudiziarie.</li></ul>
<h3>Obbligatorietà della comunicazione dei dati</h3><p>Il conferimento dei dati personali richiesti nelle maschere presenti sul sito è obbligatorio per ricevere le informazioni e/o il materiale eventualmente richiesto dai visitatori e/o per richiedere l’accesso alla nostra area riservata.</p>'''),
 ('luogo', 'Luogo e modalità di trattamento', '''<p>I suoi dati vengono trattati all’interno dell’Unione Europea. Tutte le operazioni di trattamento vengono svolte su supporto cartaceo e/o per mezzo di strumenti elettronici.</p>'''),
 ('terzi', 'Comunicazione dei suoi dati a terzi', '''<p>Il Titolare del trattamento ha affidato i servizi di sviluppo e manutenzione del sito a un fornitore specializzato, appositamente nominato “Responsabile autonomo del trattamento” ai sensi dell’art. 28 del RGPD.</p><p>Il sito e il dominio di posta utilizzato per la ricezione delle richieste dei visitatori e l’invio di informazioni sono gestiti, in hosting, da Aruba S.p.A. all’interno del territorio dell’Unione Europea.</p>'''),
 ('conservazione', 'Periodo di conservazione dei dati', '''<p>I dati raccolti per la finalità illustrata al punto A “Finalità del trattamento” saranno conservati:</p><ul><li>per lo scambio di informazioni e/o materiali e saranno conservati fino alla eventuale richiesta di cancellazione da parte dell’Interessato o di revoca del consenso;</li><li>per tutto il periodo necessario a erogare il servizio “area riservata” e saranno cancellati entro 2 (due) settimane dalla chiusura della sua area riservata.</li></ul>'''),
 ('diritti', 'I suoi diritti', '''<p>Lei ha il diritto di richiedere e di ricevere, in qualunque momento, informazioni in merito ai suoi dati personali trattati dalla nostra società o di chiederne la rettifica. Ove applicabile, ha diritto di chiederne la cancellazione, di limitarne il trattamento e di ricevere, in un formato strutturato, di uso comune e leggibile da dispositivo automatico, i dati personali che la riguardano; ha, inoltre, il diritto di opporsi al trattamento dei suoi dati, ai sensi di quanto previsto all’art. 21 del RGPD, o di proporre un reclamo all’Autorità Garante competente secondo quanto previsto all’art. 77 del RGPD.</p><p>Può indirizzare ogni richiesta in merito ai suoi diritti direttamente al Titolare del trattamento ai recapiti riportati nel paragrafo “Titolare del trattamento” della presente informativa. Occorre ricordarLe che l’art. 2-undeicies del Codice prevede espliciti e limitati casi in cui Lei non potrà far valere i suoi diritti.</p>'''),
 ('cookie', 'Cookie policy', '''<h3>Definizioni</h3><p>I cookie sono brevi stringhe di testo che i siti visitati dall’utente inviano al suo terminale, generalmente al browser, dove vengono memorizzati per essere poi ritrasmessi agli stessi siti alla successiva visita del medesimo utente. Nel corso della navigazione sul sito, l’utente potrebbe ricevere sul suo terminale anche cookie che vengono inviati da siti o da web server diversi (cookie di terze parti), su cui possono risiedere alcuni elementi (immagini, suoni, specifici link a pagine di altri domini; elenco non esaustivo) presenti sul sito che lo stesso sta visitando.</p>
<p>La presente informativa è resa solamente per il sito www.dplmediazione.it e non anche per altri siti web eventualmente consultati dall’utente tramite link, per i quali si rinvia alle rispettive informative/policy.</p>
<p>I sistemi informatici e le procedure software preposte al funzionamento del sito acquisiscono automaticamente, nel normale esercizio, alcune informazioni inerenti alla navigazione web, la cui trasmissione è implicita nell’uso dei protocolli di comunicazione internet. Si tratta di informazioni che non sono raccolte per essere associate a interessati identificati, ma che per loro natura potrebbero, mediante associazioni ed elaborazioni con dati detenuti da terzi, permettere di identificare gli utenti o i navigatori. In questa categoria rientrano le seguenti informazioni (elenco non esaustivo):</p>
<ul><li>Indirizzi IP;</li><li>Nomi di dominio dei computer utilizzati dagli utenti che si connettono al sito;</li><li>Orario della richiesta;</li><li>Il metodo utilizzato nel sottoporre la richiesta al server web;</li><li>La dimensione del file ottenuto in risposta;</li><li>Il codice numerico indicante lo stato della risposta data dal server web;</li><li>Altri parametri relativi al sistema operativo e all’ambiente informatico dell’utente.</li></ul>
<p>Questi dati sono utilizzati al solo fine di ricavare informazioni statistiche anonime sull’uso del sito web e per controllarne il corretto funzionamento.</p>'''),
 ('tipologie', 'Tipologie di cookie', '''<p>I cookie sono generalmente classificati nel seguente modo:</p><ul><li>Cookie di navigazione o di sessione, che garantiscono la normale navigazione e fruizione del sito web;</li><li>Cookie di funzionalità, che permettono all’utente la navigazione in funzione di una serie di criteri selezionati al fine di migliorare il servizio reso all’utente;</li><li>Cookie di prestazione, che raccolgono informazioni sull’efficienza delle risposte di un sito web alle richieste dell’utente in forma anonima, al solo fine di migliorare le funzionalità del sito Internet;</li><li>Cookie di profilazione, che permettono di creare profili relativi all’utente e sono utilizzati al fine di inviare messaggi pubblicitari in linea con le preferenze manifestate dallo stesso nell’ambito della navigazione in rete.</li></ul>
<p>Le tipologie di cookie utilizzati dal sito www.dplmediazione.it sono i seguenti:</p>
<table><thead><tr><th>Tipo di cookie</th><th>Finalità del cookie</th><th>Origine</th></tr></thead><tbody>
<tr><td>Cookie di sessione e di navigazione</td><td>Questi cookie sono essenziali per una corretta navigazione e per fruire delle funzioni del sito. L’uso di questi cookies, che non sono memorizzati in modo persistente sul dispositivo dell’utente e sono automaticamente eliminati con la chiusura del browser, è strettamente limitato alla trasmissione di identificativi di sessione (costituiti da numeri casuali generati dal server) necessari per consentire l’esplorazione sicura e efficiente del sito. Queste categorie di cookie non possono essere disattivate.</td><td>Cookie del Titolare</td></tr>
<tr><td>Cookie di funzionalità</td><td>Questi cookie consentono di ricordare le scelte effettuate (come a esempio il nome utente, la lingua o la posizione geografica, la presa visione della cookie policy) e forniscono funzioni migliorate e personalizzate. Le informazioni raccolte da tali cookie non tengono traccia dell’attività di navigazione su altri siti web. Questa categoria di cookie non può essere disattivata.</td><td>Cookie del Titolare</td></tr>
<tr><td>Cookie analitici o statistici</td><td>Questi cookie sono impostati da Google Analytics e sono impiegati al fine di raccogliere informazioni sul modo in cui i visitatori utilizzano il sito, ivi compreso il numero di visitatori e le pagine visitate sul sito web. Le informazioni sono utilizzate in forma anonima per fini statistici. Questa tipologia di cookie resta sul computer del visitatore per circa 24 mesi. Le terze parti potrebbero, previo consenso dell’utente, usare questi cookie anche per scopi diversi da quelli di analisi.</td><td>Cookie del Titolare</td></tr>
</tbody></table>
<h3>Google Analytics</h3><p>Questi cookie sono utilizzati per raccogliere informazioni in formato anonimo e analizzare alcuni aspetti della navigazione sul nostro sito: le pagine più visitate, il livello di interesse statistico in forma aggregata in ordine all’utilizzo del sito web visitato (elenco non esaustivo).</p>
<p>I dati generati da Google Analytics sono conservati da Google così come indicato nella informativa reperibile al seguente link: <a href="https://support.google.com/analytics/topic/2919631?hl=it&amp;ref_topic=1008008" target="_blank" rel="noopener">support.google.com/analytics/topic/2919631</a>.</p>
<p>Per consultare l’informativa privacy della società Google Inc., Titolare autonomo del trattamento dei dati, relativi al servizio Google Analytics, si rinvia al sito internet <a href="https://support.google.com/analytics/answer/6004245" target="_blank" rel="noopener">support.google.com/analytics/answer/6004245</a>.</p>
<p>Per la disattivazione della raccolta di dati ai fini di analisi effettuata da Google Analytics, si può visitare la pagina del “Componente aggiuntivo del browser per la disattivazione di Google Analytics” <a href="https://tools.google.com/dlpage/gaoptout?hl=it" target="_blank" rel="noopener">tools.google.com/dlpage/gaoptout</a>.</p>'''),
 ('social', 'Social network', '''<p>Su alcune pagine possono essere presenti video pubblicati su YouTube, che potrebbe installare cookie per rilevare le preferenze sull’utilizzo di questo servizio. Per maggiori informazioni su come YouTube utilizza i cookie, consultare la specifica privacy policy: <a href="http://www.google.com/intl/it/policies/privacy" target="_blank" rel="noopener">google.com/intl/it/policies/privacy</a>.</p>
<p>Sulle pagine del sito possono essere presenti pulsanti e widgets di social network per agevolare l’interazione con le piattaforme social e la condivisione di contenuti direttamente dalle pagine di questo sito web.</p>
<p>A titolo informativo, si riportano di seguito gli indirizzi web delle informative e delle modalità per la gestione dei cookie di alcuni social network:</p><ul><li>Facebook: <a href="https://www.facebook.com/help/cookies" target="_blank" rel="noopener">facebook.com/help/cookies</a></li><li>Twitter: <a href="https://help.twitter.com/it/rules-and-policies/twitter-cookies" target="_blank" rel="noopener">help.twitter.com/it/rules-and-policies/twitter-cookies</a></li></ul>
<p>Per impedire il monitoraggio da parte dei widget dei social network, è necessario chiudere le sessioni dei suddetti social e delle piattaforme da cui si è effettuato l’accesso prima di visitare il sito.</p>'''),
 ('gestione', 'Gestione dei cookie', '''<p>L’utente può decidere se accettare o meno i cookie utilizzando le impostazioni del proprio browser.</p><p>Attenzione: la disabilitazione totale o parziale dei cookie tecnici può compromettere l’utilizzo delle funzionalità del sito riservate agli utenti registrati. Al contrario, la fruibilità dei contenuti pubblici è possibile anche disabilitando completamente i cookie.</p>
<p>La disabilitazione dei cookie di terze parti non pregiudica in alcun modo la navigabilità.</p><p>I browser più diffusi consentono di definire impostazioni diverse per i cookie proprietari e per quelli di terze parti.</p>
<p>Maggiori informazioni sulle modalità di accettazione e rimozione dei cookie per i più diffusi browser, sono disponibili nelle seguenti pagine:</p>
<ul><li>Chrome: <a href="https://support.google.com/chrome/answer/95647?hl=it" target="_blank" rel="noopener">support.google.com/chrome/answer/95647</a></li><li>Firefox: <a href="https://support.mozilla.org/it/kb/Gestione%20dei%20cookie" target="_blank" rel="noopener">support.mozilla.org/it/kb/Gestione dei cookie</a></li><li>Internet Explorer: <a href="http://windows.microsoft.com/it-it/windows7/how-to-manage-cookies-in-internet-explorer-9" target="_blank" rel="noopener">windows.microsoft.com</a></li><li>Safari: <a href="http://support.apple.com/kb/HT1677?viewlocale=it_IT" target="_blank" rel="noopener">support.apple.com/kb/HT1677</a></li></ul>'''),
]

def privacy(src):
    b = hero('Privacy', 'e cookie', 'Come trattiamo i tuoi dati personali e quali cookie usa questo sito.', btn('Scrivi al titolare', 'mailto:news@dplmediazione.it'), ['GDPR · Reg. UE 679/2016', 'Cookie policy'])
    toc = ''.join(f'<a href="#{i}">{t}</a>' for i, t, _ in PRIV)
    prose = '<p class="upd">Testo dal sito attuale dplmediazione.it</p>' + ''.join(f'<h2 id="{i}">{t}</h2>{c}' for i, t, c in PRIV)
    b += sec(f'<div class="legal"><nav class="toc" aria-label="Indice">{toc}</nav><article class="prose">{prose}</article></div>', '')
    return mk(src, 'privacy.html', 'Privacy e cookie', b)

def _all():
    out = [(familiare, 'mediazione-familiare.html'), (sanitaria, 'mediazione-sanitaria.html'), (formazione, 'formazione.html'), (sedi, 'sedi.html'), (sede_milano, 'sede-milano.html'),
           (modulistica, 'modulistica.html'), (contatti, 'contatti.html'), (sedi_conv, 'sedi-convenzionate.html'), (privacy, 'privacy.html')]
    for c, r, *_ in CITIES:
        if c != 'Milano': out.append(((lambda src, c=c, r=r: sede(src, c, r)), f'sede-{slug(c)}.html'))
    for n, s in REGIONS: out.append(((lambda src, n=n, s=s: regione(src, n, s)), f'regione-{s}.html'))
    import news
    out += news.pages(mk, COURSES)
    return out
ALL = _all()
