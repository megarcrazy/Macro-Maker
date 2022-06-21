
import PyQt5
from PyQt5.QtWidgets import QMainWindow
import src.settings as settings
from src.buttonRecordMacro import ButtonRecordMacro
from src.buttonRunMacro import ButtonRunMacro
from src.menuBar import MenuBar
from src.informationTextBox import InformationTextBox
from src.functions.fileManager import FileManager
import src.constants as c


class WindowMacroMaker(QMainWindow):
    def __init__(self, directory):
        super().__init__()
        self._directory = directory
        self._file_manager = FileManager()
        self._initUI()
        
    def _initUI(self):
        self._setWindow()
        self._toolBar = MenuBar(self)
        self._button_record_macro = ButtonRecordMacro(self)
        self._button_run_macro = ButtonRunMacro(self)
        self._information_text_box = InformationTextBox(self)
        self.show()
    
    def _setWindow(self):
        self.setGeometry(100, 100, 600, 400)
        self.setWindowIcon(PyQt5.QtGui.QIcon(self._directory + '/images/mouse.jpg'))
        self.setWindowTitle('WindowMacroMaker')

    # Get the directory of the software
    def get_directory(self):
        return self._directory

    # Storage location to store the script temporarily
    def get_temp_url(self):
        temp_url = settings.TEMP_FILE
        return temp_url

    def get_url(self):
        url = self._file_manager.get_url()
        return url

    def change_url(self, url):
        self._file_manager.change_url(url)
        self._information_text_box.change_url_text(url)
        if url.split('/')[-1] == 'temp.csv':
            print('temp.csv is a reserved name. please use another')
            self._change_status(c.INSTRUCTION_RECORD_STARTED)

    # Change text box message
    def _change_status(self, status):
        self._information_text_box.change_instruction(status)
    
    # Change status message for opening or saving files
    def choose_url(self, url):
        if url.split('/')[-1] == 'temp.csv':
            self._change_status(c.INSTRUCTION_ERROR_RESERVE_FILE)
            return
        elif url.split('.')[-1] != 'csv':
            self._change_status(c.INSTRUCTION_WRONG_FILE_TYPE)
            return
        self.change_url(url)
        self._change_status(c.INSTRUCTION_SUCCESSFULLY_OPENED_FILE)

    # Change status message for ending macro record
    def change_status_record_escaped(self):
        self._change_status(c.INSTRUCTION_RECORD_ESCAPED)
