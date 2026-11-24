# -*- coding: utf-8 -*-
"""Contenu du site, en français et en anglais.
Les compteurs du haut de page sont calculés à partir de ces données (build.py),
pour qu'un chiffre ne puisse pas se contredire d'une section à l'autre."""

GH = "https://github.com/Julie-Landrevie"

PROFIL = dict(
    nom="Julie Landrevie",
    email="julie.landrevie@free.fr",
    linkedin="https://www.linkedin.com/in/julie-landrevie/",
    github=GH,
)

# Portes d'entrée : le rôle affiché et l'accroche changent selon la porte choisie.
PORTES = {
    "tout": dict(
        role=("Ingénieure data · performance et IA appliquées au football",
              "Data engineer · performance and AI applied to football"),
    ),
    "performance": dict(
        titre=("Performance & football féminin", "Performance & women's football"),
        texte=("Suivi de charge, seuils adaptés aux joueuses, analyse vidéo : des indicateurs qu'un staff peut lire et utiliser.",
               "Load monitoring, thresholds fitted to female players, video analysis: indicators a staff can read and use."),
        role=("Data & performance · football féminin",
              "Data & performance · women's football"),
    ),
    "data-ia": dict(
        titre=("Data & IA", "Data & AI"),
        texte=("Pipelines de données contrôlés, assistant d'IA générative évalué, code testé : la rigueur d'une ingénieure appliquée au sport.",
               "Quality-checked data pipelines, an evaluated generative-AI assistant, tested code: engineering rigour applied to sport."),
        role=("Ingénieure data · Python, SQL & IA générative",
              "Data engineer · Python, SQL & generative AI"),
    ),
}

METHODE = [
    (("Vérifier", "Check"),
     ("Complétude, doublons, valeurs impossibles. Rien n'est corrigé en silence.",
      "Completeness, duplicates, impossible values. Nothing is silently fixed.")),
    (("Mesurer", "Measure"),
     ("Des indicateurs définis avant de regarder les résultats, et une référence pour comparer.",
      "Indicators defined before looking at results, and a baseline to compare with.")),
    (("Localiser", "Locate"),
     ("Trouver le maillon faible : la donnée, le calcul, la recherche ou le modèle.",
      "Find the weak link: the data, the computation, the retrieval or the model.")),
    (("Corriger et remesurer", "Fix and re-measure"),
     ("Une correction ciblée, la même mesure, et des limites écrites noir sur blanc.",
      "One targeted fix, the same measurement, and limits written down.")),
]

from projets import PROJETS, AUTRES  # noqa: E402

TESTS = {"mpg-optimizer": 33, "etudes-football-feminin": 19, "vestiaire-metrics": 21, "pass-network": 18, "lois-du-jeu-ia": 17,
         "womens-football-opportunity": 12}

