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
        self.expression = 0
    
    def setExpression(self, expresion, normalize=False):
        try:
            t = sym.symbols('t')
            expression = sym.sympify(expresion)
            expression_function = sym.lambdify(t, expression, 'numpy')
            self.expression = expression_function
            return True
        except sym.SympifyError:
            return False
        except Exception:
            return False
    
    def setXY(self, xmin, xmax, scale):           
        x_values = np.linspace(xmin * scale, xmax * scale, 10000)
        self.y = self.expression(x_values)
        self.x = x_values
        