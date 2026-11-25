"""Pages de partage pour LinkedIn : une petite page par lien, avec sa propre miniature.

LinkedIn affiche l'image indiquée par la balise og:image de la page partagée. Les applications
Streamlit, GitHub ou Notion ne permettent pas de choisir cette image : on partage donc
https://julie-landrevie.github.io/l/<nom>.html, qui porte la bonne miniature et renvoie
aussitôt le visiteur vers la vraie adresse.

Usage : python3 build/partage.py   (écrit le dossier l/ ; miniatures dans assets/linkedin/)
"""
from html import escape
from pathlib import Path

SITE = "https://julie-landrevie.github.io"
ROOT = Path(__file__).resolve().parents[1]

# nom de la page, adresse de destination, miniature, titre, description
LIENS = [
    ("portfolio", SITE + "/", "00_portfolio", "Julie Landrevie — Data & performance football",
     "Portfolio : 14 études en football (féminin en priorité), données et code ouverts, en français et en anglais."),
    ("portfolio-en", SITE + "/?lang=en", "00_portfolio", "Julie Landrevie — Football data & performance",
     "Portfolio: 14 football studies (women's football first), open data and code, in English and French."),
    ("charge", SITE + "/#charge", "01_suivi_charge", "Suivi de charge et de forme en football féminin d’élite",
     "50 joueuses, 2 saisons, 10 075 fichiers GPS : contrôle qualité, ACWR, alertes lisibles par un staff (données SoccerMon)."),
    ("tableau-de-bord", SITE + "/womens-football-load-monitoring/", "23_tableau_de_bord_charge",
     "Tableau de bord du suivi de charge — football féminin",
     "Charge, ACWR, wellness, GPS et alertes de 50 joueuses, en ligne (données SoccerMon)."),
    ("vestiaire", SITE + "/#vestiaire", "02_vestiaire", "Vestiaire : les seuils de sprint masculins cachent des joueuses",
     "Avec les seuils féminins publiés par SkillCorner, les matchs sans sprint passent de 43 % à 15 %."),
    ("opportunites", SITE + "/#opportunites", "03_opportunites", "Comparer les joueuses à opportunités égales",
     "Une remplaçante presse un tiers de plus par minute que la même joueuse titulaire (×1,33), 4 championnats féminins."),
    ("app-opportunites", "https://womens-football-opportunity.streamlit.app", "03_opportunites",
     "Application — comparer les joueuses à opportunités égales",
     "Classer les joueuses par 90 minutes, par possession ou ajusté à l’adversaire : WSL, Frauen-Bundesliga, Liga F, Serie A."),
    ("phases-arretees", SITE + "/#phases-arretees", "04_phases_arretees", "Phases arrêtées : autant chez les femmes que chez les hommes",
     "39,8 % du xG hors penalty des deux côtés (données StatsBomb)."),
    ("penalties", SITE + "/#penalties", "05_penalties", "Penalties : où tirent les joueuses",
     "60,9 % de réussite en séance de tirs au but, contre 76,2 % en match (données StatsBomb)."),
    ("fiabilite", SITE + "/#fiabilite", "06_fiabilite", "Combien de minutes avant qu’une statistique soit fiable ?",
     "22 statistiques sur 24 fiables sur une saison de WSL (données StatsBomb)."),
    ("lois", SITE + "/#lois", "07_lois_du_jeu_ia", "Assistant IA sur les Lois du Jeu : RAG et évaluation",
     "Réponses fausses : 22 % sans le livret officiel de l’IFAB, 0 avec."),
    ("video", SITE + "/#video", "08_analyse_video", "Analyse vidéo football : Once Sport et Dartfish",
     "96 actions codées avec mon propre panneau de codage, constats pour le staff."),
    ("video-dartfish", "https://youtu.be/QwjbEjAHlig", "22_video_dartfish", "Analyse vidéo Dartfish : Supercoupe d’Espagne",
     "Codage du match, placement du gardien sur les frappes croisées, plan d’entraînement en 4 blocs."),
    ("tennis", SITE + "/#tennis", "09_tennis_de_table", "Finale de tennis de table codée point par point",
     "151 points codés dans Dartfish : finale des Championnats de France 2025."),
    ("tracking", SITE + "/#tracking", "10_tracking", "Intensité physique et données de tracking",
     "Vérifier qu’une vitesse est possible avant de l’interpréter."),
    ("app-physical", "https://physical-tracking.streamlit.app", "10_tracking", "Application — Physical Tracking",
     "Distances, vitesses, sprints et zones d’intensité (SkillCorner et Metrica Sports, données ouvertes)."),
    ("scoutpro", SITE + "/#scoutpro", "11_scoutpro", "ScoutPro : profils de joueuses et de joueurs",
     "6 343 profils, percentiles par groupe de postes (données StatsBomb)."),
    ("app-scoutpro", "https://scoutpro-football.streamlit.app", "11_scoutpro", "Application — ScoutPro",
     "Fiches de scouting et percentiles par poste (données StatsBomb)."),
    ("xg", SITE + "/#xg", "12_xg_passes", "xG, profils de tir et réseaux de passes",
     "Qui crée de vraies occasions, et par où passe le jeu (données StatsBomb)."),
    ("app-xg", "https://xg-shooting-analysis.streamlit.app", "12_xg_passes", "Application — xG & Shooting",
     "Cartes de tirs, xG et profils de finisseurs (données StatsBomb)."),
    ("app-tactical", "https://tactical-dashboard-football.streamlit.app", "15_tactical_dashboard",
     "Application — Tactical Dashboard", "Réseaux de passes, xG, pressing et zones pour tout match StatsBomb ouvert."),
    ("app-pass-network", "https://pass-network.streamlit.app", "16_pass_network", "Application — Pass Network",
     "Réseaux de passes et centralité des joueuses et joueurs (données StatsBomb)."),
    ("mpg", SITE + "/#mpg", "13_mpg_optimizer", "MPG Optimizer : collecte automatisée et optimisation",
     "520 joueurs croisés entre l’API MPG et FBref, équipe optimale sous budget."),
    ("app-mpg", "https://mpg-optimizer.streamlit.app", "13_mpg_optimizer", "Application — MPG Optimizer",
     "Composer la meilleure équipe Mon Petit Gazon sous contrainte de budget."),
    ("wc", SITE + "/#wc", "14_world_cup", "World Cup 2026 Predictor : modèle de Poisson",
     "7 952 matchs internationaux pour calibrer le modèle, 2 000 tournois simulés."),
    ("app-world-cup", "https://worldcup-2026-predictor.streamlit.app", "14_world_cup", "Application — World Cup 2026 Predictor",
     "Probabilités de victoire, buteurs et tableau final simulés (modèle de Poisson)."),
    ("github", "https://github.com/Julie-Landrevie", "20_github", "Julie Landrevie — le code de mes projets sur GitHub",
     "Python et R sur données ouvertes, plus de 120 tests."),
    ("notion", "https://notion.so/julie-landrevie", "21_notion", "Julie Landrevie — portfolio détaillé (Notion)",
     "Chaque projet en détail : le besoin, les données, la méthode, les limites."),
]

