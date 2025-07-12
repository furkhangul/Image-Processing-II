#Renk ile Nesne Tespiti
"""
-Belirli renklerde bulunan nesnelerin tespitinin nasıl yapılacağını kontur
bulma yöntemi ile öğrenilmektedir.

-Kontur basitçe, aynı renk veya yoğunluğa sahip tüm sürekli noktaları birleştiren
bir eğri olarak açıklanabilir.

-Konturlar, şekil analizi ve nesne algılama ve tanıma için kullanışlı bir araçtır.

"""
from IPython.core.completerlib import import_re

"""
Kodlama kısmında renklerin rgb'den hsv formatına çevirecez
HSV: 
HUVE -> Renk özü anlamına gelmektedir.
Saturation -> Doygunluk Kavramı
Value -> Parlaklık kavramı
"""

import cv2
import numpy as np
from collections import deque
#Nesne merkezini depolayacak veri tipi
tampon_bolge = 15
noktalar = deque(maxlen= tampon_bolge)

#Şimdi ise mavi rengin aralığını HSV formatında belirleyeceğiz.
#Bunu paint ile değerlendirebiliriz.
blueLow = (84,98,0)
blueUpper = (179,255,255 )

#Kamera oluşturacaz.
capture = cv2.VideoCapture(0)
#Kamera genişlik->3 ve yükselik->4
capture.set(3,960)
capture.set(4,480)

while True:
    success, read = capture.read()

    if success:
        #Detayları azaltmak adına blur ekliyoruz.
        blur = cv2.blur(read,ksize=(10,10))
        cv2.imshow("Video",blur)
        hsv_cevir = cv2.cvtColor(blur, cv2.COLOR_BGR2HSV)
        cv2.imshow("hsv",hsv_cevir)
        #Artk mavi için maske oluşturmaya başlayacağız.
        maske = cv2.inRange(hsv_cevir,blueLow,blueUpper)
        cv2.imshow("Maskeleme İşlemi",maske)

    if cv2.waitKey(1) & 0xFF == ord("q"):
        break
