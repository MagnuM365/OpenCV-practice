import cv2 as cv
import numpy as np
import matplotlib.pyplot as plt

img = cv.imread('Photos/2.jpg')
img_resize = cv.resize(img, (800, 500), interpolation=cv.INTER_AREA)
cv.imshow('img', img_resize)

# gray = cv.cvtColor(img_resize, cv.COLOR_RGB2GRAY)
# cv.imshow("Gray", gray)

#grayscale histogram
# gray_hist = cv.calcHist([gray], [0], None, [256], [0,256])

# plt.figure()
# plt.title('Histogram')
# plt.xlabel('Bins')
# plt.ylabel('# of pixels')
# plt.plot(gray_hist)
# plt.xlim([0, 256])
# plt.show()

#color histogram
plt.figure()
plt.title('Color Histogram')
plt.xlabel('Bins')
plt.ylabel('# of pixels')

colors = ('b', 'g', 'r')
for i,col in enumerate(colors):
    hist = cv.calcHist([img_resize], [i], None, [256], [0,256])
    plt.plot(hist, color=col)
    plt.xlim([0, 256])
plt.show()

cv.waitKey(0)