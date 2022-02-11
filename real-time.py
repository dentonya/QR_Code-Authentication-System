import numpy as np
from pyzbar.pyzbar import decode
import cv2

#decoding in real time
#scanning qr code from camera feed
video = cv2.VideoCapture(0)
video.set(3,640)
video.set(4,740)

while True:
    success, image = video.read()
    for barcode in decode(image):
        encoded_text = barcode.data.decode('utf-8')
        print(encoded_text)
        polygon_points = np.array([barcode.polygon],np.int32)
        polygon_points =polygon_points.reshape(-1,1,2)
        rect_points = barcode.rect
        cv2.polylines(image,[polygon_points],True,(255,255,0),5)
        cv2.putText(image,encoded_text,(rect_points[0],rect_points[1]),cv2.FONT_HERSHEY_DUPLEX,0.8,(255,255,0),2)
    cv2.imshow("Video",image)
    cv2.waitKey(1)