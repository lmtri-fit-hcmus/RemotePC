
# import OS module
import os

def listDir(path): 
    # Get the list of all files and directories
    dir_list = os.listdir(path)
    res = ""
    for i in dir_list:
        res = res + str(i) + "\n"
    return res