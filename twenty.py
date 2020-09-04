'''
Created on Apr 26, 2020

@author: lalith
'''
import tkinter as tk
from tkinter import *
from tkinter import ttk
from PIL import ImageTk, Image
from tkinter import messagebox

class Twenty:
    
    def __init__(self, window):
        twenty_image = ImageTk.PhotoImage(Image.open("24.jpg"))
        twenty_button = tk.Button(window, image = twenty_image, bg = "#1F1B24", command = lambda:self.twenty_window(twenty_image))
        twenty_label = tk.Label(window, text = "24")
        twenty_button.grid(row = 2, column = 3)
        twenty_label.grid(row = 3, column = 3)
    
    def twenty_window(self, twenty_image):
        twenty = tk.Toplevel()
        twenty.geometry("500x500")
        twenty.configure(bg = "#1F1B24")
        twenty_label = tk.Label(twenty, image = twenty_image, bg = "#1F1B24")
        values = [1, 2, 3, 4, 5]
        num_tickets = ttk.Combobox(twenty, values = values)
        num_tickets_label = tk.Label(twenty, text = "Number of tickets: ", font = ("Calibri", "16"), fg = "white", bg = "#1F1B24")
        ok = tk.Button(twenty, text = "OK", width = 5, command = lambda:self.__del__(values, num_tickets, twenty))
        twenty_label.grid(row = 1, column = 2)
        num_tickets_label.grid(row = 3, column = 1)
        num_tickets.grid(row = 3, column = 2)
        ok.grid(row = 5, column = 2)
        twenty.mainloop()
    
    def __del__(self, values, num_tickets, twenty):
        file = open("Movies\24.txt", "r+")
        old_tickets_available = [1,]
        purchase = values[num_tickets.current()]
        for position, line in enumerate(file):
            if position in old_tickets_available:
                ticket = line.split()
                value = int(ticket[2])
                if value > 0 and purchase < value:
                        new_tickets_available = value - purchase
                        file = open("Movies\24.txt", "w")
                        file.write("Title: 24")
                        file.write("\nTickets Available: {}".format(new_tickets_available))
                else:
                    error = messagebox.showinfo("Error code 404: Order Error", "Sorry, tickets for 24 have been sold out. Please choose another movie.")
        file.close()
        twenty.destroy()