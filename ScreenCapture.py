import pyautogui
import os
from datetime import datetime

def ScreenCapture():
    myScreenshot = pyautogui.screenshot()
    now = datetime.now()
    path="Screen Capture\\"+str(now.hour)+""+str(now.minute)+""+str(now.second)+""+str(now.day)+""+str(now.month)+"_"+str(now.year)+".png"
    if not os.path.exists("Screen Capture"):
      os.mkdir("Screen Capture")
    myScreenshot.save(path)
    # myScreenshot.save(path)
    return path