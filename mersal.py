'''
Created on Apr 26, 2020

@author: lalith
'''
import tkinter as tk
from tkinter import *
from tkinter import ttk
from PIL import ImageTk, Image
from tkinter import messagebox

class Mersal:
    
    def __init__(self, window):
        mersal_image = ImageTk.PhotoImage(Image.open("mersal.jpg"))
        mersal_button = tk.Button(window, image = mersal_image, bg = "#1F1B24", command = lambda:self.mersal_window(mersal_image))
        mersal_label = tk.Label(window, text = "Mersal")
        mersal_button.grid(row = 2, column = 5)
        mersal_label.grid(row = 3, column = 5)
    
    def mersal_window(self, mersal_image):
        mersal = tk.Toplevel()
        mersal.geometry("500x500")
        mersal.configure(bg = "#1F1B24")
        mersal_label = tk.Label(mersal, image = mersal_image, bg = "#1F1B24")
        values = [1, 2, 3, 4, 5]
        num_tickets = ttk.Combobox(mersal, values = values)
        num_tickets_label = tk.Label(mersal, text = "Number of tickets: ", font = ("Calibri", "16"), fg = "white", bg = "#1F1B24")
        ok = tk.Button(mersal, text = "OK", width = 5, command = lambda:self.__del__(values, num_tickets, mersal))
        mersal_label.grid(row = 1, column = 2)
        num_tickets_label.grid(row = 3, column = 1)
        num_tickets.grid(row = 3, column = 2)
        ok.grid(row = 5, column = 2)
        mersal.mainloop()
    
    def __del__(self, values, num_tickets, mersal):
        file = open("Movies\mersal.txt", "r+")
        old_tickets_available = [1,]
        purchase = values[num_tickets.current()]
        for position, line in enumerate(file):
            if position in old_tickets_available:
                ticket = line.split()
                value = int(ticket[2])
                if value > 0 and purchase < value:
                        new_tickets_available = value - purchase
                        file = open("Movies\mersal.txt", "w")
                        file.write("Title: Mersal")
                        file.write("\nTickets Available: {}".format(new_tickets_available))
                else:
                    error = messagebox.showinfo("Error code 404: Order Error", "Sorry, tickets for 24 have been sold out. Please choose another movie.")
        file.close()
        mersal.destroy()