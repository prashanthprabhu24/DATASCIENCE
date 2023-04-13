import cv2

cat = cv2.imread("../Datasets/Images_bin/cat_large.jpg")

cv2.imshow('Cat', cat)

cv2.waitKey(0)