import os

def Restart():      
    os.system("shutdown /r /t 15")
    return ""

# restart = input("Do you wish to restart your computer ? (yes / no): ")
# if restart == 'no':
#     exit()
# else:
    # os.system("shutdown /r /t 1")
    # print("Reset successfully")

# import WinUtils
# WinUtils.Restart(WinUtils.SHTDN_REASON_MINOR_OTHER)

# import ctypes
# user32 = ctypes.WinDLL('user32')
# user32.ExitWindowsEx(0x00000002, 0x00000000)

# import win32api
# win32api.InitiateSystemShutdown()
