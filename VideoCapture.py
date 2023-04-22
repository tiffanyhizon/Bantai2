import cv2
from datetime import datetime

# http://www.learningaboutelectronics.com/Articles/How-to-save-a-video-Python-OpenCV.php

class MyVideoCapture:
    name = ""
    def __init__(self, video_source=0, name=""):
        self.now = datetime.now()
        self.name = name

        # Open the video source
        self.vid = cv2.VideoCapture(video_source)
        if not self.vid.isOpened():
            raise ValueError("Unable to open video source", video_source)

        # Get video source width and height
        self.width = int(self.vid.get(cv2.CAP_PROP_FRAME_WIDTH))
        self.height = int(self.vid.get(cv2.CAP_PROP_FRAME_HEIGHT))
    
    def create_writer(self, name=""):
        """
        Creates a writer which saves video output of the VideoCapture

        @param name File name
        """
        self.four_cc = cv2.VideoWriter_fourcc(*'mp4v')
        file_name = 'bin/history/{} {}.mp4'.format(name, self.now.strftime("%Y-%m-%d %H_%M_%S"))
        print(file_name, "created.")
        self.writer = cv2.VideoWriter(filename=file_name, fourcc=self.four_cc, fps=20.0, frameSize=(self.width, self.height))


    def grab_frame(self):
        if self.vid.isOpened() and self.vid.grab():
            self.ret, self.frame = self.vid.retrieve()
            if self.ret:
                return (self.ret, cv2.cvtColor(self.frame, cv2.COLOR_BGR2RGB))

        return (self.ret, None)
    
    def write_frame(self):
        if self.vid.isOpened() and self.writer is not None and self.ret and self.frame is not None:
            self.writer.write(self.frame)

    def get_frame(self):
        if self.vid.isOpened():
            return self.vid.grab()
        else:
            return False

    def retrieve_frame(self):
        if self.vid.isOpened():
            return (self.ret, cv2.cvtColor(self.frame, cv2.COLOR_BGR2RGB))
        else:
            return (False, None)

    # Release the video source when the object is destroyed
    def __del__(self):
        if self.vid.isOpened():
            self.vid.release()
