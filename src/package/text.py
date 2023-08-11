import sympy as sym
import scipy.signal as signal
from scipy.optimize import basinhopping
import numpy as np

# This file contains a class that allows to define a line.

class Text():
    def __init__(self, *args, normalize=False):
        self.line_object = {}
        
        self.title = ""
        self.x = 0
        self.y = 0
        self.rotation = 0
        self.text = ""
        self.color = "#000000"
        self.size = 10
        self.ha = 'center'
        self.va = 'center'
        self.weight = 'normal'
        self.style = 'normal'
        self.opacity = 100.00
        self.plotNum = 0
        self.plotted = False
        self.textObject = 0