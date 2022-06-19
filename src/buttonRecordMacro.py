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
        btn.setGeometry(100, 125, 100, 50)
        btn.clicked.connect(self.clickme)

    # Load script on click
    def clickme(self):
        listener = Listener(self._window)
        # Detect user input for mouse and keyboard
        thread1 = threading.Thread(target=listener.listen)
        # Wait for listener to end and save script into a temporary file
        thread2 = threading.Thread(target=listener.wait_finish, args=(self._window.get_temp_url(),))
        thread1.start()
        thread2.start()
        # Change the file location to temp.csv for saving
        temp_url = self._window.get_temp_url()
        self._window.change_url(temp_url)
