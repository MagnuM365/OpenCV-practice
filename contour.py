import cv2 as cv
import numpy as np

img = cv.imread('Photos/2.jpg')

img_resize = cv.resize(img, (800, 500), interpolation=cv.INTER_AREA)
# cv.imshow('car', img_resize)

blank = np.zeros(img_resize.shape, dtype='uint8')

gray = cv.cvtColor(img_resize, cv.COLOR_BGR2GRAY)
cv.imshow('Gray car', gray)

# canny = cv.Canny(img_resize, 125, 175)
# cv.imshow("Canny", canny)

ret, thresh = cv.threshold(gray, 125, 255, cv.THRESH_BINARY)
cv.imshow("Thresh", thresh)

contours, hierarchy = cv.findContours(thresh, cv.RETR_TREE, cv.CHAIN_APPROX_SIMPLE)

cv.drawContours(blank, contours, -1, (0,255,0), 1)
cv.imshow("Contour", blank)

print(f'{len(contours)}')

cv.waitKey(0)