import cv2 as cv
import matplotlib.pyplot as plt

img = cv.imread('Photos/2.jpg')

img_resize = cv.resize(img, (800, 500), interpolation=cv.INTER_AREA)

# #bgr to gray
# gray = cv.cvtColor(img_resize, cv.COLOR_BGR2GRAY)
# cv.imshow('Gray', gray)

# #bgr to hsv
# hsv = cv.cvtColor(img_resize, cv.COLOR_BGR2HSV)
# cv.imshow('HSV', hsv)

# #bgr to lab

#OpenCV uses bgr format. To use it in external environment such as matplotlib it needs to be converted to rgb

#bgr to rgb
# rgb = cv.cvtColor(img_resize, cv.COLOR_BGR2RGB)
# cv.imshow('RGB', rgb)

# plt.imshow(rgb)
# plt.show()


#Split the color channels from image

b, g, r = cv.split(img_resize)
cv.imshow('Blue', b)
cv.imshow('Green', g)
cv.imshow('Red', r)

#We can also merge as
merge = cv.merge([b,g,r])
cv.imshow('Merge_img', merge)

cv.waitKey(0)