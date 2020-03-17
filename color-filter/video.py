import cv2
import numpy as np
import keyboard

cap = cv2.VideoCapture(0)

while True:
	a, frame = cap.read()
	hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

	lower_red = np.array([140,50,6])
	upper_red = np.array([200,190,250])
	
	mask = cv2.inRange(hsv, lower_red, upper_red)

	#whichever is in the range will be 1, and then whichever are 1 will get original color from image
	res = cv2.bitwise_and(frame, frame, mask = mask)

	kernel = np.ones((15,15), np.float32)/225
	#smoothed = cv2.filter2D(res, -1, kernel)

	cv2.imshow('frame', frame)
#	cv2.imshow('mask', mask)
	cv2.imshow('res', res)
	#cv2.imshow('smoothed', smoothed)

	key = cv2.waitKey(1)

	if keyboard.is_pressed('q'):
		break

cv2.destroyAllWindows()
cap.release()