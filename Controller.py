from enum import Enum
import cv2
from VideoCapture import *

# VideoCapture serves as out model
# Window Manager serves as our view

class Controller:
    model = None
    viewManager = None
    def __init__(self, master, model, viewmanager):
        # Setting up the model and view
        print("Controller initialized")
        self.model = model
        self.viewManager = viewmanager
        self.master = master

    # ========== Encode your data here ========== 

        # sample data for notification window
        notification_data=[
               "First Test Data 1", "First Test Data 2", "First Test Data 3", "First Test Data 4", "First Test Data 5",
               "First Test Data 6", "First Test Data 7", "First Test Data 8", "First Test Data 9", "First Test Data 10",
               "First Test Data 11", "First Test Data 12", "First Test Data 13", "First Test Data 14", "First Test Data 15",
               "First Test Data 16", "First Test Data 17", "First Test Data 18", "First Test Data 19", "First Test Data 20"
                ]
        notification_data2=[
               "Second Test Data 1", "Second Test Data 2", "Second Test Data 3", "Second Test Data 4", "Second Test Data 5",
               "Second Test Data 6", "Second Test Data 7", "Second Test Data 8", "Second Test Data 9", "Second Test Data 10",
               "Second Test Data 11", "Second Test Data 12", "Second Test Data 13", "Second Test Data 14", "Second Test Data 15",
               "Second Test Data 16", "Second Test Data 17", "Second Test Data 18", "Second Test Data 19", "Second Test Data 20"
                ]
        
        # sample data for history window
        history_data=[
               "History Test Data 1", "History Test Data 2", "History Test Data 3", "History Test Data 4", "History Test Data 5",
               "History Test Data 6", "History Test Data 7", "History Test Data 8", "History Test Data 9", "History Test Data 10",
               "History Test Data 11", "History Test Data 12", "History Test Data 13", "History Test Data 14", "History Test Data 15",
               "History Test Data 16", "History Test Data 17", "History Test Data 18", "History Test Data 19", "History Test Data 20"
                ]

        

    # ==============================================
        
        # Inserting data into notifications window 
        # self.viewManager.setNotificationData([notification_data, notification_data2])

    def show(self):
        self.master.mainloop()

    def save_recording(self):
        pass

    def save_video(self):
        pass
