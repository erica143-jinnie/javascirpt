import tkinter as tk
from tkinter import ttk, messagebox

class RestaurantOrderManagment:
    def __init__(self,root):
        self.root = root
        self.root = title(
            "Restaurant Managment App")
        self.menu_items = {
            "FRIES MEAL": 2,
            "LUNCH MEAL": 2,
            "BURGER MEAL": 3,
            "PIZZA MEAL" : 4,
            "CHESSE BURGER":2.5,
            "DRINKS": 1
        }
        self.exchange_rate = 82
        self.setup_background(root)
        frame = ttk.Frame(root)
        frame.place(relx=0.5, rely=0.5,
                    anchor=tk.CENTER)
                    
        ttk.label(frame
                  text="Restaurant Order Managment",
                  font=("Arial",20,"bold")).grid(row=0
                                                 columnspan=3,
                                                 padx=10,
                                                 pady=10)
        self.menu_labels = {}
        self.menu_quantities = {}
        for i,(item,price) in enumrate(self.menu_items(), start=1):
            label = ttk.Label(frame,
                              text="{item} (${price}):",
                              font=)