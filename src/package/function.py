import sympy as sym
import numpy as np
from .Parser import ExprParser

# This file contains a class that allows to define a line.

class Function():
    def __init__(self, *args, normalize=False):
        self.line_object = {}
        self.eparser = ExprParser()
        
        self.x = np.array([])
        self.y = np.array([])
    
    def setExpression(self, expression, normalize=False):
        try:
            self.eparser.setTxt(expression)
            return True
        except sym.SympifyError:
            print("Expression error")
            return False
        except Exception:
            print("Expression error")
            return False
    
    def setXY(self, xmin, xmax, scale):
        self.y = np.array([])           
        x_values = np.linspace(xmin * scale, xmax * scale, 5000)
        values = self.eparser.evaluate_function(x_values)
        self.y = np.append(self.y, values)
        self.x = x_values
        