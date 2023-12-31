import sympy as sym
import scipy.signal as signal
from scipy.optimize import basinhopping
import numpy as np
from .Parser import ExprParser
import traceback

# This file contains a class that allows to define a line.

class Line():
    def __init__(self, *args, normalize=False):
        self.line_object = {}
        self.eparser = ExprParser()
        
        self.x = []
        self.y = []
        
    
    def setXY(self, firstPointX, firstPointY, secondPointX, secondPointY):
        num = 10000
        self.x = np.linspace(firstPointX, secondPointX, num)
        self.y = np.linspace(firstPointY, secondPointY, num)
        
        