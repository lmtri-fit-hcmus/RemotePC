import cv2
import os
from datetime import datetime
def WebcamCapture():
    cam = cv2.VideoCapture(0)
    # cv2.namedWindow("Computer Network Capture")


    ret,frame = cam.read()
    if not ret:
        print("failed to grab frame")
        return
    if not os.path.exists("Webcam Capture"):
      os.mkdir("Webcam Capture")

    now = datetime.now()
    path="Webcam Capture\\"+str(now.hour)+""+str(now.minute)+""+str(now.second)+""+str(now.day)+""+str(now.month)+"_"+str(now.year)+".png"

    cv2.imwrite(path,frame) 
    print("Capture successfully")
    return path
