'''
Created on Apr 26, 2020

@author: lalith
'''
import tkinter as tk
from tkinter import *
from tkinter import ttk
from PIL import ImageTk, Image
from tkinter import messagebox

class Bigil:
    
    def __init__(self, window):
        bigil_image = ImageTk.PhotoImage(Image.open("bigil.jpg"))
        bigil_button = tk.Button(window, image = bigil_image, bg = "#1F1B24", command = lambda:self.bigil_window(bigil_image))
        bigil_label = tk.Label(window, text = "Bigil")
        bigil_button.grid(row = 2, column = 4)
        bigil_label.grid(row = 3, column = 4)
    
    def bigil_window(self, bigil_image):
        bigil = tk.Toplevel()
        bigil.geometry("500x500")
        bigil.configure(bg = "#1F1B24")
        bigil_label = tk.Label(bigil, image = bigil_image, bg = "#1F1B24")
        values = [1, 2, 3, 4, 5]
        num_tickets = ttk.Combobox(bigil, values = values)
        num_tickets_label = tk.Label(bigil, text = "Number of tickets: ", font = ("Calibri", "16"), fg = "white", bg = "#1F1B24")
        ok = tk.Button(bigil, text = "OK", width = 5, command = lambda:self.__del__(values, num_tickets, bigil))
        bigil_label.grid(row = 1, column = 2)
        num_tickets_label.grid(row = 3, column = 1)
        num_tickets.grid(row = 3, column = 2)
        ok.grid(row = 5, column = 2)
        bigil.mainloop()
    
    def __del__(self, values, num_tickets, bigil):
        file = open("Movies\bigil.txt", "r+")
        old_tickets_available = [1,]
        purchase = values[num_tickets.current()]
        for position, line in enumerate(file):
            if position in old_tickets_available:
                ticket = line.split()
                value = int(ticket[2])
                if value > 0 and purchase < value:
                        new_tickets_available = value - purchase
                        file = open("Movies\bigil.txt", "w")
                        file.write("Title: Bigil")
                        file.write("\nTickets Available: {}".format(new_tickets_available))
                else:
                    error = messagebox.showinfo("Error code 404: Order Error", "Sorry, tickets for 24 have been sold out. Please choose another movie.")
        file.close()
        bigil.destroy()