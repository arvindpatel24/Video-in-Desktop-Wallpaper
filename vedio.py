import numpy as np
import cv2
import time
import os
import ctypes

cap = cv2.VideoCapture('Shakira-Waka Waka.mp4')
index = 0
while(cap.isOpened()):
    index = index +1
    ret, frame = cap.read()
    cv2.imwrite('images/'+str(index)+'.jpg',frame)
        
#     path = 'C:\\Users\\Ravi\\Desktop\\LCO\\Day 13\\'+str(index)+'.jpg'
#     ctypes.windll.user32.SystemParametersInfoW(20, 0, path , 0)

#     gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    cv2.imshow('frame',frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()