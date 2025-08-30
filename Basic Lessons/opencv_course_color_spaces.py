import os
import cv2

img = cv2.imread(os.path.join(".", "data", "squirrel.jpg")) 

rgb_img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
gray_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
hsv_img = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)

cv2.imshow('image', img)
cv2.imshow('image_rgb', rgb_img)
cv2.imshow('gray_img', gray_img)
cv2.imshow('hsv_img', hsv_img)
cv2.waitKey(0)  
