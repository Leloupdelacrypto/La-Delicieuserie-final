"""Composants HTML partagés. Génération statique sans moteur de templates."""
import json
from html import escape

from content import DOMAIN, EMAIL, MAPS, MEDIA, PAGES, SOCIAL

BRAND = "La Délicieuserie"
NOINDEX = {"thanks", "error", "legal", "privacy"}


def url(key):
    return PAGES[key][0]


def link(key, label=None, css="", suffix=""):
    attr = f' class="{css}"' if css else ""
    return f'<a{attr} href="{url(key)}{escape(suffix)}">{escape(label or PAGES[key][1])}</a>'


def image(name, *, hero=False, sizes="(max-width: 720px) 90vw, 32vw"):
    width, height, alt = MEDIA[name]
    variants = sorted({480, 800, width})
    srcset = ", ".join(f"/assets/media/{name}-{w}.webp {w}w" for w in variants)
    loading = 'fetchpriority="high" loading="eager"' if hero else 'loading="lazy" decoding="async"'
    return (f'<img src="/assets/media/{name}-800.webp" srcset="{srcset}" sizes="{sizes}" '
            f'width="{width}" height="{height}" alt="{escape(alt)}" {loading}>')


def brand():
    return f'''<a class="brand" href="/" aria-label="La Délicieuserie, accueil">
    <img src="/assets/media/logo-96.webp" srcset="/assets/media/logo-96.webp 1x, /assets/media/logo-192.webp 2x" width="53" height="53" alt="">
    <span>{BRAND}</span></a>'''


def header(key):
    choices = [("biscuits", "Nos sablés"), ("mariage", "Mariages"), ("famille", "Fêtes de famille"),
               ("entreprise", "Entreprises"), ("atelier", "L’atelier")]
    nav = "\n".join(f'<a href="{url(k)}"'+(' aria-current="page"' if k == key else '')+
                    f'>{label}</a>' for k, label in choices)
    return f'''<a class="skip" href="#main">Aller au contenu</a>
<header class="masthead" id="accueil"><div class="wrap header-inner">
  {brand()}
  <button class="menu-toggle" type="button" aria-expanded="false" aria-controls="navigation" hidden><i aria-hidden="true"></i> Menu</button>
  <nav id="navigation" aria-label="Navigation principale">{nav}
    {link("devis","Demander un devis","button nav-quote")}</nav>
</div></header>'''


def footer():
    pages = " ".join(link(k) for k in ("biscuits", "mariage", "famille", "entreprise", "atelier", "devis"))
    socials = " ".join(f'<a href="{u}">{s}</a>' for s,u in SOCIAL.items())
    return f'''<footer class="foot"><div class="wrap">
<div class="foot-grid"><div>{brand()}<p>Biscuiterie artisanale à Calais<br>Pas-de-Calais, France</p></div>
<div><h2>À découvrir</h2><nav aria-label="Navigation de pied de page">{pages}</nav></div>
<div><h2>Joindre l’atelier</h2><a href="tel:+33617419761">06 17 41 97 61</a><a href="mailto:{EMAIL}">{EMAIL}</a></div>
<div><h2>Suivre l’atelier</h2>{socials}</div></div>
<div class="foot-bottom"><span>© La Délicieuserie</span>{link("legal")}{link("privacy", "Données personnelles")}
<a href="/confidentialite/#cookies" data-cookies>Gérer les cookies</a></div>
<p id="cookie-status" class="form-status" role="status"></p></div></footer>'''


def crumbs(key):
    return f'''<nav class="crumb wrap" aria-label="Fil d’Ariane"><ol><li>{link("home")}</li><li aria-current="page">{escape(PAGES[key][1])}</li></ol></nav>'''


def structured(key):
    path, label, title, desc = PAGES[key]
    business = {"@id": DOMAIN + "/#biscuiterie", "@type": "Bakery", "name": BRAND, "url": DOMAIN + "/",
                "telephone": "+33617419761", "email": EMAIL, "logo": DOMAIN + "/assets/media/logo-480.webp",
                "image": DOMAIN + "/assets/media/partage.jpg", "sameAs": [SOCIAL[k] for k in ("Instagram","Facebook","LinkedIn")],
                "address": {"@type": "PostalAddress", "addressLocality": "Calais", "postalCode": "62100", "addressCountry": "FR"}}
    page = {"@type": "ContactPage" if key == "devis" else "AboutPage" if key == "atelier" else "WebPage",
            "@id": DOMAIN+path+"#page", "url": DOMAIN+path, "name": title, "description": desc,
            "inLanguage": "fr-FR", "isPartOf": {"@id": DOMAIN+"/#site"}}
    graph = [page, {"@type":"WebSite", "@id":DOMAIN+"/#site", "url":DOMAIN+"/", "name":BRAND, "publisher":{"@id":business["@id"]}}]
    if key in {"home","atelier","devis"}:
        graph.append(business)
    if key not in {"home","error","thanks"}:
        crumb = {"@type":"BreadcrumbList", "@id":DOMAIN+path+"#fil", "itemListElement":[
            {"@type":"ListItem","position":1,"name":"Accueil","item":DOMAIN+"/"},
            {"@type":"ListItem","position":2,"name":label,"item":DOMAIN+path}]}
        page["breadcrumb"] = {"@id": crumb["@id"]}
        graph.append(crumb)
    return json.dumps({"@context":"https://schema.org","@graph":graph},ensure_ascii=False,indent=2)


