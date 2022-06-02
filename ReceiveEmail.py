from email import message
import imaplib
import email

def ReceiveEmail(email_address,password):
    list_sub = []
    detail_list = []
    imap_server = "imap.gmail.com"

    imap = imaplib.IMAP4_SSL(imap_server)
    imap.login(email_address,password)

    imap.select("Inbox")
    #retcode, msgnums = imap.search(None,"(UNSEEN)")
    retcode, msgnums = imap.search(None,"(UNSEEN)")

    if retcode == 'OK':
        for msgnum in msgnums[0].split():
            _, data = imap.fetch(msgnum,"(RFC822)")
            
            message = email.message_from_bytes(data[0][1])

            print("Message Number:", msgnum)
            print("From: ", message.get('From'))
            print("To: ", message.get('To'))
            print("BCC: ", message.get('BCC'))
            print("Date: ", message.get('Date'))
            print("Subject: ", message.get('Subject'))
            message_num = str(msgnum)[2:-1]
            _from = message.get('From')[message.get('From').rfind('<')+1:-1]
            detail_list.append([message_num, _from,message.get('To'), message.get('Subject'), message.get('Date')])
            temp = (message.get('Subject').replace('\r\n', '')).split(' - ')
            if(temp[0]=='REGISTRY'):
                for i in temp:
                    print(i)
                miss_count = 6 - len(temp)
                for i in range(0,miss_count):
                    temp.append("")
                list_sub.append(temp)
            elif temp[0] == 'COPY FILE':
                list_sub.append(temp)
            elif temp[0] == 'LIST DIR':
                list_sub.append(temp)
            else:
                list_sub.append(message.get('Subject'))
            print("content: ")

            for part in message.walk():
                if part.get_content_type() == "text/plain":
                    print(part.as_string())
        imap.close()
    return list_sub, detail_list