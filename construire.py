"""Fabrique index.html : une page qui ouvre l'application Claude avec la demande déjà écrite.

Le lien claude://code/new?q=… est documenté par Anthropic (support.claude.com, article 14729294) :
il pré-remplit l'onglet Code sans rien envoyer. Pas de paramètre pour le modèle ni l'effort.
On passe par une page https parce qu'Outlook supprime souvent les liens claude:// dans les mails.
Garder le lien encodé sous ~2 000 caractères (limite connue de Windows pour ouvrir une application).

Lancer : python3 construire.py
"""
from html import escape
from pathlib import Path
from urllib.parse import quote

DEMANDE = (
    "Installe proprement sur mon PC GitHub, Git et ce qui peut être utile, au bon endroit. "
    "Connecte mon compte GitHub (pjean-baptiste-hub, déjà connecté dans Edge), accepte mes invitations "
    "en attente et récupère mes dossiers (zita, prepa). "
    "Prépare chaque étape (ouvre les pages, donne-moi le texte prêt à copier-coller) : je n'ai qu'à valider, "
    "je fais moi-même les confirmations et les mots de passe. "
    "Fais une micro-doc. Je ne suis pas du tout technique : parle-moi avec des mots ultra simples, en français, "
    "sans jargon, explique le moins possible, ne m'embrouille pas avec GitHub. "
    "Fais en sorte que tout reste propre, même si mes demandes ne sont pas claires. "
    "N'hésite pas à mettre d'autres projets sur GitHub quand c'est utile, tant que ça me prend zéro temps et "
    "zéro décision ; je comprendrai plus tard, à l'usage. "
    "Synchronise toujours tout automatiquement (un script qui envoie tout tout seul, c'est parfait) : jamais "
    "de branches ni de fusions compliquées, jamais de question là-dessus, et ne me dis pas « j'ai poussé » : "
    "c'est du jargon. "
    "Note ces règles dans tes instructions permanentes pour la suite."
)

LIEN = "claude://code/new?q=" + quote(DEMANDE, safe="")
assert len(LIEN) < 2000, len(LIEN)

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
      <li>Si Claude demande un dossier, choisissez <b>Documents</b>.</li>
      <li>En bas, choisissez <b>Opus 5.5</b> et l'effort <b>High</b>, puis <b>Envoyer</b>.</li>
      <li>Ensuite, répondez <b>Oui</b> ou <b>Autoriser</b> quand Windows ou Claude le demandent, et tapez vous-même vos mots de passe.</li>
    </ol>
  </div>

  <div class="carte">
    <h2>Le bouton ne fait rien ?</h2>
    <p class="apres">Copiez la demande, ouvrez l'application Claude, onglet <b>Code</b>, collez-la, puis Envoyer.</p>
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
print(f"index.html écrit ; lien de {len(LIEN)} caractères")
