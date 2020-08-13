#-*- coding:utf-8 -*-
import cv2
import numpy as np
#from matplotlib import pyplot as plt

img = cv2.imread("C:\\Users\\deros\\Documents\\sotsuken\\yuri.jpg")
# 入力画像を読み込み
hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)

cv2.imwrite("C:\\Users\\deros\\Documents\\sotsuken\\hsv.png", hsv)