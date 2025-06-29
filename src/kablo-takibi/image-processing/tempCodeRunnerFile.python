import os;
import cv2;
import numpy as np;

klasor_yolu = "output"


def get_shape_name(approx):
    sides = len(approx)
    if sides == 3:
        return "Üçgen"
    elif sides == 4:
        # Kare mi dikdörtgen mi?
        x, y, w, h = cv2.boundingRect(approx)
        aspect_ratio = float(w)/h
        if 0.95 < aspect_ratio < 1.05:
            return "Kare"
        else:
            return "Dikdörtgen"
    elif sides == 5:
        return "Beşgen"
    elif sides == 6:
        return "Altıgen"
    elif sides > 6:
        return "Daire"
    else:
        return "Bilinmeyen"

    
for dosya in os.listdir(klasor_yolu):
    if dosya.endswith(".jpg") or dosya.endswith(".png"):
        yol = os.path.join(klasor_yolu, dosya)
        img = cv2.imread(yol)
        if img is None:
            print(f"Yüklenemedi: {dosya}")
            continue
        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        edges = cv2.Canny(gray, 50, 150) # Kenar tespiti
        contours, _ = cv2.findContours(edges, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE) # Kontur bulma
        
        for i, contour in enumerate(contours[:10]): # İlk 10 şekli işle
            approx = cv2.approxPolyDP(contour, 0.04 * cv2.arcLength(contour, True), True)
            shape_name = get_shape_name(approx)
    
            cv2.drawContours(img, [approx], 0, (0, 255, 0), 2) # Şekli çiz ve isim etiketle
            x, y = approx[0][0]
            cv2.putText(img, shape_name, (x, y - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.6, (255, 0, 0), 2)

    # Görüntüyü göster
    cv2.imshow(f"Şekiller - {dosya}", img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
