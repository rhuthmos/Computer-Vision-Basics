import cv2, time
import keyboard
#external camera
video = cv2.VideoCapture(0)
a = 0


while (True):
	a = a + 1

	#frame
	check, frame = video.read()

	print(frame)
	#showing framee
	cv2.imshow("Capturing", frame)

	# keyboard input
	key = cv2.waitKey(1)

	if keyboard.is_pressed('q'):
		break
print(a)

# release everything
video.release()

cv2.destroyAllWindows