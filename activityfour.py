from logging import root
import tkinter as tk
from tkinter import ttk, messagebox

class RestaurantOrderMangement:
    def __init__(self, root):
    self.root = root
    self.root.title(
       "Restaurant Mangement App")
    
    self.menu_items = {
        "FRIES MEAL": 2,
        "LUNCH MEAL": 2,
        "BURGER MEAL": 3,
        "PIZZA MEAL": 4,
        "CHEESE BURGER": 2.5,
        "DRINKS": 1
    }

    self.exchange_rate = 82

    self.setup_background(root)

    frame = ttk.Frame(root)
    frame.place(relx=0.5, rely=0.5, anchor=tk.CENTER)

    ttk.Label

