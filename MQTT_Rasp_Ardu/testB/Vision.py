import cv2
import numpy as np

frameWidth = 640
frameHeight = 480
cap = cv2.VideoCapture(0)
cap.set(3, frameWidth)
cap.set(4, frameHeight)

def empty(a):
    pass

def getContours(img, imgContour):
    areaMin = 40000
    contours, hierarchy = cv2.findContours(img, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)

    for cnt in contours:
        area = cv2.contourArea(cnt)
        if area > areaMin:
            cv2.drawContours(imgContour, cnt, -1, (255, 0, 255), 7)
            peri = cv2.arcLength(cnt, True)
            approx = cv2.approxPolyDP(cnt, 0.02 * peri, True)
            x, y, w, h = cv2.boundingRect(approx)
            cv2.rectangle(imgContour, (x, y), (x+w, y+h), (0, 255, 0), 5)
            cv2.putText(imgContour, "Points: " + str(len(approx)), (x+100, y+100), cv2.FONT_HERSHEY_COMPLEX, 0.7, (0, 255, 0), 2)
            cv2.putText(imgContour, "Area: " + str(int(area)), (x+100, y+125), cv2.FONT_HERSHEY_COMPLEX, 0.7, (0, 255, 0), 2)
            app = len(approx)
            ar = area
            return [app, ar]



def cheakArea():
    threshold1 = 30
    threshold2 = 30
    ret, img = cap.read()
    imgContour = img.copy()
    imgroi = img[0:480, 120:520].copy()
    imgBlur = cv2.GaussianBlur(imgroi, (7, 7), 1)
    imgGray = cv2.cvtColor(imgBlur, cv2.COLOR_BGR2GRAY)
    imgCanny = cv2.Canny(imgGray, threshold1, threshold2)
    kernel = np.ones((5, 5))
    imgDil = cv2.dilate(imgCanny, kernel, iterations=1)
    
    if getContours(imgDil, imgroi) != None:
        app = getContours(imgDil, imgContour)[0]
        ar = getContours(imgDil, imgContour)[1]
        if app == 4 and ar >49000:
            return True
        else:
            return False
    else:
        pass