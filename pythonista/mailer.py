#import smtplib that will send said email
import smtplib 

#import the email module
#from email.message import EmailMessage
import email

textfile = input('Enter the email to be sent: ')
#we need to read the message
with open(textfile) as fp:
    #create a plain text message
    msg = EmailMessage()
    msg.set_content(fp.read())

#enter the email addresses to be used in the program 
#me == my email address
#you == your email address
msg['subject']= f'The contents of {textfile}'
msg['from']= skyskylar123098@gmail.com
msg['to']=bloomh123@gmail.com

#send the email using smtp protocol from your localhost
s=smtplib.SMTP('localhost')
s.send_message(msg)
s.quit()
