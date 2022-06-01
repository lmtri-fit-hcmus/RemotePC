import os
 
def Shutdown(): 
    os.system("shutdown /s /t 1")
    return ""
    # shutdown = input("Do you wish to shutdown your computer ? (yes / no): ")
  
    # if shutdown == 'no':
    #     exit()
    # else:
        

# import time
# import subprocess

# def Shutdown():
#     subprocess.call(["shutdown.exe","-f","-s","-t","26"])
    
# import os
# print("REBOOTING")
# os.system("shutdown -t 0 -r -f")
