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
        
    
    def setXY(self, expresion, xmin, xmax):
        try:
            x = sym.symbols('x')
            expression = sym.sympify(expresion)
            expression_function = sym.lambdify(x, expression, 'numpy')
            
            x_values = np.linspace(xmin, xmax, 10000)
            self.y = expression_function(x_values)
            self.x = x_values
        except sym.SympifyError as e:
            print("SympifyError:", e)
        except Exception as e:
            print("An error occurred:", e)