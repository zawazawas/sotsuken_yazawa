#-*- coding:utf-8 -*-
import cv2
import numpy as np

img = cv2.imread("C:\\Users\\deros\\Documents\\sotsuken\\yuri.jpg")

x, y = 70, 100
w, h = 80, 15

img[y:y + h, x:x + w] = 0

cv2.imwrite("C:\\Users\\deros\\Documents\\sotsuken\\output.png", img)