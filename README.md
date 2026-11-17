# julie-landrevie.github.io

Portfolio de Julie Landrevie : data, performance et IA appliquées au football (football féminin en priorité).

- **Deux portes d'entrée** : `#performance` (performance et football féminin) et `#data-ia` (data et IA).
- **Deux langues** : bouton FR / EN, ou `?lang=en` dans l'adresse.
- **Glossaire**, registre des preuves (chaque chiffre renvoie au fichier qui le produit), résultats nuls publiés.

Liens à donner dans une candidature :
- performance : https://julie-landrevie.github.io/#performance
- data et IA : https://julie-landrevie.github.io/#data-ia
- en anglais : https://julie-landrevie.github.io/?lang=en#performance

## Modifier le site

Le texte est dans `build/contenu.py` (français et anglais côte à côte), la mise en page dans `build/gabarit.html`.
Après une modification :

```bash
python3 build/build.py   # régénère index.html ; les compteurs sont recalculés
```

Ajouter un projet = ajouter une entrée dans `PROJETS` (question, chiffres, texte, visuels, limites, liens) et, si besoin, une ligne dans `PREUVES`.

Charte : fond #f6f1e7, DM Serif Display + Lato, vert d'eau #0d8f84, une seule mise en avant rouille #cc4a12.
