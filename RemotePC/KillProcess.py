import os
 
def KillProcess(name):
    os.system("taskkill /f /im " + name)
    return "Kill process successfully"