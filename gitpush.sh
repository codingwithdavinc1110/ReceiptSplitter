#!/usr/bin/env bash

# ==== ATTENZIONE ====
# Creare una nuova branch:
# git switch -c nome_ramo
# Oppure selezionare una branch esistente:
# git switch nome_ramo
# Poi, dopo aver apportato modifiche e/o implementazioni eseguire semplicemente:
# ./gitpush.sh

# set=shell settings
# -euo: e=exit on error, u=unset variables as errors
# o pipefail=returns the last comand execution with a
# value different than 0 instead of the last script command
set -euo pipefail

# Usa sempre il ramo attualmente selezionato.
BRANCH="$(git branch --show-current)"

if [ -z "$BRANCH" ]; then
    echo "Errore: non sei su una branch (forse sei in detached HEAD)."
    exit 1
fi

if [ "$BRANCH" = "main" ]; then
    echo "Errore: crea o seleziona una branch dedicata prima di procedere."
    exit 1
fi

while true; do
    # -rp: r=escape disabled, p=prompt
    read -rp "Messaggio di commit: " commit_msg

    # -z: z=no text submitted
    if [ -z "$commit_msg" ]; then
        echo "Il messaggio non può essere vuoto."
        continue
    fi

    read -rp "Confermi il messaggio: \"$commit_msg\"? [s/N] " confirm
    case "$confirm" in
        # input cases
        [sS]|[sS][iI]|[yY]|[yY][eE][sS])
            break
            ;;
        *)
            echo "Ok, reinserisci il messaggio."
            ;;
    esac
done

git add .
git commit -m "$commit_msg"
git push -u origin "$BRANCH"