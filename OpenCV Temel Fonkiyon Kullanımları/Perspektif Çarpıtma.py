"""
Perspektif Çarpıtma

Görüntüler yamuk ve doğru değil ise bu yöntem ile yönünü ayarlayabilir ve düzenleyebiliriz.
Biz insanlar yamuk duran nesnelerin tespitini gerçekleştirebilmekte sorun yaşamaz iken
bilgisayarlar veriyi okuya bilmesi için aynı veri setinden olmasına dikkat eder.
Eğer yamuk veya farklı boyutlarda ise kabul edilmez bundan dolayı bizim her bir veriyi
aynı boyut ve eğime indirgememeiz çok önemlidir.
"""

import cv2
import numpy as np
url = r"C:\Users\Furkan\Downloads\dene.jpg"
img = cv2.imread(url)
cv2.imshow("Orijinal", img)

#yükseklik ve uzunluk konumlarını öğreniyorum

ilkkonum = np.float32([[0,0],[0,405],[480,0],[480,405]])
sonkonum = np.float32([[480,405],[480,0],[0,405],[0,0]])

degis = cv2.getPerspectiveTransform(ilkkonum,sonkonum)
print(degis)


#nihai değişmiş resim:
cikti = cv2.warpPerspective(img,degis,(480,405))
cv2.imshow("Değişmiş", cikti)
cv2.waitKey(10000)
cv2.destroyAllWindows()


#Burada resmi 180 derece döndürerek tam tersi yönde bakmaya çalıştık.
