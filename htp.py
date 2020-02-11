import tkinter, os, sys
from tkinter import *
from tkinter import PhotoImage
import pygame as pg

root = Tk()
root.geometry("1080x500")
filename = PhotoImage(file= "E:\Space Invaders\Backgrounds\howtoplay.gif")
background_label = Label(image =filename)
background_label.place(x=0, y=0, relwidth=1, relheight=1)




root.resizable(0,0)
pg.init()
my_gui = Main(root)
root.mainloop()
