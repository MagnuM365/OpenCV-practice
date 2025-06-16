import cv2 as cv
import numpy as np

img = cv.imread('Photos/3.jpg')
img_resize = cv.resize(img, (800, 500), interpolation=cv.INTER_AREA)
cv.imshow('img', img_resize)

gray = cv.cvtColor(img_resize, cv.COLOR_BGR2GRAY)

#laplacian method
lap = cv.Laplacian(gray, cv.CV_64F)
lap = np.uint8(np.absolute(lap))
cv.imshow('Laplacian', lap)

#sobel
sobelx = cv.Sobel(gray, cv.CV_64F, 1,0)
sobely = cv.Sobel(gray, cv.CV_64F, 0,1)
combined = cv.bitwise_or(sobelx, sobely)
cv.imshow('Sobel combined', combined)

#most popular
canny = cv.Canny(gray, 150, 175)
cv.imshow('canny', canny)


cv.waitKey(0)