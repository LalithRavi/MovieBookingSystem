'''
Created on Apr 25, 2020

@author: lalith
'''
import tkinter as tk
from tkinter import *
from tkinter import ttk
from PIL import ImageTk, Image
from tkinter import messagebox

class Jumanji:
    
    def __init__(self, window):
        jumanji_image = ImageTk.PhotoImage(Image.open("jumanji.jpg"))
        jumanji_button = tk.Button(window, image = jumanji_image, bg = "#1F1B24", command = lambda:self.jumanji_window(jumanji_image))
        jumanji_label = tk.Label(window, text = "Jumanji")
        jumanji_button.grid(row = 2, column = 4)
        jumanji_label.grid(row = 3, column = 4)
    
    def jumanji_window(self, jumanji_image):        
        jumanji = tk.Toplevel()
        jumanji.geometry("500x500")
        jumanji.configure(bg = "#1F1B24")
        jumanji_label = tk.Label(jumanji, image = jumanji_image, bg = "#1F1B24")
        values = [1, 2, 3, 4, 5]
        num_tickets = ttk.Combobox(jumanji, values = values)
        num_tickets_label = tk.Label(jumanji, text = "Number of tickets: ", font = ("Calibri", "16"), fg = "white", bg = "#1F1B24")
        ok = tk.Button(jumanji, text = "OK", width = 5, command = lambda:self.__del__(values, num_tickets, jumanji))
        jumanji_label.grid(row = 1, column = 2)
        num_tickets_label.grid(row = 3, column = 1)
        num_tickets.grid(row = 3, column = 2)
        ok.grid(row = 5, column = 2)
        jumanji.mainloop()
    
    def __del__(self, values, num_tickets, jumanji):
            file = open("Movies\jumanji.txt", "r+")
            old_tickets_available = [1,]
            purchase = values[num_tickets.current()]
            for position, line in enumerate(file):
                if position in old_tickets_available:
                    ticket = line.split()
                    value = int(ticket[2])
                    if value > 0 and purchase < value:
                        new_tickets_available = value - purchase
                        file = open("Movies\jumanji.txt", "w")
                        file.write("Title: Jumanji")
                        file.write("\nTickets Available: {}".format(new_tickets_available))
                    else:
                        error = messagebox.showinfo("Error code 404: Order Error", "Sorry, tickets for Jumanji have been sold out. Please choose another movie.")
            file.close()
            jumanji.destroy()