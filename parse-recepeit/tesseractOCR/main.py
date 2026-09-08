import easyOCRReader
import findPricesWithRe

def main():
    ocrResult = "../ocrResult.txt"
    reResult = "../reResult.txt"
    easyOCRReader.readImage("../images/scontrinoFake.png", ocrResult)
    findPricesWithRe.findPricesAndStrings(ocrResult, reResult)

if __name__ == "__main__":
    main()