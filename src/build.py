import re, base64, os, sys
src=open('src.html').read()
src=src.replace('overflow-x:hidden}','overflow-x:clip}',1)
LOGO=open('logo.svg').read().strip()
def svg(s,cls='ico'):
    return s.replace('<svg ','<svg class="%s" aria-hidden="true" '%cls,1)
arrow='<svg width="18" height="18" viewBox="0 0 18 18" fill="none"><path d="M10.5 4.3125L15.1875 8.99999L10.5 13.6875M14.625 8.99999H2.8125" stroke="%s" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round"/></svg>'
chev='<svg width="20" height="20" viewBox="0 0 20 20" fill="none"><path d="M4.79102 7.91666L9.99935 13.125L15.2077 7.91666" stroke="white" stroke-width="1.25" stroke-linecap="square"/></svg>'
acc='<svg width="20" height="20" viewBox="0 0 20 20" fill="none"><path d="M6.66602 8.3335L9.99935 11.6668L13.3327 8.3335" stroke="#19234B" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round"/></svg>'
video='<svg width="28" height="28" viewBox="0 0 28 28" fill="none"><path d="M3.20898 5.5415H17.7923V22.4582H3.20898V5.5415Z" stroke="white" stroke-width="1.5" stroke-linejoin="round"/><path d="M17.7923 11.6665L24.7923 8.1665V19.8332L17.7923 16.3332V11.6665Z" stroke="white" stroke-width="1.5" stroke-linejoin="round"/></svg>'
clock='<svg viewBox="0 0 22 22" fill="none"><path d="M11 7.1V11l2.5 2.5M19.5 11a8.5 8.5 0 1 1-17 0 8.5 8.5 0 0 1 17 0Z" stroke="#fff" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round"/></svg>'
file='<svg class="ic" viewBox="0 0 20 20" fill="none"><path d="M12.7 17.7h3.3v-10L10.6 2.3H4v15.4h3.3m3.3-15.4v5.4H16M10 11.5v5.2m-2.1-2.1 2.1 2.1 2.1-2.1" stroke="#19234B" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round"/></svg>'
users='<svg class="ic" viewBox="0 0 20 20" fill="none"><path d="M12 11c3-1.2 6.8.7 7.2 5.9H14M9 5.8a2.7 2.7 0 1 1-5.5 0 2.7 2.7 0 0 1 5.5 0Zm7.5 0a2.7 2.7 0 1 1-5.4 0 2.7 2.7 0 0 1 5.4 0ZM.8 16.9h10.7C11 8.5 1.4 8.5.8 16.9Z" stroke="#19234B" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round"/></svg>'
cal='<svg class="ic" viewBox="0 0 20 20" fill="none"><path d="M6.5 4V2.3m7 1.7V2.3M3.1 4h13.8v12.9H3.1V4Z" stroke="#19234B" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round"/></svg>'
ok='<svg class="ok" viewBox="0 0 18 18"><path fill="#19234B" fill-rule="evenodd" d="M9 1.5a7.5 7.5 0 1 0 0 15 7.5 7.5 0 0 0 0-15Zm2.7 6a.56.56 0 0 0-.9-.7l-3 3.6-1-1.1a.56.56 0 1 0-.8.8l1.5 1.5a.56.56 0 0 0 .8 0l3.4-4.1Z"/></svg>'
ur='<svg class="ico" aria-hidden="true" width="14" height="14" viewBox="0 0 18 18" fill="none" style="transform:rotate(-45deg)"><path d="M10.5 4.3125L15.1875 8.99999L10.5 13.6875M14.625 8.99999H2.8125" stroke="currentColor" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round"/></svg>'
def rings(cs,uid):
    d=' '.join(f'M{cx-r},{cy} a{r},{r} 0 1,0 {2*r},0 a{r},{r} 0 1,0 {-2*r},0' for cx,cy,r in cs)
    circ=''.join(f'<circle cx="{cx}" cy="{cy}" r="{r}"/>' for cx,cy,r in cs)
    return (f'<defs><clipPath id="clip{uid}"><path fill-rule="evenodd" clip-rule="evenodd" d="{d}"/></clipPath>'
            f'<filter id="soft{uid}" x="-10%" y="-10%" width="120%" height="120%"><feGaussianBlur stdDeviation="9"/></filter></defs>'
            f'<path fill-rule="evenodd" d="{d}" fill="rgb(186,199,249)" fill-opacity=".10"/>'
            f'<g clip-path="url(#clip{uid})"><g fill="none" stroke="#BAC7F9" stroke-opacity=".16" stroke-width="14" filter="url(#soft{uid})">{circ}</g></g>'
            f'<g fill="none" stroke="#fff" stroke-opacity=".38" stroke-width="1">{circ}</g>')

