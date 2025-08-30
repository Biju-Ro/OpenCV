import os
import cv2

img = cv2.imread(os.path.join(".", "data", "writing.png")) 

img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY, img)
ret, thresh = cv2.threshold(img_gray, 88, 255, cv2.THRESH_BINARY)

thresh = cv2.blur(thresh, (7,7))
ret, thresh = cv2.threshold(thresh, 88, 255, cv2.THRESH_BINARY)



cv2.imshow('image', img)
cv2.imshow('thresh', thresh)
cv2.waitKey(0)