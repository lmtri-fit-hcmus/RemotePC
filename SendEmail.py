import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.application import MIMEApplication
from os.path import basename
from email.mime.text import MIMEText
from email.mime.image import MIMEImage
def SendEmail(mail_content, sender_address,sender_pass, receiver_address, mail_subject,type):

    #Setup the MIME
    message = MIMEMultipart()
    message['From'] = sender_address
    message['To'] = receiver_address
    if isinstance(mail_subject, list):
        subject = ' - '.join(mail_subject)
        message['Subject'] = subject 
    else: message['Subject'] = mail_subject 
    #The body and the attachments for the mail
    if(type == "text"):
        message.attach(MIMEText(mail_content, 'plain'))
    elif type == "image":
        #image_section
        image_open = open(mail_content,'rb').read( )
        image_ready = MIMEImage(image_open,'jpg',name = 'Picture')
        message.attach(image_ready)
    elif type =="file":
        with open(mail_content, "rb") as fil:
            part = MIMEApplication(fil.read(), Name=basename(mail_content) )
        # After the file is closed
        part['Content-Disposition'] = 'attachment; filename="%s"' % basename(mail_content)
        message.attach(part)
    session = smtplib.SMTP('smtp.gmail.com', 587) #use gmail with port
    session.starttls() #enable security
    session.login(sender_address, sender_pass) #login with mail_id and password
    text = message.as_string()
    session.sendmail(sender_address, receiver_address, text)
    session.quit()
    print('Mail Sent')  