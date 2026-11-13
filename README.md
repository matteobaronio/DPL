# DPL Mediazione & Co. — sito

Prototipo navigabile del nuovo sito di DPL Mediazione, sviluppato dal design in Figma (file *DPL-Mediazione*).

## Pagine

Architettura: «Poldo's Proposal» (Figma `481:37`, pagina Website Architecture).

| File | Pagina | Note |
|---|---|---|
| `index.html` | Home | Figma `613:2294` |
| `chi-siamo.html` | Chi siamo | L'idea, il team, recensioni, aree |
| `mediazione-civile.html` | Mediazione · Civile e commerciale | |
| `mediazione-familiare.html` | Mediazione · Familiare | |
| `mediazione-sanitaria.html` | Mediazione · Sanitaria, penale e lavorativa | |
| `formazione.html` | Formazione · Civile e commerciale | Link esterni a dplaccademy.it |
| `sedi.html` | Le nostre sedi (20 città) | |
| `sede-*.html` | Una pagina per ogni sede (20) | Milano completa; le altre con indirizzo, referente e professionisti da completare |
| `modulistica.html` | Modulistica | PDF su dplmediazione.it/docs |
| `rassegna-stampa.html` | News & eventi · Rassegna stampa | Contenuti segnaposto |
| `rassegna-*.html` | Un articolo per ogni card (7) | Testi segnaposto, link alla fonte da inserire |
| `eventi.html` | News & eventi · Eventi | |
| `evento-*.html` | Una pagina per ogni evento (6) | Dettagli, iscrizione, «Aggiungi al calendario» |
| `contatti.html` | Contatti + Lavora con noi | Modulo Netlify Forms |
| `sedi-convenzionate.html` | Sedi ex Art. 6 D.M. 150/23 | |
| `regione-*.html` | Una pagina per ogni regione (20) | Elenco accordi dal sito attuale |
| `privacy.html` | Privacy e cookie | Testo dal sito attuale |
| `404.html` | Pagina non trovata | Figma `715:144`; messaggio diverso a ogni ricarica (3) |

Le pagine interne (tranne la home) sono costruite in codice, da riportare in Figma.

Tutti i link restano in questo sito, tranne i servizi «fuori dal sito» dell'architettura: DPL Accademy, Area riservata (dplmediazione.eu), DPL Magazine e YouTube. I PDF della modulistica sono serviti da `/docs/` tramite `_redirects` (proxy Netlify verso l'archivio attuale).

Ogni pagina è un file HTML autonomo: font (Zodiak, Switzer), immagini e grafiche sono incorporati, quindi si apre con un doppio clic o si pubblica così com'è (es. GitHub Pages dalla root del branch `main`).

## Comportamento

- Layout desktop a 1440 px che scala con la larghezza (`--u`), layout dedicato sotto i 900 px.
- Smooth scrolling con Lenis 1.1.13 (CDN jsDelivr, fallback unpkg).
- Un solo easing per tutte le animazioni: CustomEase «osmo» `M0,0 C0.625,0.05 0,1 1,1` = `cubic-bezier(.625,.05,0,1)`.
- Blur in entrata solo su titoli e testi (non sul titolo della hero né sui menu).
- Selezione testo: sfondo `#BAC7F9`, testo `#19234B`.
- Cambio pagina: tendina blu notte con il simbolo DPL che si disegna e si riempie; all'arrivo la tendina si apre verso l'alto.

## Sorgenti (`src/`)

- `src.html` — sorgente della home (le misure desktop sono scritte come `U(n)`, convertite in `calc(n*var(--u))`).
- `common.py` — scheletro e CSS condivisi delle pagine interne.
- `cs.py`, `mc.py` — Chi siamo e Mediazione civile.
- `kit.py` — libreria di sezioni (hero, righe con visual animati, card con icone DPL, step, FAQ, liste, blog, legale, form).
- `pages.py` — tutte le altre pagine dell'architettura.
- `news.py` — rassegna stampa, eventi, pagine di articoli ed eventi, 404.
- `build.py` — incorpora logo, icone, immagini (`assets/`) e font (`fonts/`) e scrive i file HTML.

```bash
cd src && python3 build.py
# poi: pages/dpl-home.html → index.html, e nei link "dpl-home.html" → "index.html"
```

## Fonti dei contenuti

| Contenuto | Fonte | Letta il |
|---|---|---|
| Corsi (Formazione, «Corsi della sede») ed eventi | [dplmediazione.it/formazione-civcom.html](https://www.dplmediazione.it/formazione-civcom.html) — elenco caricato via JavaScript | 12/11/2026 |

Dati da verificare con DPL prima della messa online (date, prezzi, crediti; il biennale familiari risulta concluso a luglio 2026).

## Da completare

- Testi nuovi da approvare (sottotitoli delle aree, step 02–04, pagina Mediazione civile).
- Team di Chi siamo: foto, nomi, ruoli e presentazioni.
- Link ancora segnaposto (`#`) per le pagine non ancora sviluppate.
- Foto «licence to check» dal moodboard: verificare le licenze prima della messa online.
