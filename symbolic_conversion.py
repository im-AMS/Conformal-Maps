"""
this module deals with symbolic computation
it can accept a function of z (ex: z**2) or in the real and imaginary part(ex: a**2 + I*b**2)
"""
from imports import *


def w_symbolic_split(z):
    Real = re(z)
    Imag = im(z)
    return Real, Imag


def w_numeric(z):

    # Function which converts Sympy to normal python variable
    z = lambdify((a, b), z, "numpy")
    return z


grid = w_numeric(z)


def anim(ip_fn, x, y, i):
    """
    Function which creates the cool frames for the slider.
    what it does is
    (input function - Grid) * i + Grid
    here grid is the function w=z
    """
    global grid
    return (ip_fn(x, y) - grid(x, y)) * i + grid(x, y)


# Testing purpose
if __name__ == "__main__":
    a = w_numeric(z**2)
    for j in np.arange(0, 1.1, 0.10):
        print(anim(a, x=1, y=1, i=j))
