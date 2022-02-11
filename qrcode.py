import numpy as np
from pyzbar.pyzbar import decode
import cv2

image = cv2.imread("qrcodes/qr_code_txt.png")
coded_infor = decode(image)
print(coded_infor)

for barcode in decode(image):
    print(barcode.data) #in bytes
    encoded_text = barcode.data.decode('utf-8')
    print(encoded_text)
    print(barcode.rect)
