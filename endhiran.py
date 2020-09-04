'''
Created on Apr 26, 2020

@author: lalith
'''
import tkinter as tk
from tkinter import *
from tkinter import ttk
from PIL import ImageTk, Image
from tkinter import messagebox

class Endhiran:
    
    def __init__(self, window):
        endhiran_image = ImageTk.PhotoImage(Image.open("endhiran.jpg"))
        endhiran_button = tk.Button(window, image = endhiran_image, bg = "#1F1B24", command = lambda:self.endhiran_window(endhiran_image))
        endhiran_label = tk.Label(window, text = "Endhiran 2.0")
        endhiran_button.grid(row = 2, column = 1)
        endhiran_label.grid(row = 3, column = 1)
    
    def endhiran_window(self, endhiran_image):
        endhiran = tk.Toplevel()
        endhiran.geometry("500x500")
        endhiran.configure(bg = "#1F1B24")
        endhiran_label = tk.Label(endhiran, image = endhiran_image, bg = "#1F1B24")
        values = [1, 2, 3, 4, 5]
        num_tickets = ttk.Combobox(endhiran, values = values)
        num_tickets_label = tk.Label(endhiran, text = "Number of tickets: ", font = ("Calibri", "16"), fg = "white", bg = "#1F1B24")
        ok = tk.Button(endhiran, text = "OK", width = 5, command = lambda:self.__del__(values, num_tickets, endhiran))
        endhiran_label.grid(row = 1, column = 2)
        num_tickets_label.grid(row = 3, column = 1)
        num_tickets.grid(row = 3, column = 2)
        ok.grid(row = 5, column = 2)
        endhiran.mainloop()
    
    def __del__(self, values, num_tickets, endhiran):
        file = open("Movies\endhiran.txt", "r+")
        old_tickets_available = [1,]
        purchase = values[num_tickets.current()]
        for position, line in enumerate(file):
            if position in old_tickets_available:
                ticket = line.split()
                value = int(ticket[2])
                if value > 0 and purchase < value:
                        new_tickets_available = value - purchase
                        file = open("Movies\endhiran.txt", "w")
                        file.write("Title: Endhiran 2.0")
                        file.write("\nTickets Available: {}".format(new_tickets_available))
                else:
                    error = messagebox.showinfo("Error code 404: Order Error", "Sorry, tickets for 2.0 have been sold out. Please choose another movie.")
        file.close()
        endhiran.destroy()