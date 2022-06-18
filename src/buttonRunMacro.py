import PyQt5
from src.button import Button
from src.functions.macroRunner import MacroRunner
from src.functions.scriptManager import ScriptManager


# This button is clicked to run a recorded macro
class ButtonRunMacro(Button):

    def __init__(self, window):
        super().__init__(window)
        self._macro_runner = MacroRunner()
        self.initialise()

    def initialise(self):
        btn = PyQt5.QtWidgets.QPushButton('Run', self._window)
        btn.setToolTip('Run a saved script')
        btn.setGeometry(100, 150, 100, 50)
        btn.clicked.connect(self.clickme)

    def clickme(self):
        self._macro_runner.reset()
        script_array = ScriptManager.loadScript(self._window.get_url())
        self._macro_runner.runScript(script_array)
