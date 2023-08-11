import sympy as sym
import scipy.signal as signal
from scipy.optimize import basinhopping
import numpy as np
from .Parser import ExprParser
import traceback

# This file contains a class that allows to define a line.

class Point():
    def __init__(self, *args, normalize=False):
        self.line_object = {}
        self.eparser = ExprParser()
        
        self.x = []
        self.y = []
        
    
    def setXY(self, xPoint, yPoint):
        self.x = []
        self.y = []
        self.x.append(xPoint)
        self.y.append(yPoint)
        
        