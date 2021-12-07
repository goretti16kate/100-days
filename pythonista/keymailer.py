import cv2
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders


#open the camera video node to access the see3CAM_130(cameras that are uvc compliant that has plug and play support and
# does not reqire to install additional device drivers manually)
#open the device at ID 0
cap =cv2.VideoCapture(0)

# check if the user selected camera is open successfully

if not (cap.isOpened()):
    print("Could not open video device")

# to set the resolution
#frame_width = cap.set(cv2.CAP_PROP_FRAME_WIDTH, 640) 
#frame_height = cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 480)

frame_width =int(cap.get(3))
frame_height = int(cap.get(4)) 
size = (frame_width, frame_height)

#videowriter object will create a frame of above defined the output is stored in 'filename.avi' file
result = cv2.VideoWriter('filename.mp4', cv2.VideoWriter_fourcc(*'mp4v'),10 , size)

#grab the frame continuously from the camera and show it in the preview window

while(True):
    #capture frame-by-frame
    ret, frame = cap.read()
    if ret == True :

        #write the frame into the file
        result.write(frame)

    #print (frame)
    #display the resulting frame
        cv2.imshow("preview", frame) 

    #waits for the user to input 'q' to quit the application

        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    else:
        break

#release the camera 
cap.release()
result.release()
        
cv2.destroyAllWindows()
# we'll use the MIME module to make it more flexible ,it's also needed to set the attachment with the mail 
mail_content = ''' Hello,
This is a test mail.
in this mail we are sending some attachments.
The mail is sent using python SMTP library.
Thank you.
'''
#the mail addresses and password
sender_email = 'bloomh123@gmail.com'
sender_pass = input('Enter your password sender: ')
receiver_email = 'gorettikate@gmail.com'

#setup the MIME
message = MIMEMultipart()

message['From'] = sender_email
message['To'] = receiver_email
message['Subject'] = 'A test mail using python. It has an attachment'

# the subject line 
# The body and attachments for the mail
message.attach(MIMEText(mail_content, 'plain'))
attach_file_name = 'filename.mp4'
attach_file = open (attach_file_name,'rb') # open the file as binary mode

#read the byte stream
payload = MIMEBase('application', 'octate-stream')
payload.set_payload((attach_file).read())


#encode the attachment using base64 encoding scheme
encoders.encode_base64(payload)
#add header for the attachment 
payload.add_header('content-decomposition', 'attachment', filename = attach_file_name)
message.attach(payload)
#create smtp session for sending 
session =smtplib.SMTP('smtp.gmail.com', 587)#use gmail with port 587 since we're using transport layer security

#enable security
session.starttls()

#login with mail_id and password
session.login(sender_email,sender_pass)

text = message.as_string()
session.sendmail(sender_email, receiver_email, text)
session.quit()
print ("Mail Sent")


