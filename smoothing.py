import cv2 as cv

img = cv.imread('Photos/5.jpg')

img_resize = cv.resize(img, (800, 500), interpolation=cv.INTER_AREA)

#Averaging
# average = cv.blur(img_resize, (5,5))
# cv.imshow('average_blur', average)

# #Gaussian blur
# g_blur = cv.GaussianBlur(img_resize, (7,7), 0)
# cv.imshow('G_blur', g_blur)

# #Median blur
# median = cv.medianBlur(img_resize, 3)
# cv.imshow('median', median)

#Bilateral
bilateral = cv.bilateralFilter(img_resize, 10, 35, 35)
cv.imshow('Bilateral', bilateral)

cv.waitKey(0)