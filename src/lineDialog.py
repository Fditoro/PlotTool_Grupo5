# PyQt5 modules
from math import inf
from PyQt5.QtWidgets import QWidget
from PyQt5.QtCore import Qt

# Project modules
from src.ui.lineGenerator import Ui_lineGeneratorWidget
from src.package.line import Line
from src.package.point import Point

class lineDialog(QWidget, Ui_lineGeneratorWidget):

    def __init__(self, MainWindow):
        super(lineDialog, self).__init__()
        self.setupUi(self)

        self.l = Line()
        self.p = Point()
        
    def setLine(self):
        fpx = self.firstPointX.value()
        fpy = self.firstPointY.value()
        spx = self.secondPointX.value()
        spy = self.seconPointY.value()
        self.l.setXY(fpx, fpy, spx, spy)
        self.hide()
    
    def setPoint(self):
        xP = self.pointX.value()
        yP = self.pointY.value()
        self.p.setXY(xP,yP)
        self.hide()

    def getTitle(self):
        return self.titleEdit.text()