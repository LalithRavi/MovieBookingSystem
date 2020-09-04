'''
Created on Apr 25, 2020

@author: lalith
'''
import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
from English_Movies import *
from Tamil_Movies import *
    
def choice(lst, window, option):
    if lst[option] == "English":
        window.destroy()
        english = English()
    elif lst[option] == "Tamil":
        window.destroy()
        tamil = Tamil()
    elif lst[option] == "Choose your language":
        error = messagebox.showinfo("Error code 400: Language Error", "Please choose a valid language")

main = tk.Tk()
main.geometry("400x250")
main.configure(bg = "#1F1B24")
main.title("Cinema Spark")
values = ["Choose Your language", "English", "Tamil"]
language_label = tk.Label(main, text = "Language: ", fg = "white", bg = "#1F1B24")
language_input = ttk.Combobox(main, values = values)
language_input.current(0)
choose = tk.Button(main, text = "OK", width = 5, command = lambda:choice(values, main, language_input.current()))
logo_image = ImageTk.PhotoImage(Image.open("cinespark_logo.png"))
logo_label = tk.Label(main, image = logo_image, bg = "#1F1B24")
logo_label.grid(row = 1, column = 2)
spacer = tk.Label(text = "", height = 1, bg = "#1F1B24")
language_label.grid(column = 2)
language_input.grid(column = 2)
spacer.grid(row = 4, column = 2)
choose.grid(column = 2)
main.mainloop()