import cv2
import os 

#read image
image_path = os.path.join(".", "data", "squirrel.jpg")

img = cv2.imread(image_path)

#wrtite image

cv2.imwrite(os.path.join(".", "data", "squirrel_out.jpg"), img)

#show image

cv2.imshow('image', img)
cv2.waitKey(0)