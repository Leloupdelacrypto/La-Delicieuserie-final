"""Contenus, métadonnées et légendes du site. Texte en français, liens stables."""

DOMAIN = "https://www.ladelicieuserie.fr"
EMAIL = "ladelicieuserie@gmail.com"
MAPS = "https://www.google.com/maps?cid=7066990526774449785"
SOCIAL = {
    "Instagram": "https://www.instagram.com/la_delicieuserie/",
    "Facebook": "https://www.facebook.com/p/La-D%C3%A9licieuserie-61555204563313/",
    "LinkedIn": "https://www.linkedin.com/company/la-delicieuserie/",
    "Messenger": "https://www.messenger.com/t/188037521066732",
}
CASE = "https://fr.linkedin.com/posts/anne-sophie-dubois-7bb5b437a_biscuiterieartisanale-biscuitpersonnalis%C3%A9-activity-7404415030093565952-A0nl"

# URL, libellé de navigation, title et description.
PAGES = {
    "home": ("/", "Accueil", "Biscuiterie artisanale à Calais · La Délicieuserie", "À Calais, Anne-Sophie façonne des sablés personnalisés pour mariages, fêtes de famille et entreprises. Découvrez ses idées de biscuits et demandez votre devis."),
    "biscuits": ("/biscuits-personnalises/", "Nos sablés", "Biscuits et sablés personnalisés sur mesure · La Délicieuserie", "Forme, prénom, date, dessin ou logo : découvrez comment personnaliser un sablé, sa recette, ses dimensions et sa conservation. Devis auprès de l’atelier."),
    "mariage": ("/biscuits-mariage/", "Mariage", "Biscuits de mariage personnalisés pour vos invités · La Délicieuserie", "Imaginez des sablés de mariage avec vos prénoms, une date ou un motif, à offrir aux invités ou à déposer sur la table. Demandez un devis pour votre réception."),
    "entreprise": ("/biscuits-entreprise/", "Entreprises", "Biscuits avec logo pour entreprises et séminaires · La Délicieuserie", "Des biscuits personnalisés à votre logo pour un séminaire, un salon ou un cadeau client. Découvrez un projet réalisé et préparez votre demande de devis."),
    "famille": ("/biscuits-fetes-de-famille/", "Fêtes de famille", "Sablés pour anniversaire, baptême et naissance · La Délicieuserie", "Un prénom pour un baptême, un âge pour un anniversaire, un message de naissance : composez un sablé à offrir à vos proches et parlez-en à l’atelier."),
    "atelier": ("/biscuiterie-calais/", "L’atelier", "L’atelier d’Anne-Sophie, biscuiterie à Calais · La Délicieuserie", "Rencontrez Anne-Sophie Dubois, créatrice de La Délicieuserie à Calais. Découvrez son travail, les modalités de retrait et d’envoi et ses coordonnées."),
    "devis": ("/devis/", "Demander un devis", "Demander un devis pour vos biscuits personnalisés · La Délicieuserie", "Contactez Anne-Sophie à Calais pour un devis gratuit. Indiquez votre occasion, la date et la quantité envisagées, ou contactez l’atelier par téléphone."),
    "legal": ("/mentions-legales/", "Mentions légales", "Mentions légales · La Délicieuserie", "Identification de l’éditrice de La Délicieuserie, immatriculation et coordonnées de contact pour le site de la biscuiterie artisanale à Calais."),
    "privacy": ("/confidentialite/", "Confidentialité", "Données personnelles et cookies · La Délicieuserie", "Utilisation des données pour traiter les devis, destinataires des messages, gestion des cookies de mesure d’audience et exercice de vos droits."),
    "thanks": ("/thanks.html", "Confirmation", "Merci pour votre demande · La Délicieuserie", "Confirmation de transmission de votre demande de devis à La Délicieuserie."),
    "error": ("/404.html", "Page introuvable", "Page introuvable · La Délicieuserie", "Retrouvez les sablés personnalisés de La Délicieuserie ou contactez directement l’atelier."),
}
INDEXED = ("home", "biscuits", "mariage", "entreprise", "famille", "atelier", "devis")

