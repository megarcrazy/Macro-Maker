import PyQt5
from src.windowObject import WindowObject


class InformationTextBox(WindowObject):
    
    def __init__(self, window):
        super().__init__(window)
        self._textBox = None
        self._text = 'No file opened'
        self.initialise()

    def initialise(self):
        self._textBox = PyQt5.QtWidgets.QLabel(self._text, self._window)
        self._textBox.setGeometry(100, 25, 300, 50)
        self._textBox.setFont(PyQt5.QtGui.QFont('Arial', 10))

    def change_text(self, url):
        text = url
        file_name = text.split('/')[-1]
        text = f'File location: {file_name}'
        self._textBox.setText(text)
