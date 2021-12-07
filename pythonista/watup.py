import pygame # we'll use its sound component
import tkinter as tk # we'll use it for our gui since i'm yet to learn  pyqt5
import os #so that we can be able to interact with the operating system directly
from tkinter.filedialog import askdirectory #it permits to select directory
#from playsound import playsound

#create the window of the music player
music_player = tk.Tk()#creates the window
music_player.title("Musica es Bonito")#title of the window
music_player.geometry("450x350")

#create a dir that prompts the user to choose the folder where the music files are listed with the help of the os module
directory = askdirectory()
os.chdir(directory)#permits to change the current dir
song_list = os.listdir()# it returns the list of songs

#the variable called play_list brings the interface to display the items to the user
play_list = tk.Listbox(music_player, font = "Helvetica 12 bold",bg = "pink",selectmode=tk.SINGLE)

#the loop will push the program to select each item from the song_list and insert them into the listbox
for item in song_list:
    pos = 0
    play_list.insert(pos, item)
    pos +=1

#loading and playing sounds using pygame
pygame.init()
pygame.mixer.init()

#functions to control the music player
def play():
    # pygame.mixer.music.play(play_list.get(tk.ACTIVE))
    #pygame.mixer.music.load(play_list.get(tk.ACTIVE))
    #var.set(play_list.get(tk.ACTIVE))
    #pygame.mixer.music.play()
    #playsound('')

def stop():
    pygame.mixer.music.stop()

def pause():
    pygame.mixer.music.pause()

def unpause():
    pygame.mixer.music.unpause()

# create the buttons for the interface of the music player
Button1 = tk.Button(music_player, width = 5, height = 3, font ="Helvetica 12 bold", text = "PLAY", command=play, bg="purple",fg="blue")
Button2 = tk.Button(music_player, width=5, height=3, font="Helvetica 12 bold", text="STOP", command=stop, bg="red", fg="white")
Button3 = tk.Button(music_player, width=5, height=3, font="Helvetica 12 bold", text="PAUSE", command=pause, bg="blue", fg="white")
Button4 = tk.Button(music_player, width=5, height=3, font="Helvetica 12 bold", text="UNPAUSE", command=unpause, bg="orange", fg="white")

var = tk.StringVar()
song_title = tk.Label(music_player,font ="Helvetica 12 bold", textvariable=var)

song_title.pack()
Button1.pack(fill="x")
Button2.pack(fill="x")
Button3.pack(fill="x")
Button4.pack(fill="x")

play_list.pack(fill="both", expand="yes")

music_player.mainloop()
