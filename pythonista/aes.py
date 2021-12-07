#import pyaes that implements the symmetric key encryption algorithm
import pyaes
#import pbkdf2 that implements the password to key derivation algorithm
import pbkdf2, binascii, os
#import secret which helps in generating secure random numbers for managing secrets
import secrets
#import tkinter for the gui
import tkinter as Tk

# derive a 256-bit aes encryption key from the password
password = "s3cr3t*c0d3"

#generate a random salt which you'll have to save otherwise the encryption will be unbreakable
passwordsalt = os.urandom(16)
key = pbkdf2.PBKDF2(password, passwordsalt).read(32)

#makes the encryption key a hexadecimal thing
print ('AES encryption key: ',binascii.hexlify(key))

# we'll then generate a random 256-bit initial vector
# it'll return an int with 256 random bits
iv = secrets.randbits(256)

# enter the plain text that will be encrypted
plaintext = "Text for encryption"
aes = pyaes.AESModeOfOperationCTR(key, pyaes.Counter(iv))
ciphertext = aes.encrypt(plaintext)
print('Encrypted: ',binascii.hexlify(ciphertext))
