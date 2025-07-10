#Kontur Algılama
"""
Kontur tespiti, aynı renk veya yoğunluğa sahip tüm kesintisiz noktaları (sınırlar
ile birlikte) birleştirmeyi amaçlayan yöntemdir.

Konturlar şekil analizi ve nesne algılama ve tanımlama için kullanılır.
"""

import cv2
import matplotlib.pyplot as plt
import numpy as np

# Görüntüyü gri tonlamalı (grayscale) olarak okuruz
img = cv2.imread("contur.jpg", 0)
plt.figure()
plt.imshow(img, cmap="gray")
plt.axis("off")
plt.title("Orijinal Görüntü")

# Kontür tespiti için:
# cv2.RETR_CCOMP => Konturları iki seviyeli bir hiyerarşiyle bulur:
#   - 1. seviye: dış konturlar (nesnenin dış sınırı)
#   - 2. seviye: iç konturlar (delikler, boşluklar)
#
# cv2.CHAIN_APPROX_SIMPLE => Kontur noktalarını sıkıştırır.
#   - Örn: bir düz çizgi boyunca sadece uç noktalar tutulur.
#   - Bu, bellek kullanımını azaltır ve işlemi hızlandırır.

# cv2.findContours() fonksiyonu OpenCV versiyonuna göre farklılık gösterebilir:
# OpenCV 4.x ve sonrası: iki çıktı döner (konturlar, hiyerarşi)
# OpenCV 3.x: üç çıktı döner (görüntü, konturlar, hiyerarşi)
# Bu nedenle OpenCV versiyonuna dikkat et!

# Bizim kodumuzda OpenCV 3.x'e göre yazılmış:
image, contours, hierasch = cv2.findContours(img, cv2.RETR_CCOMP, cv2.CHAIN_APPROX_SIMPLE)

# Konturları çizmek için önce görüntüyü BGR (renkli) formata çeviriyoruz
img_color = cv2.cvtColor(img, cv2.COLOR_GRAY2BGR)

# Konturlar üzerinde döngü kurarak her konturu çizeceğiz
# enumerate(): hem index (i) hem de konturu (cnt) alır
for i, cnt in enumerate(contours):
    # hiyerarşi bilgisini kontrol ederiz:
    # [0, 1, 2, 3] -> [next, previous, first child, parent]
    # Eğer dış kontursa farklı renkte, iç kontursa başka renkte çizebiliriz
    if hierasch[0][i][3] == -1:
        # dış kontur (parent yok)
        cv2.drawContours(img_color, contours, i, (0, 255, 0), 2)  # yeşil
    else:
        # iç kontur (bir parent var)
        cv2.drawContours(img_color, contours, i, (0, 0, 255), 2)  # kırmızı

plt.figure()
plt.imshow(cv2.cvtColor(img_color, cv2.COLOR_BGR2RGB))
plt.axis("off")
plt.title("Tespit Edilen Konturlar")
plt.show()
