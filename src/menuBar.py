import PyQt5
from src.windowObject import WindowObject
from src.functions.scriptManager import ScriptManager
import src.settings as settings


class MenuBar(WindowObject):

    def __init__(self, window):
        super().__init__(window)
        self._initUI()
        self._default_folder_location = self._window.get_directory() + settings.DEFAULT_SAVE_FOLDER

    def _initUI(self):
        main_menu = self._window.menuBar()
        file_menu = main_menu.addMenu('&File')
        self._addOpenAction(file_menu)
        self._addSaveAsAction(file_menu)

    # Add the 'Open' menu item in the File menu tab
    def _addOpenAction(self, file_menu):
        open_menu = PyQt5.QtWidgets.QAction(self._window)
        open_menu.setObjectName('actionOpen')
        open_menu.setText('&Open')
        open_menu.triggered.connect(self._openAction)
        file_menu.addAction(open_menu)

    # Prompts user to open an existing macro file
    def _openAction(self):
        instruction = 'Save script file'
        url, _ = PyQt5.QtWidgets.QFileDialog.getOpenFileName(
            self._window, instruction, self._default_folder_location, settings.FILE_TYPE
        )
        print(url)
        self._window.choose_url(url)
        print('o-poo-n')

    # Add the 'Save As' menu item in the File menu tab
    def _addSaveAsAction(self, file_menu):
        save_as_menu = PyQt5.QtWidgets.QAction(self._window)
        save_as_menu.setObjectName('actionSaveAs')
        save_as_menu.setText('&Save As')
        save_as_menu.triggered.connect(self._saveAsAction)
        file_menu.addAction(save_as_menu)

    # Prompts user to create a save file. 
    # Copies the script from temp.csv and stores in a target url
    def _saveAsAction(self):
        instruction = 'Save script file'
        url, _ = PyQt5.QtWidgets.QFileDialog.getSaveFileName(
            self._window, instruction, self._default_folder_location, settings.FILE_TYPE
        )
        self._window.change_url(url)
        script_array = ScriptManager.loadScript(self._window.get_temp_url())
        ScriptManager.saveScript(script_array, url)
