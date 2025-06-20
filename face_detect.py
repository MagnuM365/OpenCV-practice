import cv2 as cv

image = cv.imread('Photos/women2.jpg')

img = cv.resize(image, (700, 500), interpolation=cv.INTER_AREA)
# cv.imshow('women', img)

#convert to gray
gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
cv.imshow('women', gray)

haar_cascade = cv.CascadeClassifier('haar_face.xml')
faces_rect = haar_cascade.detectMultiScale(gray, scaleFactor=1.2, minNeighbors=10)
print(f'no.={faces_rect}')
print(f'no.={len(faces_rect)}')

for(x,y,w,h) in faces_rect:
    cv.rectangle(img, (x,y), (x+w, y+h), (0,255,0), thickness=2)

cv.imshow('face_detect', img)

cv.waitKey(0)