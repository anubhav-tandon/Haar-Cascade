import cv2
import numpy as np

img1= cv2.imread('3D-Matplotlib.png')
img2= cv2.imread('mainlogo.png')

rows,cols,channels = img2.shape
roi = img1[0:rows,0:cols]

img2gray = cv2.cvtColor(img2, cv2.COLOR_BGR2GRAY)
ret, mask = cv2.threshold(img2gray, 220, 255, cv2.THRESH_BINARY_INV) # if pixel grtr thn 220 convert to 255(white) else 0(black) and then INV (inverse it) tht means first lighter portion becomes white then inversed to black.
# TRUE = 255 False=0 
mask_inv = cv2.bitwise_not(mask) #bg=white img=black whereas mask=->bg=black detected img=white

img1_bg = cv2.bitwise_and(roi, roi, mask=mask_inv)
img2_fg = cv2.bitwise_and(img2, img2, mask=mask)

dst= cv2.add(img1_bg, img2_fg)
img1[0:rows,0:cols] = dst

cv2.imshow('img1',img1)
cv2.imshow('img2gray',img2gray)
cv2.imshow('img2',img2)
cv2.imshow('mask',mask)
cv2.imshow('mask_inv',mask_inv)
cv2.waitKey(0)
cv2.destroyAllWindows() 
