#import the required libraries/modules
import math
import random
import tkinter as tk

print(" Hola amiga!!¡\n Choose the range you wish to guess: \n 1. 1 to 10\n 2. 1 to 100\n 3. 1 to 50 ")
ranger=int(input(" :"))

if ranger == 1:
        number= random.randint(1,10)
        print(" you picked option 1")
elif ranger == 2:
        number = random.randint(1,100)
        print(" you picked option 2")
elif ranger == 3:
        number = random.randint(1,50)
        print("you picked option 3")
else:
        print(" Enter a valid number :-(")




def guessing(number,ranger):
    while True:
        count = 1
        print(" you have three guesses\n begineth:")
        guess = int(input("guess ", count)
        if guess == number:
           pass



#guessing(number,ranger)

