import smtplib, ssl
import getpass

port = 465 #for ssl
smtp_server = "smtp.gmail.com"
sender_email = "bloomh123@gmail.com"
receiver_email = input("Enter the email address of the receiver: ")
message = input("write the message: ")
password = getpass.getpass(prompt ="Type in your password then press enter: ",stream = None)


#create a secure ssl context
context = ssl.create_default_context()

with smtplib.SMTP_SSL(smtp_server, port, context=context) as server:
    server.login(sender_email, password)

    #send email here
    server.sendmail(sender_email,receiver_email,message)