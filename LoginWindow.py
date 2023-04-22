import tkinter as tk
from PIL import Image,ImageTk
from VideoCapture import *
from tkinter import Toplevel
from NotificationWindow import *
from HistoryWindow import *
from Util import *
import cv2

class LoginWindow:
    button_font = ("Arial", 13)
    button_color = "#345"
    primary_color = "#9bb"
    secondary_color = "#345"
    showMenu = None

    def __init__(self, parent, title = "Window 1", width = 500, height = 700):
        self.root = parent
        self.width = width
        self.height = height
        if isinstance(parent, tk.Tk):
            self.pos_x, self.pos_y = self.get_wind_pos()
            self.root.geometry('{}x{}+{}+{}'.format(self.width, self.height, self.pos_x, self.pos_y))
            self.root.title(title)
            self.root.resizable(0, 0)
        
        self.create_ui(self.root)

    def show(self):
        self.update()
    
    def update(self):
        pass

    def create_ui(self, parent):
        container_cover = tk.Frame(parent, bg=self.secondary_color)
        container = tk.Frame(container_cover, bg=self.secondary_color)

        logo_wh = (125, 125)
        self.logo_big = ImageTk.PhotoImage(Image.open("BantAI.png").resize([logo_wh[0], logo_wh[1]], Image.BILINEAR))
        self.ui_logo = tk.Canvas(container, bd=0, bg=self.secondary_color, highlightthickness=0, height=125, relief="solid")
        self.ui_logo.pack(padx=10, pady=10, fill="x")

        username_lbl = tk.Label(container, text="Username:", font="Arial 13", bg=self.secondary_color, fg="#fff")
        username_entr = tk.Entry(container, font="Arial 13")
        password_lbl = tk.Label(container, text="Password:", font="Arial 13", bg=self.secondary_color, fg="#fff")
        password_entr = tk.Entry(container, font="Arial 13", show="*")

        username_lbl.pack(padx=10, pady=10, anchor="w")
        username_entr.pack(padx=10, pady=10, fill="x")
        password_lbl.pack(padx=10, pady=10, anchor="w")
        password_entr.pack(padx=10, pady=10, fill="x")

        self.login_btn = tk.Button(container, text="Login", font="Arial 13", bg=self.secondary_color, fg="#fff", relief="solid", bd=0)
        self.login_btn.pack(padx=10, pady=10, ipady=10, fill="x")

        container.pack(padx=100, pady=150, fill="both", expand=True)
        container_cover.pack(padx=0, pady=0, fill="both", expand=True)

        self.ui_logo.create_image(135, 125//2, image=self.logo_big, anchor=tk.CENTER)

    def setLoginCommand(self, command):
        if self.login_btn is not None:
            self.login_btn.configure(command=command)



    def get_wind_pos(self):
        posx = (self.root.winfo_screenwidth() // 2) - (self.width // 2)
        posy = (self.root.winfo_screenheight() // 2) - (self.height // 2) - 50

        return (posx, posy)

