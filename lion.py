'''
Created on Apr 25, 2020

@author: lalith
'''
import tkinter as tk
from tkinter import *
from tkinter import ttk
from PIL import ImageTk, Image
from tkinter import messagebox

class Lion:
    
    def __init__(self, window):
        lion_image = ImageTk.PhotoImage(Image.open("thelionking.jpg"))
        lion_button = tk.Button(window, image = lion_image, bg = "#1F1B24", command = lambda:self.lion_window(lion_image))
        lion_label = tk.Label(window, text = "The Lion King")
        lion_button.grid(row = 5, column = 3)
        lion_label.grid(row = 6, column = 3)
    
    
    def lion_window(self, lion_image):        
        lion = tk.Toplevel()
        lion.geometry("500x500")
        lion.configure(bg = "#1F1B24")
        lion_label = tk.Label(lion, image = lion_image, bg = "#1F1B24")
        values = [1, 2, 3, 4, 5]
        num_tickets = ttk.Combobox(lion, values = values)
        num_tickets_label = tk.Label(lion, text = "Number of tickets: ", font = ("Calibri", "16"), fg = "white", bg = "#1F1B24")
        ok = tk.Button(lion, text = "OK", width = 5, command = lambda:self.__del__(values, num_tickets, lion))
        lion_label.grid(row = 1, column = 2)
        num_tickets_label.grid(row = 3, column = 1)
        num_tickets.grid(row = 3, column = 2)
        ok.grid(row = 5, column = 2)
        lion.mainloop()
        
    def __del__(self, values, num_tickets, lion):
        file = open("Movies\Thelionking.txt", "r+")
        old_tickets_available = [1,]
        purchase = values[num_tickets.current()]
        for position, line in enumerate(file):
            if position in old_tickets_available:
                ticket = line.split()
                value = int(ticket[2])
                if value > 0 and purchase < value:
                    new_tickets_available = value - purchase
                    file = open("Movies\Thelionking.txt", "w")
                    file.write("Title: The Lion King")
                    file.write("\nTickets Available: {}".format(new_tickets_available))
                else:
                    error = messagebox.showinfo("Error code 404: Order Error", "Sorry, tickets for The Lion King have been sold out. Please choose another movie.")
        file.close()
        lion.destroy()