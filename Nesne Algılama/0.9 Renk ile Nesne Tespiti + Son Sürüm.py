#Renk ile Nesne Tespiti
"""
-Belirli renklerde bulunan nesnelerin tespitinin nasıl yapılacağını kontur
bulma yöntemi ile öğrenilmektedir.

-Kontur basitçe, aynı renk veya yoğunluğa sahip tüm sürekli noktaları birleştiren
bir eğri olarak açıklanabilir.

-Konturlar, şekil analizi ve nesne algılama ve tanıma için kullanışlı bir araçtır.
"""
import numpy as np
import cv2
from collections import deque

"""
Kodlama kısmında renklerin rgb'den hsv formatına çevirecez
HSV: 
Hue -> Renk özü anlamına gelmektedir.
Saturation -> Doygunluk Kavramı
Value -> Parlaklık kavramı
"""

# Nesne merkezini depolayacak veri tipi
tampon_bolge = 15
noktalar = deque(maxlen=tampon_bolge)

# Mavi rengin HSV formatındaki aralığı
blueLow = (100, 150, 50)  # daha iyi sonuç için önerilen değer
blueUpper = (140, 255, 255)

# Kamera başlatma
capture = cv2.VideoCapture(0)
if not capture.isOpened():
    print("Kamera açılamadı.")
    exit()

# Kamera çözünürlüğü
capture.set(3, 960)
capture.set(4, 480)

while True:
    success, read = capture.read()

    if success:
        # Görüntüyü bulanıklaştır
        blur = cv2.blur(read, ksize=(10, 10))
        cv2.imshow("Video", blur)

        # BGR'den HSV'ye çevir
        hsv_cevir = cv2.cvtColor(blur, cv2.COLOR_BGR2HSV)
        cv2.imshow("HSV", hsv_cevir)

        # Maske oluştur
        maske = cv2.inRange(hsv_cevir, blueLow, blueUpper)
        cv2.imshow("Maske", maske)

        # Erozyon ve genişleme uygulayarak gürültüyü azalt
        maske = cv2.erode(maske, None, iterations=2)
        maske = cv2.dilate(maske, None, iterations=2)
        cv2.imshow("Maske - İşlenmiş", maske)

        # Kontur bulma
        contours, _ = cv2.findContours(maske.copy(), cv2.RETR_CCOMP, cv2.CHAIN_APPROX_SIMPLE)
        merkez = None

        if len(contours) > 0:
            # En büyük konturu bul
            c = max(contours, key=cv2.contourArea)

            # Dikdörtgene çevir
            rect = cv2.minAreaRect(c)
            ((x, y), (width, height), rotation) = rect
            s = "x: {}, y: {}, width: {}, height: {}, rotation: {}".format(
                np.round(x), np.round(y), np.round(width), np.round(height), np.round(rotation)
            )
            print(s)

            # Kutucuğu çiz
            box = cv2.boxPoints(rect)
            box = np.int64(box)
            cv2.drawContours(read, [box], 0, (0, 0, 255), 2)

            # Moment hesapla ve merkez noktayı bul
            M = cv2.moment(c)
            if M["m00"] != 0:
                center = (int(M["m10"] / M["m00"]), int(M["m01"] / M["m00"]))
                cv2.circle(read, center, 5, (255, 0, 255), -1)

            # Ekrana metin yaz
            cv2.putText(read, s, (50, 50), cv2.FONT_HERSHEY_DUPLEX, 1, (0, 0, 0), 2)

        cv2.imshow("Orijinal Tespit", read)

    # Çıkış için 'q' tuşuna bas
    if cv2.waitKey(1) & 0xFF == ord("q"):
        break

# Kaynakları serbest bırak
capture.release()
cv2.destroyAllWindows()
