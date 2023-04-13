import cv2

capture = cv2.VideoCapture("../Datasets/Videos_bin/dog.mp4")
c = 0
isTrue = True
while isTrue:
    isTrue, frame = capture.read()
    frame_time = 20
    cv2.waitKey(frame_time)

    cv2.imshow('Dog', frame)

capture.release()
cv2.destroyAllWindows()
