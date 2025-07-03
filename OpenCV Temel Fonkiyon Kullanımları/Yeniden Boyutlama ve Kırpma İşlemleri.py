"""
Yeniden Boyutlama ve Kırpma İşlemleri

Görüntü işleme sırasında resim bazen istediğimiz formatta olamayabiliyor bundan dolayı
işlemer sekteye uğrayabiliyor veya makina bu veriyi tam olarak işlemede sıkıntı yaşayabiliyor.
Bunun için resim boyutlandırma işlemleri gerçekleştirilmektedir.

Bazen resimlerin boyutu hem memory açısından hem performans açısından çok önemlidir.
Mesela derin öğrenmede kullanacağımız bir kütüphane belli resim boyutlarını alabilmekte
biz bunu kullanabilmemiz için kırpma ve boyutlandırma işlemlerini iyi bilmemiz gerekmektedir.
"""
import time

import cv2, time
url = r"C:\Users\Furkan\Downloads\lena.png"


img = cv2.imread(url)
print("resim boyutu: ", img.shape)

cv2.imshow("Resim", img)

yeniboyut = cv2.resize(img, (800,800))
print("Yeni resim boyutu:", yeniboyut.shape)


#Kırpma işlemi için ilk 400 elemanını almak için 300e kadar
kirpilmis = img[:300, :400]
cv2.imshow("Kırpılmış", kirpilmis)
cv2.imshow("Yeni boyutlu resim", yeniboyut)
cv2.waitKey(10000)
cv2.destroyAllWindows()
