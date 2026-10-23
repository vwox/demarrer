# demarrer

Page `https://vwox.github.io/demarrer/` : un bouton qui ouvre l'application Claude (Cowork) avec la demande d'installation de GitHub déjà écrite, un second bouton pour la même demande dans l'onglet Code, et un bouton « Copier » en dernier recours. La demande se termine par un test de bout en bout et une proposition d'essai (renommer la page de la prépa, couleur du temps liturgique).

- Modifier la demande : changer `DEMANDE` dans `construire.py`, lancer `python3 construire.py`, publier.
- Le lien `claude://code/new?q=…` est documenté par Anthropic (support.claude.com, article 14729294, juin 2026) : il pré-remplit sans envoyer ; rien pour choisir le modèle ou l'effort.
- Cowork d'abord (choix de Blaise, 23/10) : depuis le 6/10/2026 il tourne dans le cloud (Pro et Max), mais garde la main sur le PC tant que l'application est ouverte (dossiers, extensions locales, contrôle de l'écran en bêta). Lancer des commandes n'est pas documenté : s'il ne peut rien installer, la demande lui fait dire de rouvrir dans l'onglet Code, qui le peut.
- Page https plutôt que lien direct dans le mail : Outlook supprime souvent les liens `claude://`. Lien encodé gardé sous 2 000 caractères (limite connue de Windows pour lancer une application).

Créée le 23/10/2026 pour le Père Jean-Baptiste (dossier Zita, `tmp/mails-2010/README.md`).
