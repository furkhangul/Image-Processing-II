"""
Şekil ve Metin ekleme işlemleri

OpenCV üzerinden video veya resim üzerine şekil veya metin ekleme işlemi çok ama çok önemlidir.
Bir nesne tespiti ve takibinde çok önemli bir rol almaktadır.
Yazılar ise bunların en modern şekilde gözükmesini sağlamaya çalışan yapıalrdır.
"""
import cv2, numpy

#siyah arka plan oluşturmak için numpy kütüphanesini kullanıyoruz.

img = numpy.zeros((512,512,3), numpy.uint8)
cv2.imshow("Siyah Arka Plan", img)


#Çizgi eklemek için
#Burada sırası ile: resim, başlangıç noktası, bitiş noktası, renk ve kalınlık belirtildi.
cv2.line(img,(0,0),(512,512),(225,0,0),3)
cv2.imshow("Cizgi", img)


#Dikdörtgen eklemek için

#Sırası ile (resim, başlangıç noktası, bitiş noktası, renk, FILLED: içini doldurmak için kullanılır).
cv2.rectangle(img,(0,0),(256,256), (0,0,225), cv2.FILLED)
cv2.imshow("Dikdortgen", img)


#Çember için
#Sırası ile: (resim, merkez, yarıçap, renk, FILLED: isteğe bağlı)
cv2.circle(img,(300,300),45,(45,45,45),cv2.FILLED)
cv2.imshow("Cember", img)


#Metin için:
#Sırası ile: (resim,başlangıç noktası, font, kalınlığı, rengi)
cv2.putText(img,"Sekil",(350,350),cv2.FONT_HERSHEY_COMPLEX,2,(225,225,225),)
cv2.imshow("Yazi", img)
cv2.waitKey(10000)
cv2.destroyAllWindows()



