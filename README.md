# Portfolio — Flask

Première version du portfolio inspirée de votre maquette : accueil, à propos, compétences, services, réalisations filtrables, formations et formulaire de contact.

## 1. Prérequis
- Python 3.10 ou plus récent
- Un navigateur web
- (Facultatif) Visual Studio Code

Vérifiez Python dans un terminal :
```bash
python --version
```
Sur certains systèmes Windows, utilisez `py --version`.

## 2. Installer et lancer le site

Ouvrez un terminal dans le dossier `portfolio_flask`, puis exécutez :

```bash
python -m venv .venv
```

Activez l’environnement virtuel :

**Windows (PowerShell)**
```powershell
.venv\Scripts\Activate.ps1
```

**Windows (Invite de commandes)**
```bat
.venv\Scripts\activate
```

**macOS / Linux**
```bash
source .venv/bin/activate
```

Installez les dépendances et lancez le site :
```bash
pip install -r requirements.txt
python app.py
```

Ouvrez ensuite http://127.0.0.1:5000 dans votre navigateur.

## 3. Ajouter vos images

Placez vos ressources dans `static/images/`. Les noms utilisés par défaut sont :
- `portrait-hero.png` — photo dans la bannière d’accueil
- `portrait-about.jpg` — photo de la section À propos
- `portrait-contact.png` — photo de la section Contact
- `project-luna-horizon.jpg`
- `project-bvc-school.jpg`
- `project-luna-supports.jpg`
- `project-04.jpg`, `project-05.jpg`, `project-06.jpg`

Si vos fichiers portent d’autres noms, renommez-les ou modifiez les chemins dans `app.py` et `templates/index.html`.
Les cartes de projets affichent un visuel de remplacement tant qu’une image n’est pas présente.

## 4. Personnaliser le contenu
- Textes, services, compétences et projets : `app.py`
- Structure HTML : `templates/index.html`
- Couleurs, mise en page et responsive : `static/css/style.css`
- Filtres du portfolio et menu mobile : `static/js/main.js`

## 5. À savoir avant publication
Le formulaire vérifie les champs et affiche une confirmation, mais **n’envoie pas encore de vrai e-mail**. Il faudra connecter un service SMTP ou une API e-mail. Changez aussi `app.secret_key` et désactivez le mode debug en production.
