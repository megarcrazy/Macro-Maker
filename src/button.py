import PyQt5
from src.windowObject import WindowObject


class Button(WindowObject):

    def __init__(self, window):
        super().__init__(window)
        PyQt5.QtWidgets.QToolTip.setFont(PyQt5.QtGui.QFont('SansSerif', 10))
