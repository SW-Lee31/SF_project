import cv2
import numpy as np #마스크 영상생성에 필요한 컬러범위 지정에 사용할 numpy 패키지를 import 합니다.

cap = cv2.VideoCapture(0)

#각 HSV별 범위
lower_white = np.array([100, 0, 200])
upper_white = np.array([255, 255, 255])
lower_yallow = np.array([20, 100, 80])
upper_yallow = np.array([60, 255, 255])
lower_black = np.array([0, 0, 0])
upper_black = np.array([255, 30, 300])
'''
count = 0
list_yallow = []
for i in range(10):
    list_yallow.append('yallow')
list_white = []
for i in range(10):
    list_white.append('white')
'''
list_color = []
def info(hsv_h, hsv_s, hsv_v):
    if hsv_h >= lower_white[0] and hsv_h <=  upper_white[0] and hsv_s >= lower_white[1] and hsv_s <= upper_white[1] and hsv_v >= lower_white[2] and hsv_v <= upper_white[2]:
        color_info = 'white'
        return color_info
    elif hsv_h >= lower_yallow[0] and hsv_h <= upper_yallow[0] and hsv_s >= lower_yallow[1] and hsv_s <= upper_yallow[1] and hsv_v >= lower_yallow[2] and hsv_v <= upper_yallow[2]:
        color_info = 'yallow'
        return color_info
    elif hsv_h >= lower_black[0] and hsv_h <=  upper_black[0] and hsv_s >= lower_black[1] and hsv_s <= upper_black[1] and hsv_v >= lower_black[2] and hsv_v <= upper_black[2]:
        color_info = 'black'
        return color_info
    else:
        color_info = 'unknown'
        return color_info

while True:
         ret, frame = cap.read()
         #입력받은 카메라 영상의 컬러 시스템을 BGR에서 HSV로 변경
         hsv= cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
         
         #화면 원래 크기 h = 240, w = 640 의 중앙점 설정
         frame_h = 240
         frame_w = 320
         
         #중앙점의 HSV 값 저장
         hsv_color_info = hsv[frame_h,frame_w]
         
         #H,S,V의 값 비교를 위한 각각의 정보 저장    
         hsv_h = hsv_color_info[0]
         hsv_s = hsv_color_info[1]
         hsv_v = hsv_color_info[2]
         
         a = str(info(hsv_h, hsv_s, hsv_v))
         print('a: ', a)
                          
         if len(list_color) < 10:
            list_color.append(a)
            #print('list_color: ', list_color)
         elif len(list_color) > 9:
            print('list_color: ', list_color)
            print('list_color.count(white): ', list_color.count('white'))
            if list_color.count('yallow') == 10:
                f =open('data.bin','wb')
                f.write(str(list_color[-1]).encode())
                f.close()
                list_color.clear()
            elif list_color.count('white') == 10:
                f =open('data.bin','wb')
                f.write(str(list_color[-1]).encode())
                f.close()
                list_color.clear()
            elif list_color.count('unknown') == 10:
                f =open('data.bin','wb')
                f.write(str(list_color[-1]).encode())
                f.close()
                list_color.clear()
            else:
                del list_color[0]
         
         cv2.imshow('image', frame)         
         
         if cv2.waitKey(1) & 0xFF == ord('q'):
                 break
cap.release()
cv2.destroyAllWindows()