# -*- coding: utf-8 -*-
"""Génère index.html à partir de contenu.py.  Lancer : python3 build/build.py"""
import html, json, sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent))
from contenu import *  # noqa

RACINE = Path(__file__).resolve().parent.parent
DEMO_LOIS = json.load(open(Path(__file__).parent / "demo_lois.json", encoding="utf-8"))


def t(fr, en, tag="span", cls=""):
    """Un texte dans les deux langues ; la langue inactive est masquée en CSS."""
    c = f' class="{cls}"' if cls else ""
    return f'<{tag}{c} data-l="fr">{fr}</{tag}><{tag}{c} data-l="en" lang="en">{en}</{tag}>'


def tt(paire, tag="span", cls=""):
    return t(paire[0], paire[1], tag, cls)


def esc(s):
    return html.escape(s, quote=True)


import re
def num(v):
    """Un nombre à la française et sa version anglaise (24,8 % -> 24.8% ; 10 075 -> 10,075)."""
    if isinstance(v, tuple):
        return t(esc(v[0]), esc(v[1]), "span", "n")
    en = re.sub(r"(\d),(\d)", r"\1.\2", v)
    en = re.sub(r"(\d) (\d{3})", r"\1,\2", en).replace(" %", "%")
    return t(esc(v), esc(en), "span", "n")


# ---------- compteurs calculés (une seule source) ----------
n_projets = len(PROJETS) + len(AUTRES)
n_tests = sum(TESTS.values())
COMPTEURS = [
    (str(n_projets), ("études détaillées, données et code ouverts", "detailed studies, open data and code")),
    (f"{n_tests // 10 * 10}+", ("tests unitaires sur quatre projets", "unit tests across four projects")),
    ("10 075", ("fichiers GPS de joueuses contrôlés", "GPS files from female players checked")),
    ("4", ("résultats nuls ou contre-intuitifs publiés", "null or counter-intuitive results published")),
]


PANNEAU = ('<div class="panneau" aria-label="Panneau de codage">'
           + t("Structure du panneau de codage", "Coding panel structure", "span", "panneau-titre")
           + '<div class="p-ligne">' + t("Catégories", "Categories", "span", "p-lab")
           + "".join(t(a, b, "span", "tag") for a, b in [("Tir", "Shot"), ("Passe", "Pass"), ("Dribble", "Dribble"), ("Tacle", "Tackle"), ("Interception", "Interception")])
           + '</div><div class="p-ligne">' + t("Sous-critères", "Sub-criteria", "span", "p-lab")
           + "".join(t(a, b, "span", "tag sub") for a, b in [("Zone du terrain", "Pitch zone"), ("Type de passe", "Pass type"), ("Résultat de l\'action", "Outcome")])
           + '</div><div class="p-ligne">' + t("Plan d\'entraînement", "Training plan", "span", "p-lab")
           + "".join(t(a, b, "span", "tag bloc") for a, b in [("Technique", "Technical"), ("Physique", "Physical"), ("Tactique", "Tactical"), ("Mental", "Mental")])
           + "</div></div>")


def visuel(f, cfr, cen):
    return (f'<figure><a href="assets/{f}" target="_blank" rel="noopener"><img src="assets/{f}" alt="{esc(cfr)}" loading="lazy"></a>'
            f'<figcaption>{t(esc(cfr), esc(cen))}</figcaption></figure>')


def carte_projet(p):
    portes = " ".join(p["portes"])
    ordre = " ".join(f'data-o-{k}="{v}"' for k, v in p["ordre"].items())
    stack_en = p.get("stack_en", p["stack"])
    chips = "".join(t(esc(a), esc(b), "span", "chip") for a, b in zip(p["stack"], stack_en))
    chiffres = "".join(
        f'<div class="fig"><b>{num(v)}</b>{t(esc(d[0]), esc(d[1]), "span")}</div>' for v, d in p["chiffres"])
    corps = ""
    for i, s in enumerate(p["sections"]):
        corps += f'<section class="bloc"><h4>{tt(s["titre"])}</h4>'
        corps += t("".join(f"<p>{x}</p>" for x in s["texte"][0]), "".join(f"<p>{x}</p>" for x in s["texte"][1]), "div")
        if p.get("panneau") is not None and i == (p["panneau"] if isinstance(p["panneau"], int) and p["panneau"] is not True else 0):
            corps += PANNEAU
            if p.get("youtube"):
                corps += (f'<div class="video"><iframe src="https://www.youtube-nocookie.com/embed/{p["youtube"]}" title="Vidéo Dartfish" '
                          'loading="lazy" allow="encrypted-media; picture-in-picture" allowfullscreen></iframe></div>')
        if s["visuels"]:
            cls = "galerie" + (" seule" if len(s["visuels"]) == 1 else "")
            corps += f'<div class="{cls}">' + "".join(visuel(*v) for v in s["visuels"]) + "</div>"
        corps += "</section>"
    demo = DEMOS.get(p.get("demo"), "")
    liens = "".join(f'<a href="{u}" target="_blank" rel="noopener">{t(esc(a), esc(b))}</a>' for a, b, u in p["liens"])
    return f'''
<article class="projet" id="{p["id"]}" data-portes="{portes}" {ordre}>
  <div class="projet-tete">
    <span class="kicker">{p["annee"]}</span>
    <h3>{tt(p["titre"])}</h3>
    <p class="question">{tt(p["question"])}</p>
  </div>
  <div class="figs">{chiffres}</div>
  <details>
    <summary>{t("Lire l\'étude", "Read the study")}</summary>
    <div class="etude">
      {corps}
      {demo}
      <div class="limites"><strong>{t("Ce que l\'étude ne permet pas de conclure", "What this study cannot conclude")}</strong>{tt(p["limites"], "p")}</div>
    </div>
  </details>
  <div class="pied-projet"><div class="chips">{chips}</div><div class="liens">{liens}</div></div>
</article>'''


