'''
Created on Apr 26, 2020

@author: lalith
'''
import tkinter as tk
from tkinter import *
from tkinter import ttk
from PIL import ImageTk, Image
from tkinter import messagebox

class Pattas:
    
    def __init__(self, window):
        pattas_image = ImageTk.PhotoImage(Image.open("pattas.jpg"))
        pattas_button = tk.Button(window, image = pattas_image, bg = "#1F1B24", command = lambda:self.pattas_window(pattas_image))
        pattas_label = tk.Label(window, text = "Pattas")
        pattas_button.grid(row = 5, column = 1)
        pattas_label.grid(row = 6, column = 1)
    
    def pattas_window(self, pattas_image):
        pattas = tk.Toplevel()
        pattas.geometry("500x500")
        pattas.configure(bg = "#1F1B24")
        pattas_label = tk.Label(pattas, image = pattas_image, bg = "#1F1B24")
        values = [1, 2, 3, 4, 5]
        num_tickets = ttk.Combobox(pattas, values = values)
        num_tickets_label = tk.Label(pattas, text = "Number of tickets: ", font = ("Calibri", "16"), fg = "white", bg = "#1F1B24")
        ok = tk.Button(pattas, text = "OK", width = 5, command = lambda:self.__del__(values, num_tickets, pattas))
        pattas_label.grid(row = 1, column = 2)
        num_tickets_label.grid(row = 3, column = 1)
        num_tickets.grid(row = 3, column = 2)
        ok.grid(row = 5, column = 2)
        pattas.mainloop()
    
    def __del__(self, values, num_tickets, pattas):
        file = open("Movies\pattas.txt", "r+")
        old_tickets_available = [1,]
        purchase = values[num_tickets.current()]
        for position, line in enumerate(file):
            if position in old_tickets_available:
                ticket = line.split()
                value = int(ticket[2])
                if value > 0 and purchase < value:
                        new_tickets_available = value - purchase
                        file = open("Movies\pattas.txt", "w")
                        file.write("Title: Pattas")
                        file.write("\nTickets Available: {}".format(new_tickets_available))
                else:
                    error = messagebox.showinfo("Error code 404: Order Error", "Sorry, tickets for 24 have been sold out. Please choose another movie.")
        file.close()
        pattas.destroy()