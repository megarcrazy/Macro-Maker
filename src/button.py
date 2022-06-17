import PyQt5


class Button:

    def __init__(self, window):
        self._window = window
        PyQt5.QtWidgets.QToolTip.setFont(PyQt5.QtGui.QFont('SansSerif', 10))
