import cv2
import numpy as np
# 0 for 1st webcam, 1 for 2nd webcam and so on...
cap=cv2.VideoCapture(0)
# Define the codec and create VideoWriter object
fourcc =cv2.VideoWriter_fourcc(*'XVID')
out = cv2.VideoWriter('output.avi',fourcc,20.0,(640,480))

while True:
    ret, frame = cap.read()                         # Capture frame-by-frame
    gray = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)   # Convert to gray
    #frame = cv2.flip(frame,0)                      # 0->inverted to 180 degree or use -ve dimension eg -180
    #out.write(frame)
    cv2.imshow('frame',frame)
    cv2.imshow('gray',gray)

    if cv2.waitKey(1) & 0xFF == ord('q'):           # Pres key 'q' to kill all windows
        break

cap.release()
#out.release()
cv2.destroyAllWindows()
