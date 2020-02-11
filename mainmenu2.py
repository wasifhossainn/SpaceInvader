import tkinter, os, sys
from tkinter import *
from tkinter import PhotoImage
import pygame as pg #import modules such as tkinter and pygame

root = Tk()
root.geometry("1080x500") #sets the size of the screen 
filename = PhotoImage(file= "assets/background.gif") #setthe background 
background_label = Label(image =filename)
background_label.place(x=0, y=0, relwidth=1, relheight=1)

#Images being defined and called from the asset folder
img = PhotoImage(file="assets/GHEY.png")
img2 = PhotoImage(file="assets/multiplayer.png") 
img3 = PhotoImage(file="assets/howtoplay.png")
img4 = PhotoImage(file="assets/exit.png")
img5 = PhotoImage(file="assets/musicbutton.png")
img6= PhotoImage(file="assets/stopmusic.png")
img7 = PhotoImage(file="assets/howtoplay2.gif")
img8 = PhotoImage(file="assets/BACKBUTTON.png")
img9= PhotoImage(file="assets/powerups2.png")
img10= PhotoImage(file="assets/powerups.gif")
img11 = PhotoImage(file= "assets/lives.png")
img12 = PhotoImage(file= "assets/points.gif")
img13 = PhotoImage(file="assets/scoreboard.png")


#Defining the buttons and main menu screen
class Main():
    def __init__(self, master):
        self.master = master
        master.title("Space Invaders") #set the title

        self.sp_button = Button(master, text="Single Player", command=self.opensp, image = img, borderwidth=0, cursor ="hand2", highlightthickness=0)
        self.sp_button.place(y= 125, x=540, anchor = "center") #creates single player button and defines the attributes

        self.mp_button = Button(master, text="MultiPlayer", command=self.openmp, image = img2, borderwidth=0, cursor ="hand2", highlightthickness=0)
        self.mp_button.place(y= 225, x=540,anchor = "center") #creates Multiplayer player button and defines the attributes

        self.powerup_button = Button(master, command = self.openpowerup, image= img9, borderwidth=0,cursor ="hand2", highlightthickness=0)
        self.powerup_button.place(y= 450, x=150,anchor = "center") #creates power up button and defines the attributes

        self.lives_button = Button(master, command = self.openlives, image= img11, borderwidth=0,cursor ="hand2", highlightthickness=0)
        self.lives_button.place(y= 450, x=930,anchor = "center") #creates ives/scores button and defines the attributes

        self.scores_button = Button(master, command = self.openscores, image= img13, borderwidth=0,cursor ="hand2", highlightthickness=0)
        self.scores_button.place(y= 450, x=250,anchor = "center") #creates scoreboard button and defines the attributes
        
        self.htp_button = Button(master, command=self.openhtp, image = img3, borderwidth=0,cursor ="hand2", highlightthickness=0)
        self.htp_button.place(y= 325, x=540,anchor = "center") #creates how to play button and defines the attributes

        self.close_button = Button(master, command=self.quit, image = img4, borderwidth=0,cursor ="hand2", highlightthickness=0)
        self.close_button.place(y= 425, x=540,anchor = "center") #creates exit button and defines the attributes

        self.playButton = Button(master, command = self.play, image= img5, borderwidth=0,cursor ="hand2", highlightthickness=0)
        self.playButton.place(y= 450, x=50,anchor = "center") #creates play music button and defines the attributes

        self.stopButton = Button(master, command = self.stop, image= img6, borderwidth=0,cursor ="hand2", highlightthickness=0)
        self.stopButton.place(y= 450, x=1030,anchor = "center") #creates stop music button and defines the attributes

