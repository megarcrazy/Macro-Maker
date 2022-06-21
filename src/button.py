import PyQt5
from src.windowObject import WindowObject


class Button(WindowObject):

    def __init__(self, window):
        super().__init__(window)
        PyQt5.QtWidgets.QToolTip.setFont(PyQt5.QtGui.QFont('SansSerif', 10))

    def _check_running(self):
        if self._window._running:
            print('Already running')
            return True
        return False