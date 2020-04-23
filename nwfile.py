import cv2

cap=cv2.VideoCapture(0)
cap.set(3,3840)
cap.set(4,2160)
cap.set(10,200)


while True:
    success,img=cap.read()
    cv2.imshow("vid",img)
    if cv2.waitKey(1) & 0xFF ==ord('q'):
        break