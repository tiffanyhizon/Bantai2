import tkinter as tk
from PIL import ImageTk, Image
from PIL import Image,ImageTk
import Window_App as window_app
import Util

class WindowManager:
    window_stack = []

    notification_data = None
    history_data = None

    def __init__(self, parent, no_of_windows=2):
        print("Window manager created!")
        self.root = parent

        self.main_window = window_app.LoginWindow(self.root)
        self.main_window.setLoginCommand(self.OpenWindow1)

    def OpenWindow1(self):
        for widgets in self.root.winfo_children():
            widgets.destroy()

        self.root.state("zoomed")
        list_streams = [ 
                         window_app.MyVideoCapture("footage/SN_13.mp4", name="cam1"),
                         window_app.MyVideoCapture("footage/SN_25.mp4", name="cam2"),
                         window_app.MyVideoCapture("footage/SN_36.mp4", name="cam3"),
                         window_app.MyVideoCapture("footage/SN_42.mp4", name="cam4")
                        ]

        m_tmp = window_app.MainWindow(self.root)
        m_tmp.SetStreams(list_streams)
        self.main_window = m_tmp
        # self.main_window.setAreaPillImages(
        #         ["Koala.jpg", "video.png", "Koala.jpg", "video.png"],
        #         ["test1", "test2", "test3", "test4"]
        #         )
        # canvases = [
        #             Util.CreateDataPillCanvas(),
        #
        #         ]
        # self.main_window.setAreaPillImages(canvases)
        self.main_window.update()

    # ==================== HELPERS ==================== 
    def setLogo(self, logo_path):
        self.logo = ImageTk.PhotoImage(file = logo_path)
        self.root.iconphoto(False, self.logo)

    def setSurveillanceStreams(self, stream_paths):
        if type(self.main_window) is type(window_app.MainWindow):
            self.main_window.SetStream1(stream_paths[0])
            self.main_window.SetStream2(stream_paths[1])
            self.main_window.SetStream3(stream_paths[2])
            self.main_window.SetStream4(stream_paths[3])
            self.main_window.update()
    
    def setNotificationData(self, notif_data=None, list_index=0):
        self.notification_data = notif_data
        if list_index == 1:
            self.main_window.encodeNotificationData(data=self.notification_data)
        elif list_index == 2:
            self.main_window.encodeNotificationData(data2=self.notification_data)
        else:
            self.main_window.encodeNotificationData(data=self.notification_data[0], data2=self.notification_data[1])


    def setHistoryData(self, histo_data=None):
        self.history_data = histo_data
        self.main_window.encodeHistoryData(self.history_data)

    def setWindow2PillImage1(self, image_path="", photoimage=None):
        self.second_window_panel.setPillImage1(image_path, photoimage)

    def setWindow2PillImage2(self, image_path="", photoimage=None):
        self.second_window_panel.setPillImage2(image_path, photoimage)

    def setWindow2PillImage3(self, image_path="", photoimage=None):
        self.second_window_panel.setPillImage3(image_path, photoimage)

    def setWindow2PillImage4(self, image_path="", photoimage=None):
        self.second_window_panel.setPillImage4(image_path, photoimage)
