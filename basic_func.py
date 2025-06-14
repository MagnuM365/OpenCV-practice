import cv2 as cv

img = cv.imread("Photos/2.jpg")

rescaled_img = cv.resize(img, (800, 500), interpolation=cv.INTER_AREA)
# cv.imshow("car", rescaled_img)

# convert to greyscale
gray = cv.cvtColor(rescaled_img, cv.COLOR_BGR2GRAY)
cv.imshow("Gray", gray)

# Blur image
blur = cv.GaussianBlur(rescaled_img, (7,7), cv.BORDER_DEFAULT)
cv.imshow("Blur", blur)

#Edge cascade
cascade = cv.Canny(rescaled_img, 125, 175)
cv.imshow("canny", cascade)

#Other methods - Eroding, Dilating, crop

cv.waitKey(0)