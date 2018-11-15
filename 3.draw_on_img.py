# In this file we will draw some shapes and put some text on the image file.
import cv2
import numpy as np

img = cv2.imread('t1.png',cv2.IMREAD_COLOR)

cv2.line(img,(0,0), (800,800), (0,255,0), 15)    ##bgr green
cv2.rectangle(img,(0,0), (250,150), (0,0,255), 5)
cv2.circle(img,(100,63), 55, (255,0,0), -1)

pts=np.array([[10,5],[20,30],[70,20],[50,10]], np.int32)  ##np.int32->datatype
#pts = pts.reshape((-1,1,2))
cv2.polylines(img, [pts], True, (0,255,255),4)

font = cv2.FONT_HERSHEY_SIMPLEX
cv2.putText(img, 'Hello!', (0,130), font, 1,(200,255,255), 2,cv2.LINE_AA )

cv2.imshow('image',img)
cv2.waitKey(0)
cv2.destroyAllWindows()

  
