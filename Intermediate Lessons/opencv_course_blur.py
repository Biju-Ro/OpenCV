import os
import cv2

img = cv2.imread(os.path.join(".", "data", "squirrel.jpg"))
noise_img = cv2.imread(os.path.join(".", "data", "noise.png"))

k_size = 11
blur_img = cv2.blur(img, (k_size,1))
gaus_img = cv2.GaussianBlur(img, (k_size,k_size), 3)
median_img = cv2.medianBlur(img, k_size)
noise_median_img = cv2.medianBlur(noise_img, k_size)

cv2.imshow('image', img)
cv2.imshow('noise_image', noise_img)
cv2.imshow('noise_median_img', noise_median_img)

#cv2.imshow('blur_img', blur_img)
#cv2.imshow('gaus_img', gaus_img)
#cv2.imshow('median_img', median_img)

cv2.waitKey(0)