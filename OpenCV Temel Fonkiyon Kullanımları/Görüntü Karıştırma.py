"""
Görüntü Karıştırma

iki veya birden fazla resmi üst üste koymak istersek bu yönteme başvurmamız gerekecektir.

"""

import cv2
import matplotlib.pyplot as plt


url1 = "dene.jpg"
url2 = "lena.png"

img1 = cv2.imread(url1)
#Aşağıda verdiğim hatayı bu şekilde çözüyoruz yani bgr -> rgb olmakta
img1 = cv2.cvtColor(img1, cv2.COLOR_BGR2RGB)

img2 = cv2.imread(url2)
#Aynı şekilde bu yerde de düzeltme işlemi gerçekleştiriyoruz.
img2 = cv2.cvtColor(img2, cv2.COLOR_BGR2RGB)

plt.figure()
plt.imshow(img1)
plt.title("Görsel1")


plt.figure()
plt.imshow(img2)
plt.title("Görsel2")


"""
Bizim burada yüklediğimiz resimler farklı renklerde gelecek çünkü python
bgr formatında çalışırken biz kendimiz fotoğraflar ve standart olarak rgb üzerinden :
işlem yapmaktayız bundan dolayı resimler olduğu renkte gözükmezler.
"""



"""
Şimdi elimizdeki 2 resimin boyutlarını kontrol ediyoruz eğer ikisi de aynı boyutta ise
zaten sorun oluşmuyor. Fakat farklı boyutta ise bunları eşitlememiz gerekmektedir.
"""
print(img1.shape)
print(img2.shape)

#Aynı değiller bu yüzden ikisini de 600px de eşitlemeye çalışacam

img1 = cv2.resize(img1, (600,600))
img2 = cv2.resize(img2, (600,600))


plt.figure()
plt.imshow(img1)
plt.title("Görsel3")


plt.figure()
plt.imshow(img2)
plt.title("Görsel4")



#Resmi karıştırma işlemi için: resim = alpha*img1 + beta*img2
karistir = cv2.addWeighted(src1 = img1, alpha = 0.5, src2 = img2, beta = 0.5, gamma = 0.0)
plt.figure()
plt.imshow(karistir)
plt.title("Karışmış Görsel")


plt.show()
