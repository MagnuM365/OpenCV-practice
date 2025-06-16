import cv2 as cv
import numpy as np

img = cv.imread('Photos/3.jpg')
img_resize = cv.resize(img, (800, 500), interpolation=cv.INTER_AREA)
cv.imshow('img', img_resize)

gray = cv.cvtColor(img_resize, cv.COLOR_BGR2GRAY)

#convert grayscale to binary image
threshold, thresh = cv.threshold(gray, 150, 255, cv.THRESH_BINARY)
cv.imshow('Thresshold', thresh)

threshold, thresh_inv = cv.threshold(gray, 150, 255, cv.THRESH_BINARY_INV)
cv.imshow('Thresshold', thresh_inv)

#Adaptive Thresholding

adaptive_thresh = cv.adaptiveThreshold(gray, 255, cv.ADAPTIVE_THRESH_MEAN_C, cv.THRESH_BINARY, 11, 3)
cv.imshow('adaptive threshold', adaptive_thresh)
cv.waitKey(0)