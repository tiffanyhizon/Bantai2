import cv2
import tkinter as tk
import matplotlib.pyplot as plt
import pandas as pd
from tkinter.ttk import Separator, Style
from PIL import ImageTk, Image
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import (FigureCanvasTkAgg, NavigationToolbar2Tk)

class Util:
    def __init__(self, parent, title="", bg="white", font="Arial 14"):
        super().__init__(parent)
    
    def CreateNotificationPill(self, parent, imgpath="", title="title", message="Nettification message", width=500, height=100, font=None, side="top"):
        container = tk.Frame(parent, bd=2)
        lbl_message = tk.Label(container, text="{}: {}".format(title, message))
        lbl_message.pack(padx=20, pady=0, side=side)

        return container

    def CreateHistoryPill(parent, imgpath="", title="title", width=500, height=100, font=None, side="top"):
        container = tk.Frame(parent, bd=2)
        container.columnconfigure(0, weight=1)
        container.columnconfigure(1, weight=10)
        container.rowconfigure(0, weight=1)
        lbl_message = tk.Label(container, text="{}".format(title))
        canv = tk.Canvas(container, height=40, width=40, bd=0, highlightbackground="#222", highlightthickness=2)
        
        lbl_message.grid(padx=20, column=1, row=0, sticky="news")
        canv.grid(padx=10, column=0, row=0, sticky="news")

        return container

    def ScaleDimensions(dim1=(338, 266), dim2=(704, 540)):
        m = dim2[0] / dim1[0]
        n = dim2[1] / dim1[1]
        if (m < n):
            m *= 1.75
            return (int(dim1[0] * m), int(dim1[1] * m * 1.1))
        else:
            n *= 1.75
            return (int(dim1[0] * n), int(dim1[1] * n))

    def rescale_frame(frame, percent=75):
        width = int(frame.shape[1] * percent/ 100)
        height = int(frame.shape[0] * percent/ 100)
        dim = (width, height)
        return cv2.resize(frame, dim, interpolation =cv2.INTER_AREA)

    def CreateStatPill(parent, image=None, title="Pill", width=600, height=80, font=None, value=""):
        container = tk.Frame(parent, bg="#9bb", bd=2, highlightbackground="#222", highlightthickness=2)
        lbl_frme = tk.Frame(container, bg="#9bb", highlightthickness=0)
        lbl = tk.Label(lbl_frme, text=title, font=("Arial 20"), fg="#222", bg="#9bb")
        lbl_val = tk.Label(lbl_frme, text=value, font=("Arial 15"), fg="#222", bg="#9bb")
        canv = tk.Canvas(container, height=50, width=50, bd=0, bg="#9bb", highlightbackground="#222", highlightthickness=0)

        if image:
            canv.create_image(0, 0, anchor=tk.NW, image=image)
        
        canv.pack(padx=2, pady=2, side="left")
        lbl.grid(column=0, row=0, sticky="w")
        lbl_val.grid(column=0, row=1, sticky="w")
        lbl_frme.pack(fill="both")
        return container

    def CreateDataPill(parent, image, title="Pill", width=500, height=100, font=None, side="top"):
        container = tk.Frame(parent, highlightbackground="#222", highlightthickness=1, bg="#fff")
        container.columnconfigure(0, weight=1)
        container.rowconfigure(0, weight=1)
        container.rowconfigure(1, weight=1)

        lbl = tk.Label(container, text=title, font=("Arial 12"), bg="#fff")
        canv = tk.Canvas(container, height=height, width=width, bg="#fff", highlightbackground="#fff")

        canv.create_image(width//2, height//2, anchor=tk.CENTER, image=image)
        
        lbl.grid(column=0, row=0, padx=20, pady=0, sticky="nw")
        canv.grid(column=0, row=1, padx=2, pady=2, sticky="nw")

        return container
    
    def CreateDataPlotCanvas(parent, file_path, title="Graph", headers=[""], sort_by=[], width=70, height=50, font=None, to_pack=True):
        container = tk.Canvas(parent, bg="#334455", width=width, height=height)
        fig = Figure(figsize=(10,5), dpi=72)

        # Read csv file
        heads = headers
        data = pd.read_csv(file_path, names=heads)
        data.sort_values(sort_by, axis=0, ascending=[False], inplace=True)
        # x,y = data[heads[0]],data[heads[1]]
        
        counterx = 0
        countery = 0
        xtmp = []
        # ytmp = []
        # for i in range(len(data[heads[0]])-1):
        #     if data[heads[0]][i] == data[heads[0]][i+1]:
        #         counterx += 1
        #         xtmp.append(counterx)
        # x = xtmp
        # y = ytmp
        y = data[heads[1]]
        x = data[heads[4]]


        plt.rc('text', color="white")
        plt.rc('axes', labelcolor="white")
        plot_1 = fig.add_subplot(111)
        plot_1.plot(x,y)
        plot_1.fill_between(x, y)
        fig.patch.set_facecolor((51/255, 68/255, 85/255))
        plot_1.set_facecolor((51/255, 68/255, 85/255))

        fig_canvas = FigureCanvasTkAgg(fig, master=container) 
        fig_canvas.draw()
        print("data pill canvas created.")
        if to_pack:
            fig_canvas.get_tk_widget().pack()

        return container
    
    def ReadCsvFile(file_path, heads, sort_by):
        data = pd.read_csv(file_path, names=heads)
        data.sort_values(sort_by, axis=0, ascending=[False], inplace=True)
        return list(data)

    def CreateDataPieCanvas(parent, file_path, title="Graph", headers=[""], sort_by=[], width=70, height=50, font=None, to_pack = True):
        container = tk.Canvas(parent, bg="#334455", width=width, height=height)
        fig = Figure(figsize=(5,5), dpi=72, facecolor="#334455")

        # Read csv file
        heads = headers
        data = pd.read_csv(file_path, names=heads)
        data.sort_values(sort_by, axis=0, ascending=[False], inplace=True)
        violation = []
        counter = 0
        for i in range(len(data[heads[1]])-1):
            if data[heads[1]][i] == data[heads[1]][i+1]:
                counter += 1
            else:
                counter = 0
                violation.append(counter)
        x = [10, 1, 2, 1, 2]
        mylabels = ["Walking", "Striking", "Runing", "Kicking", "Standing"]

        plt.rc('text')
        plt.rc('axes')
        plot_1 = fig.add_subplot(111)
        plot_1.pie(x, radius=1.2, autopct = '%1.1f%%', textprops=dict(color='black'))
        plot_1.set_facecolor((51/255, 68/255, 85/255))
        plot_1.legend(mylabels, loc="lower right", labelcolor="black")

        fig_canvas = FigureCanvasTkAgg(fig, master=container) 
        fig_canvas.draw()
        print("data pie canvas created.")
        if to_pack:
            fig_canvas.get_tk_widget().pack()

        return container
    
    
    def CreateButtonArray(parent, count=0, titles=[], commands=None, anchor="left", bg="#fff", fg="#333", bd=1, hl=0):
        output = []
        for i in range(count):
            output.append(tk.Button(parent, text=titles[i], font=("Arial 12"), bd=bd, bg=bg, relief="solid", foreground=fg, highlightthickness=hl))
        if commands:
            for i in range(count):
                if commands[i] is not None:
                    output[i].configure(command=commands[i])
        return output
    
    def CreateFormalList(parent, command=None, data=None):
        container = tk.Frame(parent, bg="#9bb")
        canv1 = tk.Canvas(container, bg="#9bb")

        lbl_frame = tk.Frame(canv1, bg="#fff")
        lbl_frame.columnconfigure(0, weight=1)
        lbl_frame.columnconfigure(1, weight=1)
        lbl_frame.columnconfigure(2, weight=1)
        lbl_frame.columnconfigure(3, weight=1)
        lbl_frame.columnconfigure(4, weight=1)
        lbl_frame.rowconfigure(0, weight=1)
        lbl = tk.Label(lbl_frame, text="Camera", bg="#fff").grid(column=0, row=0, sticky="news")
        lbl2 = tk.Label(lbl_frame, text="Recording ID", bg="#fff").grid(column=1, row=0, sticky="news")
        lbl3 = tk.Label(lbl_frame, text="Duration", bg="#fff").grid(column=2, row=0, sticky="news")
        lbl4 = tk.Label(lbl_frame, text="Date", bg="#fff").grid(column=3, row=0, sticky="news")
        lbl5 = tk.Label(lbl_frame, text="Violation", bg="#fff").grid(column=4, row=0, sticky="news")
        lbl_frame.pack(ipadx=0, ipady=0, side="top", fill="x")

        lb = tk.Listbox(canv1, width=128, bd=0, relief="solid")
        lb.pack(side="left", fill="both", expand=True)
        scroll = tk.Scrollbar(canv1)
        scroll.pack(side="right", fill="y")

        list_length = len(data) if data is not None else 20
        for i in range(list_length):
            i_data = 0
            if data is not None:
                i_data = data[i]
            else:
                i_data = i
            lb.insert(tk.END, i_data)

        # ======== List Double Click Acion ========
        if command is not None:
            lb.bind('<Double-1>', command)
        
        lb.config(yscrollcommand=scroll.set)
        scroll.config(command=lb.yview)
        canv1.pack(fill="both", expand=True)

        return container

    def createConnectionStatusFrame(parent, secondary_color="#345", font="Arial 13", button_font="Arial 13", commands=None):
        connection_status_frame = tk.Frame(parent, bg=secondary_color)
        connection_status_frame.rowconfigure(0, weight=1)
        connection_status_frame.rowconfigure(1, weight=1)
        connection_status_frame.rowconfigure(2, weight=1)
        connection_status_frame.columnconfigure(0, weight=1)

        # sp = Separator(parent, orient="horizontal")
        # sp.grid(column=0, row=2, sticky="we")
        # style = Style(parent)
        # style.configure("TSeparator", bg="#222", relief="solid")
        # sp_menu = Separator(connection_status_frame, orient="horizontal")
        # sp_menu.grid(column=0, row=1, padx=10, sticky="we")

        ## Connection Status Elements
        lbl_connstat = tk.Label(connection_status_frame, text="Connection Status:", font=font, bg=secondary_color, fg="#fff")

        srv_frme = tk.Frame(connection_status_frame, bg=secondary_color)
        srv_frme.columnconfigure(0, weight=1)
        srv_frme.rowconfigure(0, weight=1)
        srv_frme.rowconfigure(1, weight=1)
        ##
        lbl_svr = tk.Label(srv_frme, text="Server:", font=font, bg=secondary_color, fg="#fff")
        btn_srv = tk.Button(srv_frme, text="Connected", font=button_font, bd=0, bg="#375", relief="solid", foreground="#fff", highlightthickness=0)

        alrt_frme = tk.Frame(connection_status_frame, bg=secondary_color)
        alrt_frme.columnconfigure(0, weight=5)
        alrt_frme.columnconfigure(0, weight=1)
        alrt_frme.rowconfigure(0, weight=1)
        alrt_frme.rowconfigure(1, weight=1)
        ##
        lbl_alrt = tk.Label(alrt_frme, text="Alert Module:", font=font, bg=secondary_color, fg="#fff")
        btn_alrt = tk.Button(alrt_frme, text="Connected", font=button_font, bd=0, bg="#678", relief="solid", foreground="#fff", highlightthickness=0)
        btn_alrt_mnu = tk.Button(alrt_frme, text="Menu", font=button_font, bd=0, bg="#abc", relief="solid", foreground="#fff", highlightthickness=0)

        ### Positioning Connection Status Elements within fame
        lbl_connstat.pack(padx=10, pady=0, fill="x")

        lbl_svr.grid(column=0, row=0, sticky="nw")
        btn_srv.grid(ipadx=20, ipady=5, padx=5, pady=0, column=0, row=1, sticky="ew")
        lbl_alrt.grid(column=0, row=0, sticky="nw")
        btn_alrt.grid(ipadx=20, ipady=5, padx=5, pady=0, column=0, row=1, sticky="w")
        btn_alrt_mnu.grid(ipadx=5, ipady=5, padx=5, pady=0, column=1, row=1, sticky="e")

        srv_frme.pack(padx=0, pady=5, fill="both", expand=True)
        alrt_frme.pack(padx=0, pady=5, fill="both", expand=True)

        if commands is not None:
            btn_srv.configure(command=commands[0])
            btn_alrt.configure(command=commands[1])
            btn_alrt_mnu.configure(command=commands[2])

        return connection_status_frame

