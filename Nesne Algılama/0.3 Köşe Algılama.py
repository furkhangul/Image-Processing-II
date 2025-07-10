#Köşe Algılama
"""
Özellik Nedir ?
Bilgisayarda görmede, genellikle bir resim veya videonun farklı çerçeveleri
arasında eşleşen noktalar bulmanız gerekir. Çünkü, iki görüntünün birbiriyle
nasıl ilişkili olduğunu bilirsek, her iki görüntüyü de bilgi almak için
kullanabiliriz.

Eşleştirme noktaları dediğimizde, genel anlamda sahnedeki kolayca taşıyabileceğimiz
özelliklere atıfta bulunuyoruz.
Bu özellikler benzersiz şekilde tanımlanabilir olmalıdır.

Temel Özellikler: Köşeler ve Kenarlar
"""

"""
Köşe Algılama

Köşeler, iki kenarın kesişmesi olduğu için bu iki kenarın yönlerinin değiştiği
bir noktayı temsil eder.

Köşeler, resimdeki renk geçişindeki bir varyasyonu temsil ettiğinden, bu vayasyonu
arayacağız.Görüntü yoğunluğundaki varyasyonu arayacağız

Formül
E(u,v) =  ∑ w(x,y) =[I(x+u, y+v) - I(x,y)]^2
         x,y
"""

import cv2
import matplotlib.pyplot as plt
import numpy as np

img = cv2.imread("sudoku.png", 0)
img = np.float32(img)
print(img.shape)
plt.figure(), plt.imshow(img, cmap="gray"), plt.title("Orijinal"),plt.axis("off")


#Harris Corner Detection
#blocksize = komşuluk boyutu yani kaç tane komşusuna bakacağımızı belirliyor.
#karnelsize = kutucuğun boyutunu belirler
#k = Harristeki parametrelerden bi tanesi
harris = cv2.cornerHarris(img, blockSize= 2,ksize=3, k=0.04 )
plt.figure(), plt.imshow(harris, cmap="gray"), plt.title("Harris"),plt.axis("off")

#Daha iyi görselleştirmek için:
harris = cv2.dilate(harris, None)
img[harris>0.2*harris.max()] = 1
plt.figure(), plt.imshow(harris, cmap="gray"), plt.title("Harris"),plt.axis("off")



#Shi Tomsi Detection
img = cv2.imread("sudoku.png", 0)
img = np.float32(img)
corners = cv2.goodFeaturesToTrack(img, 500, 0.01,10)
corners = np.int64(corners)
for i in corners:
    x,y = i.ravel()
    cv2.circle(img,(x,y),3,(125,125,125),cv2.FILLED,)
plt.imshow(img)
plt.show()
