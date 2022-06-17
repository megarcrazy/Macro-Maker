from msilib.schema import File
from PyQt5.QtWidgets import QWidget
import PyQt5
from src.buttonRecordMacro import ButtonRecordMacro
from src.buttonRunMacro import ButtonRunMacro
from src.fileManager import FileManager


class WindowMacroMaker(QWidget):
    def __init__(self, current_directory):
        super().__init__()
        self._current_directory = current_directory
        self._file_manager = FileManager()
        self.initUI()
        
    def initUI(self):
        self.setWindow()
        self._buttonRecordMacro = ButtonRecordMacro(self)
        self._buttonRunMacro = ButtonRunMacro(self)
        self.show()
    
    def setWindow(self):
        self.setGeometry(100, 100, 600, 400)
        self.setWindowIcon(PyQt5.QtGui.QIcon(self._current_directory + '/images/mouse.jpg'))
        self.setWindowTitle('WindowMacroMaker')
