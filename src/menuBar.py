import PyQt5
import os
from src.windowObject import WindowObject
from src.functions.scriptManager import ScriptManager


class MenuBar(WindowObject):

    def __init__(self, window):
        super().__init__(window)
        self.initUI()

    def initUI(self):
        main_menu = self._window.menuBar()
        file_menu = main_menu.addMenu('&File')
        self.addOpenAction(file_menu)
        self.addSaveAsAction(file_menu)

    def addOpenAction(self, file_menu):
        open_menu = PyQt5.QtWidgets.QAction(self._window)
        open_menu.setObjectName('actionOpen')
        open_menu.setText('&Open')
        open_menu.triggered.connect(self.OpenAction)
        file_menu.addAction(open_menu)

    def OpenAction(self):
        url, _ = PyQt5.QtWidgets.QFileDialog.getOpenFileName()
        print(url)
        print(self.check_valid_url(url))
        if not self.check_valid_url(url):
            return
        self._window.change_url(url)
        print('o-poo-n')
        
    def addSaveAsAction(self, file_menu):
        save_as_menu = PyQt5.QtWidgets.QAction(self._window)
        save_as_menu.setObjectName('actionSaveAs')
        save_as_menu.setText('&Save As')
        save_as_menu.triggered.connect(self.SaveAsAction)
        file_menu.addAction(save_as_menu)

    # Copies the script from temp.csv and stores in a target url
    def SaveAsAction(self):
        directory = self._window.get_directory()
        url, _ = PyQt5.QtWidgets.QFileDialog.getSaveFileName(
            self._window, 'Save script file', directory, 'CSV (Comma delimited) (*.csv)'
        )
        print(url)
        if not self.check_valid_url(url):
            return
        self._window.change_url(url)
        script_array = ScriptManager.loadScript(self._window.get_temp_url())
        ScriptManager.saveScript(script_array, url)

    @staticmethod
    def check_valid_url(url):
        if url.split('/')[-1] == 'temp.csv':
            print('temp.csv is a reserved name. please use another')
            return False
        elif url.split('.')[-1] != 'csv':
            print('please open a csv file')
            return False
        return True