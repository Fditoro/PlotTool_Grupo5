# PyQt5 modules
from math import inf
from PyQt5.QtWidgets import QWidget
from PyQt5.QtCore import Qt

# Project modules
from src.ui.lineGenerator import Ui_lineGeneratorWidget

class lineGeneratorWindow(QWidget, Ui_lineGeneratorWidget):

    def __init__(self):
        super(lineGeneratorWindow, self).__init__()
        self.setupUi(self)
    
