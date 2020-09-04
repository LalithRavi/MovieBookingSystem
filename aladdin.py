'''
Created on Apr 25, 2020

@author: lalith
'''
import tkinter as tk
from tkinter import *
from tkinter import ttk
from PIL import ImageTk, Image
from tkinter import messagebox

class Aladdin:
    
    def __init__(self, window):
        aladdin_image = ImageTk.PhotoImage(Image.open("aladdin.jpg"))
        aladdin_button = tk.Button(window, image = aladdin_image, bg = "#1F1B24", command = lambda:self.aladdin_window(aladdin_image))
        aladdin_label = tk.Label(window, text = "Aladdin")
        aladdin_button.grid(row = 2, column = 5)
        aladdin_label.grid(row = 3, column = 5)
   
    def aladdin_window(self, aladdin_image):            
        aladdin = tk.Toplevel()
        aladdin.geometry("500x500")
        aladdin.configure(bg = "#1F1B24")
        aladdin_label = tk.Label(aladdin, image = aladdin_image, bg = "#1F1B24")
        values = [1, 2, 3, 4, 5]
        num_tickets = ttk.Combobox(aladdin, values = values)
        num_tickets_label = tk.Label(aladdin, text = "Number of tickets: ", font = ("Calibri", "16"), fg = "white", bg = "#1F1B24")
        ok = tk.Button(aladdin, text = "OK", width = 5, command = lambda:self.__del__(values, num_tickets, aladdin))
        aladdin_label.grid(row = 1, column = 2)
        num_tickets_label.grid(row = 3, column = 1)
        num_tickets.grid(row = 3, column = 2)
        ok.grid(row = 5, column = 2)
        aladdin.mainloop()
        
    def __del__(self, values, num_tickets, aladdin):
        file = open("Movies\Aladdin.txt", "r+")
        old_tickets_available = [1,]
        purchase = values[num_tickets.current()]
        for position, line in enumerate(file):
            if position in old_tickets_available:
                ticket = line.split()
                value = int(ticket[2])
                if value > 0 and purchase <= value:
                    new_tickets_available = value - purchase
                    file = open("Movies\Aladdin.txt", "w")
                    file.write("Title: Aladdin")
                    file.write("\nTickets Available: {}".format(new_tickets_available))
                else:
                    error = messagebox.showinfo("Error code 404: Order Error", "Sorry, tickets for Aladdin have been sold out. Please choose another movie.")
        file.close()
        aladdin.destroy()
    
