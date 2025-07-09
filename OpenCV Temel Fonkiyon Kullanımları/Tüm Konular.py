#ÖDEV

import cv2
import matplotlib.pyplot as plt

img = cv2.imread("lena.png")
#img = cv2.cvtColor(img1, cv2.COLOR_BGR2RGB)
plt.figure()
#plt.imshow(img)
plt.title("Orijinal Resim")
plt.axis("off")



#Resim Boyutu Öğrenmek için
print("Boyut: ",img.shape)

#Resmi Yeniden Boyutlandırma (4/5 oranında)
yeniboyut = cv2.resize(img,(int(img.shape[1]*4/5),int(img.shape[0]*4/5)))
cv2.imshow("Yeniden Boyutlandırılmış",yeniboyut)


#Orijinal resime yazı ekleme
yazi = cv2.putText(img,"Lena",(150,150), cv2.FONT_HERSHEY_DUPLEX,1,(0,0,250))
cv2.imshow("Yazı Hali", yazi)

#Orijinal resme 50 trashold değeri üzerindekileri beyaz altındakileri siyah yap
#Binary yöntemi ile yapılsın

_, trash = cv2.threshold(img,thresh=50,maxval=225, type=cv2.THRESH_BINARY)
cv2.imshow("Trashold Yöntemi", trash)

#Gaussin bulanıklaştırma uygula
blur = cv2.GaussianBlur(img,ksize=(3,3),sigmaX= 7, sigmaY=7)
cv2.imshow("Blurlu", blur)

#Orijinal resime laplacian gradyan uygula
laplacian = cv2.Laplacian(img,ddepth=cv2.CV_16S)
cv2.imshow("Laplacian", laplacian)

#Histogramını çizdirme:
histo = cv2.calcHist(img,channels= [0], mask = None, histSize=[256], ranges=[0,256])
cv2.imshow("Histogram", histo)
plt.show()
