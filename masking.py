import cv2 as cv
import numpy as np

img = cv.imread('Photos/3.jpg')
img_resize = cv.resize(img, (800, 500), interpolation=cv.INTER_AREA)
cv.imshow('img', img_resize)

blank = np.zeros(img_resize.shape[:2], dtype='uint8')
# cv.imshow("Blank", blank)

mask = cv.circle(blank, (img_resize.shape[1]//2,img_resize.shape[0]//2), 100, 255, -1)
# cv.imshow('Mask', mask)

masked = cv.bitwise_and(img_resize, img_resize, mask=mask)
cv.imshow('Masked', masked)


cv.waitKey(0)