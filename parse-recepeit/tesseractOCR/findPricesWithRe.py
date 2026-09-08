import re

def findPricesAndStrings(textFileInput, textFileOutput):
    """Questa funzione prende la stringa risultante della lettura easyocr e prende soltanto le stringhe utili con prezzi e frasi

    Args:
        textFileInput (txt): Questo è il file di testo dove easyOCR ha fatto la sua lettura
        textFileOutput (txt): Questo è il file dove viene messo l'output
    """
    with open(textFileInput, "r") as file:
        contenuto = file.read()
        pattern_apici = r"'([^']*)'"
        resultRE = re.findall(pattern_apici, contenuto)
        with open(textFileOutput,"w") as writingFile:
            writingFile.write(str(resultRE))
            

