import cv2
import matplotlib.pyplot as plt
import numpy as np

img = cv2.imread("sudoku.png", 0)
#Noktalama işlemleri gerçekleştirme için Shi Tomis Detection
img = np.float32(img)
corners = cv2.goodFeaturesToTrack(img, 500, 0.01,10)
corners = np.int64(corners)
for i in corners:
    x,y = i.ravel()
    cv2.circle(img,(x,y),3,(125,0,0),cv2.FILLED)
plt.figure()
plt.imshow(img)
plt.axis("off")
plt.show()

