# Histogram
"""
Görüntü histogramı, dijital görüntüdeki ton dağılımını grafiksel olarak gösterir.
Her bir ton değeri için piksel sayısını içerir.
Belirli bir görüntü için histograma bakılarak ton dağılımı analiz edilebilir.
"""

import cv2
import matplotlib.pyplot as plt
import numpy as np  # Maske işlemleri için gerekli

# Görüntüyü oku ve BGR'den RGB'ye çevir
img_bgr = cv2.imread("dene.jpg")
img = cv2.cvtColor(img_bgr, cv2.COLOR_BGR2RGB)

# Görüntüyü göster
plt.figure(), plt.imshow(img), plt.title("Orijinal Resim"), plt.axis("off")

# Piksel sayısını yazdır
print("Piksel Sayısı (Yükseklik, Genişlik, Kanal):", img.shape)

# -------------------------------
# TEK KANAL (örneğin RED) için histogram (maske YOK)
histogram_img = cv2.calcHist([img], channels=[0], mask=None, histSize=[256], ranges=[0, 256])
plt.figure()
plt.plot(histogram_img, color='red')
plt.title("Kırmızı Kanal Histogramı (maskesiz)")
plt.xlabel("Piksel Değeri")
plt.ylabel("Piksel Sayısı")
plt.grid()

# -------------------------------
# TÜM RENK KANALLARI için histogram (maske YOK)
colors = ['blue', 'green', 'red']
plt.figure()
for i, col in enumerate(colors):
    hist = cv2.calcHist([img], channels=[i], mask=None, histSize=[256], ranges=[0, 256])
    plt.plot(hist, color=col)
plt.title("RGB Histogram (maskesiz)")
plt.xlabel("Piksel Değeri")
plt.ylabel("Piksel Sayısı")
plt.grid()

# -------------------------------
# MASKE kullanarak histogram örneği
# (resmin ortasındaki küçük bir bölgeyi seçelim)
mask = np.zeros(img.shape[:2], dtype=np.uint8)
mask[100:200, 100:200] = 255  # sadece bu bölgedeki pikseller dahil edilecek

# Maskeyi görselleştir
plt.figure(), plt.imshow(mask, cmap="gray"), plt.title("Maske"), plt.axis("off")

# Maskeli histogram (örneğin RED kanal)
masked_hist = cv2.calcHist([img], channels=[0], mask=mask, histSize=[256], ranges=[0, 256])
plt.figure()
plt.plot(masked_hist, color='red')
plt.title("Kırmızı Kanal Histogramı (maskeli)")
plt.xlabel("Piksel Değeri")
plt.ylabel("Piksel Sayısı")
plt.grid()

plt.show()
