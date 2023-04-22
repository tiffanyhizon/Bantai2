from datetime import datetime

class Notification:
    def __init__(self, title='Notofication', message=''):
        self.title = title
        self.message = message

    def setTitle(self, title):
        self.title = title

    def getTitle(self):
        return self.title
    
    def setMessage(self, messg):
        self.message = messg
    
    def getMessage(self):
        return self.message
    
    def save(self):
        now = datetime.now()
        with open('./bin/Notifications.txt') as file:
            file.write('({}){}: {}'.format(now.strftime("%d/%m/%Y %H:%M:%S"), self.title, self.message))

