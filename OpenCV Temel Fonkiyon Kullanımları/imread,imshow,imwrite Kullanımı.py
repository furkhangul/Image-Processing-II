import cv2
import time
"""
Opencv ile görseli içe aktarmak için imread fonkiyonu kullanılır.
"""
url=r"C:\Users\Furkan\Downloads\a.jpg"
img = cv2.imread(url ,0 )

"""
url , 0 şeklinde yazılan şey aslında resmi siyah beyaz şekilde gösterilmesini sağlar
"""

#Görselleşitirmek için ise imshow fonksiyonu kullanılır.
cv2.imshow("resim" , img)

bekle = cv2.waitKey(0) &0xFF
if bekle == 27: #27 tuşu klavyede esc tuşu anlamına gelir
    cv2.destroyWindow("resim")
elif bekle == ord("a"):
    cv2.imwrite("resim" ,img)


"""
imread: Görüntüyü okumak için kullanılır.
imwrite: Bellekte bir görüntüyü diske yazdırır.
imshow: namedWindow ve waitKey ile birlikte bellekteki bir resmi görüntülemek için kullanılır.
"""