NULS = [
    (("Le wellness n'anticipe pas les blessures déclarées", "Wellness does not anticipate reported injuries"),
     ("Sur 155 épisodes, l'ACWR médian monte à peine avant la déclaration (≈ 0,95 → 1,07) et le wellness ne baisse pas. Je ne vends pas de « prédiction des blessures ».",
      "Across 155 episodes, the median ACWR barely rises before the report (≈ 0.95 → 1.07) and wellness does not drop. I do not sell “injury prediction”."),
     "charge"),
    (("Le juge automatique s'est trompé 3 fois sur 3", "The automatic judge was wrong 3 times out of 3"),
     ("Les trois réponses qu'il jugeait fausses étaient justes ; l'une révélait même une erreur dans la réponse de référence.",
      "The three answers it marked wrong were right; one even revealed an error in the reference answer."),
     "lois"),
    (("Les seuils féminins changent peu le classement", "Women's thresholds barely change the ranking"),
     ("Corrélation de rang de 0,96 : le gain est dans le profil de chaque joueuse, pas dans la hiérarchie de l'effectif.",
      "Rank correlation of 0.96: the gain is in each player's profile, not in the squad hierarchy."),
     "vestiaire"),
    (("La charge ressentie seule rate les pics GPS", "Perceived load alone misses GPS peaks"),
     ("Dans 92 % des pics de course à haute intensité, l'ACWR sur la charge ressentie reste sous le seuil.",
      "In 92% of high-speed running peaks, the perceived-load ACWR stays below the threshold."),
     "charge"),
    (("Phases arrêtées : aucune différence entre femmes et hommes", "Set pieces: no difference between women and men"),
     ("39,8 % du xG des deux côtés, écart 0,0 point [−1,3 ; +1,3] sur 2 861 matchs. L'idée reçue ne tient pas.",
      "39.8% of xG on both sides, a 0.0-point gap [−1.3; +1.3] over 2,861 matches. The common belief does not hold."), "phases-arretees"),
    (("Penalties : même réussite chez les femmes et les hommes", "Penalties: same conversion for women and men"),
     ("76,2 % contre 75,1 %, écart non significatif. Il faudrait environ 1 070 penalties par groupe pour détecter 5 points.",
      "76.2% against 75.1%, a non-significant gap. About 1,070 penalties per group would be needed to detect 5 points."), "penalties"),
    (("L'ajustement aux adversaires ne change rien", "Adjusting for opponents changes nothing"),
     ("Au plus 2 joueuses bougent de 20 points de percentile, même en Serie A, au calendrier déséquilibré. Je ne le mets pas en avant.",
      "At most 2 players move by 20 percentile points, even in Serie A with its unbalanced schedule. I do not promote it."), "opportunites"),
]

PREUVES = [
    ("22 % → 0", ("réponses fausses sans / avec le livret", "wrong answers without / with the booklet"), "lois", GH + "/lois-du-jeu-ia/blob/main/outputs/comparaison.md", "outputs/comparaison.md"),
    ("94 %", ("réponses exactes, version 2", "correct answers, version 2"), "lois", GH + "/lois-du-jeu-ia/blob/main/outputs/comparaison.md", "outputs/comparaison.md"),
    ("98 %", ("ACWR recalculé fidèle à la source", "recomputed ACWR matches the source"), "charge", GH + "/womens-football-load-monitoring#résultats-sur-soccermon-50-joueuses-2-équipes-20202021", "README, Résultats"),
    ("13–16", ("épisodes d'alerte par joueuse et par an", "alert episodes per player per year"), "charge", GH + "/womens-football-load-monitoring#résultats-sur-soccermon-50-joueuses-2-équipes-20202021", "README, Résultats"),
    ("43 → 15 %", ("séances de match sans sprint", "match sessions with no sprint"), "vestiaire", GH + "/vestiaire-metrics#résultats-sur-soccermon", "README, Résultats"),
    ("0,96", ("corrélation de rang entre seuils", "rank correlation between thresholds"), "vestiaire", GH + "/vestiaire-metrics#résultats-sur-soccermon", "README, Résultats"),
    ("520", ("joueurs croisés MPG × FBref", "players matched MPG × FBref"), "mpg", GH + "/mpg-optimizer", "README"),
    ("24,8 %", ("chances de titre de l'Espagne selon le modèle", "Spain's title chance per the model"), "wc", GH + "/world-cup-predictor", "README"),
    ("39,8 %", ("Part du xG hors penalty née des phases arrêtées jouées dans la moitié adverse, femmes et hommes", "Share of non-penalty xG from set pieces taken in the opponent's half, women and men"),
     "phases-arretees", "https://github.com/Julie-Landrevie/etudes-football-feminin/blob/main/resultats/etude2_differences.csv", "etude2_differences.csv"),
    ("46,9 %", ("Même mesure à la Coupe du monde féminine 2023, la plus élevée des compétitions féminines", "Same measure at the 2023 Women's World Cup, the highest of the women's competitions"),
     "phases-arretees", "https://github.com/Julie-Landrevie/etudes-football-feminin/blob/main/resultats/etude2_par_competition.csv", "etude2_par_competition.csv"),
    ("60,9 %", ("Réussite des penalties féminins en séance de tirs au but (87), contre 76,2 % en match", "Women's penalty conversion in shootouts (87), against 76.2% in matches"),
     "penalties", "https://github.com/Julie-Landrevie/etudes-football-feminin/blob/main/resultats/etude3_reussite.csv", "etude3_reussite.csv"),
    ("22 / 24", ("Statistiques par 90 min fiables sur une saison de WSL (fiabilité ≥ 0,7)", "Per-90 statistics reliable over a WSL season (reliability ≥ 0.7)"),
     "fiabilite", "https://github.com/Julie-Landrevie/etudes-football-feminin/blob/main/resultats/etude1_fiabilite.csv", "etude1_fiabilite.csv"),
    ("2 026 min", ("Minutes pour que les contres deviennent une statistique fiable en WSL", "Minutes for blocks to become a reliable statistic in the WSL"),
     "fiabilite", "https://github.com/Julie-Landrevie/etudes-football-feminin/blob/main/resultats/etude1_fiabilite.csv", "etude1_fiabilite.csv"),
    ("×1,33", ("Pressions par minute d'une remplaçante, comparée à elle-même titulaire sur la même fenêtre de match", "Pressures per minute for a substitute, compared with herself as a starter over the same match window"),
     "opportunites", GH + "/womens-football-opportunity/blob/main/outputs/comparaison/tables/meme_fenetre.csv", "meme_fenetre.csv"),
    ("34 %", ("Joueuses qui changent d'au moins 20 points de percentile en pressions, du par 90 au par possession adverse", "Players moving by at least 20 percentile points in pressures, from per 90 to per opponent possession"),
     "opportunites", GH + "/womens-football-opportunity/blob/main/outputs/comparaison/tables/deplacements_4_ligues.csv", "deplacements_4_ligues.csv"),
]

