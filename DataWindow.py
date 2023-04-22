import tkinter as tk
from tkinter.ttk import Separator, Style
from PIL import ImageTk, Image
from Util import *

# https://www.activestate.com/resources/quick-reads/how-to-add-images-in-tkinter/
# https://www.c-sharpcorner.com/blogs/basics-for-displaying-image-in-tkinter-python

class DataWindow(tk.Frame):

    font = ("Arial", 12)
    button_font = ("Arial", 13)
    primary_color = "#9bb"
    secondary_color = "#345"

    def __init__(self, parent, title = "Window 2", width = 1520, height = 780):
        super().__init__(parent)

        self.root = tk.Frame(parent, bg=self.primary_color, bd=0, highlightthickness=0)
        window_w = width
        window_h = height
        if isinstance(parent, tk.Tk) or isinstance(parent, tk.Toplevel):
            pos_x, pos_y = 0, 0
            parent.geometry('{}x{}+{}+{}'.format(window_w, window_h, pos_x, pos_y))
            parent.title(title)

        self.root.columnconfigure(0, weight=2, minsize=240)
        self.root.columnconfigure(1, weight=6)
        self.root.columnconfigure(2, weight=6)
        self.root.rowconfigure(0, weight=1)

        """
            ==============================-
            |______________1_____________||
            |                            ||
            |______________2_____________||
            |                            ||
            |                            ||
            |              3             ||
            |                            ||
            |                            ||
            |============================||
        """
        # Main Panel
        data_frame = tk.Frame(self.root, relief="solid", bg=self.primary_color, bd=0, highlightthickness=0)

        data_frame.rowconfigure(0, weight=1)
        data_frame.rowconfigure(1, weight=1)
        data_frame.rowconfigure(2, weight=4, minsize=60)
        data_frame.rowconfigure(3, weight=1)
        data_frame.rowconfigure(4, weight=15)
        data_frame.columnconfigure(0, weight=1)

        data_frame_menu = tk.Frame(data_frame, bg=self.primary_color, relief="solid")
        data_frame_ribbon = tk.Frame(data_frame, bg=self.primary_color, relief="solid")
        data_frame_canvases = tk.Frame(data_frame, bg="#fff", relief="solid")

        # (1) Menu frame Elements
        btn_home = tk.Button(data_frame_menu, text="Home", font=self.button_font, bg=self.primary_color, fg="#fff", bd=0, highlightthickness=0).pack(side="left", ipadx=10)
        
        # (2) Ribbon frame Elements
        data_frame_ribbon.rowconfigure(0, weight=1)
        data_frame_ribbon.columnconfigure(0, weight=1)

        rbnfrme_stat = tk.Frame(data_frame_ribbon, bg=self.primary_color)

        self.default_image = ImageTk.PhotoImage(Image.open("video.png").resize([50, 50], Image.BILINEAR))

        self.default_image = ImageTk.PhotoImage(Image.open("total_violations.png").resize([50, 50], Image.BILINEAR))
        self.default_image = ImageTk.PhotoImage(Image.open("public_smoking.png").resize([50, 50], Image.BILINEAR))
        self.default_image = ImageTk.PhotoImage(Image.open("public_drinking.png").resize([50, 50], Image.BILINEAR))

        rbncanv_1 = Util.CreateStatPill(rbnfrme_stat, title="Anomally Detector")
        rbncanv_2 = Util.CreateStatPill(rbnfrme_stat, title="Audio Detected")
        rbncanv_3 = Util.CreateStatPill(rbnfrme_stat, title="Total Detection")

        rbncanv_1.pack(padx=10, pady=0, fill="x", expand=True, side="left")
        rbncanv_2.pack(padx=10, pady=0, fill="x", expand=True, side="left")
        rbncanv_3.pack(padx=10, pady=0, fill="x", expand=True, side="left")

        rbnfrme_stat.grid(padx=20, column=0, row=0, sticky="news")

        # (3) Data frame Elements
        data_frame_canvases.rowconfigure(0, weight=10)
        data_frame_canvases.rowconfigure(1, weight=1)
        data_frame_canvases.columnconfigure(0, weight=8)
        data_frame_canvases.columnconfigure(1, weight=1)
        self.data_frame_canvases_recent = tk.Frame(data_frame_canvases, bg=self.primary_color)
        self.data_frame_canvases_detected = tk.Frame(data_frame_canvases, bg=self.primary_color)

        self.pill_img1 = ImageTk.PhotoImage(Image.open("graph.png").resize([400, 100], Image.BILINEAR))
        self.pill_img2 = ImageTk.PhotoImage(Image.open("graph.png").resize([400, 100], Image.BILINEAR))
        self.pill_img3 = ImageTk.PhotoImage(Image.open("graph2.png").resize([140, 280], Image.BILINEAR))
        self.pill_img4 = ImageTk.PhotoImage(Image.open("graph2.png").resize([140, 280], Image.BILINEAR))

        # self.data_canv1 = Util.CreateDataPill(parent=self.data_frame_canvases_detected, image=self.pill_img1, title="Anomaly Detected")
        # self.data_canv2 = Util.CreateDataPill(parent=self.data_frame_canvases_detected, image=self.pill_img2, title="Audio Detected")
        # self.data_canv3 = Util.CreateDataPill(parent=self.data_frame_canvases_recent, image=self.pill_img3, title="Recent Anomaly\nDetected", side="top", width=170, height=350)
        # self.data_canv4 = Util.CreateDataPill(parent=self.data_frame_canvases_recent, image=self.pill_img4, title="Recent Audio\nDetected", side="top", width=170, height=350)
        self.data_canv1 = Util.CreateDataPlotCanvas(parent=self.data_frame_canvases_detected, file_path="data.csv", headers=["ID", "Violation", "Area", "Cam", "Date"], sort_by=["Date"], width=30, height=1300)
        self.data_canv2 = Util.CreateDataPlotCanvas(parent=self.data_frame_canvases_detected, file_path="data.csv", headers=["ID", "Violation", "Area", "Cam", "Date"], sort_by=["Date"], width=30, height=0, to_pack=False)
        # self.data_canv2 = tk.Canvas(self.data_frame_canvases_recent, bg="#345", width=100)
        # temp3 = Util.CreateFormalList(self.data_canv2, data = Util.ReadCsvFile("data.csv", heads=["ID", "Violation", "Area", "Cam", "Date"], sort_by=["ID"]))
        # temp3.pack()
        self.data_canv3 = Util.CreateDataPieCanvas(parent=self.data_frame_canvases_recent, file_path="data.csv", headers=["ID", "Violation", "Area", "Cam", "Date"], sort_by=["Violation"], width=30, height=1300)
        self.data_canv4 = Util.CreateDataPieCanvas(parent=self.data_frame_canvases_recent, file_path="data.csv", headers=["ID", "Violation", "Area", "Cam", "Date"], sort_by=["Violation"], width=30, height=0, to_pack=False)

        self.data_canv1.pack(padx=5, pady=0, side="top", fill="both", expand=True)
        self.data_canv2.pack(padx=5, pady=0, side="top", fill="both", expand=True)
        self.data_canv3.pack(padx=5, pady=0, side="top", fill="both", expand=True)
        self.data_canv4.pack(padx=5, pady=0, side="top", fill="both", expand=True)
        self.data_frame_canvases_detected.grid(column=0, row=0, sticky="news")
        self.data_frame_canvases_recent.grid(column=1, row=0, sticky="news")

        data_frame_canvases_buttons = tk.Frame(data_frame_canvases, bg=self.primary_color)
        button_commands = [self.changeGraph, None, None]
        data_buttons = Util.CreateButtonArray(data_frame_canvases_buttons, 3, ["Button"]*3, commands=button_commands, bg=self.primary_color, fg="#fff", bd=0)
        for btn in data_buttons:
            btn.pack(padx=0, pady=0, ipadx=15, ipady=5, side="left")
        
        data_button_far_right = Util.CreateButtonArray(data_frame_canvases_buttons, 1, ["Button"], anchor="right", bg=self.primary_color, fg="#fff", bd=0)
        data_button_far_right[0].pack(padx=0, pady=0, ipadx=25, ipady=5, side="right")

        data_frame_canvases_buttons.grid(column=0, row=1, columnspan=2, padx=0, pady=0, sticky="news")

        # Data frame internal frame positioning
        sp_menu = Separator(data_frame, orient="horizontal")
        sp_menu.grid(column=0, row=1, padx=10, sticky="we")
        sp_ribbon = Separator(data_frame, orient="horizontal") 
        sp_ribbon.grid(column=0, row=3, sticky="we")
        data_frame_menu.grid(column=0, row=0, padx=0, pady=0, sticky="new")
        data_frame_ribbon.grid(column=0, row=2, padx=0, pady=0, sticky="nsew")
        data_frame_canvases.grid(column=0, row=4, padx=10, pady=10, sticky="news")

        # Positioning frames within window
        data_frame.grid(column=0, row=0, columnspan=3, rowspan=1, padx=0, pady=0, sticky="news")

        # self.root.pack(fill="both", expand=True)
    
    def show(self):
        self.root.mainloop()

    def get_window(self):
        return self.root

    def closeWindow(self):
        self.root.close()
    
    def changeGraph(self):
        self.data_canv1.destroy()
        self.data_canv2.destroy()
        self.data_canv3.destroy()
        self.data_canv4.destroy()
        self.pill_img1 = ImageTk.PhotoImage(Image.open("test_graph1.png").resize([400, 100], Image.BILINEAR))
        self.pill_img2 = ImageTk.PhotoImage(Image.open("test_graph2.png").resize([400, 100], Image.BILINEAR))
        self.pill_img3 = ImageTk.PhotoImage(Image.open("test_graph3.png").resize([140, 200], Image.BILINEAR))
        self.pill_img4 = ImageTk.PhotoImage(Image.open("test_graph3.png").resize([140, 200], Image.BILINEAR))
        self.data_canv1 = Util.CreateDataPill(parent=self.data_frame_canvases_detected, image=self.pill_img1, title="sample1 graph")
        self.data_canv2 = Util.CreateDataPill(parent=self.data_frame_canvases_detected, image=self.pill_img1, title="sample2 graph")
        self.data_canv3 = Util.CreateDataPill(parent=self.data_frame_canvases_detected, image=self.pill_img1, title="sample3 graph")
        self.data_canv4 = Util.CreateDataPill(parent=self.data_frame_canvases_detected, image=self.pill_img1, title="sample4 graph")
        self.data_canv1.pack(padx=20, pady=10, side="top")
        self.data_canv2.pack(padx=20, pady=10, side="top")
        self.data_canv3.pack(padx=20, pady=10, side="left")
        self.data_canv4.pack(padx=20, pady=10, side="left")

    def setPillImage1_canv(self, canvas, title="Graph no.1"):
        self.data_canv1.destroy()
        self.data_canv1 = canvas
        self.data_canv1.pack(padx=20, pady=10, side="top")
    def setPillImage2_canv(self, canvas, title="Graph no.2"):
        self.data_canv2.destroy()
        self.data_canv2 = canvas
        self.data_canv2.pack(padx=20, pady=10, side="top")
    def setPillImage3_canv(self, canvas, title="Graph no.3"):
        self.data_canv3.destroy()
        self.data_canv3 = canvas
        self.data_canv3.pack(padx=20, pady=10, side="top")
    def setPillImage4_canv(self, canvas, title="Graph no.4"):
        self.data_canv4.destroy()
        self.data_canv4 = canvas
        self.data_canv4.pack(padx=20, pady=10, side="top")

    def setPillImage1(self, file_path="", photoimage=None, title="Anomaly Detected"):
        if file_path != "":
            self.pill_img1 = ImageTk.PhotoImage(Image.open(file_path).resize([400, 100], Image.BILINEAR))
        elif photoimage is not None:
            self.pill_img1 = photoimage

        self.data_canv1.destroy()
        self.data_canv1 = Util.CreateDataPill(parent=self.data_frame_canvases_detected, image=self.pill_img1, title=title)
        self.data_canv1.pack(padx=20, pady=10, side="top")

    def setPillImage2(self, file_path="", photoimage=None, title="Anomaly Detected"):
        if file_path != "":
            self.pill_img2 = ImageTk.PhotoImage(Image.open(file_path).resize([400, 100], Image.BILINEAR))
        elif photoimage is not None:
            self.pill_img2 = photoimage

        self.data_canv2.destroy()
        self.data_canv2 = Util.CreateDataPill(parent=self.data_frame_canvases_detected, image=self.pill_img2, title=title)
        self.data_canv2.pack(padx=5, pady=0, side="top")


    def setPillImage3(self, file_path="", photoimage=None, title="Recent Anomaly\nDetected"):
        if file_path != "":
            self.pill_img3 = ImageTk.PhotoImage(Image.open(file_path).resize([140, 280], Image.BILINEAR))
        elif photoimage is not None:
            self.pill_img3 = photoimage

        self.data_canv3.destroy()
        self.data_canv3 = Util.CreateDataPill(parent=self.data_frame_canvases_recent, image=self.pill_img3, title=title, side="top", width=170, height=350)
        self.data_canv3.pack(padx=5, pady=0, side="left")

    def setPillImage4(self, file_path="", photoimage=None, title="Recent Audio\nDetected"):
        if file_path != "":
            self.pill_img4 = ImageTk.PhotoImage(Image.open(file_path).resize([140, 280], Image.BILINEAR))
        elif photoimage is not None:
            self.pill_img4 = photoimage

        self.data_canv4.destroy()
        self.data_canv4 = Util.CreateDataPill(parent=self.data_frame_canvases_recent, image=self.pill_img4, title=title, side="top", width=170, height=350)
        self.data_canv4.pack(padx=5, pady=0, side="left")

