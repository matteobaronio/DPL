# DPL Mediazione & Co. — sito

Prototipo navigabile del nuovo sito di DPL Mediazione, sviluppato dal design in Figma (file *DPL-Mediazione*).

## Pagine

| File | Pagina | Figma |
|---|---|---|
| `index.html` | Home | Home Desktop `613:2294` |
| `chi-siamo.html` | Chi siamo | Chi siamo / Desktop / 1440w — v1 `689:121` |
| `mediazione-civile.html` | Mediazione civile e commerciale | — costruita in codice, da riportare in Figma |

Ogni pagina è un file HTML autonomo: font (Zodiak, Switzer), immagini e grafiche sono incorporati, quindi si apre con un doppio clic o si pubblica così com'è (es. GitHub Pages dalla root del branch `main`).

## Comportamento

- Layout desktop a 1440 px che scala con la larghezza (`--u`), layout dedicato sotto i 900 px.
- Smooth scrolling con Lenis 1.1.13 (CDN jsDelivr, fallback unpkg).
- Un solo easing per tutte le animazioni: CustomEase «osmo» `M0,0 C0.625,0.05 0,1 1,1` = `cubic-bezier(.625,.05,0,1)`.
- Blur in entrata solo su titoli e testi (non sul titolo della hero né sui menu).
- Selezione testo: sfondo `#BAC7F9`, testo `#19234B`.

## Sorgenti (`src/`)

- `src.html` — sorgente della home (le misure desktop sono scritte come `U(n)`, convertite in `calc(n*var(--u))`).
- `cs.py`, `mc.py` — generano Chi siamo e Mediazione civile riusando testa, header, menu, footer e JS della home.
- `build.py` — incorpora logo, icone, immagini (`assets/`) e font (`fonts/`) e scrive i file HTML.

```bash
cd src && python3 build.py
# poi: pages/dpl-home.html → index.html, e nei link "dpl-home.html" → "index.html"
```

## Da completare

- Testi nuovi da approvare (sottotitoli delle aree, step 02–04, pagina Mediazione civile).
- Team di Chi siamo: foto, nomi, ruoli e presentazioni.
- Link ancora segnaposto (`#`) per le pagine non ancora sviluppate.
- Foto «licence to check» dal moodboard: verificare le licenze prima della messa online.
