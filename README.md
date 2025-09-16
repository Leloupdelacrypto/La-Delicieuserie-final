# La Délicieuserie — Site vitrine
Gabarit statique prêt pour GitHub Pages. Palette et textes adaptés à la biscuiterie artisanale.

## Déploiement
- Uploadez les fichiers à la racine du dépôt GitHub.
- Activez *Settings → Pages → Deploy from a branch* (branche `main`, dossier `/`).
- Les images principales proviennent d'Unsplash (libre d'usage).

## Crédit images (Unsplash)
- Cookies hero : https://images.unsplash.com/photo-1542838132-92c53300491e?auto=format&fit=crop&w=1600&q=80
- Grid 1 : https://images.unsplash.com/photo-1509440159596-0249088772ff?auto=format&fit=crop&w=1200&q=80
- Grid 2 : https://images.unsplash.com/photo-1541781774459-bb2af2f05b55?auto=format&fit=crop&w=1200&q=80
- Grid 3 : https://images.unsplash.com/photo-1488477181946-6428a0291777?auto=format&fit=crop&w=1200&q=80
- Personnalisation : https://images.unsplash.com/photo-1519681393784-d120267933ba?auto=format&fit=crop&w=1200&q=80
- Atelier : https://images.unsplash.com/photo-1514516430039-5845f26b18d7?auto=format&fit=crop&w=1200&q=80

Remplacez `assets/logo.png` par votre logo haute définition si besoin, ainsi que `assets/favicon.png`.

## Formulaire de contact (Formspree ou Netlify)
- **Formspree (recommandé pour GitHub Pages)** : remplacez `https://formspree.io/f/your-id` par votre endpoint (créé sur https://formspree.io/).
- **Netlify Forms** (si vous déployez sur Netlify) : remplacez le `<form>` par :
  ```html
  <form name="contact" method="POST" data-netlify="true">
    <input type="hidden" name="form-name" value="contact">
    ...
  </form>
  ```
  et ajoutez un redirect `netlify.toml` si besoin.

## Carrousel produits
- 4 fiches produits, navigation par flèches et points, responsive.
- Modifiez les images, titres, textes et prix directement dans `index.html`.
