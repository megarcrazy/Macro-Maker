import PyQt5
from src.button import Button
from src.functions.macroRunner import MacroRunner
from src.functions.scriptManager import ScriptManager


# This button is clicked to run a recorded macro
class ButtonRunMacro(Button):

    def __init__(self, window):
        super().__init__(window)
        self._initialise()

    def _initialise(self):
        btn = PyQt5.QtWidgets.QPushButton('Run', self._window)
        btn.setToolTip('Run a saved script')
        btn.setGeometry(100, 200, 100, 50)
        btn.clicked.connect(self._clickme)

    # Run script on click
    def _clickme(self):
        if self._check_running():
            return
        macro_runner = MacroRunner(self._window)
        script_array = ScriptManager.loadScript(self._window.get_url())
        macro_runner.runScript(script_array)
