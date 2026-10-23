"""Fabrique index.html : une page qui ouvre l'application Claude avec la demande déjà écrite.

Les liens claude://cowork/new?q=… et claude://code/new?q=… sont documentés par Anthropic
(support.claude.com, article 14729294) : ils pré-remplissent sans rien envoyer. Pas de paramètre pour le
modèle ni l'effort. Bouton principal : Cowork (choix de Blaise) ; il tourne dans le cloud depuis le
6/10/2026 mais garde la main sur le PC tant que l'application est ouverte (extensions locales, contrôle de
l'écran en bêta). Si Cowork ne peut rien installer, la demande lui fait dire de rouvrir dans l'onglet Code,
qui lance les commandes sur le PC : second bouton.
On passe par une page https parce qu'Outlook supprime souvent les liens claude:// dans les mails.
Garder les liens encodés sous ~2 000 caractères (limite connue de Windows pour ouvrir une application).

Lancer : python3 construire.py
"""
from html import escape
from pathlib import Path
from urllib.parse import quote

DEMANDE = (
    "Installe proprement sur mon PC Git, GitHub et ce qui peut être utile (par le terminal, une extension ou "
    "le contrôle de l'écran). "
    "Connecte mon compte GitHub (pjean-baptiste-hub, déjà connecté dans Edge), accepte mes invitations et "
    "récupère mes dossiers (zita, prepa). "
    "Prépare chaque étape (pages ouvertes, texte prêt à coller) : je ne fais que valider et taper mes mots de passe. "
    "Fais une micro-doc. Je ne suis pas du tout technique : mots ultra simples, en français, sans jargon, "
    "le moins d'explications possible. "
    "Garde tout propre même si mes demandes sont floues ; mets d'autres projets sur GitHub quand c'est utile, "
    "sans me demander de décision. "
    "Synchronise tout automatiquement (un script qui envoie tout seul, c'est parfait), sans branches ni questions, "
    "et ne me dis jamais « j'ai poussé » : c'est du jargon. "
    "Note ces règles dans tes instructions permanentes. "
    "Fais un vrai test de bout en bout, puis dis-moi : « C'est bon, tout marche. Pour essayer, je peux créer ou "
    "modifier n'importe quel site : par exemple renommer vwox.github.io/prepa en "
    "vwox.github.io/prepa-mariage-lagrasse, ou changer sa couleur selon le temps liturgique. » "
    "Si tu ne peux rien installer d'ici, dis-moi en une phrase de rouvrir cette demande dans l'onglet Code."
)

LIEN = "claude://cowork/new?q=" + quote(DEMANDE, safe="")
LIEN_CODE = "claude://code/new?q=" + quote(DEMANDE, safe="")
assert max(len(LIEN), len(LIEN_CODE)) < 2000, (len(LIEN), len(LIEN_CODE))

