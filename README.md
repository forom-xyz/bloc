# Bloc Couleur

Site web de **Bloc Couleur**, le parti violet du Québec, porté par la coopérative sociale Forom.
Destination : **https://bloc.forom.xyz**

Website of **Bloc Couleur**, Québec's purple party, led by the social co-op Forom.

## Fichiers

| Fichier | Rôle |
| --- | --- |
| `index.html` | Le site complet à mettre en ligne (généré par `build.py`). |
| `page.html` | La source qu'on modifie. |
| `build.py` | Recrée `index.html` à partir de `page.html`. |
| `favicon.svg`, `favicon-32.png`, `apple-touch-icon.png` | Le logo en pixels pour l'onglet du navigateur. |

## Modifier le site

1. Modifier `page.html`.
2. Lancer `python3 build.py` pour recréer `index.html`.
3. Publier `index.html` et les fichiers d'icône (tout sauf `page.html` et `build.py`).

Le site est une seule page statique : aucun serveur ni outil d'installation n'est nécessaire.
Il fonctionne sur n'importe quel hébergeur statique (GitHub Pages, Netlify, Cloudflare Pages).

### Mises à jour fréquentes

- **Étape d'un projet** : dans `page.html`, changer `data-stage` sur la carte du projet
  (1 Idée, 2 Prototype, 3 Test, 4 Partagé).
- **Joueurs de Worlds** : changer le texte `~20 / 100` et le nombre de cases `class="on"`
  dans la barre (1 case = 10 joueurs).

## Licence

Contenu sous licence Creative Commons CC BY-SA 4.0.
