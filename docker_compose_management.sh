#!/usr/bin/env bash

# set=impostazioni shell
# -euo: e=exit on error, u=unset variables as errors
# o pipefail=ritorna l'ultimo risultato di esecuzione di un comando diverso da zero invece
# che il risultato dell'ultimo comando in assoluto
set -euo pipefail

# argomento da inserire durante l'invocazione 
# se non verranno introdotti argomenti lo script segnalerà un errore e non
# si bloccherà oppure non terminerà come se l'esecuzione fosse
# stata un successo
option=${1:-}

case "$option" in
    # pattern di input per i vari comandi
    [sS]|[sS][tT][aA][rR][tT])
        docker compose \
            --env-file ./infra/.env \
            --file ./infra/docker-compose.yml \
            up
        ;; # termine script (exit $0)
    [iI]|[iI][nN][sS][pP][eE][cC][tT][iI][oO][nN])
        # Ispeziona stato, log e raggiungibilità di Postgres e Redis
        set -a # -a=auto-export esportazione dei valori letti
                # successivamente con source
        source ./infra/.env
        set +a
        docker compose --env-file ./infra/.env --file ./infra/docker-compose.yml up -d
	    docker compose --env-file ./infra/.env --file ./infra/docker-compose.yml ps
	    docker compose --env-file ./infra/.env --file ./infra/docker-compose.yml logs db
	    docker compose --env-file ./infra/.env --file ./infra/docker-compose.yml exec db \
		pg_isready -U "$POSTGRES_USER" -d "$POSTGRES_DB"
	    docker compose --env-file ./infra/.env --file ./infra/docker-compose.yml logs redis
	    docker compose --env-file ./infra/.env --file ./infra/docker-compose.yml exec redis \
		redis-cli -a "$REDIS_PASSWORD" --no-auth-warning ping
        ;;
        # per verificare personalmente crea un file temporaneo con 
        # l'operatore di sovrascrittura e cerca con ctrl+f o grep se sei
        # un complessato i seguenti log
        #
        # infra-db-1 Running
        # infra-redis-1 Running
        # PONG (l'equivalente di $0 per redis-cli ping)

    [xX]|[sS][tT][oO][pP])
        docker compose \
            --env-file ./infra/.env \
            --file ./infra/docker-compose.yml \
            down
        ;;
    
    [hH]|[hH][eE][lL][pP])
        echo "start: avvia docker e istanze container"
        echo "inspection: verifica che i container del progetto siano funzionanti"
        echo "stop: elimina container e disattiva docker"
        echo "help: mostra questo messaggio"
        ;;
    *)
        echo "Uso: $0 {start|stop|help}"
        exit 1
        ;;
esac