# ---------- démos ----------
def ordinal(n):
    suf = "th" if 10 <= n % 100 <= 20 else {1: "st", 2: "nd", 3: "rd"}.get(n % 10, "th")
    return f"{n}{suf}"

A19 = [("Course à haute vitesse", "High-speed running", 56, 35),
       ("Distance de sprint", "Sprint distance", 24, 52),
       ("Nombre de sprints", "Number of sprints", 19, 71),
       ("Accélérations hautes", "High accelerations", 11, 3),
       ("Décélérations hautes", "High decelerations", 49, 48)]
lignes = "".join(
    f'<div class="a19-l{" accent" if i == 2 else ""}" data-h="{h}" data-f="{f}">'
    f'<span class="a19-nom">{t(fr, en)}</span>'
    f'<span class="a19-piste"><span class="a19-ref" style="left:{h}%"></span><span class="a19-pt" style="left:{f}%"></span></span>'
    f'<span class="a19-v">{t(f"{f}e", ordinal(f))}</span></div>'
    for i, (fr, en, h, f) in enumerate(A19))
DEMO_A19 = f'''
<div class="demo" id="demo-a19">
  <div class="demo-tete"><strong>{t("Démo : la joueuse A-19 selon les seuils", "Demo: player A-19 under each threshold")}</strong>
    <div class="bascule" role="group" aria-label="Seuils">
      <button type="button" data-seuil="h" aria-pressed="false">{t("Seuils masculins", "Men's thresholds")}</button>
      <button type="button" data-seuil="f" aria-pressed="true">{t("Seuils féminins", "Women's thresholds")}</button>
    </div></div>
  <p class="demo-sous">{t("Percentile parmi 63 joueuses de champ, moyenne par séance sur 63 séances GPS. Repère gris : l'autre jeu de seuils.",
                           "Percentile among 63 outfield players, per-session average over 63 GPS sessions. Grey mark: the other set of thresholds.")}</p>
  <div class="a19">{lignes}</div>
  <p class="demo-note">{t("Ses sprints entre 23 et 25 km/h existent : le seuil de 25 km/h les effaçait. Ses accélérations hautes restent basses : une question à vérifier en vidéo, pas un diagnostic.",
                           "Her sprints between 23 and 25 km/h exist: the 25 km/h threshold erased them. Her high accelerations stay low: a question to check on video, not a diagnosis.")}</p>
</div>'''

barres = [(("Réponses exactes", "Correct answers"), [75, 81, 94]),
          (("Réponses fausses", "Wrong answers"), [22, 0, 0]),
          (("Refus à tort", "Wrong refusals"), [3, 19, 3])]
versions = [("Sans document", "No document"), ("RAG v1", "RAG v1"), ("RAG v2", "RAG v2")]
graph = ""
for (lab, vals) in barres:
    graph += f'<div class="bg-groupe"><span class="bg-lab">{tt(lab)}</span>'
    for i, v in enumerate(vals):
        cls = "bg-b" + (" accent" if (lab[0] == "Réponses exactes" and i == 2) else (" ref" if i == 0 else ""))
        graph += (f'<div class="bg-l"><span class="bg-v">{tt(versions[i])}</span>'
                  f'<span class="bg-piste"><span class="{cls}" style="width:{max(v, 0.6)}%"></span></span>'
                  f'<span class="bg-n">{num(str(v) + " %")}</span></div>')
    graph += "</div>"
onglets = "".join(f'<button type="button" data-q="{k}" aria-pressed="{"true" if i == 0 else "false"}">{t(d["court_fr"], d["court_en"])}</button>'
                  for i, (k, d) in enumerate(DEMO_LOIS.items()))
