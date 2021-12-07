import random
import pycryptodome
#to ensure the message is 16 bytes so that the aes encryption can work
key = input("Enter the password/ key: ")
text= input("Enter the text to be encrypted: ")
plain_text= text + (16 - len(text) % 16)*"{"
print (plain_text)
print (len(plain_text))
#we need to have an initialization vector for the key(password) a random one
iv = ''.join([chr(random.randint(0,0xFF)) for i in range (16)])
print (iv)
aes = AES.new(key, AES.MODE_CBC,iv)
encd = aes.encrypt(plain_text)
