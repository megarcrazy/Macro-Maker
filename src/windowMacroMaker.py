from PyQt5.QtWidgets import QWidget
import PyQt5
import src.settings
from src.buttonRecordMacro import ButtonRecordMacro
from src.buttonRunMacro import ButtonRunMacro
from src.menuBar import MenuBar
from src.informationTextBox import InformationTextBox
from src.fileManager import FileManager


class WindowMacroMaker(PyQt5.QtWidgets.QMainWindow):
    def __init__(self, directory):
        super().__init__()
        self._directory = directory
        self._file_manager = FileManager()
        self.initUI()
        
    def initUI(self):
        self.setWindow()
        self._toolBar = MenuBar(self)
        self._button_record_macro = ButtonRecordMacro(self)
        self._button_run_macro = ButtonRunMacro(self)
        self._information_text_box = InformationTextBox(self)
        self.show()
    
    def setWindow(self):
        self.setGeometry(100, 100, 600, 400)
        self.setWindowIcon(PyQt5.QtGui.QIcon(self._directory + '/images/mouse.jpg'))
        self.setWindowTitle('WindowMacroMaker')

    # Get the directory of the software
    def get_directory(self):
        return self._directory

    # Storage location to store the script temporarily
    def get_temp_url(self):
        temp_url = src.settings.TEMP_FILE
        return temp_url

    def get_url(self):
        url = self._file_manager.get_url()
        return url
    
    def change_url(self, url):
        self._file_manager.change_url(url)
        self._information_text_box.change_text(url)
