import cv2
import numpy as np

frameWidth = 640
frameHeight = 480
cap = cv2.VideoCapture(0)
cap.set(3, frameWidth)
cap.set(4, frameHeight)

def empty(a):
    pass

cv2.namedWindow("Parameters")
cv2.resizeWindow("Parameters", 640, 240)
#cv2.createTrackbar("Threshold1", "Parameters", 223, 255, empty)
#cv2.createTrackbar("Threshold2", "Parameters", 255, 255, empty)
#cv2.createTrackbar("Area", "Parameters", 40000, 70000, empty)

def getContours(img, imgContour):
    areaMin = 40000
    contours, hierarchy = cv2.findContours(img, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)
    for cnt in contours:
        area = cv2.contourArea(cnt)
        #areaMin = cv2.getTrackbarPos("Area", "Parameters")
        if area > areaMin:
            cv2.drawContours(imgContour, cnt, -1, (255, 0, 255), 7)
            peri = cv2.arcLength(cnt, True)
            approx = cv2.approxPolyDP(cnt, 0.02 * peri, True)
            x, y, w, h = cv2.boundingRect(approx)
            cv2.rectangle(imgContour, (x, y), (x+w, y+h), (0, 255, 0), 5)
            cv2.putText(imgContour, "Points: " + str(len(approx)), (x+100, y+100), cv2.FONT_HERSHEY_COMPLEX, 0.7, (0, 255, 0), 2)
            cv2.putText(imgContour, "Area: " + str(int(area)), (x+100, y+125), cv2.FONT_HERSHEY_COMPLEX, 0.7, (0, 255, 0), 2)       
            app = len(approx)
            ar = int(area)
            return app, ar
'''
def check(app, ar):
    if app == 4 and ar > 70000:
        return True
    else:
        return False
   '''
while True:
    threshold1 = 35
    threshold2 = 35
    ret, img = cap.read()
    imgContour = img.copy()
    imgBlur = cv2.GaussianBlur(img, (7, 7), 1)
    imgGray = cv2.cvtColor(imgBlur, cv2.COLOR_BGR2GRAY)

    #threshold1 = cv2.getTrackbarPos("Threshold1", "Parameters")
    #threshold2 = cv2.getTrackbarPos("Threshold2", "Parameters")
    
    imgCanny = cv2.Canny(imgGray, threshold1, threshold2)
    kernel = np.ones((5, 5))
    imgDil = cv2.dilate(imgCanny, kernel, iterations=1)

    app = getContours(imgDil, imgContour)[0]
    ar = getContours(imgDil, imgContour)[1]
    
    #app, ar = getContours(imgDil, imgContour)
    
    #check(app, ar)
    print('app: ', app)
    print('ar: ', ar)


    # imgStack = stackImages(0.8, ([img, imgCanny], [imgDil, imgContour])) #화면 붙여서 출력하는 메서드

    cv2.imshow("Result", imgContour)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
