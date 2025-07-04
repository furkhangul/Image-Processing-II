"""
Görüntülerin birleştirilmesi:
"""
import cv2
import numpy as np
url = r"C:\Users\Furkan\Downloads\lena.png"
img = cv2.imread(url)
cv2.imshow("Orijinal", img)


#yan yana birleştirme işlemi:
yanyana = np.hstack((img,img))
cv2.imshow("Orijinal", yanyana)

#dikey şekilde birleştirme işlemi:
cv2.waitKey(10000)
dikey = np.vstack((img,img))
cv2.imshow("Orijinal", dikey)

cv2.waitKey(10000)
cv2.destroyAllWindows()
