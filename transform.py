import cv2 as cv
import numpy as np

img = cv.imread('Photos/3.jpg')

img_resize = cv.resize(img, (800, 500), interpolation=cv.INTER_AREA)
# cv.imshow('car', img_resize)

#translation

tx = 100
ty = 100

mat = np.float32([[1, 0, tx],
                  [0, 1, ty]])

h = img_resize.shape[0]
w = img_resize.shape[1]

translate = cv.warpAffine(img_resize, mat, (w, h))
# cv.imshow("car", translate)

#Rotation

center = (w // 2, h // 2)
angle = 180
scale = 1.0
Mat = cv.getRotationMatrix2D(center, angle, scale)
rotate = cv.warpAffine(img_resize, Mat, (w, h))
# cv.imshow("car", rotate)

#flip image

flip = cv.flip(img_resize, 0)
cv.imshow("flip", flip)


cv.waitKey(0)