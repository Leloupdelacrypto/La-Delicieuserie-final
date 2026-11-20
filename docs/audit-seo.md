# La Délicieuserie · Audit et livraison

**20 novembre 2026.** Site de référence [www.ladelicieuserie.fr](https://www.ladelicieuserie.fr/). Base Git `271d958`. La branche `refonte-seo-design-2026` est destinée à la revue. Le HTML, le CSS, le JavaScript, les avis JSON et la page de remerciement téléchargés depuis le domaine public correspondent octet pour octet à cette base. Les dossiers d’images d’origine et l’historique Git sont conservés.

## Diagnostic priorisé

| Constat vérifié sur la version de départ | Impact SEO | Impact commercial | Difficulté | Traitement |
|---|---|---|---|---|
| Un seul document concentre les prestations. Les liens de navigation renvoient à ses ancres. | Fort | Fort | Moyenne | Un document HTML indexable par intention principale, liens entre occasions et devis contextualisé. |
| Pas de canonical ni de JSON-LD. Sitemap et robots en 404. Les quatre variantes HTTP/HTTPS et avec/sans www ont répondu 200 depuis le point de contrôle. | Fort | Moyen | Moyenne | Canonical HTTPS www, sitemap de sept URL, robots, type Bakery et fils d’Ariane. Règles 301 à tester sur le véritable hébergeur. |
| Images chargées au premier affichage, sept fichiers supérieurs à 2 Mo décimaux et aucune des 17 balises image avec les deux dimensions. | Fort | Fort | Faible | WebP avec srcset, tailles intrinsèques, chargement principal prioritaire et chargement différé secondaire. |
| Le bouton « Contact direct » pointe vers contact@exemple.fr. Deux correctifs JS modifient l’adresse de retour du formulaire. L’ancien README nomme Formspree, le code utilise FormSubmit. | Moyen | Fort | Faible | Coordonnées réelles, un retour absolu, POST avec repli natif, erreur lisible et données conservées à l’écran pour réessayer. |
| 107 déclarations CSS importantes, composants réécrits plusieurs fois, contrôles photo masqués, identifiant reviewsData répété trois fois. | Moyen | Fort | Moyenne | Feuille commune, zoom au clavier, navigation entre les images, restauration du focus et galerie lisible sans JS. |
| Les citations de secours et le fichier de six avis divergent. Cinq liens courts mènent à Maps, le sixième ne désigne pas un avis identifiable. Le contenu exact n’a pas pu être authentifié à la source. | Moyen | Fort | Faible | Lien vers la fiche Google issue de l’identifiant d’origine, sans recopier les témoignages ou les notes. JSON d’origine conservé. |
| Le lien légal pointe vers #. Une balise Google figure dans le document avant que le visiteur ait fait un choix, en plus du blocage automatique du gestionnaire. | Moyen | Fort | Moyenne | Pages légales préparées et fournisseur Analytics conditionné au choix. Le comportement réseau initial du site public avant correction reste indéterminé. |
| index.html et index 4.html partagent le même objet Git. L’URL index%204.html renvoyait déjà 404 sur le domaine public. Une URL inventée renvoyait une vraie 404. | Moyen | Faible | Faible | Redirection de compatibilité, traitement de /index.html et page 404 dédiée. |
| La page thanks.html était publiquement accessible sans directive noindex. | Faible | Faible | Faible | Confirmation hors sitemap et noindex, toujours accessible après transmission. |

## Requêtes et parcours

Étude qualitative de résultats francophones, sans accès au compte Search Console, au Keyword Planner ou à une mesure de positions dans Calais. La priorité décrit la proximité d’un devis et l’adéquation avec l’offre.

| Page | Priorité et requêtes | Intention et contenu |
|---|---|---|
| / | Haute · biscuiterie artisanale Calais, La Délicieuserie | Identifier l’activité locale, comparer les trois occasions puis demander un devis. |
| /biscuits-entreprise/ | Haute · biscuits avec logo entreprise, biscuits événementiels, cadeau client | Demande commerciale précise, concurrence de catalogues et d’artisans. Logo, quantité, conditionnement et réalisation pour les séminaires d’Adeo. |
| /biscuits-mariage/ | Haute · biscuits personnalisés mariage, sablés cadeaux d’invités, marque-place | Mariés et organisateurs recherchent une personnalisation précise. Prénoms, table, quantités et date de remise. |
| /biscuiterie-calais/ | Haute pour la confiance locale · atelier de biscuiterie à Calais, retrait La Délicieuserie | Rencontrer la créatrice et organiser le retrait ou l’envoi. Cette page approfondit les modalités locales de l’accueil. |
| /biscuits-personnalises/ | Intermédiaire · biscuits personnalisés, sablés personnalisés | Requête générique concurrentielle. Choix de la forme et du message, composition et conservation, liens vers les occasions. |
| /biscuits-fetes-de-famille/ | Intermédiaire · sablés baptême, biscuits personnalisés naissance, biscuits anniversaire prénom | Trois sections distinctes avec prénom et date, âge et thème. Une seule page familiale évite de multiplier les pages peu documentées. |
| /devis/ | Conversion · devis biscuits personnalisés, contact La Délicieuserie | Date, quantité, occasion et message, avec accès direct au téléphone et à l’e-mail. |

Les résultats mariage présentent des offres précises de marque-places. Les résultats entreprise mettent en avant logos et demandes de devis. Les requêtes très larges « cadeaux gourmands personnalisés » et « cadeaux d’entreprise personnalisés » couvrent aussi chocolats, paniers et objets publicitaires. Elles sont abordées dans les prestations pertinentes. [Mille Petits Biscuits](https://millepetitsbiscuits.fr/produit/marque-place/) · [Le Joyeux Biscuit](https://lejoyeuxbiscuit.com/pages/professionnels) · [Le Petit Biscuit Français](https://lepetitbiscuitfrancais.fr/) · [La Fabrique de Méline](https://www.lafabriquedemeline.com/produit/biscuit-sable-nounours-a-personnaliser/) · [Kisseo](https://kisseo.fr/tous-les-cadeaux-personnalises/cadeau-entreprise/).

## Informations locales et éditoriales

- L’API publique de recherche d’entreprises confirme Anne-Sophie Dubois, nom commercial La Délicieuserie, établissement actif à Calais, SIREN 898 724 166, SIRET 898 724 166 00019. Le site d’origine donne le téléphone et la messagerie professionnels. Aucune rue ou plage horaire d’accueil n’a été déduite de la domiciliation. [Registre public](https://recherche-entreprises.api.gouv.fr/search?q=898724166) · [Site de l’atelier](https://www.ladelicieuserie.fr/).
- La créatrice annonce des envois en France et décrit la gravure et le conditionnement d’une commande Adeo. Ces informations étayent les pages locale et professionnelle. [Envois en France](https://fr.linkedin.com/posts/anne-sophie-dubois-7bb5b437a_retour-sur-les-rencontres-entreprises-et-activity-7376938793435598848-qmoa) · [Réalisation Adeo](https://fr.linkedin.com/posts/anne-sophie-dubois-7bb5b437a_biscuiterieartisanale-biscuitpersonnalis%C3%A9-activity-7404415030093565952-A0nl).
- Les photographies et visuels du dépôt sont conservés. Neuf fichiers .jpg sont en réalité encodés en PNG. Les cinq panneaux textuels ne sont pas des photographies. Le visuel de baptême contient des métadonnées Google AI, préservées dans ses dérivés. Les scènes de biscuits sont présentées comme inspirations. Le portrait et le logo constituent l’image de partage. Des photos de commandes dont l’atelier possède les droits, en particulier pour les entreprises et les mariages, rendraient ces pages plus convaincantes.
- Les mentions « certification HACCP », « hygiène irréprochable » et « écoresponsable » ont été sorties de l’argumentaire dans l’attente de justificatifs précis. Le lien Google, les contacts, les réseaux, la composition, l’épaisseur, les modalités de personnalisation et la conservation publiées par l’atelier sont préservés.
- Le profil LinkedIn et les métadonnées Facebook/Instagram sont cohérents avec l’identité de l’atelier. Messenger redirige vers une connexion. L’identifiant de la fiche Google préexistante est conservé. Demander à la propriétaire de confirmer sa maîtrise et l’URL officielle. [Fiche Google](https://www.google.com/maps?cid=7066990526774449785).

## Technique et recette

Toutes les pages ont un titre descriptif distinct, un H1, une description et les métadonnées de partage. Les sept pages commerciales figurent dans le sitemap. Les pages légales préparatoires, la confirmation et la 404 portent noindex. La page atelier, l’accueil et le devis déclarent le même établissement Bakery, sous-type de LocalBusiness et d’Organization. L’adresse contient uniquement les éléments vérifiés. Les résultats locaux enrichis soumis aux exigences de Google restent incertains. Les FAQ visibles répondent aux questions sur le produit et la commande. Google a retiré son résultat enrichi FAQ en mai 2026. [Établissements locaux](https://developers.google.com/search/docs/appearance/structured-data/local-business) · [Historique Google](https://developers.google.com/search/updates).

Les contrôles Python portent sur le sitemap, les liens locaux, les fragments, les images, les titres, les robots, les identifiants HTML, le JSON-LD et la configuration du devis. Les tests Node couvrent consentement, retrait, aperçu, double clic, réponse serveur négative, réessai, antispam et confirmation. Huit tests réussis.

Dans Chromium, 34 combinaisons page/largeur ont été examinées à 320, 390, 768, 1040, 1041 et 1280 pixels CSS. Les 11 pages principales et utilitaires ont aussi été contrôlées avec axe-core 4.14.1 à 390 et 1280 px (22 analyses). Le contrôle final ne relève aucune infraction automatisée dans les règles WCAG A/AA sélectionnées et aucun débordement horizontal. Ces contrôles ne constituent pas un audit humain exhaustif.

Le menu mobile, Échap, la galerie, le passage à l’image suivante, le devis entreprise prérempli, les erreurs de saisie et une soumission simulée ont été testés dans le navigateur. L’aperçu autonome a également été parcouru de l’accueil au mariage puis au devis, avec sélection du bon événement. En essai isolé, la CMP existante a chargé zéro balise Google après refus, une après accord, puis zéro sur la page rechargée après retrait. Un script local remplaçait Google dans cet essai. Les identifiants de mesure et de CMP ont été conservés dans le code de la branche.

Le devis fonctionne en POST. Le parcours avec JavaScript exploite le point de terminaison AJAX de FormSubmit. La transmission simulée est vérifiée. La réception effective en boîte professionnelle et l’activation de FormSubmit restent à contrôler avec l’exploitante. La copie préparatoire comporte des coordonnées directes en cas d’indisponibilité du service. [Documentation FormSubmit](https://formsubmit.co/documentation) · [Confidentialité du service](https://formsubmit.co/privacy.pdf) · [Gestionnaire de consentement](https://www.consentmanager.net/en/help/how-to-guides/working-with-google-consent-mode/).

## Ce qui change à l’écran

Sur l’ancien accueil, le grand bandeau réunit la présentation et plusieurs liens vers des sections de la même page. Dans la refonte, l’accroche courte, l’image des sablés gravés et le bouton « Demander un devis » partagent le premier écran. Trois entrées illustrées conduisent aux mariages, aux entreprises et aux fêtes de famille. Sur téléphone, le devis et l’accès aux sablés précèdent l’image. Les pages de prestation reprennent l’occasion dans le formulaire et disposent de leur propre galerie. Les bleus, l’orange, le turquoise et le fond crème d’origine sont conservés.

## Mesures avant et après

Trois paires de chargements à froid alternés de l’accueil dans Chromium, fenêtre mobile émulée de 390 × 844 px, sans défilement. Chaque essai dispose de nouvelles URL de ressources pour éviter la réutilisation du cache. Les appels externes sont neutralisés dans les deux versions. Le poids additionne le document et les ressources locales chargées, avec le même petit script de mesure, à partir des tailles de corps encodés remontées par le navigateur. Le réseau et le processeur ne sont pas bridés. Unités décimales.

| Indicateur | Avant | Après |
|---|---:|---:|
| Poids initial local, identique sur les trois essais | 20 051 821 octets (20,05 Mo) | 238 917 octets (239 ko), soit −98,8 % |
| Requêtes locales au premier affichage | 22 | 14 |
| LCP médian (élément principal visible) | 1,604 s | 1,536 s |
| LCP minimum à maximum | 0,300 à 1,912 s | 1,196 à 2,028 s |
| CLS médian (stabilité visuelle) | 0 | 0 |
| CLS maximal observé | 0,0055 | 0 |
| Feuille CSS, fichier source | 32 079 octets | 15 705 octets |
| JavaScript propre au site, fichiers sources cumulés | 14 722 octets | 7 651 octets, consentement inclus |

La baisse du poids est reproductible dans ces conditions. Les plages de LCP se recouvrent et ces essais ne permettent pas de conclure à une amélioration du délai chez les clients. Le visuel principal passe de 2 418 746 octets à 22 818, 50 672 ou 96 668 octets selon la variante responsive. Les dix grands visuels dans leur variante WebP la plus large totalisent environ 629 ko contre 19,68 Mo pour les sources correspondantes.

Le lancement local de Lighthouse a échoué dans cet environnement et l’API PageSpeed Insights a renvoyé une limite de quota. Aucun score Performance, SEO ou Accessibilité Lighthouse n’est disponible. L’INP et les Core Web Vitals au 75e centile des visiteurs réels nécessitent des données terrain après publication.

## Avant une mise en ligne autorisée

1. Compléter les mentions légales avec l’adresse de domiciliation à publier, la direction de publication, l’hébergeur effectif (nom, adresse et téléphone), le médiateur de la consommation et, si applicable, la TVA et les mentions d’immatriculation complémentaires. Confirmer les durées réellement pratiquées dans la messagerie et les garanties de transfert des prestataires. [Service Public](https://entreprendre.service-public.gouv.fr/vosdroits/F37351) · [Médiation](https://entreprendre.service-public.gouv.fr/vosdroits/F33338) · [CNIL](https://cnil.fr/fr/cookies-et-autres-traceurs/regles/cookies/FAQ).
2. En préproduction de l’hébergeur, tester un vrai devis avec l’atelier, sa réception dans la messagerie et la possibilité de répondre à l’expéditeur. Vérifier le bandeau en français, le refus, l’acceptation et le retrait avec les paramètres régionaux réels. Vérifier dans GA4 que les événements automatiques ne capturent aucune valeur de champ.
3. Sur le véritable serveur Apache/LiteSpeed ou son équivalent, valider le certificat des deux noms, les réponses 301 des versions HTTP, sans www, /index.html et /index%204.html, les URL de prestation avec barre finale, le statut 404 réel, le cache, la compression et l’absence de boucle derrière un éventuel proxy TLS. Le serveur de prévisualisation statique ne lit pas .htaccess.
4. Avant la bascule, exporter les clics, impressions, requêtes et pages de la propriété Search Console. Après publication autorisée, soumettre le sitemap HTTPS www et inspecter l’accueil, les pages entreprise et mariage, l’atelier et le devis. Contrôler l’URL canonique choisie par Google et les erreurs d’exploration. Après 28 jours puis environ 3 mois, comparer clics, impressions et demandes effectivement reçues, en tenant compte de la saisonnalité. [Search Console](https://support.google.com/webmasters/answer/7576553?hl=fr) · [Sitemap](https://developers.google.com/search/docs/crawling-indexing/sitemaps/build-sitemap?hl=fr).
5. Depuis la fiche Google Business Profile, vérifier le nom, le téléphone, le lien HTTPS, la catégorie réellement proposée par Google la plus proche de l’activité, les modalités d’accueil et les services. Distinguer le secteur où l’entreprise se déplace de l’envoi postal national. Ajouter des photographies originales avec accord de l’atelier et utiliser le lien officiel d’avis. [Aide Google Business Profile](https://support.google.com/business/answer/3039617?hl=fr).

Sans accès propriétaire, l’état d’indexation, les positions, les volumes de requêtes et l’évolution des devis restent à mesurer. La recette locale permet de juger le poids et le comportement des pages. Les données Core Web Vitals de visiteurs réels, dont l’INP au 75e centile, doivent être relevées séparément.
