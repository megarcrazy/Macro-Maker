import PyQt5
from src.button import Button
from src.functions.listener import Listener


# This button is clicked to start recording the macro
class ButtonRecordMacro(Button):

    def __init__(self, window):
        super().__init__(window)
        self._initialise()
    
    def _initialise(self):
        btn = PyQt5.QtWidgets.QPushButton('Record', self._window)
        btn.setToolTip('Initiating macro recording')
        btn.setGeometry(100, 125, 100, 50)
        btn.clicked.connect(self._clickme)

    # Load script on click
    def _clickme(self):
        listener = Listener(self._window)
        listener.run_listener()
        # Change the file location to temp.csv for saving
        temp_url = self._window.get_temp_url()
        self._window.change_url(temp_url)
