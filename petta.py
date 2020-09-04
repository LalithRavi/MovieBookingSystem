'''
Created on Apr 26, 2020

@author: lalith
'''
import tkinter as tk
from tkinter import *
from tkinter import ttk
from PIL import ImageTk, Image
from tkinter import messagebox

class Petta:
    
    def __init__(self, window):
        petta_image = ImageTk.PhotoImage(Image.open("petta.jpg"))
        petta_button = tk.Button(window, image = petta_image, bg = "#1F1B24", command = lambda:self.petta_window(petta_image))
        petta_label = tk.Label(window, text = "Petta")
        petta_button.grid(row = 5, column = 3)
        petta_label.grid(row = 6, column = 3)
    
    def petta_window(self, petta_image):
        petta = tk.Toplevel()
        petta.geometry("500x500")
        petta.configure(bg = "#1F1B24")
        petta_label = tk.Label(petta, image = petta_image, bg = "#1F1B24")
        values = [1, 2, 3, 4, 5]
        num_tickets = ttk.Combobox(petta, values = values)
        num_tickets_label = tk.Label(petta, text = "Number of tickets: ", font = ("Calibri", "16"), fg = "white", bg = "#1F1B24")
        ok = tk.Button(petta, text = "OK", width = 5, command = lambda:self.__del__(values, num_tickets, petta))
        petta_label.grid(row = 1, column = 2)
        num_tickets_label.grid(row = 3, column = 1)
        num_tickets.grid(row = 3, column = 2)
        ok.grid(row = 5, column = 2)
        petta.mainloop()
    
    def __del__(self, values, num_tickets, petta):
        file = open("Movies\petta.txt", "r+")
        old_tickets_available = [1,]
        purchase = values[num_tickets.current()]
        for position, line in enumerate(file):
            if position in old_tickets_available:
                ticket = line.split()
                value = int(ticket[2])
                if value > 0 and purchase < value:
                        new_tickets_available = value - purchase
                        file = open("Movies\petta.txt", "w")
                        file.write("Title: Petta")
                        file.write("\nTickets Available: {}".format(new_tickets_available))
                else:
                    error = messagebox.showinfo("Error code 404: Order Error", "Sorry, tickets for 24 have been sold out. Please choose another movie.")
        file.close()
        petta.destroy()