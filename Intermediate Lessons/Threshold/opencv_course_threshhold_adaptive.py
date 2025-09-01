import os
import cv2

img = cv2.imread(os.path.join(".", "data", "writing.png")) 

#convert to gray
img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

#apply adaptive threshold
thresh = cv2.adaptiveThreshold(img_gray, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, 11, 6)

cv2.imshow('image', thresh)
cv2.imshow('img_image', img)
cv2.waitKey(0)
