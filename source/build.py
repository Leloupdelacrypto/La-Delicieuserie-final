"""Reconstruire avec python3 -B source/build.py depuis le dépôt (bibliothèque standard)."""
from html import escape
from pathlib import Path

from content import CASE, DOMAIN, EMAIL, INDEXED, MAPS, PAGES, SERVICES
from layout import (button_quote, contact_band, faq, gallery, image, link, occasion_cards,
                    picture, shell, strip, url)

ROOT = Path(__file__).resolve().parents[1]


def home():
    return f'''<section class="hero"><div class="wrap hero-grid"><div class="hero-copy">
    <p class="kicker">Biscuiterie artisanale à Calais</p>
    <h1>Des sablés<br><em>à votre image.</em></h1>
    <p class="lead">Un prénom, une date, un logo… Anne-Sophie prépare vos biscuits à la main et les personnalise pour un mariage, une fête de famille ou un cadeau d’entreprise.</p>
    <div class="actions">{button_quote()}{link("biscuits","Découvrir les sablés","text-link")}</div></div>
    {picture("hero","Sablés gravés · Formes et messages",True)}</div></section>
    {strip()}
    <section class="wrap occasions-section" id="produits"><div class="section-head"><div><p class="kicker">Les occasions</p>
    <h2>Un biscuit pour <em>chaque occasion.</em></h2></div></div>{occasion_cards()}</section>
    <section class="story" id="apropos"><div class="wrap story-grid">
    <div class="portrait">{image("portrait",sizes="(max-width: 760px) 75vw, 410px")}</div>
    <div><p class="kicker">L’atelier de Calais</p><h2>Les mains<br><em>d’Anne-Sophie.</em></h2>
    <p>À Calais, Anne-Sophie Dubois a fait de son goût pour la pâtisserie et le dessin son métier. Elle prépare chaque sablé au beurre, puis y inscrit le détail qui le rend personnel.</p>
    {link("atelier","Rencontrer la créatrice","text-link")}</div></div></section>
    <section class="wrap practical"><div id="personnalisation"><p class="kicker">Sur mesure</p><h2>Que peut-on graver sur un sablé ?</h2>
    <p>Un mot, une date, un dessin ou un logo. La taille du biscuit et le niveau de détail se choisissent ensemble.</p>{link("biscuits","Explorer les possibilités","text-link")}</div>
    <div id="temoignages"><p class="kicker">Avis clients</p><h2>Leurs moments gourmands</h2>
    <p>Retrouvez les avis publiés sur la fiche Google de La Délicieuserie.</p><a class="text-link" href="{MAPS}">Consulter les avis sur Google</a></div></section>
    {contact_band()}'''


def service(key):
    data=SERVICES[key]
    blocks=[]
    for title,text in data["blocks"]:
        case_link = f'<a class="text-link" href="{CASE}">Voir la réalisation pour Adeo</a>' if key == "entreprise" and "Adeo" in title else ""
        blocks.append(f'<article><h3>{escape(title)}</h3><p>{escape(text)}</p>{case_link}</article>')
    related = [k for k in ("biscuits","mariage","famille","entreprise","atelier") if k != key]
    links = ' '.join(link(k,css="related-link") for k in related)
    return f'''<section class="service-hero wrap"><div><p class="kicker">{data["label"]}</p>
    <h1>{data["heading"]}<br><em>{data["em"]}</em></h1>
    <p class="lead">{data["intro"]}</p>{button_quote(key,data["cta"])}</div>
    {picture(data["image"],data["caption"])}</section>
    <section class="reading wrap"><h2>{data["section"]}</h2><div class="three-info">{''.join(blocks)}</div></section>
    {gallery(data["gallery"])}{faq(data["faq"])}
    <nav class="related wrap" aria-label="Autres idées de sablés"><strong>À découvrir aussi</strong>{links}</nav>
    {contact_band(key)}'''


