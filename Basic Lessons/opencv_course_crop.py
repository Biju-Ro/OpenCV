import os
import cv2

#crop

img = cv2.imread(os.path.join(".", "data", "squirrel.jpg"))

cropped_img = img[300:600, 400:800]

print(img.shape)
print(cropped_img.shape)

cv2.imshow('image', img)
cv2.imshow('image2', cropped_img)
cv2.waitKey(0)