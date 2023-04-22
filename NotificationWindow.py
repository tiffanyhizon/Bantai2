import tkinter as tk
from PIL import Image,ImageTk
from VideoCapture import *
from tkinter import *
from tkinter import ttk
from Util import *
import cv2

class NotificationWindow:
    header_font_bold = ("Arial", 18, "bold")
    list1_data = None
    list2_data = None
    def __init__(self, parent):
        self.root = parent
        self.main_container = tk.Frame(parent, bg="#9bb")

        # =============== Refresh ================
        btn_container = tk.Frame(self.main_container, bg="#9bb")
        btn_container.columnconfigure(0, weight=2)
        btn_container.columnconfigure(1, weight=2)
        btn_container.columnconfigure(2, weight=2)
        btn_container.columnconfigure(3, weight=1)
        btn_refresh = tk.Button(btn_container, bg="#345", fg="#fff", text="Refresh", command=self.refreshLists)
        btn_refresh.grid(column=3, row=0, padx=20, pady=5, ipadx=20, ipady=3, sticky="e")
        btn_container.pack(side="top", fill="both")

        # ================ List 1 ================ 
        self.container = Util.CreateFormalList(self.main_container, data=self.list1_data)
        self.container.pack(padx=20, pady=5, fill="both", expand=True)

        # ================ List 2 ================ 
        self.container2 = Util.CreateFormalList(self.main_container)
        self.container2.pack(padx=20, pady=5, fill="both", expand=True)
    
    def get_window(self):
        return self.main_container

    def print_test(self, event):
        print("test worked.")

    def encodeData(self, data, data2=None):
        if data is not None:
            self.list1_data = data
        if data2 is not None:
            self.list2_data = data2

    def refreshLists(self):
        self.container.destroy()
        self.container2.destroy()

        self.container = Util.CreateFormalList(self.main_container, data=self.list1_data)
        self.container.pack(padx=20, pady=5, fill="both", expand=True)

        self.container2 = Util.CreateFormalList(self.main_container, data=self.list2_data)
        self.container2.pack(padx=20, pady=5, fill="both", expand=True)
