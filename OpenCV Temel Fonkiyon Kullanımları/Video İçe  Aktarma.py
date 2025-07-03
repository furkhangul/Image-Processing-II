"""
Open CV üzerinden video içe aktarma işlemi url üzerinden gerçekleşir.
Video okuma işlemi fotoğraftaki gibi gerçekleşir. Video dediğimiz kavram da zaten
binlerde fotoğrafın bir araya gelmesi ile oluşan fotoğraf dizini.

videoyu içe aktar derken birden fazla resmi hızlı bir şekilde aktarılması olayıdır.
"""

import cv2,time

#video url ile uzantımızı ekliyoruz.
video_url = r"C:\Users\Furkan\Downloads\video.mp4"
#cap: capture yani video demek istiyoruz
#video.capture ise resimleri ard arda hızlı şekide eklenmesini sağlar.
cap = cv2.VideoCapture(video_url)


#Genişlik ve yükseklik sağlamak için:
#get fonksiyonunun 3. indexi ile genişliği 4. indexi ile yüksekliği bulurum.
print("Genişlik:", cap.get(3))
print("Yükseklik:", cap.get(4))

#Eğer cap yani video çalıştırılmazsa yani False durumu gerçekleşir ise Hata mesajı alınır.
if cap.isOpened() == False:
    print("Hata")


#Burada ise iki değişken atıyorum ve bu değişkenlerden birincisi boolean iken
#ikincisi ise işlemin adı olmakta burada return doğru olup olmadığını frame ise okunan veriyi temsil ediyor.
while True:
    ret, frame = cap.read()
    if ret == True:
        time.sleep(0.01)
        #time kütüphanesini kullanmazsak çok hızlı akar ve bu yüzden bir şey algılayamayız.

        cv2.imshow("Video", frame)
    else: break #video bitmiştir bundan dolayı biter
    if cv2.waitKey(1) & 0xFF == ord("q"):
        break #Burada ise q tuşuna basınca kapanır.
cap.release()
cv2.destroyAllWindows()


#time.sleep ile oynayarak istediğimiz gibi ayarlamalar yapabilmekteyiz.( hızlı veya yavaş)
