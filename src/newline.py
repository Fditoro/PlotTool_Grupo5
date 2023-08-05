# PyQt5 modules
from math import inf
from PyQt5.QtWidgets import QWidget
from PyQt5.QtCore import Qt

# Project modules
from src.ui.newline import Ui_NewLineWidget

class NewLineWindow(QWidget, Ui_NewLineWidget):

    def __init__(self):
        super(NewLineWindow, self).__init__()
        self.setupUi(self)
    