GLOSSAIRE = [
    ("ACWR", ("Rapport entre la charge des 7 derniers jours et celle des 28 derniers. Un repère de progressivité, pas un prédicteur de blessure.",
              "Ratio of the last 7 days' load to the last 28 days'. A guide to progression, not an injury predictor.")),
    ("EWMA", ("Moyenne mobile qui donne plus de poids aux jours récents ; utilisée pour lisser la charge aiguë et chronique.",
              "Moving average giving more weight to recent days; used to smooth acute and chronic load.")),
    ("sRPE", ("Charge ressentie : effort perçu sur 10 multiplié par la durée de la séance en minutes.",
              "Session RPE: perceived effort out of 10 times session duration in minutes.")),
    ("Wellness", ("Questionnaire quotidien (fatigue, sommeil, douleurs, stress, humeur), comparé à la moyenne habituelle de chaque joueuse.",
                  "Daily questionnaire (fatigue, sleep, soreness, stress, mood), compared with each player's usual level.")),
    ("Monotonie", ("Charge moyenne de la semaine divisée par sa variabilité : une semaine sans variation est monotone.",
                   "Weekly mean load divided by its variability: a week with no variation is monotonous.")),
    ("Épisode d'alerte", ("Jours d'alerte consécutifs regroupés en un seul signal, pour qu'un staff lise un épisode et non dix jours.",
                          "Consecutive alert days grouped into one signal, so a staff reads one episode, not ten days.")),
    ("Seuils féminins", ("Vitesses et accélérations adaptées aux joueuses (sprint au-delà de 23 km/h chez SkillCorner, contre 25 km/h chez les hommes).",
                         "Speed and acceleration thresholds fitted to female players (sprint above 23 km/h for SkillCorner, vs 25 km/h for men).")),
    ("Percentile", ("Rang sur 100 : au 71e percentile, une joueuse fait mieux que 71 % du groupe.",
                    "Rank out of 100: at the 71st percentile a player does better than 71% of the group.")),
    ("Corrélation de rang", ("Mesure si deux classements se ressemblent : 1 = identiques, 0 = sans lien.",
                             "Measures how similar two rankings are: 1 = identical, 0 = unrelated.")),
    ("RAG", ("Génération augmentée par recherche : on cherche d'abord les passages utiles d'un document, puis le modèle répond à partir de ces passages.",
             "Retrieval-augmented generation: first retrieve the useful passages of a document, then the model answers from them.")),
    ("BM25", ("Méthode de recherche par mots-clés qui pondère chaque mot selon sa rareté ; simple et explicable.",
              "Keyword search that weights each word by its rarity; simple and explainable.")),
    ("Rappel de la recherche", ("Part des questions pour lesquelles le bon passage figure parmi ceux retrouvés.",
                                "Share of questions where the right passage is among those retrieved.")),
    ("Juge automatique", ("Second appel à un modèle de langage pour noter une réponse ; utile à grande échelle, à contrôler par relecture.",
                          "A second language-model call that grades an answer; useful at scale, to be checked by review.")),
    ("xG", ("Buts attendus : probabilité qu'un tir devienne un but, selon sa position et sa situation.",
            "Expected goals: probability that a shot becomes a goal, given its position and situation.")),
    ("Modèle de Poisson", ("Modèle qui estime la probabilité de marquer 0, 1, 2… buts à partir de la force des équipes.",
                           "Model estimating the probability of scoring 0, 1, 2… goals from team strength.")),
    ("Tests unitaires", ("Petits programmes qui vérifient automatiquement que le code donne le résultat attendu.",
                         "Small programs that automatically check the code returns the expected result.")),
]

