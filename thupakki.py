'''
Created on Apr 26, 2020

@author: lalith
'''
import tkinter as tk
from tkinter import *
from tkinter import ttk
from PIL import ImageTk, Image
from tkinter import messagebox

class Thupakki:
    
    def __init__(self, window):
        thupakki_image = ImageTk.PhotoImage(Image.open("thupakki.jpg"))
        thupakki_button = tk.Button(window, image = thupakki_image, bg = "#1F1B24", command = lambda:self.thupakki_window(thupakki_image))
        thupakki_label = tk.Label(window, text = "Thupakki")
        thupakki_button.grid(row = 5, column = 4)
        thupakki_label.grid(row = 6, column = 4)
    
    def thupakki_window(self, thupakki_image):
        thupakki = tk.Toplevel()
        thupakki.geometry("500x500")
        thupakki.configure(bg = "#1F1B24")
        thupakki_label = tk.Label(thupakki, image = thupakki_image, bg = "#1F1B24")
        values = [1, 2, 3, 4, 5]
        num_tickets = ttk.Combobox(thupakki, values = values)
        num_tickets_label = tk.Label(thupakki, text = "Number of tickets: ", font = ("Calibri", "16"), fg = "white", bg = "#1F1B24")
        ok = tk.Button(thupakki, text = "OK", width = 5, command = lambda:self.__del__(values, num_tickets, thupakki))
        thupakki_label.grid(row = 1, column = 2)
        num_tickets_label.grid(row = 3, column = 1)
        num_tickets.grid(row = 3, column = 2)
        ok.grid(row = 5, column = 2)
        thupakki.mainloop()
    
    def __del__(self, values, num_tickets, thupakki):
        file = open("Movies\thupakki.txt", "r+")
        old_tickets_available = [1,]
        purchase = values[num_tickets.current()]
        for position, line in enumerate(file):
            if position in old_tickets_available:
                ticket = line.split()
                value = int(ticket[2])
                if value > 0 and purchase < value:
                        new_tickets_available = value - purchase
                        file = open("Movies\thupakki.txt", "w")
                        file.write("Title: Thupakki")
                        file.write("\nTickets Available: {}".format(new_tickets_available))
                else:
                    error = messagebox.showinfo("Error code 404: Order Error", "Sorry, tickets for 24 have been sold out. Please choose another movie.")
        file.close()
        thupakki.destroy()