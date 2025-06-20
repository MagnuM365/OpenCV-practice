import cv2 as cv
import numpy as np

people = ['Ben Afflek', 'Elton John', 'Jerry Seinfield', 'Madonna', 'Mindy Kaling']
haar_cascade = cv.CascadeClassifier('haar_face.xml')

# Load trained model
face_recognizer = cv.face.LBPHFaceRecognizer_create()
face_recognizer.read('face_trained.yml')

# Load test image
img = cv.imread(r'D:\python files\OpenCV_practice\Faces\val\ben_afflek\4.jpg')
gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)

# Detect face
faces_rect = haar_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=4)

for (x,y,w,h) in faces_rect:
    faces_roi = gray[y:y+h, x:x+w]

    label, confidence = face_recognizer.predict(faces_roi)
    print(f'Label = {people[label]} with confidence = {confidence}')

    cv.putText(img, str(people[label]), (20, 20), cv.FONT_HERSHEY_SIMPLEX, 1.0, (0,255,0), 2)
    cv.rectangle(img, (x,y), (x+w, y+h), (0,255,0), 2)

cv.imshow('Detected Face', img)
cv.waitKey(0)
