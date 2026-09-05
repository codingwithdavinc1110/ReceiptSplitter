
# Cose da sapere prima di mettersi ad aggeggiare con il progetto

pip install -r requirements.txt

# Ricordare che

Bisogna entrare nell'ambiente virtuale per poter runnare il codice.
`source .venv/bin/activate` 

Io che ho la riga di comando fish trovo
`source .venv/bin/activate.fish` 

# Checklist 

# Appunti pratici

Per quanto riguarda tesseractOne, la prima versione, il risultato è abbastanza decente. Sicuramente, non so se per il font, o per il formato dell'immagine, non riesce a capire le parole. Ha comunque una lettura decente. Non è ancora testato ancora su scontrino vero (forse viene meglio?)


- [x] Testato su immagine fake, funziona decente.
- [x] Testare su immagini vere 
- [ ] Fare in modo di standardizzare i file, le immagini devono essere tutte jpg

## Ulteriori questioni riguardo la visione delle immagini

Ho notato che laddove si presenta qualcosa del tipo "PRODOTTO"EURO:     "NUMERO" c'è qualche problema di lettura, forse vi si dovrebbe combinare una piccola AI che macini su tanti scontrini così da combinare il suo risultato con quello del tesseract. C'è da dire che forse una sola foto non basta? Forse dovremmo tenere conto di un video da un paio di secondi diviso in molti frame...? C'è da considerare sicuramente che gli utenti non saranno sempre in condizioni ottimali ma ci dobbiamo aspettare che si accenda il flash della fotocamera posteriore per recuperare immagini il più chiare possibili.

Per capire c'è da studiare bene le seguenti righe di codice:

```python
    img = cv2.resize(img, None, fx=4, fy=4, interpolation=cv2.INTER_CUBIC) # Il fattore di moltiplicazione dell'immagine è un x4
    blur = cv2.GaussianBlur(img, (5, 5), 0)
    thresh = cv2.adaptiveThreshold(
        blur, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, 
        cv2.THRESH_BINARY_INV, 11, 2
    ) # questo in caso il testo sia nero su sfondo bianco, (Binarizzazione)
    kernel = np.ones((3, 3), np.uint8) 
    opening = cv2.morphologyEx(thresh, cv2.MORPH_OPEN, kernel, iterations=2) # rimuovi il rumore all'immagine
    return opening
```

# Appunti teorici

Per migliorare l'accuratezza bisgona capire ancora meglio come funziona il pre-processing. Ogni passaggio, sia un po' dal punto di vista teorico che dal punto di vista pratico delle funzioni che vengono usate. 