# Dimensions de la plus grande variante conservée. Les fichiers d’origine restent intacts.
MEDIA = {
    "hero": (1184, 864, "Assortiment de sablés gravés de messages et de motifs sur une planche en bois"),
    "part1": (1024, 1024, "Sablé d’anniversaire gravé d’un cygne et de l’inscription « 10 ans »"),
    "part2": (1184, 864, "Illustration de baptême : un faon, un prénom et une date gravés sur un sablé"),
    "part3": (1184, 864, "Sablé aux bords cannelés orné de deux alliances, de prénoms et d’une date"),
    "pros1": (1088, 960, "Sablés ronds et rectangulaires avec messages et motifs gravés"),
    "pros2": (1088, 960, "Sablé rond gravé du mot « Merci » au milieu de biscuits à motifs"),
    "pros3": (1088, 960, "Assortiment de biscuits à motif et à message sur un plateau en bois"),
    "atelier": (1280, 1167, "Four, plaques de biscuits et robot pâtissier sous l’emblème de la biscuiterie"),
    "personnalisation": (1184, 864, "Poste de personnalisation avec ordinateur et machine de marquage"),
    "portrait": (800, 800, "Anne-Sophie Dubois, créatrice de La Délicieuserie, en tenue de travail"),
}

# Un texte par intention de recherche. Les légendes décrivent ce que montre l’image.
SERVICES = {
    "biscuits": {
        "label": "La personnalisation", "heading": "Les sablés", "em": "personnalisés.",
        "intro": "Choisissez ce que vous voulez raconter. Une forme attire l’œil, un mot donne le ton, un dessin fait reconnaître l’occasion au premier regard.",
        "image": "hero", "caption": "Formes et motifs de personnalisation", "cta": "Imaginer mes sablés",
        "section": "Du dessin au biscuit",
        "blocks": [
            ("Une forme pour commencer", "Rond, rectangle ou silhouette particulière : partez de votre idée, puis précisez la place que le biscuit occupera sur la table ou dans son emballage. L’atelier vous aide à choisir un format adapté."),
            ("Un message qui se lit", "Un prénom, une date ou quelques mots laissent de la place au motif. Pour une inscription plus longue ou un logo détaillé, échangez avec Anne-Sophie sur la taille et la lisibilité du dessin."),
            ("Une recette au beurre", "Les sablés contiennent de la farine de blé, du beurre, du sucre, des œufs et du sucre vanillé bourbon. Ils sont préparés sans conservateur. La recette contient du blé (gluten), du lait et des œufs."),
        ],
        "gallery": [("pros2","Un petit mot à offrir"),("personnalisation","Le poste de personnalisation"),("part3","Prénoms et date")],
        "faq": [
            ("Quelle est l’épaisseur d’un sablé ?", "Les sablés de l’atelier font 4 mm d’épaisseur. La forme et la taille du motif se discutent au moment du devis."),
            ("Combien de temps les biscuits se conservent-ils ?", "L’atelier indique une conservation de trois mois. Pour votre commande, référez-vous aux indications communiquées avec les biscuits."),
            ("Que préciser si un invité a une allergie ?", "Contactez l’atelier avant de commander pour vérifier la composition et les risques de traces. La recette de base contient du blé, du lait et des œufs."),
        ],
    },
    "mariage": {
        "label": "Les mariages", "heading": "Des biscuits", "em": "pour votre mariage.",
        "intro": "Un petit cadeau posé sur une serviette, un prénom à la place d’un carton, quelques mots pour remercier vos invités. Le sablé peut accompagner votre table jusqu’au dernier détail.",
        "image": "part3", "caption": "Inspiration mariage · Alliances et prénoms", "cta": "Parler de mon mariage",
        "section": "Sur votre table de mariage",
        "blocks": [
            ("Un cadeau pour chaque invité", "Vos deux prénoms et la date de la cérémonie suffisent à personnaliser chaque sablé. Un motif de votre faire-part peut aussi servir de point de départ."),
            ("Un marque-place à croquer", "Pour varier les prénoms d’un biscuit à l’autre, indiquez-le dès le premier échange. Vous pourrez convenir avec l’atelier de la liste à préparer et de la façon de répartir les pièces."),
            ("Organiser la réception", "Précisez la date à laquelle vous avez besoin des biscuits, le nombre de convives et le lieu de réception. L’emballage et le mode de remise pourront être étudiés avec le devis."),
        ],
        "gallery": [("part3","Deux alliances sur un sablé"),("hero","Une idée de table gourmande"),("pros2","Un merci pour les invités")],
        "faq": [
            ("Peut-on assortir les biscuits au faire-part ?", "Décrivez le motif, les initiales ou le thème à reprendre. L’atelier étudiera quels détails peuvent rester lisibles sur le format choisi."),
            ("Faut-il connaître le nombre définitif d’invités ?", "Une estimation suffit pour le premier échange. Signalez que le nombre peut évoluer afin de convenir avec l’atelier de la quantité définitive."),
        ],
    },
    "entreprise": {
        "label": "Les professionnels", "heading": "Des biscuits", "em": "à votre logo.",
        "intro": "Accueillir les participants d’un séminaire, remercier un client ou offrir un souvenir de salon : votre logo ou votre message prend place sur un sablé fabriqué à Calais.",
        "image": "pros1", "caption": "Inspiration entreprise · Messages et motifs", "cta": "Demander un devis entreprise",
        "section": "Préparer votre commande professionnelle",
        "blocks": [
            ("Un logo qui se reconnaît", "Indiquez le texte et les éléments de votre identité visuelle à garder. Une version simple du logo donne à l’atelier un point de départ pour discuter de la taille, de la forme et du marquage."),
            ("Une attention au bon moment", "Pour une pause de séminaire, comptez les participants. Pour des cadeaux clients ou collaborateurs, partez du nombre de destinataires et précisez la présentation envisagée."),
            ("Un exemple pour Adeo", "Anne-Sophie présente une commande de biscuits personnalisés pour les séminaires d’Adeo. Elle y décrit la gravure et le conditionnement des sablés dans son atelier à Calais."),
        ],
        "gallery": [("pros1","Logos et messages"),("pros2","Un biscuit pour remercier"),("pros3","Différentes formes de sablés")],
        "faq": [
            ("Comment transmettre mon logo ?", "Décrivez votre projet dans le formulaire. Vous pourrez ensuite envoyer le visuel directement par e-mail à l’atelier et convenir du fichier adapté au marquage."),
            ("Comment obtenir un chiffrage pour un événement ?", "Précisez la date de remise souhaitée, le nombre de biscuits et la destination. Si vous envisagez plusieurs messages ou différents conditionnements, signalez-le dans votre demande."),
        ],
    },
    "famille": {
        "label": "Les fêtes de famille", "heading": "Des sablés pour", "em": "les jours de fête.",
        "intro": "Un âge, un nouveau prénom ou la date d’un baptême peuvent se raconter sur un biscuit. Choisissez un détail que les proches reconnaîtront tout de suite.",
        "image": "part1", "caption": "Inspiration anniversaire · Un âge et un motif", "cta": "Préparer ma fête",
        "section": "Une idée pour chaque fête",
        "blocks": [
            ("Pour un anniversaire", "Associez l’âge à un animal, une passion ou un petit message. Les biscuits peuvent accompagner le gâteau ou se glisser dans un sachet à offrir au départ des invités."),
            ("Pour un baptême ou une communion", "Le prénom et la date composent un souvenir simple. Un faon, une étoile ou un autre motif choisi par la famille peut compléter la gravure."),
            ("Pour annoncer une naissance", "Faites découvrir le prénom aux proches sur un sablé. Pour une baby shower, un motif commun à tous les biscuits peut également reprendre le thème de la fête."),
        ],
        "gallery": [("part1","Un cygne pour un anniversaire"),("part2","Illustration de baptême"),("part3","Un prénom et une date")],
        "faq": [
            ("Peut-on prévoir plusieurs motifs ?", "Indiquez les prénoms, âges ou motifs que vous aimeriez associer. L’atelier vous précisera la faisabilité et la répartition des biscuits dans son devis."),
            ("Que préparer pour une première demande ?", "L’occasion, une quantité même approximative et la date de la fête permettent de cadrer le projet. Une idée de motif ou quelques mots à graver peuvent suffire pour commencer."),
        ],
    },
}
