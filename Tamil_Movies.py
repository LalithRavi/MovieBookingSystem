'''
Created on Apr 25, 2020

@author: lalith
'''
import tkinter as tk
from tkinter import *
from tkinter import ttk
from PIL import ImageTk, Image
from tkinter import messagebox
from endhiran import *
from twenty import *
from bigil import *
from mersal import *
from pattas import *
from petta import *
from thupakki import *

class Tamil:
    
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
        
        endhiran = Endhiran(root)
        
        spacer = tk.Label(root, text = "", width = 15, bg = "#1F1B24")
        spacer.grid(row = 2, column = 2)
        
        twenty = Twenty(root)
        
        bigil = Bigil(root)
        mersal = Mersal(root)
        
        spacer = tk.Label(text = "", height = 5, bg = "#1F1B24")
        spacer.grid(row = 4, column = 1)
        
        pattas = Pattas(root)
        
        spacer = tk.Label(root, text = "", width = 15, bg = "#1F1B24")
        spacer.grid(row = 5, column = 2)
        
        petta = Petta(root)
        
        spacer = tk.Label(root, text = "", width = 15, bg = "#1F1B24")
        
        thupakki = Thupakki(root)
        
        root.protocol("WM_DELETE_WINDOW", lambda:self.__del__(root))
        root.mainloop()
    
    def __del__(self, window):
        confirm = messagebox.askyesno("Exit", "Are you sure that you want to exit the program?")
        if confirm == True:
            window.destroy()