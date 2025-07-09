#Gradyanlar
"""
Görüntü gradyanı, görüntüdeki yoğunluk veya renkteki yönlü bir değişikliktir.
Kenar algılamada kullanılır.
"""

import cv2
import matplotlib.pyplot as plt

img = cv2.imread("sudoku.png", 0)
plt.figure(), plt.imshow(img,cmap="gray"),plt.axis("off"),plt.title("Orijinal Resim")

#X eksenindeki gradyanları: resim, derinlik, x ekseni, y elseni, karnel size ( alınan kare alanı )
sobelx = cv2.Sobel(img, ddepth = cv2.CV_16S , dx = 1, dy= 0,ksize=5 )
#Y eksenindeki gradyanları:
sobely = cv2.Sobel(img, ddepth = cv2.CV_16S , dx = 0, dy= 1,ksize=5 )
#Her iki gradyan için:
laplacian = cv2.Laplacian(img,ddepth=cv2.CV_16S)


plt.figure(), plt.imshow(sobelx,cmap="gray"),plt.axis("off"),plt.title("Sobel X Resim")
plt.figure(), plt.imshow(sobely,cmap="gray"),plt.axis("off"),plt.title("Sobel Y Resim")
plt.figure(), plt.imshow(laplacian,cmap="gray"),plt.axis("off"),plt.title("Laplacian Resim")
plt.show()