panneaux = ""
for i, (k, d) in enumerate(DEMO_LOIS.items()):
    panneaux += f'''<div class="q-panneau" data-q="{k}"{"" if i == 0 else " hidden"}>
  <p class="q-question">{t(esc(d["question"]), esc(d["question_en"]))}</p>
  <div class="q-reps">
    <div class="q-rep faux"><span class="q-tag">{t("Sans le livret · fausse", "Without the booklet · wrong")}</span>{t(esc(d["sans"]), esc(d["sans_en"]), "p")}</div>
    <div class="q-rep juste"><span class="q-tag">{t("Avec le livret (v2) · exacte", "With the booklet (v2) · correct")}</span>{t(esc(d["avec"]), esc(d["avec_en"]), "p")}</div>
  </div>
  <p class="q-ref">{t("Référence : " + esc(d["ref"]), "Reference: " + esc(d["ref_en"]))}</p>
</div>'''
DEMO_LOIS_HTML = f'''
<div class="demo" id="demo-lois">
  <div class="demo-tete"><strong>{t("Résultats sur 40 questions", "Results on 40 questions")}</strong></div>
  <div class="bargraph">{graph}</div>
  <div class="demo-tete demo-tete2"><strong>{t("Démo : trois questions, sans puis avec le livret", "Demo: three questions, without then with the booklet")}</strong>
    <div class="bascule onglets" role="group">{onglets}</div></div>
  {panneaux}
  <p class="demo-note">{t("Réponses réelles du modèle (mistral-large-4), enregistrées pendant l'évaluation : aucun appel n'est fait depuis cette page.",
                           "Real model answers (mistral-large-4) recorded during the evaluation, translated from French: this page makes no live call.")}</p>
</div>'''
DEMOS = {"a19": DEMO_A19, "lois": DEMO_LOIS_HTML}

# ---------- sections ----------
portes_html = ""
for cle in ("performance", "data-ia"):
    p = PORTES[cle]
    portes_html += f'''<a class="porte" href="#{cle}" data-porte="{cle}">
  <span class="kicker">{t("Dossier", "Track")}</span>
  <span class="porte-titre">{tt(p["titre"])}</span>
  <span class="porte-texte">{tt(p["texte"])}</span>
  <span class="porte-cta">{t("Voir les projets →", "See the projects →")}</span></a>'''

roles = "".join(f'<p class="role" data-role="{k}">{tt(v["role"])}</p>' for k, v in PORTES.items())
compteurs = "".join(f'<div><b>{num(v)}</b>{t(esc(d[0]), esc(d[1]))}</div>' for v, d in COMPTEURS)
methode = "".join(f'<li><strong>{tt(a)}</strong>{tt(b)}</li>' for a, b in METHODE)
projets = "".join(carte_projet(p) for p in PROJETS)
autres = "".join(f'<article class="mini"><h4>{tt(a)}</h4>{tt(b, "p")}<a href="{u}" target="_blank" rel="noopener">{t("Application ↗", "App ↗")}</a></article>'
                 for a, b, u in AUTRES)
nuls = "".join(f'<li><a class="nul-lien" href="#{pid}"><strong>{tt(a)}</strong></a>{tt(b, "p")}</li>' for a, b, pid in NULS)
preuves = "".join(
    f'<tr><td class="num">{num(v)}</td><td>{tt(d)}</td><td><a href="#{pid}">{pid}</a></td>'
    f'<td><a href="{u}" target="_blank" rel="noopener">{esc(f)} ↗</a></td></tr>'
    for v, d, pid, u, f in PREUVES)
glossaire = "".join(f'<div class="g-item"><dt>{esc(m)}</dt><dd>{tt(d)}</dd></div>' for m, d in GLOSSAIRE)
exp = "".join(f'<li><strong>{tt(a)}</strong> <span class="date">{d}{t("aujourd’hui", "present")}</span>{tt(b, "p")}</li>'
              for a, d, b in PARCOURS["experience"])
form = "".join(f'<li><span class="date">{a}</span> {tt(b)}</li>' for a, b in PARCOURS["formation"])
outils = "".join(f"<li>{tt(x)}</li>" for x in PARCOURS["outils"])
langues = "".join(f"<li>{tt(x)}</li>" for x in PARCOURS["langues"])

page = (RACINE / "build" / "gabarit.html").read_text(encoding="utf-8")
for cle, val in dict(ROLES=roles, PORTES=portes_html, COMPTEURS=compteurs, METHODE=methode, PROJETS=projets,
                     NULS=nuls, PREUVES=preuves, GLOSSAIRE=glossaire, EXP=exp, FORM=form,
                     OUTILS=outils, LANGUES=langues, EMAIL=PROFIL["email"], LINKEDIN=PROFIL["linkedin"],
                     GITHUB=PROFIL["github"], NPROJ=str(n_projets)).items():
    page = page.replace("{{" + cle + "}}", val)
# Apostrophes typographiques dans le texte (pas dans les attributs ni le script).
morceaux = re.split(r"(<script>.*?</script>)", page, flags=re.S)
page = "".join(m if m.startswith("<script>") else
               re.sub(r">([^<]*)<", lambda x: ">" + x.group(1).replace("&#x27;", "’").replace("'", "’") + "<", m)
               for m in morceaux)
assert "{{" not in page, page[page.index("{{"):page.index("{{") + 40]
(RACINE / "index.html").write_text(page, encoding="utf-8")
print("index.html :", len(page) // 1024, "Ko ;", n_projets, "projets ;", n_tests, "tests")
