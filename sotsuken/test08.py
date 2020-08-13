#マスキング処理

#-*- coding:utf-8 -*-
import cv2
import numpy as np
#from matplotlib import pyplot as plt


#赤色の検出
def detect_red_color(img):
    #HSV色空間に変換
    hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)

    #赤色の領域
    #HSVの範囲を指定
    hsv_min = np.array([0,64,0])        #hsvの下限
    hsv_max = np.array([30,255,255])    #hsvの上限
    mask1 = cv2.inRange(hsv, hsv_min, hsv_max) 

    #赤色はHの値が分かれている
    hsv_min = np.array([150,64,0])
    hsv_max = np.array([179,255,255])
    mask2 = cv2.inRange(hsv, hsv_min, hsv_max) 

    #赤色領域のマスク(255:赤　0:赤以外)
    mask = mask1 + mask2

    #マスキング処理
    masked_img = cv2.bitwise_and(img, img, mask = mask)
    
    return mask, masked_img

def detect_green_color(img):
    #HSV色空間に変換
    hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)

    #緑色の領域
    #HSVの範囲を指定
    hsv_min = np.array([30,64,0])        #hsvの下限
    hsv_max = np.array([90,255,255])    #hsvの上限
    mask = cv2.inRange(hsv, hsv_min, hsv_max) 

    #マスキング処理
    masked_img = cv2.bitwise_and(img, img, mask = mask)
    
    return mask, masked_img

def detect_blue_color(img):
    #HSV色空間に変換
    hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)

    #緑色の領域
    #HSVの範囲を指定
    hsv_min = np.array([50/360*179,64,0])        #hsvの下限
    hsv_max = np.array([150/360*179,255,255])    #hsvの上限
    mask = cv2.inRange(hsv, hsv_min, hsv_max) 

    #マスキング処理
    masked_img = cv2.bitwise_and(img, img, mask = mask)
    
    return mask, masked_img

img = cv2.imread("C:\\Users\\deros\\Documents\\sotsuken\\test01.jpg")

#色検出
red_mask, red_masked_img = detect_red_color(img)
green_mask, green_masked_img = detect_green_color(img)
blue_mask, blue_masked_img = detect_blue_color(img)


#結果を出力
cv2.imwrite("C:\\Users\\deros\\Documents\\sotsuken\\red_mask.jpg", red_mask)
cv2.imwrite("C:\\Users\\deros\\Documents\\sotsuken\\red_masked_img.jpg", red_masked_img)
cv2.imwrite("C:\\Users\\deros\\Documents\\sotsuken\\green_mask.png", green_mask)
cv2.imwrite("C:\\Users\\deros\\Documents\\sotsuken\\green_masked_img.png", green_masked_img)
cv2.imwrite("C:\\Users\\deros\\Documents\\sotsuken\\blue_mask.png", blue_mask)
cv2.imwrite("C:\\Users\\deros\\Documents\\sotsuken\\blue_masked_img.png", blue_masked_img)