import cv2
import numpy as np
from pyzbar.pyzbar import decode


cap = cv2.VideoCapture(0)
cap.set(3,480)
cap.set(4,480)

while True:
    success, img = cap.read()
    for barcode in decode(img):
        mydata = barcode.data.decode('utf-8')
        print(mydata)
        pts = np.array([barcode.polygon],np.int32)
        pts = pts.reshape(-1,1,2)
        cv2.polylines(img,[pts],True,(34,139,34),2)
        cv2.putText(img,mydata,(50,50),cv2.FONT_ITALIC,0.9,(255,0,0),2)

    cv2.imshow('CAM',img)
    cv2.waitKey(1)