def atelier():
    return f'''<section class="service-hero wrap"><div><p class="kicker">Calais · Pas-de-Calais</p>
    <h1>L’atelier<br><em>d’Anne-Sophie.</em></h1>
    <p class="lead">Derrière La Délicieuserie, il y a Anne-Sophie Dubois. C’est dans son atelier de biscuiterie à Calais qu’elle réunit ses deux passions, la gourmandise et le travail du détail.</p>
    {link("devis","Contacter l’atelier","button")}</div>{picture("portrait","Anne-Sophie Dubois · Créatrice de La Délicieuserie")}</section>
    <section class="reading wrap"><h2>Du beurre, de la pâte et un dessin</h2><div class="three-info">
    <article><h3>Le geste artisanal</h3><p>Farine de blé, beurre, sucre, œufs et sucre vanillé bourbon composent la pâte. Les sablés sont fabriqués à la main à Calais. Forme, taille et motif sont choisis selon le projet.</p></article>
    <article><h3>Retirer une commande à Calais</h3><p>Échangez avec Anne-Sophie pour convenir des modalités, du lieu et du moment du retrait. Le délai dépend notamment de la quantité souhaitée.</p><a class="text-link" href="tel:+33617419761">06 17 41 97 61</a></article>
    <article><h3>Recevoir ses sablés</h3><p>Les envois sont possibles en France. Indiquez votre commune et la date souhaitée pour que l’atelier puisse préciser le conditionnement, le transport et son coût dans le devis.</p><a class="text-link" href="mailto:{EMAIL}">Écrire à Anne-Sophie</a></article>
    </div></section>
    {gallery([("atelier","L’espace de fabrication"),("personnalisation","Le poste de marquage"),("portrait","Anne-Sophie Dubois")])}
    <section class="wrap local-links"><h2>Retrouver la biscuiterie</h2><p>Consultez les avis sur la fiche de l’atelier ou découvrez l’une de ses réalisations pour des séminaires.</p>
    <a class="text-link" href="{MAPS}">La Délicieuserie sur Google</a> {link("entreprise","Les biscuits pour entreprises","text-link")}</section>
    {contact_band()}'''


def quote():
    return f'''<section class="wrap form-layout"><div class="form-intro"><p class="kicker">Contacter l’atelier</p>
    <h1>Votre projet<br><em>de sablés.</em></h1>
    <p class="lead">Racontez votre idée à Anne-Sophie pour recevoir un devis gratuit. Une quantité approximative suffit pour commencer.</p>
    <div class="contact-direct"><h2>En direct avec Anne-Sophie</h2><a href="tel:+33617419761">06 17 41 97 61</a>
    <a href="mailto:{EMAIL}">{EMAIL}</a><p>Calais · Retrait ou envoi en France</p></div></div>
    <form id="quote-form" class="quote-form" action="https://formsubmit.co/{EMAIL}" method="post">
    <h2>Demande de devis</h2><p class="form-hint">Les champs marqués d’un astérisque sont obligatoires.</p>
    <input type="hidden" name="_subject" value="Demande de devis — La Délicieuserie"><input type="hidden" name="_next" value="{DOMAIN}/thanks.html">
    <input type="hidden" name="_captcha" value="false"><input type="hidden" name="_template" value="table">
    <div class="trap" hidden><label>Site internet<input name="_honey" type="text" tabindex="-1" autocomplete="off"></label></div>
    <div class="fields"><label>Votre nom *<input name="name" autocomplete="name" maxlength="120" required></label>
    <label>Adresse e-mail *<input name="email" type="email" autocomplete="email" maxlength="254" required></label>
    <label>Occasion<select name="occasion" id="occasion"><option value="">À préciser</option>
    <option value="Mariage">Mariage</option><option value="Entreprise">Entreprise ou événement professionnel</option>
    <option value="Fête de famille">Fête de famille</option><option value="Anniversaire">Anniversaire</option>
    <option value="Baptême">Baptême ou communion</option><option value="Naissance">Naissance ou baby shower</option>
    <option value="Autre">Autre occasion</option></select></label>
    <label>Téléphone<input type="tel" name="phone" autocomplete="tel" maxlength="40"></label>
    <label>Date souhaitée<input type="date" name="date"></label><label>Quantité approximative<input type="number" name="quantite" min="1" step="1" inputmode="numeric"></label></div>
    <label>Votre idée *<textarea name="message" rows="4" maxlength="4000" placeholder="Un motif, une inscription, un lieu de remise…" required></textarea></label>
    <p class="form-hint">Anne-Sophie Dubois utilise ces informations pour répondre à votre demande. Le message transite par FormSubmit. {link("privacy","Utilisation des données et droits")}</p>
    <button type="submit" class="button">Envoyer ma demande</button><p class="form-status" role="status" id="form-status"></p>
    </form></section>'''


def legal():
    return f'''<section class="wrap prose"><p class="kicker">Informations du site</p><h1>Mentions <em>légales.</em></h1>
    <h2>Éditrice</h2><p>Anne-Sophie Dubois, entrepreneure individuelle exerçant sous le nom commercial La Délicieuserie, à Calais (62100). SIREN 898 724 166. SIRET 898 724 166 00019.</p>
    <p>Contact professionnel : <a href="mailto:{EMAIL}">{EMAIL}</a> ou <a href="tel:+33617419761">06 17 41 97 61</a>.</p>
    <h2>Hébergement et médiation</h2><p>Version préparatoire. L’adresse professionnelle de domiciliation, les coordonnées de l’hébergeur effectif, la direction de la publication et le médiateur de la consommation compétent restent à confirmer par l’éditrice.</p>
    <h2>Contacter l’éditrice</h2><p>Pour signaler une erreur sur ce site ou demander des précisions sur une création, vous pouvez {link("devis","écrire à l’atelier")}. Les informations sur les données personnelles figurent dans la {link("privacy","politique de confidentialité")}.</p></section>'''