PAGE = """<!DOCTYPE html>
<html lang="fr">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{title}</title>
<meta name="description" content="{desc}">
<meta property="og:type" content="website">
<meta property="og:title" content="{title}">
<meta property="og:description" content="{desc}">
<meta property="og:url" content="{share}">
<meta property="og:image" content="{image}">
<meta property="og:image:width" content="1200">
<meta property="og:image:height" content="627">
<meta name="twitter:card" content="summary_large_image">
<meta name="author" content="Julie Landrevie">
<meta name="robots" content="noindex">
<link rel="canonical" href="{target}">
<script>location.replace({target_js});</script>
<style>body{{margin:0;font:16px/1.5 Lato,system-ui,sans-serif;background:#f6f1e7;color:#1c1917;display:grid;place-items:center;min-height:100vh}}a{{color:#0d8f84}}</style>
</head>
<body><p><a href="{target}">{title} →</a></p></body>
</html>
"""


def main() -> None:
    out = ROOT / "l"
    out.mkdir(exist_ok=True)
    for name, target, thumb, title, desc in LIENS:
        assert (ROOT / "assets" / "linkedin" / f"{thumb}.png").exists(), thumb
        html = PAGE.format(title=escape(title), desc=escape(desc), share=f"{SITE}/l/{name}.html",
                           image=f"{SITE}/assets/linkedin/{thumb}.png", target=escape(target),
                           target_js='"' + target.replace('"', '') + '"')
        (out / f"{name}.html").write_text(html, encoding="utf-8")
    print(len(LIENS), "pages dans", out)


if __name__ == "__main__":
    main()
