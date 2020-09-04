'''
Created on Apr 25, 2020

@author: lalith
'''
import tkinter as tk
from tkinter import *
from tkinter import ttk
from PIL import ImageTk, Image
from tkinter import messagebox

class Fast:
    
    def __init__(self, window):
        fast_image = ImageTk.PhotoImage(Image.open("fast&furious_hobbs&shaw.jpg"))
        fast_button = tk.Button(window, image = fast_image, bg = "#1F1B24", command = lambda:self.fast_window(fast_image))
        fast_label = tk.Label(window, text = "Fast & Furious: Hobbs & Shaw")
        fast_button.grid(row = 5, column = 4)
        fast_label.grid(row = 6, column = 4)
    
    def fast_window(self, fast_image):
        fast = tk.Toplevel()
        fast.geometry("500x500")
        fast.configure(bg = "#1F1B24")
        fast_label = tk.Label(fast, image = fast_image, bg = "#1F1B24")
        values = [1, 2, 3, 4, 5]
        num_tickets = ttk.Combobox(fast, values = values)
        num_tickets_label = tk.Label(fast, text = "Number of tickets: ", font = ("Calibri", "16"), fg = "white", bg = "#1F1B24")
        ok = tk.Button(fast, text = "OK", width = 5, command = lambda:self.__del__(values, num_tickets, fast))
        fast_label.grid(row = 1, column = 2)
        num_tickets_label.grid(row = 3, column = 1)
        num_tickets.grid(row = 3, column = 2)
        ok.grid(row = 5, column = 2)
        fast.mainloop()
    
    def __del__(self, values, num_tickets, fast):
            file = open("Movies\hobbs&shaw.txt", "r+")
            old_tickets_available = [1,]
            purchase = values[num_tickets.current()]
            for position, line in enumerate(file):
                if position in old_tickets_available:
                    ticket = line.split()
                    value = int(ticket[2])
                    if value > 0 and purchase < value:
                        new_tickets_available = value - purchase
                        file = open("Movies\hobbs&shaw.txt", "w")
                        file.write("Title: Fast & Furious - Hobbs & Shaw")
                        file.write("\nTickets Available: {}".format(new_tickets_available))
                    else:
                        error = messagebox.showinfo("Error code 404: Order Error", "Sorry, tickets for Fast & Furious: Hobbs & Shaw have been sold out. Please choose another movie.")
            file.close()
            fast.destroy()