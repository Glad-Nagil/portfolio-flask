import os
from flask import Flask, render_template, request, flash, redirect, url_for
from datetime import datetime

app = Flask(__name__)
app.secret_key = os.environ.get("SECRET_KEY", "cle-locale-temporaire")

SERVICES = [
    {
        "icon": "◉",
        "title": "Coaching en communication",
        "subtitle": "",
        "items": [
            "Prise de parole en public",
            "Gestion du stress",
            "Structuration du discours",
            "Confiance en soi"
        ],
        "color": "blue",
        "image": "coaching.png"
    },
    {
        "icon": "▣",
        "title": "Montage vidéo",
        "subtitle": "Premiere Pro & CapCut",
        "items": [
            "Montage vidéos courtes",
            "Vidéos professionnelles",
            "Effets & transitions",
            "Miniatures YouTube"
        ],
        "color": "orange",
        "image": "montage-video.png"
    },
    {
        "icon": "✦",
        "title": "Design graphique",
        "subtitle": "Logos & affiches",
        "items": [
            "Création de logos",
            "Affiches & flyers",
            "Identité visuelle",
            "Contenus réseaux sociaux"
        ],
        "color": "purple",
        "image": "design-graphique.png"
    },
    {
        "icon": "⌘",
        "title": "UI/UX Design",
        "subtitle": "Web & mobile",
        "items": [
            "Maquettes UI/UX",
            "Prototypes interactifs",
            "Design d'interface",
            "Refonte de site/app"
        ],
        "color": "gradient",
        "image": "ui-ux.png"
    },
]

SKILLS = [
    {"icon": "🎙", "title": "Communication & prise de parole", "text": "Coaching, prise de parole en public, gestion du trac, storytelling.", "color": "purple"},
    {"icon": "▶", "title": "Montage vidéo", "text": "Montage dynamique, effets, transitions, reels, shorts et vidéo pro.", "color": "blue"},
    {"icon": "✎", "title": "Design graphique", "text": "Logos, affiches, flyers, bannières, identité visuelle et social media.", "color": "orange"},
    {"icon": "▦", "title": "UI/UX Design", "text": "Maquettes web & mobile, prototypes et design d’interface.", "color": "blue"},
    {"icon": "✧", "title": "Création de contenu", "text": "Communication, prise de parole et développement de la visibilité.", "color": "pink"},
]
PROJECTS = [
    {"title": "Identité visuelle — Luna Horizon", "category": "Design graphique", "image": "images/project-luna-horizon.jpg", "description": "Logo et identité visuelle pour un projet d’accompagnement international."},
    {"title": "Application mobile — BVC School", "category": "UI/UX Design", "image": "images/project-bvc-school.jpg", "description": "Concept d’interface mobile et parcours utilisateur."},
    {"title": "Supports de communication — Luna Horizon", "category": "Design graphique", "image": "images/project-luna-supports.jpg", "description": "Déclinaisons visuelles et supports de présentation."},
    {"title": "Réalisation vidéo — Projet créatif","category": "Montage vidéo","type": "video","video": "montage-video.mp4","description": "Montage vidéo professionnel réalisé avec Premiere Pro et CapCut."},    
    {"title": "Projet créatif 05", "category": "Design graphique", "image": "images/project.jpg", "description": "Ajoutez une affiche, un logo ou un visuel de campagne."},
    {"title": "Projet créatif 06", "category": "UI/UX Design", "image": "images/project-0.jpg", "description": "Ajoutez une maquette ou un prototype d’interface."},
]
TRAININGS = [
    {"title": "Parler avec impact", "text": "Maîtriser l’art de la prise de parole et devenir confiant devant n’importe quel public.", "format": "Théorie · Exercices pratiques"},
    {"title": "Créer du contenu qui attire", "text": "Apprendre à créer du contenu impactant pour développer votre visibilité.", "format": "Exercices pratiques · Projets"},
    {"title": "Design UI/UX de A à Z", "text": "Apprendre le design d’interface et créer des expériences utilisateur exceptionnelles.", "format": "Exercices pratiques · Projets"},
]

@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        name = request.form.get("name", "").strip()
        email = request.form.get("email", "").strip()
        subject = request.form.get("subject", "").strip()
        message = request.form.get("message", "").strip()
        if not all([name, email, subject, message]):
            flash("Merci de remplir tous les champs du formulaire.", "error")
        else:
            # Première version : le message est validé, mais aucun e-mail n'est envoyé.
            # Configurez un service e-mail avant de publier le site.
            app.logger.info("Message portfolio reçu à %s — nom=%s, email=%s, sujet=%s",
                            datetime.now().isoformat(timespec="seconds"), name, email, subject)
            flash("Merci ! Votre message a été validé. L’envoi réel par e-mail sera activé après configuration.", "success")
            return redirect(url_for("index") + "#contact")
    return render_template("index.html", services=SERVICES, skills=SKILLS, projects=PROJECTS, trainings=TRAININGS)

if __name__ == "__main__":
    app.run(debug=True)
