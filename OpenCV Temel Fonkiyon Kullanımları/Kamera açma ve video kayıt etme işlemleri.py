"""
Kamera açma ve video kayıt etme işlemleri
"""

import cv2

#kameraya erişim için 0 indexi kullanılır.
cap = cv2.VideoCapture(0)


#Kameramızın yükseklik ve genişliğini almak için:
width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))

print(width,height)

#Video kayıt etmek için

#
recorder = cv2.VideoWriter("video_kayıt_etme.avi", cv2.VideoWriter_fourcc(*"DIVX"),20,(width,height))

while True:
    ret, frame = cap.read()
    if not ret:
        break # Kamera açılmadıysa ya da bozulduysa çık

    recorder.write(frame)  # her frame’i videoya kaydet
    cv2.imshow("Kamera", frame) # ekrana göster

    if cv2.waitKey(1) & 0xFF == ord("q"):
        break # q tuşuna basıldığında çıkış
cap.release()
recorder.release()
cv2.destroyAllWindows()
