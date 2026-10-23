# demarrer

Page `https://vwox.github.io/demarrer/` : un bouton qui ouvre l'application Claude (onglet Code) avec la demande d'installation de GitHub déjà écrite, et un bouton « Copier » en secours.

- Modifier la demande : changer `DEMANDE` dans `construire.py`, lancer `python3 construire.py`, publier.
- Le lien `claude://code/new?q=…` est documenté par Anthropic (support.claude.com, article 14729294, juin 2026) : il pré-remplit sans envoyer ; rien pour choisir le modèle ou l'effort.
- Onglet Code et non Cowork : depuis le 6/10/2026, Cowork tourne dans le cloud (forfaits Pro et Max) et ne peut rien installer sur le PC.
- Page https plutôt que lien direct dans le mail : Outlook supprime souvent les liens `claude://`. Lien encodé gardé sous 2 000 caractères (limite connue de Windows pour lancer une application).

Créée le 23/10/2026 pour le Père Jean-Baptiste (dossier Zita, `tmp/mails-2010/README.md`).
