"""
Görüntü Eşikleme

Görsellerin üzerindeki renk pigmentlerinin eşik değerler ile belirlenip belirli aralıkları
algılayıp algılamayacağını öğreneceğiz bu sayede renklerin sınırlarını belirterek
fotoğrafta oynamalar yapabileceğiz.

örnek olrak elimizde bir resim olsun eğer 125 eşik değeri verirsek bu resmin ana hatları
çıkar karşımıza önemsiz şeyler çok gözükmez.
"""
import matplotlib.pyplot as plt
import cv2

img = cv2.imread("lena.png")
#gri skalasına çevirecek olursak
img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

#ekstra siyah beyaz yapabilmek için cmap="gray" yapmaktayız.
plt.figure()
plt.imshow(img, cmap="gray")
plt.axis("off")

#Eşikleme işlemi için ise:
    #60tan büyük ve 225 ten küçük olan pixelleri tuttu ve bize verir sondaki ise siyahları gösterir
    #Eğer cv2.THRESH_BINARY_INV yapsaydık bu sefer siyah kısım beyaz olur tam tersi olur yani.
onemsiz, esiklenmis = cv2.threshold(img, thresh= 60, maxval=225, type = cv2.THRESH_BINARY)
plt.figure()
plt.imshow(esiklenmis, cmap="gray")
plt.axis("off")



"""
Işık farklılıklarının olduğu görüntülerde, her pikselin çevresine göre ayrı eşik değeri belirleyerek siyah-beyaz ayrımı yapar.
BUndan dolayı adactive tresh kullanılır.
"""
#Sırası ile: resim, maximum değer, adaptive methodumuz, eşitleme türü, eşik değer, c değeri
adactive_tresh = cv2.adaptiveThreshold(img, 225, cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY, 11, 8)
plt.figure()
plt.imshow(adactive_tresh)
plt.axis("off")
plt.show()
