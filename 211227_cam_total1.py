import cv2
import numpy as np

class cam_total()

    lower_white = np.array([100, 0, 200])
    upper_white = np.array([255, 255, 255])
    lower_yallow = np.array([20, 100, 80])
    upper_yallow = np.array([60, 255, 255])

    cap = cv2.VideoCapture(0)
    #frame_w = cap.set(cv2.CAP_PROP_FRAME_WIDTH,640)
    #frame_h = cap.set(cv2.CAP_PROP_FRAME_HEIGHT,480)

    def info(hsv_h, hsv_s, hsv_v):
        if hsv_h >= lower_white[0] and hsv_h <=  upper_white[0] and hsv_s >= lower_white[1] and hsv_s <= upper_white[1] and hsv_v >= lower_white[2] and hsv_v <= upper_white[2]:
            #print('white')
            color_info = 'white'
            return color_info
        elif hsv_h >= lower_yallow[0] and hsv_h <= upper_yallow[0] and hsv_s >= lower_yallow[1] and hsv_s <= upper_yallow[1] and hsv_v >= lower_yallow[2] and hsv_v <= upper_yallow[2]:
            #print('yallow')
            color_info = 'yallow'
            return color_info

    def setLabel(img, pts, label):
        (x, y, w, h) = cv2.boundingRect(pts)
        pt1 = (x, y)
        pt2 = (x + w, y + h)
        cv2.rectangle(img, pt1, pt2, (0, 255, 0), 2)
        cv2.putText(img, label, (pt1[0], pt1[1]-3), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 0, 255))

    while True:
            ret, frame = cap.read()
            # frame을 흑백으로 변환
            gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
            # frame을 hsv로 변환
            hsv= cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
            # frame 잔상처리
            dst = cv2.GaussianBlur(frame, (5, 5), 0)
            
            # gray를 적응 임계처리
            thr = cv2.adaptiveThreshold(gray, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY_INV, 21, 7)
            # thr 활용 윤곽선 검출
            contours, _ = cv2.findContours(thr, cv2.RETR_LIST, cv2.CHAIN_APPROX_SIMPLE)
            
            for cont in contours:
                approx = cv2.approxPolyDP(cont, cv2.arcLength(cont, True) * 0.02, True)
                vtc = len(approx)
                area = cv2.contourArea(cont)            
                
                if area > 100:
                    setLabel(frame, cont, str(vtc))                
                    if vtc > 3 and vtc < 6:
                        frame_h = 240
                        frame_w = 320
                        
                        hsv_color_info = hsv[frame_h,frame_w]
             
                        #색상 순서 : HSV     
                        hsv_h = hsv_color_info[0]
                        hsv_s = hsv_color_info[1]
                        hsv_v = hsv_color_info[2]
                        
                        #print('info: ',info(hsv_h, hsv_s, hsv_v))
                        a = str(info(hsv_h, hsv_s, hsv_v))
                        print('a: ', a)
                        f =open('data.bin','wb')
                        f.write(a.encode())
                        f.close()
                        break
            
            cv2.imshow('image', frame)
            #cv2.imshow('thr', thr)
            if cv2.waitKey(30) > 0:
                break

    cap.release()
    cv2.destroyAllWindows()