"""
Bunalıklaştırma

Bulanıklığı, görüntünün düşük geçişli bir filtre uygulanması ile elde edilir.
Gürültüyü gidermek için elverişlidir.
Aslında görüntüde yüksek frekanslı içeriği parazit, kenarlar gibi içerikleri kaldırır.

Opencv de 3 ana tür bulanıklaştırma tekniği vardır.
Ortalama bulanıklaştırma
gauss bulanıklaştırma
medyan bulanıklaştırma
"""

"""
Ortalama Bulanıklaştırma

bir görüntünün normalleştirilmiş bir kutu filtresiyle sarılmasıyla yapılır.

çekirdek alanı altındaki tüm piksellerin ortalamasını alır ve bu ortalamya göre
öğe ile diğer değerlerin yerini değiştirir.


Gauss Bulanıklaştırma

-Bu yöntemde kutu filtresi yerine Gauss çekirdeği kullanılır.
-Pozitif ve tek olması gereken çekirdeğin genişliğini ve yüksekliğini belirtir.
-SigmaX ve SigmaY, X ve Y yönlerindeki standart sapmayı belirtmez.

Medyan Bulanıklaştırma

çekirdek alanı altındaki tüm piksellerin medyanını alır ve merkez öğe bu medyan
değerle değiştirilir.

tuz ve biber gürültüsüne karşı oldukça etkilidir.
"""

import cv2
import matplotlib.pyplot as plt
import numpy as np

#Boş hataları önlemek için
import warnings
warnings.filterwarnings("ignore")

"""
Blur: detayı azaltır, gürültüyü engeller
"""

img = cv2.imread("lena.png")
img = cv2.cvtColor(img,cv2.COLOR_BGR2RGB)

plt.figure()
plt.imshow(img)
plt.axis("off")
plt.title("Orijinal Fotoğraf")

#Ortalama bulanıklaştırma  ksize -> karnelsize = kutucuk boyutu
meanblur = cv2.blur(img, ksize=(3,3) )
plt.figure()
plt.imshow(meanblur)
plt.axis("off")
plt.title("Ortalama Bulanıklaştırılmış Fotoğraf")


#Gauss Bulanıklaştırma
#Sırası ile resim, kutucuk alanı 3*3 ve x alanındaki sigma
#Eğer y alanındaki sigma yazılmazsa xteki sigma otomatikmen devreye girer aynı şeye eşitlenir.
gausblur = cv2.GaussianBlur(img, ksize=(7,7), sigmaX= 7 )
plt.figure()
plt.imshow(gausblur)
plt.axis("off")
plt.title("Gauss Bulanıklaştırılmış Fotoğraf")

#Medyan Bulanıklaştırma
medianblur = cv2.medianBlur(img, ksize= 3)
plt.figure()
plt.imshow(medianblur)
plt.axis("off")
plt.title("Median Bulanıklaştırılmış Fotoğraf")
plt.show()
