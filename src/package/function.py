import sympy as sym
import numpy as np
from .Parser import ExprParser

# This file contains a class that allows to define a line.

class Function():
    def __init__(self, *args, normalize=False):
        self.line_object = {}
        self.eparser = ExprParser()
        
        self.x = []
        self.y = []
    
    def setExpression(self, expression, normalize=False):
        try:
            self.eparser.setTxt(expression)
            return True
        except sym.SympifyError:
            return False
        except Exception:
            return False
    
    def setXY(self, xmin, xmax, scale):           
        x_values = np.linspace(xmin * scale, xmax * scale, 10000)
        self.y = self.eparser.evaluate_function(x_values)
        self.x = x_values
        