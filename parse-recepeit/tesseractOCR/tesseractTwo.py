from PIL import Image
import cv2
import pytesseract
import numpy as np


def preprocess_for_tesseract(image_path):
    
    img = cv2.imread(image_path, 0)
    
    norm_img = np.zeros((img.shape[0], img.shape[1]))
    img = cv2.normalize(img, norm_img, 0, 255, cv2.NORM_MINMAX)
    img = deskew(img)

    img = cv2.resize(
        img, None, fx=4, fy=4, interpolation=cv2.INTER_CUBIC
    )  # Il fattore di moltiplicazione dell'immagine è un x4
    blur = cv2.GaussianBlur(img, (5, 5), 0)
    thresh = cv2.adaptiveThreshold(
        blur, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY_INV, 11, 2
    )  # questo in caso il testo sia nero su sfondo bianco, (Binarizzazione)
    img = remove_noise(img)  
    img = get_grayscale(img) 
    img = thresholding(img)
    
    return img


def main():
    with open("../tesseractResult.txt", "w") as file:
        processed_img = preprocess_for_tesseract("../images/scontrinoVero.jpg")
        file.write(pytesseract.image_to_string(processed_img, config="psm--11"))

def thresholding(image):
    return cv2.threshold(image, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU) [1]

def get_grayscale(image):
    return cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

def remove_noise(image):
    return cv2.fastNlMeansDenoisingColored(image, None, 10, 10, 7, 15)

def deskew(image):
    co_ords = np.column_stack(np.where(image > 0))
    angle = cv2.minAreaRect(co_ords)[-1]
    if angle < -45:
        angle = -(90 + angle)
    else:
        angle = -angle
    h, w = image.shape[:2]
    center = (w // 2, h // 2)
    M = cv2.getRotationMatrix2D(center, angle, 1.0)
    rotated = cv2.warpAffine(
        image, M, (w, h), flags=cv2.INTER_CUBIC, borderMode=cv2.BORDER_REPLICATE
    )
    return rotated  


if __name__ == "__main__":
    main()
