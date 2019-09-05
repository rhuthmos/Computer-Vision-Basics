import numpy as np
import cv2
import matplotlib.pyplot as plt


img = cv2.imread('iiitd.jpg')
img2 = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

clahe = cv2.createCLAHE()

cl1 = clahe.apply(img2)

#cv2.imshow('clahe image', cl1)
#cv2.imshow('original image', img2)

images = [img2, cl1]
titles = ['original','equalized']

for i in range(2):
    plt.subplot(2,2,i+1),plt.imshow(images[i],'gray')
    plt.title(titles[i])
    plt.xticks([]),plt.yticks([])

plt.subplot(2,2,3),plt.hist(img2.flatten(), 256, [0,256], color = 'r')
plt.xlim([0,256])
plt.subplot(2,2,4),plt.hist(cl1.flatten(), 256, [0,256], color = 'r')
plt.xlim([0,256])
plt.show()