def device(cs,H,uid):
    """Graphic device = XOR of two circles (Figma boolean Exclude), fill #BAC7F9 @10% + glass rim."""
    d=''.join(f'M{cx-r:.2f} {cy:.2f}a{r:.2f} {r:.2f} 0 1 0 {2*r:.2f} 0a{r:.2f} {r:.2f} 0 1 0 {-2*r:.2f} 0Z' for cx,cy,r in cs)
    x0=min(cx-r for cx,cy,r in cs); y0=min(cy-r for cx,cy,r in cs); x1=max(cx+r for cx,cy,r in cs); y1=max(cy+r for cx,cy,r in cs)
    return (f'<svg class="device ring-float" viewBox="0 0 1440 {H}" style="width:U(1440);height:U({H})" overflow="visible" aria-hidden="true">'
      f'<defs><clipPath id="dc{uid}"><path clip-rule="evenodd" d="{d}"/></clipPath>'
      f'<linearGradient id="dg{uid}" gradientUnits="userSpaceOnUse" x1="{x0:.0f}" y1="{y0:.0f}" x2="{x1:.0f}" y2="{y1:.0f}">'
      f'<stop offset="0" stop-color="#fff" stop-opacity=".55"/><stop offset=".45" stop-color="#fff" stop-opacity=".08"/><stop offset=".6" stop-color="#fff" stop-opacity=".06"/><stop offset="1" stop-color="#fff" stop-opacity=".32"/></linearGradient></defs>'
      f'<path fill="#BAC7F9" fill-opacity=".1" fill-rule="evenodd" d="{d}"/>'
      '</svg>')

def rings_svg():
    # Matteo's exported graphic (Exclude.svg, 1317x1195), placed at hero x 123.73 / y 0 — same geometry as the Figma rings
    d='M610.012 1014.92C454.229 1013.85 298.777 953.881 179.916 835.02C-59.9736 595.131 -59.973 206.193 179.917 -33.697C419.806 -273.587 808.744 -273.587 1048.63 -33.6977C1103.82 21.4932 1146.32 84.5736 1176.11 151.913C990.836 91.4254 779.048 134.806 631.796 282.058C430.578 483.277 423.317 805.004 610.012 1014.92ZM1387.76 1038.02C1179 1246.77 840.549 1246.77 631.796 1038.02C624.263 1030.48 617.002 1022.78 610.012 1014.92C768.637 1016.02 927.605 956.049 1048.63 835.02C1233.33 650.321 1275.83 377.267 1176.11 151.913C1253.5 177.176 1326.26 220.556 1387.76 282.057C1596.51 490.81 1596.51 829.266 1387.76 1038.02Z'
    return ('<defs><clipPath id="cliph"><path d="'+d+'"/></clipPath><filter id="softh" x="-10%" y="-10%" width="120%" height="120%"><feGaussianBlur stdDeviation="9"/></filter></defs>'
            '<g transform="translate(123.73 0)"><path d="'+d+'" fill="#BAC7F9" fill-opacity="0.1"/>'
            '<g clip-path="url(#cliph)"><path d="'+d+'" fill="none" stroke="#BAC7F9" stroke-opacity=".16" stroke-width="14" filter="url(#softh)"/></g>'
            '<path d="'+d+'" fill="none" stroke="#fff" stroke-opacity=".38" stroke-width="1"/></g>')
