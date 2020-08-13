#カメラの読み込み

#-*- coding:utf-8 -*-
import cv2
import numpy as np

#カメラの読み込み
cap = cv2.VideoCapture(0)

#動画終了まで繰り返し
while(cap.isOpened()):
    #フレームを取得
    ret, frame = cap.read()

    #フレームの表示
    cv2.imshow("Flame", frame)

    #Qキーが押されたら終了
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()