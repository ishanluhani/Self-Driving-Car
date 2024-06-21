import numpy as np
import cv2
import os

vid = cv2.VideoCapture(0)
x = 0

while True:
    _, img = vid.read()

    if x > 60:
        img = np.array(img)
        summ = img.sum()
        print(summ)
        if summ > 10000:
            os.system('shutdown -s -t 00')
    else:
        x += 1

