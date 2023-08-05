import sympy as sym
import scipy.signal as signal
from scipy.optimize import basinhopping
import numpy as np
from numpy.polynomial import Polynomial
from .Parser import ExprParser
import traceback

# Evaluate a polynomial in reverse order using Horner's Rule,
# for example: a3*x^3+a2*x^2+a1*x+a0 = ((a3*x+a2)x+a1)x+a0
def poly_at(p, x):
    total = 0
    for a in p:
        total = total * x + a
    return total

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
        
        