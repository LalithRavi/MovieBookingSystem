'''
Created on Apr 25, 2020

@author: lalith
'''
import tkinter as tk
from tkinter import *
from tkinter import ttk
from PIL import ImageTk, Image
from tkinter import messagebox

class Endgame:
    
    def __init__(self, window):
        endgame_image = ImageTk.PhotoImage(Image.open("avengers_endgame.jpg"))
        endgame_button = tk.Button(window, image = endgame_image, bg = "#1F1B24", command = lambda:self.endgame_window(endgame_image))
        endgame_label = tk.Label(window, text = "Avengers: Endgame")
        endgame_button.grid(row = 2, column = 1)
        endgame_label.grid(row = 3, column = 1)
    
    def endgame_window(self, endgame_image):
        endgame = tk.Toplevel()
        endgame.geometry("500x500")
        endgame.configure(bg = "#1F1B24")
        endgame_label = tk.Label(endgame, image = endgame_image, bg = "#1F1B24")
        values = [1, 2, 3, 4, 5]
        num_tickets = ttk.Combobox(endgame, values = values)
        num_tickets_label = tk.Label(endgame, text = "Number of tickets: ", font = ("Calibri", "16"), fg = "white", bg = "#1F1B24")
        ok = tk.Button(endgame, text = "OK", width = 5, command = lambda:self.__del__(values, num_tickets, endgame))
        endgame_label.grid(row = 1, column = 2)
        num_tickets_label.grid(row = 3, column = 1)
        num_tickets.grid(row = 3, column = 2)
        ok.grid(row = 5, column = 2)
        endgame.mainloop()
    
    def __del__(self, values, num_tickets, endgame):
        file = open("Movies\endgame.txt", "r+")
        old_tickets_available = [1,]
        purchase = values[num_tickets.current()]
        for position, line in enumerate(file):
            if position in old_tickets_available:
                ticket = line.split()
                value = int(ticket[2])
                if value > 0 and purchase < value:
                        new_tickets_available = value - purchase
                        file = open("Movies\endgame.txt", "w")
                        file.write("Title: Avengers - Endgame")
                        file.write("\nTickets Available: {}".format(new_tickets_available))
                else:
                    error = messagebox.showinfo("Error code 404: Order Error", "Sorry, tickets for Avengers: Endgame have been sold out. Please choose another movie.")
        file.close()
        endgame.destroy()