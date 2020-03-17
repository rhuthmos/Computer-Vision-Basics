import cv2
import numpy as np
import keyboard


img = cv2.imread('ferrari.jpg')
	
hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)

lower_red = np.array([40,20,140])
upper_red = np.array([80,160,250])

mask = cv2.inRange(img, lower_red, upper_red)

#whichever is in the range will be 1, and then whichever are 1 will get original color from image
res = cv2.bitwise_and(img, img, mask = mask)

kernel = np.ones((15,15), np.float32)/225
smoothed = cv2.filter2D(res, -1, kernel)

cv2.imshow('original', img)
#	cv2.imshow('mask', mask)
cv2.imshow('filtered', res)

cv2.waitKey(0)
cv2.destroyAllWindows()