# -*- coding: utf-8 -*-
"""
Created on Thu Aug 26 12:04:52 2021

@author: zolabar
"""

import sympy as sym
from sympy import *

x, y = sym.symbols('x, y', real=True)

z = x + sym.I*y

e = sym.E
pi = sym.pi
i = sym.I
x, y = sym.symbols('x y', real=True)
# complex number of the form z = x + i y
z = x + i * y

def confCheck(f):
    """
    This function checks if a symbolic input function is conformal. This
    check is done by checking the Cauchy-Riemann conditions.
    If the function is conformal, angles in the plotting part are preserved!

    Parameters
    ----------
    f : Symbolic function in z, or x and y

    Returns
    -------
    None.

    """
    f = eval(f)
    u = sym.re(f)
    v = sym.im(f)
    
    cond1 = sym.diff(u, x) - sym.diff(v, y)
    cond2 = sym.diff(u, y) + sym.diff(v, x)
    
    
    if sym.simplify(cond1) == 0 and sym.simplify(cond2) == 0:
        print('The function is conformal, angles are preserved :)')
    else:
        print('The function is not conformal, angle are not preseverved ...')
        
    return     