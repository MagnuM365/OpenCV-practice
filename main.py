import cv2 as cv

# img = cv.imread('Photos/2.jpg')

# img_resize = cv.resize(img, (800, 500), interpolation=cv.INTER_AREA)

# cv.imshow('car', img_resize)
# cv.waitKey(0)

def rescaleFrame(frame, scale=0.75):
    width = int(frame.shape[1] * scale)
    height = int(frame.shape[0] * scale)
    dim = (width, height)
    return cv.resize(frame, dim, interpolation=cv.INTER_AREA)

cap = cv.VideoCapture('Videos/2.mp4')
while True:
    ret, frame = cap.read()
    rescaled_vid = rescaleFrame(frame, scale=0.3)
    if ret:
        cv.imshow('Rescaled Video', rescaled_vid)
        if cv.waitKey(1) == ord('q'):
            break

cap.release() #cap.release() is used to release the video capture object
cap.destroyAllWindows()  