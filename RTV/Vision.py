import cv2
import numpy as np #마스크 영상생성에 필요한 컬러범위 지정에 사용할 numpy 패키지를 import 합니다.

cap = cv2.VideoCapture(0)
color_value = 'null'

#각 HSV별 범위
lower_red = np.array([150, 50, 50])
upper_red = np.array([180, 255, 255])

lower_blue = np.array([90, 200, 200])
upper_blue = np.array([150, 255, 255])

lower_green = np.array([45, 75, 150])
upper_green = np.array([85, 110, 255])

lower_yellow = np.array([25, 130, 200])
upper_yellow = np.array([40, 160, 255])

list_color = []
def info(hsv_h, hsv_s, hsv_v):
    if hsv_h >= lower_yellow[0] and hsv_h <=  upper_yellow[0] and hsv_s >= lower_yellow[1] and hsv_s <= upper_yellow[1] and hsv_v >= lower_yellow[2] and hsv_v <= upper_yellow[2]:
        color_info = 'yellow'
        return color_info    
    elif hsv_h >= lower_blue[0] and hsv_h <= upper_blue[0] and hsv_s >= lower_blue[1] and hsv_s <= upper_blue[1] and hsv_v >= lower_blue[2] and hsv_v <= upper_blue[2]:
        color_info = 'blue'
        return color_info
    elif hsv_h >= lower_green[0] and hsv_h <=  upper_green[0] and hsv_s >= lower_green[1] and hsv_s <= upper_green[1] and hsv_v >= lower_green[2] and hsv_v <= upper_green[2]:
        color_info = 'green'
        return color_info
    elif hsv_h >= lower_red[0] and hsv_h <=  upper_red[0] and hsv_s >= lower_red[1] and hsv_s <= upper_red[1] and hsv_v >= lower_red[2] and hsv_v <= upper_red[2]:
        color_info = 'red'
        return color_info

def fwrite(list_color):
    f =open('data.bin','wb')
    f.write(str(list_color[-1]).encode())
    f.close()
    list_color.clear()

def processCam():
    global color_value
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

    '''
    print('hsv_h', hsv_h)
    print('hsv_s', hsv_s)
    print('hsv_v', hsv_v)
    '''


    if a == 'belt':
        color_value = 'null'
        pass
    elif len(list_color) < 3:
        list_color.append(a)
    elif len(list_color) >= 3:
        if list_color.count('red') == 3:
            color_value = 'red'
            #print(color_value)
            list_color.clear()
            #fwrite(list_color)
        elif list_color.count('blue') == 3:
            color_value = 'blue'
            #print('blue')
            list_color.clear()
            #fwrite(list_color)
        elif list_color.count('green') == 3:
            color_value = 'green'
            #print(color_value)
            list_color.clear()
            #fwrite(list_color)
        elif list_color.count('yellow') == 3:
            color_value = 'yellow'
            #print('yellow')
            list_color.clear()
            #fwrite(list_color)
        else:
            del list_color[0]
            color_value = 'null'
    return color_value
    '''
    cv2.imshow('image', frame)
    
    cv2.imshow('hsv', hsv)
    
    if cv2.waitKey(1) & 0xFF == ord('q'):
         break
    cap.release()
    cv2.destroyAllWindows()
    '''