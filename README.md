# Application de préparation des déclarations de manifestations

Application web statique, sans Next.js, sans installation et sans serveur. Elle fonctionne dans un navigateur moderne.

## Démarrage rapide
1. Décompressez l’archive.
2. Ouvrez `index.html` dans votre navigateur.

Si le navigateur bloque le chargement des fichiers JSON via `file://`, lancez un serveur local dans ce dossier :
- Python : `python3 -m http.server 8000`
- Puis ouvrez `http://localhost:8000`

## Fichiers JSON
- `association.json` : coordonnées de l’association préremplies.
- `prefectures.json` : référentiel de 30 grandes villes et préfectures correspondantes. Les champs d’adresse, e-mail, téléphone et source officielle sont laissés vides volontairement pour ne pas inventer de coordonnées.

Complétez `association.json` avec les coordonnées réelles du représentant légal, le téléphone et l’e-mail de l’association.

## Fonctionnalités
- Formulaire guidé avec champs obligatoires vérifiés.
- Génération d’une lettre à partir des informations saisies.
- Prévisualisation.
- Impression ou « Enregistrer au format PDF » depuis la fenêtre d’impression du navigateur.
- Export TXT et JSON d’une déclaration.
- Brouillons/historique conservés dans `localStorage`.
- Import/export JSON du référentiel et des brouillons.
- Aucune transmission automatique à une mairie ou préfecture.

## Données et confidentialité
Les déclarations sont conservées dans le stockage local du navigateur sur l’appareil courant. Elles ne sont pas envoyées vers un serveur et ne se synchronisent pas entre appareils. Exportez une sauvegarde JSON régulièrement.

## Limites
Le référentiel couvre 30 villes seulement, et la commune de rassemblement n’est pas toujours la ville où se trouve la préfecture. Vérifiez l’autorité compétente, les délais de déclaration et les consignes locales auprès des sources officielles. Le document généré est préparatoire et ne vaut pas dépôt ni autorisation.
