import cv2
import numpy as np #마스크 영상생성에 필요한 컬러범위 지정에 사용할 numpy 패키지를 import 합니다.

cap = cv2.VideoCapture(0)

#각 HSV별 범위
lower_red = np.array([150, 30, 30])
upper_red = np.array([180, 255, 255])

lower_blue = np.array([100, 100, 100])
upper_blue = np.array([150, 255, 255])

lower_green = np.array([40, 30, 30])
upper_green = np.array([85, 150, 255])

lower_yellow = np.array([25, 30, 30])
upper_yellow = np.array([40, 255, 255])

list_color = []

#화면 원래 크기 h = 240, w = 640 의 중앙점 설정
frame_h = 240
frame_w = 320

frame_uh = 220
frame_dh = 260

frame_lw = 300
frame_rw = 340

count = 0
def processCam():
#while True:
    color_value = 'null'
    ret, frame = cap.read()
    #입력받은 카메라 영상의 컬러 시스템을 BGR에서 HSV로 변경
    hsv= cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

    #HSV 영상에서 지정한 색상범위에 해당하는 마스크 영상을 구합니다. 영상을 남길부분이 255, 그 외 영역은 0
    mask = cv2.inRange(hsv, lower_red, upper_red)
    mask1 = cv2.inRange(hsv, lower_blue, upper_blue)
    mask2 = cv2.inRange(hsv, lower_green, upper_green)
    mask3 = cv2.inRange(hsv, lower_yellow, upper_yellow)

    if mask[frame_h,frame_w] == 255 and mask[frame_uh,frame_w] == 255 and mask[frame_dh,frame_w] ==255 and mask[frame_h,frame_lw] == 255 and mask[frame_h,frame_rw] == 255:
        color_value = 'red'
    elif mask1[frame_h,frame_w] == 255 and mask1[frame_uh,frame_w] == 255 and mask1[frame_dh,frame_w] ==255 and mask1[frame_h,frame_lw] == 255 and mask1[frame_h,frame_rw] == 255:
        color_value = 'blue'
    elif mask2[frame_h,frame_w] == 255 and mask2[frame_uh,frame_w] == 255 and mask2[frame_dh,frame_w] ==255 and mask2[frame_h,frame_lw] == 255 and mask2[frame_h,frame_rw] == 255:
        color_value = 'green'
    elif mask3[frame_h,frame_w] == 255 and mask3[frame_uh,frame_w] == 255 and mask3[frame_dh,frame_w] ==255 and mask3[frame_h,frame_lw] == 255 and mask3[frame_h,frame_rw] == 255:
        color_value = 'yellow'
    return color_value