from email import message
import imaplib
import email

def ReceiveEmail(email_address,password):
    list = []
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
            list.append(message.get('Subject'))
            print("content: ")

            for part in message.walk():
                if part.get_content_type() == "text/plain":
                    print(part.as_string())
        imap.close()
    return list