'''
Created on Apr 25, 2020

@author: lalith
'''
import tkinter as tk
from tkinter import *
from tkinter import ttk
from PIL import ImageTk, Image
from tkinter import messagebox

class Shazam:
    def __init__(self, window):
        shazam_image = ImageTk.PhotoImage(Image.open("shazam.jpg"))
        shazam_button = tk.Button(window, image = shazam_image, bg = "#1F1B24", command = lambda:self.shazam_window(shazam_image))
        shazam_label = tk.Label(window, text = "Shazam")
        shazam_button.grid(row = 5, column = 1)
        shazam_label.grid(row = 6, column = 1)
    
    def shazam_window(self, shazam_image):        
        shazam = tk.Toplevel()
        shazam.geometry("500x500")
        shazam.configure(bg = "#1F1B24")
        shazam_label = tk.Label(shazam, image = shazam_image, bg = "#1F1B24")
        values = [1, 2, 3, 4, 5]
        num_tickets = ttk.Combobox(shazam, values = values)
        num_tickets_label = tk.Label(shazam, text = "Number of tickets: ", font = ("Calibri", "16"), fg = "white", bg = "#1F1B24")
        ok = tk.Button(shazam, text = "OK", width = 5, command = lambda:self.__del__(values, num_tickets, shazam))
        shazam_label.grid(row = 1, column = 2)
        num_tickets_label.grid(row = 3, column = 1)
        num_tickets.grid(row = 3, column = 2)
        ok.grid(row = 5, column = 2)
        shazam.mainloop()
    
    def __del__(self, values, num_tickets, shazam):
            file = open("Movies\shazam.txt", "r+")
            old_tickets_available = [1,]
            purchase = values[num_tickets.current()]
            for position, line in enumerate(file):
                if position in old_tickets_available:
                    ticket = line.split()
                    value = int(ticket[2])
                    if value > 0 and purchase < value:
                        new_tickets_available = value - purchase
                        file = open("Movies\shazam.txt", "w")
                        file.write("Title: Shazam")
                        file.write("\nTickets Available: {}".format(new_tickets_available))
                    else:
                        error = messagebox.showinfo("Order Error", "Error code 404: Sorry, tickets for Shazam have been sold out. Please choose another movie.")
            file.close()
            shazam.destroy()