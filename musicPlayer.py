import pygame
import tkinter as tkr
from tkinter.filedialog import askdirectory
import os

#Creating application window
musicPlayer = tkr.Tk()
musicPlayer.title('Music Player') # Setting the title
musicPlayer.geometry('450x350') # setting the dimension

directory = askdirectory(); # Ask user for music directory

os.chdir(directory)  # Setting music directory to the current music directory

songlist = os.listdir() # Creating song list.

playlist = tkr.Listbox(musicPlayer, font = 'Cambria 14 bold' ,
                       bg = 'cyan',selectmode = tkr.SINGLE)  # Creating the playlist


#Adding songs from playlist
for item in songlist:
    pos = 0   # position of the song
    playlist.insert(pos, item)
    pos = pos+1

#Initialize modules    
pygame.init()
pygame.mixer.init()
    
    
def play():
    pygame.mixer.music.load(playlist.get(tkr.ACTIVE))
    #ron.set(playlist.get(tkr.ACTIVE))
    pygame.mixer.music.play()
    
def stop():
    pygame.mixer.music.stop()
    
def pause():
    pygame.mixer.music.pause()

def resume():
    pygame.mixer.music.unpause()
    
    
#Creating Buttons

Button_Play = tkr.Button(musicPlayer, height = 3, width = 5,text = 'Play Music',font = 'Cambria 14 bold',bg = 'lime green', fg = 'Black' , command = play)
Button_Stop = tkr.Button(musicPlayer, height = 3, width = 5,text = 'Stop Music',font = 'Cambria 14 bold',bg = 'red', fg = 'Black' , command = stop)
Button_Pause = tkr.Button(musicPlayer, height = 3, width = 5,text = 'Pause Music',font = 'Cambria 14 bold',bg = 'yellow', fg = 'Black' , command = pause)
Button_resume = tkr.Button(musicPlayer, height = 3, width = 5,text = 'Resume',font = 'Cambria 14 bold',bg = 'yellow', fg = 'Black' , command = resume)

Button_Play.pack(fill = 'x')
Button_Stop.pack(fill = 'x')
Button_Pause.pack(fill = 'x')
Button_resume.pack(fill = 'x')
playlist.pack(fill = 'both' , expand = 'yes')


Sng = tkr.StringVar()
songtitle = tkr.Label(musicPlayer, font = 'Cambria 12 italic' , textvariable = Sng)
songtitle.pack()


musicPlayer.mainloop()