def shell(key, body):
    path, _, title, desc = PAGES[key]
    tags = f'<meta name="robots" content="noindex,follow">' if key in NOINDEX else ""
    canonical = "" if key == "error" else f'<link rel="canonical" href="{DOMAIN}{path}">'
    return f'''<!doctype html>
<html lang="fr">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{escape(title)}</title>
<meta name="description" content="{escape(desc)}">
{canonical}
{tags}
<meta property="og:type" content="website">
<meta property="og:locale" content="fr_FR">
<meta property="og:site_name" content="{BRAND}">
<meta property="og:title" content="{escape(title)}">
<meta property="og:description" content="{escape(desc)}">
<meta property="og:url" content="{DOMAIN}{path}">
<meta property="og:image" content="{DOMAIN}/assets/media/partage.jpg">
<meta property="og:image:width" content="1200"><meta property="og:image:height" content="630">
<meta property="og:image:alt" content="Anne-Sophie et l’emblème de La Délicieuserie">
<meta name="twitter:card" content="summary_large_image">
<meta name="theme-color" content="#FBFAF7">
<link rel="icon" type="image/png" href="/assets/media/favicon.png">
<script data-cmp-ab="1" src="https://cdn.consentmanager.net/delivery/autoblocking/ddde3729e2a51.js" data-cmp-host="a.delivery.consentmanager.net" data-cmp-cdn="cdn.consentmanager.net" data-cmp-codesrc="16"></script>
<link rel="stylesheet" href="/styles.css">
<script defer src="/script.js"></script>
<script defer src="/consent.js"></script>
<script type="application/ld+json">
{structured(key)}
</script>
</head>
<body>
{header(key)}
<main id="main" tabindex="-1">
{"" if key in ("home","thanks","error") else crumbs(key)}
{body}
</main>
{footer()}
</body></html>
'''


def button_quote(key=None, label="Demander un devis"):
    occasion = {"mariage":"mariage", "entreprise":"entreprise", "famille":"famille"}.get(key)
    return link("devis", label, "button", "?occasion="+occasion if occasion else "")


def picture(name, caption, home=False):
    return f'''<figure class="cover-art{' home-art' if home else ''}">
    <div class="picture-frame">{image(name, hero=True, sizes="(max-width: 760px) 94vw, (max-width: 1280px) 49vw, 620px")}</div>
    <figcaption>{escape(caption)}</figcaption></figure>'''


def strip():
    return '''<div class="atelier-strip"><div class="wrap"><span>Fabrication à la main</span><i aria-hidden="true">✦</i>
    <span>Retrait à Calais</span><i aria-hidden="true">✦</i><span>Envoi en France</span></div></div>'''


def contact_band(key=None):
    return f'''<section class="contact-band" id="contact"><div class="wrap band-inner"><div>
    <p class="kicker">Un projet de biscuits</p><h2>Parlons de votre <em>occasion.</em></h2>
    <p>Une idée, une date, une quantité approximative : Anne-Sophie vous répond avec un devis gratuit.</p></div>
    {button_quote(key)}</div></section>'''


def gallery(items):
    cards=[]
    for name,caption in items:
        large=f"/assets/media/{name}-{MEDIA[name][0]}.webp"
        cards.append(f'''<figure><a class="zoom-link" href="{large}" data-caption="{escape(caption)}" aria-label="Agrandir : {escape(MEDIA[name][2])}">
        {image(name)}<span class="zoom-mark" aria-hidden="true">+</span></a>
        <figcaption>{escape(caption)}</figcaption></figure>''')
    return f'''<section class="gallery-section"><div class="wrap"><p class="kicker">La galerie</p><h2>Motifs et inspirations</h2>
    <div class="gallery">{''.join(cards)}</div></div></section>
    <dialog class="lightbox" aria-labelledby="lightbox-caption"><div class="lightbox-bar">
    <button class="lightbox-close" type="button" autofocus>Fermer <span aria-hidden="true">×</span></button></div>
    <figure><img width="800" height="600" alt="" id="lightbox-image"><figcaption id="lightbox-caption" aria-live="polite"></figcaption></figure>
    <div class="lightbox-controls"><button type="button" data-step="-1">Précédente</button><button type="button" data-step="1">Suivante</button></div></dialog>'''


def faq(items):
    entries="".join(f'<details><summary>{escape(q)}</summary><p>{escape(a)}</p></details>\n' for q,a in items)
    return f'''<section class="wrap faq"><div><p class="kicker">En pratique</p><h2>Vos questions</h2></div><div>{entries}</div></section>'''


def occasion_cards():
    choices = [
        ("mariage","part3","Mariages","Prénoms, alliances et cadeaux d’invités."),
        ("entreprise","pros2","Entreprises","Logos, séminaires et cadeaux clients."),
        ("famille","part1","Fêtes de famille","Anniversaires, baptêmes et naissances."),
    ]
    cards = []
    for key,photo,name,desc in choices:
        cards.append(f'''<article class="occasion-card"><a href="{url(key)}" class="card-link">
        <div class="card-photo">{image(photo)}</div><h3>{name}</h3></a><p>{desc}</p></article>''')
    return '<div class="occasions">'+"".join(cards)+'</div>'
