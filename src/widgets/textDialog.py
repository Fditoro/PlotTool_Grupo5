# PyQt5 modules
from math import inf
from PyQt5.QtWidgets import QWidget
from PyQt5.QtCore import Qt

import re

# Project modules
from src.ui.textWindow import Ui_Dialog
from src.package.text import Text

class TextDialog(QWidget, Ui_Dialog):

    def __init__(self, MainWindow):
        super(TextDialog, self).__init__()
        self.setupUi(self)
        
        self.t = Text()
        
        self.textListArray = []
        self.textCount = 0
        
        self.addTextButton.clicked.connect(self.addNewText)
        self.removeButton.clicked.connect(self.removeText)
        
    #Adds new text to list
    def addNewText(self):
        newText = Text()
        self.textListArray.append(newText)  # Store new text
        self.textList.addItem("Label " + str(self.textCount)) # Show new text
        self.textCount += 1
    
    def removeText(self):
        listPositionText = self.textList.currentItem()
        elementToRemove = self.textList.row(listPositionText)
        del self.textListArray[elementToRemove]
        self.textList.takeItem(elementToRemove)
