
# Struttura generale del progetto. - dettata da DeepSeek da migliorare e personalizzare su necessità

---

## 🤔 Come pensare a questa struttura (logica di separazione)

Abbiamo diviso il progetto in **3 macro-aree**, che corrispondono ai 3 ruoli del team:

1.  **`/backend`** (Backend + AI)
    - Contiene tutta la "logica nascosta": l'OCR per leggere gli scontrini, l'integrazione con OpenAI, i calcoli di quanto deve pagare ciascuno.
    - Espone le **API** (endpoints) che il frontend chiamerà per ottenere i dati.
    - È completamente indipendente dal frontend; può essere testato e sviluppato separatamente con strumenti come Postman o Swagger (FastAPI lo genera automaticamente).

2.  **`/frontend`** (Frontend + UX)
    - Contiene tutto ciò che l'utente vede e tocca: schermate di login, fotocamera per scansione, dashboard con i debiti.
    - Comunica **solo** con il backend tramite chiamate HTTP (fetch/axios).
    - È pensato per essere **mobile-friendly** (responsive) e veloce.

3.  **`/infra`** (DB + Auth + Deploy)
    - Gestisce l'ambiente di esecuzione: database (Postgres), cache (Redis) e il modo in cui tutto viene messo online.
    - Definendo un `docker-compose.yml`, ogni sviluppatore può avviare l'intero progetto sul proprio PC con un solo comando (`docker-compose up`), senza dover installare Postgres manualmente.

---

## ⚡ Flusso dei dati "visivo"

Per capire come i file dialogano tra loro, segui questo flusso quando l'utente scatta una foto:

1. **Frontend** (`scan/page.tsx`) → invia l'immagine al backend tramite API (`POST /api/receipts/parse`).
2. **Backend** (`api/routes/receipts.py`) → riceve la richiesta e chiama il `services/ocr_service.py`.
3. **Servizio** (`ocr_service.py`) → usa OpenAI/Tesseract per estrarre il testo, poi `parser_service.py` trasforma il testo in una lista di prodotti.
4. **Backend** salva i dati nel database (usando i `models/`) e restituisce il JSON al frontend.
5. **Frontend** mostra la lista dei prodotti all'utente, che li assegna ai coinquilini usando il componente `SplitAssigner.tsx`.
6. **Frontend** invia le assegnazioni al backend (`POST /api/splits/`), che calcola i debiti e li salva nel DB.
7. **Frontend** aggiorna la **Dashboard** (`(dashboard)/page.tsx`) che mostra il nuovo riepilogo debiti.

---


# perse-recepeit - Per il momento Brandon 👺

Io non mi preoccuperei a scrivere tutta la directory di github in inglese. Lo tradurrei alla fine, il codice meglio in inglese sicuramente. Il progetto ha un sacco di cose da fare. Quindi qui teniamo una traccia del da farsi.

- [ ] Fare delle immagini a degli scontrini di cose che si sono comprati per usare Tesseract per estrarre il testo

# - Per il momento Giulio

# - Codice apportato da Bennett

## Come avviare l'infrastruttura

- Creare una copia di .env.example e rinominarla come .env
- Eseguire dalla root del progetto './docker-compose.yml s (s di 'start')'
- Dopo aver verificato che tutto funzioni, eseguire './docker-compose.yml x (oppure stop)'
    per concludere la sessione di utilizzo e cancellare i container

# Cosa fa esattamente il progetto?

Fin dove ho capito, correggetemi se ho capito altro, il progetto cerca prende degli scontrini e analizza ciò che è scritto sopra per dividere il conto pari fra le persone?

## Aggiornamento a che cosa fa

Per spiegarla in poche parole è un app per inquilini dove le persone devono dividere le spese, quindi quando si compra la spesa si fa una foto dello scontrino, si segna con chi si sta dividendo la spesa e l'app in automatico va segnando quanti soldi devi/ti devono.

## L'uso dell IA

Lo limiterei a qualche ricerca e qualche consiglio da "programmatore" con esperienza. Sicuramente vietato per generare codice, bisogna capire cosa stiamo facendo. Anche farsi impostare le cose... io almeno cercherò di cercare dentro qualche libro, video, di fare le somme in autonomia, anche perché l'obiettivo è imparare.
