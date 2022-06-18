import PyQt5
import threading
from src.button import Button
from src.functions.listener import Listener


# This button is clicked to start recording the macro
class ButtonRecordMacro(Button):

    def __init__(self, window):
        super().__init__(window)
        self.initialise()
    
    def initialise(self):
        btn = PyQt5.QtWidgets.QPushButton('Record', self._window)
        btn.setToolTip('Initiating macro recording')
        btn.setGeometry(100, 75, 100, 50)
        btn.clicked.connect(self.clickme)

    def clickme(self):
        listener = Listener()
        thread1 = threading.Thread(target=listener.listen)
        thread2 = threading.Thread(target=listener.wait_finish, args=(self._window.get_temp_url(),))
        thread1.start()
        thread2.start()
        # Change the file location to temp.csv
        temp_url = self._window.get_temp_url()
        self._window.change_url(temp_url)
