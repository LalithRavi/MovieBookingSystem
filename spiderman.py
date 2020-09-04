'''
Created on Apr 25, 2020

@author: lalith
'''
import tkinter as tk
from tkinter import *
from tkinter import ttk
from PIL import ImageTk, Image
from tkinter import messagebox

class Spiderman:
    
    def __init__(self, window):
        spiderman_image = ImageTk.PhotoImage(Image.open("spiderman_farfromhome.jpg"))
        spiderman_button = tk.Button(window, image = spiderman_image, bg = "#1F1B24", command = lambda:self.spiderman_window(spiderman_image))
        spiderman_label = tk.Label(window, text = "Spiderman: Far From Home")
        spiderman_button.grid(row = 2, column = 3)
        spiderman_label.grid(row = 3, column = 3)

    def spiderman_window(self, spiderman_image):
        spiderman = tk.Toplevel()
        spiderman.geometry("500x500")
        spiderman.configure(bg = "#1F1B24")
        spiderman_label = tk.Label(spiderman, image = spiderman_image, bg = "#1F1B24")
        values = [1, 2, 3, 4, 5]
        num_tickets = ttk.Combobox(spiderman, values = values)
        num_tickets_label = tk.Label(spiderman, text = "Number of tickets: ", font = ("Calibri", "16"), fg = "white", bg = "#1F1B24")
        ok = tk.Button(spiderman, text = "OK", width = 5, command = lambda:self.__del__(values, num_tickets, spiderman))
        spiderman_label.grid(row = 1, column = 2)
        num_tickets_label.grid(row = 3, column = 1)
        num_tickets.grid(row = 3, column = 2)
        ok.grid(row = 5, column = 2)
        spiderman.mainloop()
        
    def __del__(self, values, num_tickets, spiderman):
        file = open("Movies\spiderman.txt", "r+")
        old_tickets_available = [1,]
        purchase = values[num_tickets.current()]
        for position, line in enumerate(file):
            if position in old_tickets_available:
                ticket = line.split()
                value = int(ticket[2])
                if value > 0 and purchase < value:
                    new_tickets_available = value - purchase
                    file = open("Movies\spiderman.txt", "w")
                    file.write("Title: Spiderman - Far From Home")
                    file.write("\nTickets Available: {}".format(new_tickets_available))
                else:
                    error = messagebox.showinfo("Error code 404: Order Error", "Sorry, tickets for Spiderman: Far From Home have been sold out. Please choose another movie.")
        file.close()
        spiderman.destroy()