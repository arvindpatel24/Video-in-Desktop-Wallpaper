import cv2
import ctypes
import time
for i in range(1,1500):
    path = 'C:\\Users\\Ravi\\Desktop\\2020 Projects\\Project4_Vedio_in_Desktop_Wallpaper\\images\\'+str(i)+'.jpg'
    ctypes.windll.user32.SystemParametersInfoW(20, 0, path , 0)
    time.sleep(0.13)