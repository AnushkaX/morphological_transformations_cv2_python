import cv2
import numpy as np

img = cv2.imread("Images/morph.jpg",0)
bin_img = cv2.threshold(img, 127, 255, cv2.THRESH_BINARY_INV)[1]

img1 = cv2.imread("Images/closing.png",0)
bin_img1 = cv2.threshold(img1, 127, 255, cv2.THRESH_BINARY)[1]

cv2.imshow('bin', bin_img)

kernel = np.ones((5,5),np.uint8)


#Erosion
ero_img = cv2.erode(bin_img, kernel)
cv2.imshow('erode', ero_img)

#Dilation
dil_img = cv2.dilate(bin_img, kernel)
cv2.imshow('dilate', dil_img)

dil_img_2 = cv2.dilate(bin_img, cv2.getStructuringElement(cv2.MORPH_CROSS,(11,11)))
cv2.imshow('dilate cross', dil_img_2)

#Gradient
gradient = cv2.morphologyEx(bin_img, cv2.MORPH_GRADIENT, kernel)
cv2.imshow('Gradient', gradient)

#Opening
opening = cv2.morphologyEx(bin_img, cv2.MORPH_OPEN, kernel)
cv2.imshow('Opening', opening)

#Closing
closing = cv2.morphologyEx(img1, cv2.MORPH_CLOSE, kernel)
cv2.imshow('Closing', closing)



cv2.waitKey(0)
cv2.destroyAllWindows()