cities=['Avellino','Busto Arsizio','Como','Cuneo','Ivrea','Lecco','Milano','Monza','Pavia','Piacenza','Rieti','Roma','Salerno','Sondrio','Terni','Tivoli','Torino','Torre Annunziata','Varese','Velletri']
ticker='<div class="row">'+''.join(f'<span>{c}</span><i></i>' for c in cities)+'</div>'
rep={'__DEVICE_404__':device([(565,280,480),(915,535,490)],800,'n'),'__DEVICE_CS__':device([(578.54,173.63,868.72),(974.04,433.0,755.96)],516,'s'),'__DEVICE_HERO__':device([(737.5,400.5,868.5),(1134,660,756)],696,'h'),'__DEVICE_TL__':device([(486.5,775.5,680.5),(953.5,775.5,680.5)],1144,'c'),'__LOGO__':LOGO,'__ARROW_W__':svg(arrow%'white'),'__ARROW_N__':svg(arrow%'#19234B'),'__CHEV__':svg(chev),'__ACC__':svg(acc),'__ICO_VIDEO__':video,
 '__ICO_CLOCK__':clock,'__ICO_FILE__':file,'__ICO_USERS__':users,'__ICO_CAL__':cal,'__ICO_OK__':ok,'__ARROW_UR__':ur,'__TICKER__':ticker,
 '__RINGS_HERO__':rings_svg(),'__RINGS_TL__':rings([(953.5,775.9,680.65),(486.5,775.9,680.65)],'t')}
def finish(src,out):
    for k,v in rep.items(): src=src.replace(k,v)
    for k in []:
        src=src.replace(f'__PNG_{k}__','data:image/png;base64,'+base64.b64encode(open(f'assets/{k}.png','rb').read()).decode())
    for k in [f[:-4] for f in os.listdir('assets') if f.endswith('.jpg') and f'__IMG_{f[:-4]}__' in src]:
        src=src.replace(f'__IMG_{k}__','data:image/jpeg;base64,'+base64.b64encode(open(f'assets/{k}.jpg','rb').read()).decode())
    ff=''
    fd='fonts'
    if os.path.isdir(fd):
        for fn in sorted(os.listdir(fd)):
            low=fn.lower(); ext=fn.rsplit('.',1)[-1].lower()
            fmt={'woff2':'woff2','woff':'woff','otf':'opentype','ttf':'truetype'}.get(ext)
            if not fmt: continue
            fam='Zodiak' if 'zodiak' in low else 'Switzer' if 'switzer' in low else None
            if not fam: continue
            w=500 if 'medium' in low else 600 if 'semibold' in low else 400
            if 'italic' in low: continue
            mime={'woff2':'font/woff2','woff':'font/woff','otf':'font/otf','ttf':'font/ttf'}[ext]
            ff+=f"@font-face{{font-family:'{fam}';src:url(data:{mime};base64,{base64.b64encode(open(os.path.join(fd,fn),'rb').read()).decode()}) format('{fmt}');font-weight:{w};font-style:normal;font-display:swap}}\n"
    src=src.replace('/*__FONTFACE__*/',ff)
    src=re.sub(r'U\((-?[\d.]+)\)',lambda m:f'calc({m.group(1)}*var(--u))',src)
    left=re.findall(r'__[A-Z_a-z0-9-]+__',src)
    open(out,'w').write(src)
    print(out,'size',len(src),'leftover',left,'fonts',ff.count('@font-face'))

import common
finish(common.hrefs(src, '#top'),'dpl-home.html')
import cs, mc, pages
finish(cs.make(src),'chi-siamo.html')
finish(mc.make(src),'mediazione-civile.html')
for fn, fname in pages.ALL: finish(fn(src), fname)
# full standalone documents (artifact supporting pages + vault copies)
os.makedirs('pages', exist_ok=True)
DOC='<!doctype html>\n<html lang="it">\n<meta charset="utf-8">\n<meta name="viewport" content="width=device-width, initial-scale=1">\n'
for f in ['dpl-home.html','chi-siamo.html','mediazione-civile.html']+[x[1] for x in pages.ALL]:
    open('pages/'+f,'w').write(DOC+open(f).read())
