import cv2
import numpy as np
import pyfirmata
import time

board = pyfirmata.Arduino('/dev/ttyACM0')

servo_pin1 = 13
servo_pin2 = 12
servo_pin3 = 11
servo_pin4 = 10
servo_pin5 = 9

servo1 = board.get_pin('d:{}:s'.format(servo_pin1))
servo2 = board.get_pin('d:{}:s'.format(servo_pin2))
servo3 = board.get_pin('d:{}:s'.format(servo_pin3))
servo4 = board.get_pin('d:{}:s'.format(servo_pin4))
servo5 = board.get_pin('d:{}:s'.format(servo_pin5))

frameWidth = 640
frameHeight = 480
cap = cv2.VideoCapture(0)
cap.set(3, frameWidth)
cap.set(4, frameHeight)

# Create a Background Subtractor
bg_subtractor = cv2.createBackgroundSubtractorMOG2()

def empty(a):
    pass

cv2.namedWindow("Parameters")
cv2.resizeWindow("Parameters",480,240)
cv2.createTrackbar("Threshold1","Parameters",52,255,empty)
cv2.createTrackbar("Threshold2","Parameters",60,255,empty)
cv2.createTrackbar("Area","Parameters",6460,30000,empty)


def stackImages(scale,imgArray):
    rows = len(imgArray)
    cols = len(imgArray[0])
    rowsAvailable = isinstance(imgArray[0], list)
    width = imgArray[0][0].shape[1]
    height = imgArray[0][0].shape[0]
    if rowsAvailable:
        for x in range ( 0, rows):
            for y in range(0, cols):
                if imgArray[x][y].shape[:2] == imgArray[0][0].shape [:2]:
                    imgArray[x][y] = cv2.resize(imgArray[x][y], (0, 0), None, scale, scale)
                else:
                    imgArray[x][y] = cv2.resize(imgArray[x][y], (imgArray[0][0].shape[1], imgArray[0][0].shape[0]), None, scale, scale)
                if len(imgArray[x][y].shape) == 2: imgArray[x][y]= cv2.cvtColor( imgArray[x][y], cv2.COLOR_GRAY2BGR)
        imageBlank = np.zeros((height, width, 3), np.uint8)
        hor = [imageBlank]*rows
        hor_con = [imageBlank]*rows
        for x in range(0, rows):
            hor[x] = np.hstack(imgArray[x])
        ver = np.vstack(hor)
    else:
        for x in range(0, rows):
            if imgArray[x].shape[:2] == imgArray[0].shape[:2]:
                imgArray[x] = cv2.resize(imgArray[x], (0, 0), None, scale, scale)
            else:
                imgArray[x] = cv2.resize(imgArray[x], (imgArray[0].shape[1], imgArray[0].shape[0]), None,scale, scale)
            if len(imgArray[x].shape) == 2: imgArray[x] = cv2.cvtColor(imgArray[x], cv2.COLOR_GRAY2BGR)
        hor= np.hstack(imgArray)
        ver = hor
    return ver

def getContours(img,imgContour):
    contours, hierarchy = cv2.findContours(img, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)
    for cnt in contours:
        area = cv2.contourArea(cnt)
        perimeter = cv2.arcLength(cnt, True)
        areaMin = cv2.getTrackbarPos("Area", "Parameters")
        if area > areaMin:
            cv2.drawContours(imgContour, cnt, -1, (255, 0, 255), 7)
            peri = cv2.arcLength(cnt, True)
            approx = cv2.approxPolyDP(cnt, 0.02 * peri, True)
            #print(len(approx))
            x , y , w, h = cv2.boundingRect(approx)
            cv2.rectangle(imgContour, (x , y ), (x + w , y + h ), (0, 255, 0), 5)

            cv2.putText(imgContour, "Perimeter: " + str(int(perimeter)), (x + 20, y + 20), cv2.FONT_HERSHEY_COMPLEX, .7,
                        (0, 255, 0), 2)
            cv2.putText(imgContour, "Area: " + str(int(area)), (x + w + 20, y + 45), cv2.FONT_HERSHEY_COMPLEX, 0.7,
                        (0, 255, 0), 2)
            print("Area:",int(area))
            print("Peri:",int(perimeter))
            if perimeter > 680 and perimeter < 700:
                servo1.write(100)
                servo2.write(130)
                servo3.write(178)
                servo4.write(130)
                servo5.write(120)
                print('earphone')
                time.sleep(10)
                servo1.write(0)
                servo2.write(0)
                servo3.write(0)
                servo4.write(0)
                servo5.write(0)
                time.sleep(0.1)
                
            elif perimeter > 2400 and perimeter < 2450:
                servo1.write(106)
                servo2.write(100)
                servo3.write(147)
                servo4.write(126)
                servo5.write(105)
                print('holding ball')
                time.sleep(10)
                servo1.write(0)
                servo2.write(0)
                servo3.write(0)
                servo4.write(0)
                servo5.write(0)
                time.sleep(1)
            elif perimeter >  2800 and perimeter < 2850:
                servo1.write(116)
                servo2.write(139)
                servo3.write(174)
                servo4.write(154)
                servo5.write(132)
                print('savlon')
                time.sleep(10)
                servo1.write(0)
                servo2.write(0)
                servo3.write(0)
                servo4.write(0)
                servo5.write(0)
                time.sleep(1)
            else:
                servo1.write(0)
                servo2.write(0)
                servo3.write(0)
                servo4.write(0)
                servo5.write(0)
                time.sleep(0.1)

while True:
    success, img = cap.read()
    imgContour = img.copy()

    # Perform Background Subtraction
    fg_mask = bg_subtractor.apply(img)

    # Additional preprocessing for contour detection
    imgBlur = cv2.GaussianBlur(img, (7, 7), 1)
    imgGray = cv2.cvtColor(imgBlur, cv2.COLOR_BGR2GRAY)
    threshold1 = cv2.getTrackbarPos("Threshold1", "Parameters")
    threshold2 = cv2.getTrackbarPos("Threshold2", "Parameters")
    imgCanny = cv2.Canny(imgGray, threshold1, threshold2)
    kernel = np.ones((5, 5))
    imgDil = cv2.dilate(imgCanny, kernel, iterations=1)

    # Combine the foreground mask with the dilated Canny edge image
    imgDil[fg_mask == 0] = 0

    # Find contours on the modified image
    getContours(imgDil, imgContour)

    # Stack the original and processed images for display
    imgStack = stackImages(0.8, ([img, imgCanny],
                                 [imgDil, imgContour]))
    cv2.imshow("Result", imgStack)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
            
board.exit()
cap.release()
cv2.destroyAllWindows()
