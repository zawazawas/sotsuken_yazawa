#-*- coding:utf-8 -*-
import cv2
import numpy as np

img = cv2.imread("C:\\Users\\deros\\Documents\\sotsuken\\yuri.jpg")

height, width, ch = img.shape

size = width * height


print("幅" , width)
print("高さ" , height)
print("チャンネル数" , ch)
print("画素数" , size)
print("データ型" , img.dtype)

print("Bの画素値:/n", img[:,:,0])
print("Gの画素値:/n", img[:,:,1])
print("Rの画素値:/n", img[:,:,2])