import PyQt5
from src.windowObject import WindowObject
import src.constants as c


class InformationTextBox(WindowObject):
    
    def __init__(self, window):
        super().__init__(window)
        self._text_box = None
        self._text_line1 = 'No file opened.'
        self._text_line2 = 'Please open a file.'
        self.initialise()

    def initialise(self):
        self._text_box = PyQt5.QtWidgets.QLabel('', self._window)
        self._text_box.setGeometry(100, 25, 600, 50)
        self._text_box.setFont(PyQt5.QtGui.QFont('Arial', 10))
        self.update_text()

    def change_url_text(self, url):
        text = url
        file_name = text.split('/')[-1]
        self._text_line1 = f'File location: {file_name}.'
        self.update_text()

    # Instruction message gives user information on what to do.
    def change_instruction(self, status):
        if status == c.INSTRUCTION_ERROR_RESERVE_FILE:
            self._text_line2 = 'The file temp.csv is a reserved name. Please choose another name.'
        elif status == c.INSTRUCTION_WRONG_FILE_TYPE:
            self._text_line2 = 'Please choose a csv file instead.'
        elif status == c.INSTRUCTION_SUCCESSFULLY_OPENED_FILE:
            self._text_line2 = 'Press esc while recording or running to stop.'
        elif status == c.INSTRUCTION_RECORD_STARTED:
            self._text_line2 = 'Initiated recording. Press escape to end.'
        elif status == c.INSTRUCTION_RECORD_ESCAPED:
            self._text_line2 = 'Record escaped. Scripted saved in temp.csv'
        self.update_text()

    # Adds both lines of text
    def update_text(self):
        text1 = self._text_line1
        text2 = self._text_line2
        text = text1 + '\n' + text2
        self._text_box.setText(text)
