# This code is used to open an image file, using cv2.imread as well as copying its roi and pasting it to the image itself.
import numpy as np
import cv2

img = cv2.imread('t1.png', cv2.IMREAD_COLOR) 

'''img[55,55]=[255,255,255]  ##location at 55,55 gets color value 255,255,255 i.e. white
px= img[55,55]
print(px)'''              #printing color of img using px

## roi -> Regoin of image/interest 

img[100:150, 100:150] = [255,255,255]
'''roi= img[100:150, 100:150]
print (roi)'''             #printing region of img using roi datatype

tool_face= img[250:350, 280:380]
img[0:100, 0:100]= tool_face # 111-37= 74 (total pixel) 194-107=87(total pixel)

cv2.imshow('img',img)
cv2.waitKey(0)
cv2.destroyAllWindows()
