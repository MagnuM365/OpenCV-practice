import cv2 as cv
import numpy as np

#Create blank display
blank = np.zeros((500, 800, 3), dtype="uint8")
# cv.imshow("blank", blank)


#Draw a rectangle
cv.rectangle(blank, (10, 10), (500, 300), (255, 0, 0), thickness=cv.FILLED)
# cv.imshow("rectangle", blank)

#Draw a circle
cv.circle(blank, (200, 300), 100, (0, 255, 0), thickness=2)
# cv.imshow("Circle", blank)


#Write text
cv.putText(blank, 'Hello, World', (200, 300), cv.FONT_HERSHEY_DUPLEX, 1.0, (255,255,255), 2)
cv.imshow('Draw', blank)

cv.waitKey(0)