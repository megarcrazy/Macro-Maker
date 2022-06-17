""""
Macro Maker Python software made by Vincent Tang 2022

The purpose of this program is to record mouse and keyboard inputs and store in a file.
The file can be read by the program to repeat the input.
"""


import sys
import os
import PyQt5
from src.windowMacroMaker import WindowMacroMaker


def main():
    app = PyQt5.QtWidgets.QApplication(sys.argv)
    currentDir = os.path.dirname(os.path.abspath(__file__))
    _ = WindowMacroMaker(currentDir)
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()
