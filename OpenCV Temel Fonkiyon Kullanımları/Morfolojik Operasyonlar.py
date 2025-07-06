"""
Morfolojik Operasyonlar

Erezisyon (Erosion):
Görüntüdeki beyaz (nesne) alanları küçültür, gürültüyü (noise) temizler.

Genişleme (Dilation):
Beyaz alanları büyütür, kopuk bölgeleri birleştiri

Erezisyon küçültür, genişleme büyütür. Gürültü temizleme ve şekil düzeltmede kullanılırlar.

Açma (Opening)
Tanım: Önce erezisyon, sonra genişleme uygulanır.
Opening = Erosion ➝ Dilation

Ne işe yarar?

Küçük beyaz gürültüleri temizler (örneğin, rastgele lekeler)

İnce, gereksiz yapıları siler ama ana şekli korur

Kapama (Closing)
Tanım: Önce genişleme, sonra erezisyon uygulanır.
Closing = Dilation ➝ Erosion

Ne işe yarar?

Siyah boşlukları kapatır, nesne içindeki delikleri doldurur

Kopmuş kenarları birleştirir


"""

import cv2
import numpy as np

img = cv2.imread("ornek.png", 0)
_, thresh = cv2.threshold(img, 127, 255, cv2.THRESH_BINARY)

kernel = np.ones((5,5), np.uint8)

# Açma işlemi
opening = cv2.morphologyEx(thresh, cv2.MORPH_OPEN, kernel)

# Kapama işlemi
closing = cv2.morphologyEx(thresh, cv2.MORPH_CLOSE, kernel)

cv2.imshow("Orijinal", thresh)
cv2.imshow("Açma (Opening)", opening)
cv2.imshow("Kapama (Closing)", closing)
cv2.waitKey(0)
cv2.destroyAllWindows()
