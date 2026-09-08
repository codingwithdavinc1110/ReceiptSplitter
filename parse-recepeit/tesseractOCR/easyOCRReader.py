import easyocr

def readImage(imageFileInput, textFileOutput):
    """Questa è una funzione che usa easyocr per leggere uno scontrino e scrivere il risultato in un file txt

    Args:
        imageFileInput (jpg): Questa è l'immagine che deve essere letta
        textFileOutput (txt): Questo è file dove va il risultato
    """
    reader = easyocr.Reader(['it']) 
    result = reader.readtext(imageFileInput)
    with open(textFileOutput, "w") as file:
        contenuto = file.write(str(result))