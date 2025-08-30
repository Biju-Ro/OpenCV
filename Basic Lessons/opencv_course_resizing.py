import os
import cv2

#resizing

img = cv2.imread(os.path.join(".", "data", "squirrel.jpg"))

#format is width and height
resized_img = cv2.resize(img, (640, 480))

#prints height and width
print(resized_img.shape)

cv2.imshow('image', resized_img)
cv2.waitKey(0)