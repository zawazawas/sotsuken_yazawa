# -*- coding: utf-8 -*-
import cv2
import numpy as np

# 入力画像のロード
img = cv2.imread('C:\\Users\\deros\\Documents\\sotsuken\\input.png')

cv2.imshow("input", img)
cv2.waitKey(0)
cv2.destroyAllWindows()