PAGE = f"""<!doctype html>
<html lang="fr">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<meta name="robots" content="noindex">
<link rel="icon" href="data:,">
<title>Installer GitHub avec Claude</title>
<style>
  :root {{
    --fond: #f7f5f0; --carte: #ffffff; --texte: #1f2328; --doux: #5b6168;
    --accent: #232b5e; --accent-texte: #ffffff; --bord: #e2ded4; --encart: #f1eee6;
  }}
  @media (prefers-color-scheme: dark) {{
    :root {{
      --fond: #15171c; --carte: #1e2128; --texte: #e8e6e1; --doux: #a3a7ad;
      --accent: #c9d1ff; --accent-texte: #15171c; --bord: #33363e; --encart: #262a32;
    }}
  }}
  * {{ box-sizing: border-box; }}
  body {{
    margin: 0; background: var(--fond); color: var(--texte);
    font: 18px/1.55 -apple-system, "Segoe UI", system-ui, Roboto, Arial, sans-serif;
  }}
  main {{ max-width: 640px; margin: 0 auto; padding: 32px 16px 48px; }}
  h1 {{ font-size: 1.6rem; line-height: 1.25; margin: 0 0 8px; }}
  .sous-titre {{ color: var(--doux); margin: 0 0 28px; }}
  .carte {{
    background: var(--carte); border: 1px solid var(--bord); border-radius: 14px;
    padding: 22px 20px; margin-bottom: 20px;
  }}
  .bouton {{
    display: block; text-align: center; text-decoration: none; font-weight: 600;
    background: var(--accent); color: var(--accent-texte); border: 0; border-radius: 12px;
    padding: 18px 16px; font-size: 1.15rem; width: 100%; cursor: pointer;
  }}
  a.bouton.second {{ text-decoration: none; }}
  .bouton.second {{ background: transparent; color: var(--texte); border: 1.5px solid var(--bord); font-size: 1rem; padding: 12px 16px; }}
  ol {{ padding-left: 1.3em; margin: 18px 0 0; }}
  li {{ margin-bottom: 10px; }}
  li:last-child {{ margin-bottom: 0; }}
  h2 {{ font-size: 1.05rem; margin: 0 0 10px; }}
  .demande {{
    background: var(--encart); border-radius: 10px; padding: 14px 16px; margin: 12px 0 14px;
    font-size: 0.95rem; white-space: pre-wrap;
  }}
  .ok {{ color: var(--doux); font-size: 0.95rem; min-height: 1.4em; margin: 8px 0 0; text-align: center; }}
  .apres {{ color: var(--doux); font-size: 0.95rem; margin: 0; }}
</style>
</head>
<body>
<main>
  <h1>Installer GitHub avec Claude</h1>
  <p class="sous-titre">Deux minutes. Claude fait tout, vous validez.</p>

  <div class="carte">
    <a class="bouton" href="{escape(LIEN, quote=True)}">Ouvrir Claude avec la demande prête</a>
    <ol>
      <li>Si Edge demande «&nbsp;Ouvrir Claude&nbsp;?&nbsp;», cliquez <b>Ouvrir</b>.</li>
      <li>En bas, choisissez <b>Opus 5.5</b> et l'effort <b>High</b>, puis <b>Envoyer</b>.</li>
      <li>Ensuite, répondez <b>Oui</b> ou <b>Autoriser</b> quand Windows ou Claude le demandent, et tapez vous-même vos mots de passe.</li>
    </ol>
  </div>

  <div class="carte">
    <h2>Claude dit qu'il ne peut rien installer&nbsp;?</h2>
    <p class="apres">Même demande, dans l'onglet Code de Claude, qui sait installer. Si Claude demande un dossier, choisissez <b>Documents</b>.</p>
    <a class="bouton second" style="margin-top:14px" href="{escape(LIEN_CODE, quote=True)}">Rouvrir dans l'onglet Code</a>
  </div>

  <div class="carte">
    <h2>Aucun bouton ne fait rien&nbsp;?</h2>
    <p class="apres">Copiez la demande, ouvrez l'application Claude, collez-la, puis Envoyer.</p>
    <div class="demande" id="demande">{escape(DEMANDE)}</div>
    <button class="bouton second" id="copier" type="button">Copier la demande</button>
    <p class="ok" id="ok" aria-live="polite"></p>
  </div>
</main>
<script>
  document.getElementById("copier").addEventListener("click", async () => {{
    const texte = document.getElementById("demande").innerText;
    const ok = document.getElementById("ok");
    try {{
      await navigator.clipboard.writeText(texte);
      ok.textContent = "Copié. Collez-le dans Claude.";
    }} catch (e) {{
      const r = document.createRange();
      r.selectNodeContents(document.getElementById("demande"));
      const s = window.getSelection(); s.removeAllRanges(); s.addRange(r);
      ok.textContent = "Texte sélectionné : faites Ctrl+C pour le copier.";
    }}
  }});
</script>
</body>
</html>
"""

Path(__file__).with_name("index.html").write_text(PAGE, encoding="utf-8")
print(f"index.html écrit ; liens de {len(LIEN)} et {len(LIEN_CODE)} caractères")
