# La Délicieuserie

Site statique en français de la biscuiterie artisanale de Calais. Les pages HTML et leurs ressources sont prêtes à être servies depuis la racine d’un domaine. Le site fonctionne sans serveur applicatif ni base de données.

## Modifier les pages

Les textes, références, coordonnées et titres se trouvent dans `source/content.py`. Les éléments communs sont dans `source/layout.py`, les sections dans `source/build.py`. Les styles, la navigation, les galeries, le devis et le consentement utilisent `styles.css`, `script.js` et `consent.js`.

Après modification des sources, régénérer le HTML et lancer les tests depuis la racine.

```sh
python3 -B source/build.py
python3 -B tests/verify_site.py
node --test tests/interactions.test.cjs
```

Les pages déjà générées se trouvent à la racine et dans les dossiers de prestations. Python et Node sont utilisés pour la maintenance et les tests. L’hébergeur sert directement les fichiers. Pour un aperçu en développement, utiliser par exemple `python3 -m http.server 8000`. Les règles Apache de `.htaccess` nécessitent un hôte Apache ou compatible pour leur recette.

## Images, formulaire et statistiques

Les originaux restent dans `assets/images/` et `assets/logo.png`. Les pages utilisent les déclinaisons de `assets/media/`. Leurs légendes distinguent les idées de personnalisation et les réalisations documentées. Les polices et leurs licences sont dans `assets/fonts/`.

Le formulaire HTML de production fait un POST à FormSubmit. Avec JavaScript, l’envoi utilise son point d’entrée AJAX et affiche la confirmation après une réponse positive. La destinataire doit avoir activé le service pour son adresse. Sur un hôte de travail, le JavaScript affiche un essai local. Pour diffuser un aperçu isolé, remplacer aussi l’action HTML et interdire les soumissions par CSP comme dans le fichier de démonstration livré.

L’identifiant Google Analytics et le code d’intégration consentmanager proviennent du site d’origine. Le chargement de Google Analytics est conditionné au domaine canonique et à l’accord pour le fournisseur s26. Les données de devis ne sont jamais ajoutées par le code du site à un événement Analytics.

Le [rapport d’audit](docs/audit-seo.md) décrit les tests, les limites de mesure et les informations à confirmer avant publication.
