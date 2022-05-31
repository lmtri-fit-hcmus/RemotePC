import pyautogui
from datetime import datetime

def ScreenCapture():
    myScreenshot = pyautogui.screenshot()
    now = datetime.now()
    path="Screen Capture\\"+str(now.hour)+"_"+str(now.minute)+"_"+str(now.second)+"_"+str(now.day)+"_"+str(now.month)+"_"+str(now.year)+".png"
    myScreenshot.save(path)
    # myScreenshot.save(path)
    return path