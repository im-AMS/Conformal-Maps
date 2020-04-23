""""
this module deals with symbolic computation
it can accept a function of z (ex: z**2) or in the real and imaginary part(ex: a**2 + I*b**2)
"""
from imports import *
#returns re and im part of entered fn
def w_symbolic_split(z):
    Real = re(z)
    Imag = im(z)
    return Real , Imag

def w_numeric(z , frame=1):
    Real , Imag = frames(z,frame)
    Real = lambdify((a, b), Real, 'numpy')
    Imag = lambdify((a, b), Imag, 'numpy')
    return Real , Imag
# frames to show the transformation with slider in jupyter notebook
def frames(z,i):
    Real , Imag = w_symbolic_split(z)
    Real_time = (Real - a)*i + a
    Imag_time = (Imag - b)*i + b
    return Real_time , Imag_time
