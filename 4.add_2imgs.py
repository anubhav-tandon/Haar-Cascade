import cv2
import numpy as np

img1= cv2.imread('3D-Matplotlib.png')
img2= cv2.imread('mainsvmimage.png')

add= img1 + img2               ##No loss of opagueness but orginal color of img1 dot chnges to yellow

add1= cv2.add(img1,img2)       #add pixel values
# (155,211,79) + (50,170,200) = 205,381,279...translated to (205,255,255) i.e white color

weighted= cv2.addWeighted(img1, 0.6,img2, 0.4, 0) #opagueness added 0.6 i.e 60% of img1 and 40% of img2 (where last value in func is gamma value set to 0)

cv2.imshow('add',add)
cv2.imshow('add1',add1)
cv2.imshow('img1',img1)
cv2.imshow('img2',img2)
cv2.imshow('weighted',weighted)
cv2.waitKey(0)
cv2.destroyAllWindows()

























