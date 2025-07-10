"""
Kenar Algılama

Kenar algılama, görüntünün parlaklığının keskin bir şekilde değiştiği noktaları
tanımlamayı amaçlayan bir yöntemdir.
"""
import cv2
import matplotlib.pyplot as plt
import numpy as np

img = cv2.imread("bigben.png", 0)

if img is None:
    print("Görüntü yüklenemedi. Dosya yolunu kontrol edin.")
else:
    plt.figure(), plt.imshow(img, cmap="gray"), plt.axis("off"), plt.title("Orijinal")

    # Sabit threshold ile kenar
    edge = cv2.Canny(image=img, threshold1=0, threshold2=255)
    plt.figure(), plt.imshow(edge, cmap="gray"), plt.axis("off"), plt.title("Edge")

    # Medyana göre otomatik threshold
    medyan = np.median(img)
    print("Medyan değeri: ", medyan)

    low = int(max(0, (1 - 0.33) * medyan))
    high = int(min(255, (1 + 0.33) * medyan))

    print("En düşük değer:", low)
    print("En yüksek değer:", high)

    edge2 = cv2.Canny(image=img, threshold1=low, threshold2=high)
    plt.figure(), plt.imshow(edge2, cmap="gray"), plt.axis("off"), plt.title("Edge 2")

#Blur eklenerek yapılması gürültüyü minimize eder.
withblur = cv2.blur(img,ksize=(3,3))
plt.figure(), plt.imshow(withblur, cmap="gray"), plt.axis("off"), plt.title("with blur")
medyan1 = np.median(withblur)
low1 = int(max(0, (1-0.33)*medyan1))
high1 = int(max(255, (1+0.33)*medyan1))
yeniresim = cv2.Canny(withblur, threshold1= low1, threshold2=high1)
plt.figure(), plt.imshow(yeniresim, cmap="gray"), plt.axis("off"), plt.title("Blur with Edge")

plt.show()