PARCOURS = dict(
    experience=[
        (("Consultante data — cabinet de conseil (CDI)", "Data consultant — consulting firm (permanent)"), "2022 – " ,
         ("Indicateurs, tableaux de bord d'aide à la décision (SQL, Power BI) pour des équipes non techniques ; mission pour le Comité d'Organisation des Jeux Olympiques Paris 2024.",
          "KPIs and decision dashboards (SQL, Power BI) for non-technical teams; assignment for the Paris 2024 Olympic Organising Committee.")),
        (("Joueuse et coach de football féminin — France et Canada", "Women's football player and coach — France and Canada"), "2008 – ",
         ("Plus de 10 ans de compétition et coaching d'équipes universitaires féminines.",
          "10+ years of competitive play and coaching university women's teams.")),
    ],
    formation=[
        ("2025", ("DU Expertiser la performance sportive par l'analyse vidéo et le sport data science, Université de Lorraine",
                  "University diploma in video analysis and sport data science, Université de Lorraine")),
        ("2024", ("Sports Analytics, Université du Michigan (Coursera)", "Sports Analytics, University of Michigan (Coursera)")),
        ("2022", ("Ingénieure ENTPE, double diplôme Polytechnique Montréal", "Engineering degree, ENTPE, double degree with Polytechnique Montréal")),
    ],
    outils=[("Python (pandas, NumPy, SciPy, Streamlit, mplsoccer), SQL", "Python (pandas, NumPy, SciPy, Streamlit, mplsoccer), SQL"),
            ("R (tidyverse, arrow, ggplot2, R Markdown)", "R (tidyverse, arrow, ggplot2, R Markdown)"),
            ("IA générative : RAG, API de modèles de langage, évaluation", "Generative AI: RAG, language-model APIs, evaluation"),
            ("Power BI, Git, tests unitaires", "Power BI, Git, unit tests"),
            ("Dartfish et Once Sport (certifiée)", "Dartfish and Once Sport (certified)")],
    langues=[("Français, langue maternelle", "French, native"), ("Anglais C1 (TOEIC 895)", "English C1 (TOEIC 895)"), ("Espagnol B2", "Spanish B2")],
)