#Defining the functionalities of the buttons 
    def openscores(self):       #opens scoreboard and displays top 10 scores achieved in single player mode
        os.system('top10.py') 
        
    def play(self):         #plays music on loop when play button is pressed
        pg.mixer.music.load("sfx/Laszlo Fall To Light.mp3")
        pg.mixer.music.play(loops=-1)
        pg.mixer.music.set_volume(0.2)
        

    def stop(self):         #stops music when stop button is pressed  
        pg.mixer.music.stop() 


    def opensp(self):       #opens single player mode when single player button is pressed 
        os.system('SpaceInvaderssp.py')

    def openmp(self):       #opens multiplayer mode when multiplayer button is pressed 
        os.system('SpaceInvadersmp.py')

    def openlives(self):    #opens live/score instructions when live/score button is pressed 
        self.back_button = Button(command = self.back, image = img8, borderwidth=0,cursor ="hand2", highlightthickness=0) #creates a back button and defines the attributes
        self.back_button.place(y= 463, x=540,anchor = "center")  
        background_label.config(image=img12) #replaces the main menu background with a lives/scores instructions image
        Frame.place_forget(self.scores_button) #deletes scoreboard button
        Frame.place_forget(self.lives_button) #deletes live/score button
        Frame.place_forget(self.sp_button)  #deletes single player button
        Frame.place_forget(self.mp_button) #deletes multiplayer button 
        Frame.place_forget(self.htp_button) #deletes how to play button
        Frame.place_forget(self.powerup_button) #deletes power up button
        Frame.place_forget(self.close_button) #deletes exit button
        Frame.place_forget(self.playButton) #deletes play music button
        Frame.place_forget(self.stopButton) #deletes stop music button 
 

    def openpowerup(self):  #opens power up instructions when power up button is pressed 
        self.back_button = Button(command = self.back, image = img8, borderwidth=0,cursor ="hand2", highlightthickness=0) #creates a back button and defines the attributes
        self.back_button.place(y= 463, x=540,anchor = "center")
        background_label.config(image=img10)  #replaces the main menu background with a power up information image
        Frame.place_forget(self.scores_button) #deletes scoreboard button
        Frame.place_forget(self.lives_button) #deletes live/score button
        Frame.place_forget(self.sp_button) #deletes single player button
        Frame.place_forget(self.mp_button) #deletes multiplayer button 
        Frame.place_forget(self.htp_button) #deletes how to play button
        Frame.place_forget(self.powerup_button) #deletes power up button
        Frame.place_forget(self.close_button)  #deletes exit button
        Frame.place_forget(self.playButton) #deletes play music button
        Frame.place_forget(self.stopButton) #deletes stop music button 

    def openhtp(self):  #opens how to play instructions when how to play button is pressed 
        self.back_button = Button(command = self.back, image = img8, borderwidth=0,cursor ="hand2", highlightthickness=0) #creates a back button and defines the attributes
        self.back_button.place(y= 463, x=540,anchor = "center")
        background_label.config(image=img7) #replaces the main menu background with a how to play instructions image
        Frame.place_forget(self.scores_button) #deletes scoreboard button
        Frame.place_forget(self.lives_button)   #deletes live/score button
        Frame.place_forget(self.sp_button) #deletes single player button
        Frame.place_forget(self.mp_button) #deletes multiplayer button 
        Frame.place_forget(self.htp_button)  #deletes how to play button
        Frame.place_forget(self.close_button) #deletes exit button
        Frame.place_forget(self.playButton) #deletes play music button
        Frame.place_forget(self.stopButton) #deletes stop music button
        Frame.place_forget(self.powerup_button) #deletes power up button

    def back(self): #creates a back button and defines the functions 
        self.sp_button = Button(command=self.opensp, image = img, borderwidth=0, cursor ="hand2", highlightthickness=0)
        self.sp_button.place(y= 125, x=540, anchor = "center") #displays single player button on main menu screen

        self.mp_button = Button(command=self.openmp, image = img2, borderwidth=0, cursor ="hand2", highlightthickness=0)
        self.mp_button.place(y= 225, x=540,anchor = "center") #displays single player button on main menu screen

        self.htp_button = Button(command=self.openhtp, image = img3, borderwidth=0,cursor ="hand2", highlightthickness=0)
        self.htp_button.place(y= 325, x=540,anchor = "center") #displays single player button on main menu screen

        self.close_button = Button(command=self.quit, image = img4, borderwidth=0,cursor ="hand2", highlightthickness=0)
        self.close_button.place(y= 425, x=540,anchor = "center") #displays single player button on main menu screen
        
        self.scores_button = Button(command = self.openscores, image= img13, borderwidth=0,cursor ="hand2", highlightthickness=0)
        self.scores_button.place(y= 450, x=250,anchor = "center") #displays single player button on main menu screen

        self.lives_button = Button(command = self.openlives, image= img11, borderwidth=0,cursor ="hand2", highlightthickness=0)
        self.lives_button.place(y= 450, x=930,anchor = "center") #displays single player button on main menu screen

        self.playButton = Button(command = self.play, image= img5, borderwidth=0,cursor ="hand2", highlightthickness=0)
        self.playButton.place(y= 450, x=50,anchor = "center") #displays single player button on main menu screen

        self.stopButton = Button(command = self.stop, image= img6, borderwidth=0,cursor ="hand2", highlightthickness=0)
        self.stopButton.place(y= 450, x=1030,anchor = "center") #displays single player button on main menu screen

        self.powerup_button = Button(command = self.openpowerup, image= img9, borderwidth=0,cursor ="hand2", highlightthickness=0)
        self.powerup_button.place(y= 450, x=150,anchor = "center") #displays single player button on main menu screen
        
        background_label.config(image=filename) #resets background image of the main menu 
        Frame.place_forget(self.back_button) #deletes back button on the main menu 


    def quit(self):     #exit button function 
        root.destroy() #exits the game 

root.resizable(0,0) #Disables maximising the screen
pg.init()
my_gui = Main(root)
root.mainloop()
