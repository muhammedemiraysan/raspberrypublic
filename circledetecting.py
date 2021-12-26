def a(img):
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    gray_blurred = cv2.blur(gray, (3, 3))
    detected_circles = cv2.HoughCircles(gray_blurred, 
                    cv2.HOUGH_GRADIENT, 1, 20, param1 = 50,
                param2 = 30, minRadius = 10, maxRadius = 40)
    if detected_circles is not None:
        detected_circles = np.uint16(np.around(detected_circles))
        for pt in detected_circles[0, :]:
            a, b, r = pt[0], pt[1], pt[2]
            cv2.circle(gray_blurred, (a, b), 1, (0, 0, 255), 3)
            if (a, b, r) is not None:
                return a,b,r
import cv2
import numpy as np
frame = cv2.imread(smarties.png,1)
hsv = cv2.cvtColor(frame,cv2.COLOR_BGR2HSV)
lowb = np.array([50,50,50])
lowy = np.array([40, 50, 50]) 
highb = np.array([130,255,255])
highy = np.array([15, 255, 255])
maskb = cv2.inRange(hsv,lowb,highb)
masky = cv2.inRange(hsv,lowy,highy)
resb = cv2.bitwise_and(frame,frame,mask = maskb)
resy = cv2.bitwise_and(frame,frame,mask = masky)
a(resy)
a(resb)
if a(resb) is not None:
    print("blue result = ",str(a(resb)))
if a(resy) is not None:
    print("yellow result = ",str(a(resy)))