def privacy():
    return f'''<section class="wrap prose"><p class="kicker">Informations du site</p><h1>Données personnelles<br><em>et cookies.</em></h1>
    <h2>Votre demande de devis</h2><p>Anne-Sophie Dubois, entrepreneure individuelle à Calais, est responsable du traitement des demandes adressées à La Délicieuserie. Votre nom, votre e-mail et votre message permettent de préparer une réponse. Les autres champs sont facultatifs.</p>
    <p>Pour un particulier, le traitement sert à préparer, à sa demande, un éventuel contrat. Pour l’interlocuteur d’une entreprise, l’atelier s’appuie sur son intérêt légitime à traiter la demande professionnelle.</p>
    <h2>Destinataires et conservation</h2><p>Le formulaire transmet le message à FormSubmit, qui l’achemine vers la messagerie professionnelle Gmail de l’atelier. FormSubmit indique conserver une archive des soumissions pendant 30 jours. L’atelier conserve l’échange le temps de traiter votre projet puis, en cas de commande, pendant les durées applicables à sa gestion et à ses obligations légales.</p>
    <p>Version préparatoire. Le calendrier de suppression dans la messagerie et les garanties applicables aux éventuels transferts internationaux par les prestataires doivent être confirmés par l’éditrice.</p>
    <h2 id="cookies">Choisir les cookies de mesure d’audience</h2><p>Le site de l’atelier utilise consentmanager pour recueillir vos choix. Google Analytics mesure les visites après votre accord. Vous pouvez refuser la mesure d’audience ou modifier votre choix depuis le pied de chaque page.</p>
    <p><a class="text-link" href="#cookie-help" data-cookies>Ouvrir mes préférences de cookies</a></p>
    <p id="cookie-help">Si le panneau de préférences est indisponible, vous pouvez contacter l’atelier. La prévisualisation fonctionne sans mesure d’audience.</p>
    <h2>Exercer vos droits</h2><p>Pour demander l’accès, la rectification, l’effacement, la limitation ou, selon le fondement du traitement, la portabilité de vos données ou exercer votre droit d’opposition, écrivez à <a href="mailto:{EMAIL}">{EMAIL}</a>. Vous pouvez aussi <a href="https://www.cnil.fr/fr/plaintes">adresser une réclamation à la CNIL</a>.</p>
    <p><a href="https://formsubmit.co/privacy.pdf">Politique de FormSubmit</a> · <a href="https://policies.google.com/privacy?hl=fr">Politique de Google</a></p></section>'''


def notice(key):
    if key == "error":
        kicker="Erreur 404"; title="Page <em>introuvable.</em>"
        text="L’adresse a peut-être changé. Retrouvez les collections de biscuits ou écrivez directement à l’atelier."
    else:
        kicker="Demande transmise"; title="Merci pour <em>votre message.</em>"
        text=f"Anne-Sophie étudiera votre demande. Pour la compléter, vous pouvez écrire à <a href='mailto:{EMAIL}'>{EMAIL}</a>."
    return f'''<section class="wrap notice"><p class="kicker">{kicker}</p><h1>{title}</h1><p class="lead">{text}</p>
    <div class="actions">{link("home","Retour à l’accueil","button")}{link("biscuits","Découvrir les sablés","text-link")}</div></section>'''


def build():
    bodies={"home":home, "atelier":atelier, "devis":quote, "legal":legal, "privacy":privacy}
    for key,(path,*_) in PAGES.items():
        if key in SERVICES:
            body=service(key)
        elif key in bodies:
            body=bodies[key]()
        else:
            body=notice(key)
        target=ROOT / path.lstrip("/")
        if path.endswith("/"):
            target=target/"index.html"
        target.parent.mkdir(parents=True,exist_ok=True)
        target.write_text(shell(key,body),encoding="utf-8")
    entries="\n".join(f"  <url><loc>{DOMAIN}{url(k)}</loc></url>" for k in INDEXED)
    (ROOT/"sitemap.xml").write_text(f'<?xml version="1.0" encoding="UTF-8"?>\n<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n{entries}\n</urlset>\n',encoding="utf-8")


if __name__ == "__main__":
    build()
