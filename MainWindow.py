import tkinter as tk
from PIL import Image,ImageTk
from VideoCapture import *
from NotificationWindow import *
from HistoryWindow import *
from Util import *
from tkinter import Toplevel
import cv2
from DataWindow import *

class MainWindow:
    button_font = ("Arial", 14)
    button_color = "#345"
    primary_color = "#9bb"
    secondary_color = "#345"
    showMenu = None
    vid1, vid2, vid3, vid4 = None, None, None, None

    def __init__(self, parent, title = "Bantai2", width = 1529, height = 780):
        self.root = parent
        window_w = width
        window_h = height
        if isinstance(parent, tk.Tk):
            # self.pos_x, self.pos_y = self.get_wind_pos(window_w, window_h)
            self.pos_x, self.pos_y = 0, 0
            self.root.geometry('{}x{}+{}+{}'.format(window_w, window_h, self.pos_x, self.pos_y))
            self.root.title(title)
            self.root.resizable(0, 0)
        
        self.active_stream = 1
        self.delay = 16            
        self.set_record = False

        # Main Window Frames
        self.container_frame = tk.Frame(self.root, bg=self.primary_color)
        self.container_frame.columnconfigure(0, weight=1, minsize=(width-100)*0.15//1)
        self.container_frame.columnconfigure(1, weight=15, minsize=(width-100)*0.85//1)
        self.container_frame.rowconfigure(0, weight=1, minsize=height-50)
        self.display_frame_cover = tk.Frame(self.container_frame, bg=self.primary_color) # COVER
        self.display_frame = tk.Frame(self.display_frame_cover, bg=self.primary_color)
        self.display_frame_large = tk.Frame(self.display_frame_cover, bg=self.primary_color)
        self.ui_frame_cover = tk.Frame(self.container_frame, bg=self.secondary_color) # COVER
        self.ui_frame = tk.Frame(self.ui_frame_cover, bg=self.secondary_color)

        self.surveillance_frame = self.CreateSurveillanceFrame(self.display_frame_cover)

        self.areas_panel = DataWindow(self.display_frame_cover)
        self.areas_frame = self.areas_panel.get_window()
        # self.areas_panel.setPillImage1("Koala.jpg")

        self.notification_panel = NotificationWindow(self.display_frame_cover)
        self.notification_frame = self.notification_panel.get_window()

        # MENU WINDOW SETUP

        # Display Frame setup
        self.display_frame.columnconfigure(0, weight=1)
        self.display_frame.columnconfigure(1, weight=1)
        self.display_frame.rowconfigure(0, weight=1)
        self.display_frame.rowconfigure(1, weight=1)

        ## Create Canvas grid
        self.canv1 = tk.Canvas(self.display_frame, bd=0, bg="black", relief="solid", highlightbackground="#aaa", highlightthickness=2)
        self.canv2 = tk.Canvas(self.display_frame, bd=0, bg="black", relief="solid", highlightbackground="#aaa", highlightthickness=2)
        self.canv3 = tk.Canvas(self.display_frame, bd=0, bg="black", relief="solid", highlightbackground="#aaa", highlightthickness=2)
        self.canv4 = tk.Canvas(self.display_frame, bd=0, bg="black", relief="solid", highlightbackground="#aaa", highlightthickness=2)
        self.canv1.bind("<Button-1>", lambda event: self.displayCamZoom(1))
        self.canv2.bind("<Button-1>", lambda event: self.displayCamZoom(2))
        self.canv3.bind("<Button-1>", lambda event: self.displayCamZoom(3))
        self.canv4.bind("<Button-1>", lambda event: self.displayCamZoom(4))
        self.canv1.grid(column=0, row=0, pady=2, padx=2, stick="news")
        self.canv2.grid(column=1, row=0, pady=2, padx=2, stick="news")
        self.canv3.grid(column=0, row=1, pady=2, padx=2, stick="news")
        self.canv4.grid(column=1, row=1, pady=2, padx=2, stick="news")
        ## Load image on each canvas
        self.img1 = ImageTk.PhotoImage(Image.open("video.png").resize([280, 280], Image.BILINEAR))
        self.img1_large = ImageTk.PhotoImage(Image.open("video.png").resize([560, 560], Image.BILINEAR))

        # Large display setup
        self.canv_big = tk.Canvas(self.display_frame_large, bd=0, bg="black", relief="solid", highlightbackground="#aaa", highlightthickness=2)
        self.canv_big.bind("<Button-1>", lambda event : self.displayCamGrid())
        self.canv_big.pack(padx=10, pady=10, fill="both", expand=True)
        self.canv_big_btn = tk.Button(self.display_frame_large, text="Confirm", font=("Arial 12 bold"), bd=1, relief="flat", bg=self.secondary_color, fg="#fff", command=self.show_options)
        self.canv_big_btn.place(bordermode=OUTSIDE, height=40, width=100, anchor=tk.NW, x=1050, y=90)

        # UI Frame setup
        logo_wh = (125, 125)
        self.logo_big = ImageTk.PhotoImage(Image.open(self.root.logo).resize([logo_wh[0], logo_wh[1]], Image.BILINEAR))
        self.ui_logo = tk.Canvas(self.ui_frame, bd=0, bg=self.secondary_color, highlightthickness=0, height=125, relief="solid")

        self.surveil_btn = tk.Button(self.ui_frame, text="Surveillance", font=self.button_font, bd=0, bg=self.button_color, relief="solid", foreground="white", command=self.displayCamGrid)
        self.areas_btn = tk.Button(self.ui_frame, text="Areas", font=self.button_font, bd=0, bg=self.button_color, relief="solid", foreground="white", command=self.showAreas)
        self.notif_btn = tk.Button(self.ui_frame, text="Notification", font=self.button_font, bd=0, bg=self.button_color, relief="solid", foreground="white", command=self.ShowNotification) 

        self.conn = Util.createConnectionStatusFrame(self.ui_frame, commands=[None, None, self.showAreas])

        self.ui_logo.pack(padx=2, pady=2, ipadx=20, anchor="n", side="top", fill="x")
        self.surveil_btn.pack(padx=2, pady=2, ipadx=20, anchor="n", side="top", fill="x")
        self.areas_btn.pack(padx=2, pady=2, ipadx=20, anchor="n", side="top", fill="x")
        self.notif_btn.pack(padx=2, pady=2, ipadx=20, anchor="n", side="top", fill="x")

        self.conn.pack(padx=10, pady=0, side="bottom", )

        #  Window Frames Deployment
        self.container_frame.pack(padx=0, pady=0, fill="both", expand=True)
        self.ui_frame.pack(padx=20, pady=10, fill="both", expand=True)
        self.ui_frame_cover.grid(column=0, row=0, padx=0, pady=0, ipadx=10, ipady=0, sticky="news")
        self.display_frame.pack(padx=10, pady=10, fill="both", expand=True)
        self.display_frame_cover.grid(column=1, row=0, padx=0, pady=0, sticky="news")

        self.display_frame.update()
        self.ui_frame.update()
        self.display_frame_large.update_idletasks()
        self.canvas1_wh = [self.canv1.winfo_width(), self.canv1.winfo_height()]
        self.canvas2_wh = [self.canv2.winfo_width(), self.canv2.winfo_height()]
        self.canvas3_wh = [self.canv3.winfo_width(), self.canv3.winfo_height()]
        self.canvas4_wh = [self.canv4.winfo_width(), self.canv4.winfo_height()]
        self.canvasbig_wh = [self.canv_big.winfo_width(), self.canv_big.winfo_height()] 

        self.ui_logo.create_image((self.ui_frame.winfo_width()//2), logo_wh[1]//2, image=self.logo_big, anchor=tk.CENTER)


    def show(self):
        self.update()
    
    def update(self):
        if self.vid1 is None or self.vid2 is None or self.vid3 is None or self.vid4 is None:
            if self.vid1 is None:
                print("vid1 is none.")
            if self.vid2 is None:
                print("vid2 is none.")
            if self.vid3 is None:
                print("vid3 is none.")
            if self.vid4 is None:
                print("vid4 is none.")

            return

        if(self.vid1.grab_frame() and self.vid2.grab_frame() and self.vid3.grab_frame() and self.vid4.grab_frame()):
            ret1, frame1 = self.vid1.retrieve_frame()
            if ret1:
                self.photo1 = ImageTk.PhotoImage(image=Image.fromarray(frame1).resize((self.canvas1_wh[0], self.canvas1_wh[1]), Image.BILINEAR))
                self.canv1.create_image(self.canvas1_wh[0]//2, self.canvas1_wh[1]//2, image=self.photo1, anchor=tk.CENTER)
                self.canv1.create_text(40, self.canvas1_wh[1]-10, text="Cam 1", fill="white", font=("Arial 15 bold"))
                if self.set_record:
                    self.RecordStream(self.vid1)

            ret2, frame2 = self.vid2.retrieve_frame()
            if ret2:
                self.photo2 = ImageTk.PhotoImage(image=Image.fromarray(frame2).resize((self.canvas2_wh[0], self.canvas2_wh[1]), Image.BILINEAR))
                self.canv2.create_image(self.canvas2_wh[0]//2, self.canvas2_wh[1]//2, image=self.photo2, anchor=tk.CENTER)
                self.canv2.create_text(40, self.canvas2_wh[1]-10, text="Cam 2", fill="white", font=("Arial 15 bold"))
                if self.set_record:
                    self.RecordStream(self.vid2)

            ret3, frame3 = self.vid3.retrieve_frame()
            if ret3:
                self.photo3 = ImageTk.PhotoImage(image=Image.fromarray(frame3).resize((self.canvas3_wh[0], self.canvas3_wh[1]), Image.BILINEAR))
                self.canv3.create_image(self.canvas3_wh[0]//2, self.canvas3_wh[1]//2, image=self.photo3, anchor=tk.CENTER)
                self.canv3.create_text(40, self.canvas3_wh[1]-10, text="Cam 3", fill="white", font=("Arial 15 bold"))
                if self.set_record:
                    self.RecordStream(self.vid3)

            ret4, frame4 = self.vid4.retrieve_frame()
            if ret4:
                self.photo4 = ImageTk.PhotoImage(image=Image.fromarray(frame4).resize((self.canvas4_wh[0], self.canvas4_wh[1]), Image.BILINEAR))
                self.canv4.create_image(self.canvas4_wh[0]//2, self.canvas4_wh[1]//2, image=self.photo4, anchor=tk.CENTER)
                self.canv4.create_text(40, self.canvas4_wh[1]-10, text="Cam 4", fill="white", font=("Arial 15 bold"))
                if self.set_record:
                    self.RecordStream(self.vid4)
            
            # Large frame mapping
            if self.display_frame_large.winfo_ismapped():
                enlarged_frame_id = 1
                retl, framel = self.vid1.retrieve_frame()
                if self.active_stream == 2:
                    retl, framel = self.vid2.retrieve_frame()
                    enlarged_frame_id = 2
                elif self.active_stream == 3:
                    retl, framel = self.vid3.retrieve_frame()
                    enlarged_frame_id = 3
                elif self.active_stream == 4:
                    retl, framel = self.vid4.retrieve_frame()
                    enlarged_frame_id = 4

                if retl:
                    height, width, channels = framel.shape
                    self.photo_large = ImageTk.PhotoImage(image=Image.fromarray(framel).resize(Util.ScaleDimensions((width, height)), Image.BILINEAR))
                    self.canv_big.create_image(self.canv_big.winfo_width()//2, self.canv_big.winfo_height()//2, image=self.photo_large, anchor=tk.CENTER)
                    self.canv_big.create_text(100, self.canv_big.winfo_height()-20, text="Cam {}".format(enlarged_frame_id), fill="white", font=("Arial 20 bold"))
        
        self.root.after(self.delay, self.update)

    def SetStream1(self, stream):
        self.vid1 = stream
        print(self.vid1.name)

    def SetStream2(self, stream):
        self.vid2 = stream
        print(self.vid2.name)

    def SetStream3(self, stream):
        self.vid3 = stream
        print(self.vid3.name)

    def SetStream4(self, stream):
        self.vid4 = stream
        print(self.vid1.name)

    def SetStreams(self, stream_list):
        self.SetStream1(stream_list[0])
        self.SetStream2(stream_list[1])
        self.SetStream3(stream_list[2])
        self.SetStream4(stream_list[3])

    def RecordStream(self, stream):
        stream.write_frame()
    
    def CreateSurveillanceFrame(self, parent):
        container = tk.Frame(parent)
        btn = tk.Button(container, text="Surveillance")
        btn.pack()

        return container
    
    def ShowSurveillance(self):
        if self.surveillance_frame is not None:
            print("Surveillance clicked.")
            self.display_frame_cover.update()
            for wid in self.display_frame_cover.winfo_children():
                wid.pack_forget()
            
            if not self.surveillance_frame.winfo_manager():
                self.surveillance_frame.pack(padx=10, pady=10, fill="both", expand=True)

    def ShowNotification(self):
        if self.notification_frame is not None:
            print("Notifications clicked.")
            self.display_frame_cover.update()
            for wid in self.display_frame_cover.winfo_children():
                wid.pack_forget()
            
            if not self.notification_frame.winfo_manager():
                self.notification_frame.pack(padx=10, pady=10, fill="both", expand=True)

    def showAreas(self):
        print("areas clicked!")
        if self.areas_frame is not None:
            print("Areas clicked.")
            self.display_frame_cover.update()
            for wid in self.display_frame_cover.winfo_children():
                wid.pack_forget()
            
            if not self.areas_frame.winfo_manager():
                self.areas_frame.pack(padx=10, pady=10, fill="both", expand=True)
    
    def setShowAreaFrame(self, frame):
        self.show_area_frame = frame

    def setAreaPillImage1(self, file_path="", photoimage=None, title=""):
        if self.display_frame_cover.winfo_manager():
            self.areas_panel.setPillImage1(file_path, photoimage, title="")
    def setAreaPillImage2(self, file_path="", photoimage=None, title=""):
        if self.display_frame_cover.winfo_manager():
            self.areas_panel.setPillImage2(file_path, photoimage, title="")
    def setAreaPillImage3(self, file_path="", photoimage=None, title=""):
        if self.display_frame_cover.winfo_manager():
            self.areas_panel.setPillImage3(file_path, photoimage, title="")
    def setAreaPillImage4(self, file_path="", photoimage=None, title=""):
        if self.display_frame_cover.winfo_manager():
            self.areas_panel.setPillImage4(file_path, photoimage, title="")
    def setAreaPillImages(self, images, titles):
        if isinstance(images[0], str):
            self.setAreaPillImage1(images[0], title=titles[0])
            self.setAreaPillImage2(images[1], title=titles[1])
            self.setAreaPillImage3(images[2], title=titles[2])
            self.setAreaPillImage4(images[3], title=titles[3])
        elif type(images[0]) is type(ImageTk.PhotoImage):
            self.setAreaPillImage1_canv(images[0], title=titles[0])
            self.setAreaPillImage2_canv(images[1], title=titles[1])
            self.setAreaPillImage3_canv(images[2], title=titles[2])
            self.setAreaPillImage4_canv(images[3], title=titles[3])

    def ShowMenu(self):
        self.showMenu()
    
    def setMenuButtonCommand(self, command):
        if self.menu_btn is not None:
            self.menu_btn.configure(command=command)

    def displayCamGrid(self):
        self.display_frame_cover.update()
        for wid in self.display_frame_cover.winfo_children():
            wid.pack_forget()

        self.canv1.delete("all")
        self.canv2.delete("all")
        self.canv3.delete("all")
        self.canv4.delete("all")

        self.display_frame_large.pack_forget()
        self.display_frame.pack(padx=10, pady=10, fill="both", expand=True)
        print("canvas grid packed.")

    def displayCamZoom(self, cam_index=0):
        self.canv_big.delete("all")
        if cam_index == 1:
            self.active_stream = 1
        elif cam_index == 2:
            self.active_stream = 2
        elif cam_index == 3:
            self.active_stream = 3
        elif cam_index == 4:
            self.active_stream = 4
        else:
            print("zoom pass")
            self.active_stream = 1
            return

        self.display_frame.pack_forget()
        self.display_frame_large.pack(padx=10, pady=20, fill="both", expand=True)
        print("large canvas packed.")

    def encodeNotificationData(self, data=None, data2=None):
        self.notification_panel.encodeData(data, data2)
        self.notification_panel.refreshLists()

    def show_options(self, event=None):
        tp = Toplevel()
        tp.geometry("{}x{}+{}+{}".format(350, 175, 150, 150))
        tp.title("Confirm Violation")

        list_option = tk.Frame(tp)

        list_option.columnconfigure(0, weight=1)
        list_option.columnconfigure(1, weight=1)
        list_option.columnconfigure(2, weight=1)
        list_option.rowconfigure(0, weight=1)
        list_option.rowconfigure(1, weight=2)
        list_option.rowconfigure(2, weight=2)

        listbox_options = ["Standing", "Walking", "Kicking", "Running", "Intimidating", "Striking"]
        active_violation = "Standing"

        lbl_header = tk.Label(list_option, text="Is the violation {}".format(active_violation), font="Helvetica 10 bold").grid(column=0, row=0, columnspan=2, sticky="nw")

        lbl = tk.Label(list_option, text = "Confirmation:", font="Helvetica 10").grid(column=0, row=1)

        options = ttk.Combobox(list_option, values=["True", "False"])

        options.grid(column=1, row=1)

        btn_watch = tk.Button(list_option, text="Watch Video", font="Helvetica 10", bg="#9bb", bd=0, relief="solid")
        btn_edit = tk.Button(list_option, text="Edit", bg="#345", fg="#fff", width=8, font="Helvetica 10", command=tp.destroy)

        btn_watch.grid(column=2, row=1, padx=10, ipadx=2)
        btn_edit.grid(column=2, row=2, padx=10, ipadx=2)

        list_option.pack(padx=10, pady=10, fill="both", expand=True)

    def get_wind_pos(self, window_w, window_h):
        posx = (self.root.winfo_screenwidth() // 2) - (window_w // 2)
        posy = (self.root.winfo_screenheight() // 2) - (window_h // 2) - 50

        return (posx, posy)
