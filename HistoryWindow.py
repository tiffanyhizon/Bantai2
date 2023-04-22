import tkinter as tk
from PIL import Image,ImageTk
from VideoCapture import *
from tkinter import Toplevel
import cv2
from Util import *

class HistoryWindow:
    def __init__(self, parent):
        self.main_container = tk.Frame(parent, bg="#9bb")

        # =============== Refresh ================
        btn_container = tk.Frame(self.main_container, bg="#9bb")
        btn_container.columnconfigure(0, weight=2)
        btn_container.columnconfigure(1, weight=2)
        btn_container.columnconfigure(2, weight=2)
        btn_container.columnconfigure(3, weight=1)
        btn_refresh = tk.Button(btn_container, bg="#345", fg="#fff", text="Refresh")
        btn_refresh.grid(column=3, row=0, padx=20, pady=5, ipadx=20, ipady=3, sticky="e")
        btn_container.pack(side="top", fill="both")

        # ================ List 1 ================ 
        self.container = Util.CreateFormalList(self.main_container)
        self.container.pack(padx=20, pady=5, fill="both", expand=True)
    
    def get_window(self):
        return self.main_container

    def encodeData(self, data):
        self.list1_data = data

    def refreshLists(self):
        self.container.destroy()
        self.container = Util.CreateFormalList(self.main_container, data=self.list1_data)
        self.container.pack(padx=20, pady=5, fill="both", expand=True)

