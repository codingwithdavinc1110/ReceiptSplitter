
from PIL import Image
import cv2
import pytesseract
import numpy as np

def preprocess_for_tesseract(image_path):
    img = cv2.imread(image_path, 0)
    img = cv2.resize(img, None, fx=4, fy=4, interpolation=cv2.INTER_CUBIC) # Il fattore di moltiplicazione dell'immagine è un x4
    blur = cv2.GaussianBlur(img, (5, 5), 0)
    thresh = cv2.adaptiveThreshold(
        blur, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, 
        cv2.THRESH_BINARY_INV, 11, 2
    ) # questo in caso il testo sia nero su sfondo bianco, (Binarizzazione)
    kernel = np.ones((3, 3), np.uint8) 
    opening = cv2.morphologyEx(thresh, cv2.MORPH_OPEN, kernel, iterations=2) # rimuovi il rumore all'immagine
    return opening

def main():
    with open("../tesseractResult.txt", "w") as file:
        processed_img = preprocess_for_tesseract("../images/scontrinoVero.jpg")
        file.write(pytesseract.image_to_string(processed_img, config='psm--11'))
    
if __name__ == "__main__":
    main()   
