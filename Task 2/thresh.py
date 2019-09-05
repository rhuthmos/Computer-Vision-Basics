import cv2
import numpy as np
import matplotlib.pyplot as plt

img = cv2.imread('hand.jpg')
retval, threshold = cv2.threshold(img, 95 , 255, cv2.THRESH_BINARY)

grayscaled = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
retval2, threshold2 = cv2.threshold(grayscaled, 100 , 255, cv2.THRESH_BINARY)
ret, thresh3 = cv2.threshold(grayscaled, 140, 255, cv2.THRESH_TRUNC)
ret, thresh4 = cv2.threshold(grayscaled, 100, 255, cv2.THRESH_TOZERO)


gauss = cv2.adaptiveThreshold(grayscaled, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, 101, 5)
mean = cv2.adaptiveThreshold(grayscaled, 255, cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY, 101, 5)


retval3, otsu = cv2.threshold(grayscaled, 0 , 255, cv2.THRESH_BINARY+cv2.THRESH_OTSU)

blur = cv2.GaussianBlur(grayscaled,(5,5),0)
retval4, otsu2 = cv2.threshold(blur, 0 , 255, cv2.THRESH_BINARY+cv2.THRESH_OTSU)


images = [grayscaled, threshold2,thresh3,thresh4, gauss, mean, otsu, otsu2]
titles = ['original(grayscaled)', 'Binary', 'truncated','to-zero','adaptive-gauss','adaptive mean', 'otsu', 'otsu after gaussian-blur']

for i in range(8):
    plt.subplot(3,3,i+1),plt.imshow(images[i],'gray')
    plt.title(titles[i])
    plt.xticks([]),plt.yticks([])
plt.show()