import ReceiveEmail
import SendEmail
import ListProcesses

client_address = "client1.computernetwork@gmail.com"
client_pass="computernetwork" #unsecure

guess_address = "lmtri.fit.hcmus@gmail.com"

def Handling(subject):
    if subject == 'List Processes':
        content = ListProcesses.ListProcesses()
        SendEmail.SendEmail(content,client_address,client_pass,guess_address,subject,'text')
    elif subject == "demo send picture":
        content = "test.jpg"
        SendEmail.SendEmail(content,client_address,client_pass,guess_address,subject,'image')
def main():
    while True:
        #Nhận danh sách title của các thư "CHƯA ĐỌC"
        # list = ReceiveEmail.ReceiveEmail(client_address,client_pass)
        # if len(list):
        #     for i in list:
        #         #Xử lý các title tương ứng
        #         Handling(i)
        # else:
        #     print("Không có thư nào chưa đọc")
        # break
        Handling("demo send picture")
        break

#======================================================

main()