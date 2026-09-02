
from PIL import Image
import cv2
import pytesseract

def main():
    # L'immagine giustamente deve essere pre-elaborata
    
    print(pytesseract.image_to_string(Image.open("../images/scontrinoFake.png"),lang='ita'))

if __name__ == "__main__":
    main()   
