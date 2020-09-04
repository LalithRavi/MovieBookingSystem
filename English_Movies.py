'''
Created on Apr 16, 2020

@author: lalith
'''
import tkinter as tk
from tkinter import *
from tkinter import ttk
from PIL import ImageTk, Image
from tkinter import messagebox 
from endgame import *
from spiderman import *
from jumanji import *
from aladdin import *
from shazam import *
from lion import *
from fast import *

class English:
    
    def __init__(self):
        root = tk.Tk()
        root.geometry("1600x900")
        root.configure(bg = "#1F1B24")
        root.title("Cinema Spark")
        
        logo_image = ImageTk.PhotoImage(Image.open("cinespark_logo.png"))
        logo_label = tk.Label(root, image = logo_image, bg = "#1F1B24")
        logo_label.grid(row = 1, column = 4)
        
        spacer = tk.Label(root, text = "", width = 30, height = 5, bg = "#1F1B24")
        spacer.grid(row = 1, column = 0)
        
        endgame = Endgame(root)
        
        spacer = tk.Label(root, text = "", width = 15, bg = "#1F1B24")
        spacer.grid(row = 2, column = 2)
        
        spiderman = Spiderman(root)
        
        jumanji = Jumanji(root)
        aladdin = Aladdin(root)
        
        spacer = tk.Label(text = "", height = 5, bg = "#1F1B24")
        spacer.grid(row = 4, column = 1)
        
        shazam = Shazam(root)
        
        spacer = tk.Label(root, text = "", width = 15, bg = "#1F1B24")
        spacer.grid(row = 5, column = 2)
        
        lion = Lion(root)
        
        spacer = tk.Label(root, text = "", width = 15, bg = "#1F1B24")
        
        fast = Fast(root)
        
        root.protocol('WM_DELETE_WINDOW', lambda:self.__del__(root))
        root.mainloop()
        
    def __del__(self, root):
        confirm = messagebox.askyesno("Exit", "Are you sure that you want to exit the program?")
        if confirm == True:
            root.destroy()