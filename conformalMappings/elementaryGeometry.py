""""
This module deals with the plotling of graph.
"""

import numpy as np
import sympy as sym
from sympy import *
import plotly.graph_objects as go
from numba import jit
jit(nopython=True , parallel=True)




e = sym.E
pi = np.pi
i = sym.I
x ,  y = sym.symbols('x y', real = True)
#complex number of the form z = a + i b
z = x + i * y

def w_symbolic_split(z):
    """
    Function that separates real and imaginary parts
    
    

    Parameters
    ----------
    z : a complex number

    Returns
    -------
    Real : real part of z
    Imag : imaginary part of z

    """
    Real = sym.re(z)
    Imag = sym.im(z)
    return Real, Imag


def w_numeric(z):
    """
    

    Parameters
    ----------
    z : complex symbolic expression

    Returns
    -------
    w : Numerical functtion, depending on real and imaginary part of z.

    """
    w = sym.lambdify((x, y), z, "numpy")
    return w


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







# create a figure object
fig = go.Figure()


def line_grapher(x, y, color):
    """
    

    Parameters
    ----------
    x : TYPE
        DESCRIPTION.
    y : TYPE
        DESCRIPTION.
    color : TYPE
        DESCRIPTION.

    Returns
    -------
    None.

    """

    fig.add_trace(go.Scatter(x=x, y=y, line_color=color,hoverinfo='none',
                             line=dict(shape='spline'), mode='lines'))




def rectangle(z_numeric, 
              left, 
              right, 
              bottom, 
              top, 
              ticks,
              fine, 
              frame,
              vertFreq = 1):
    """
    

    Parameters
    ----------
    z_numeric : Numerical complex variable function
    left : Left boundary of rectangle.
    right : Right boundary of rectangle.
    bottom : Bottom boundary of rectangle.
    top : Top boundary of rectangle
    ticks : Line spacing.
    fine : Grid spacing.
    vertFreq: Scaling of vertical line frequency with respect to horizontal.
    frame : TYPE
        DESCRIPTION.

    Returns
    -------
    None.

    """

    fig.data = []
    
    # Horizontal Lines
    for j in np.linspace(bottom, top, ticks):   
        ones = np.ones(fine)
        t = j * ones

        linesH = np.linspace(left, right, fine)


        color2 = 'grey'
        
        if j == bottom:
            color2 = 'blue'
        if j == top:
            color2 = 'red'     
            
 
        fn_horizontal = anim(ip_fn=z_numeric, x=linesH, y=t, i=frame)

        line_grapher(fn_horizontal.real, fn_horizontal.imag, color2)
       
    # Vertical Lines   
    for j in np.linspace(left, right, vertFreq*ticks):
  
        ones = np.ones(fine)
        t = j * ones



        linesV = np.linspace(bottom, top, fine)

        color1 = 'green'
        if j == left:
            color1 = 'orange'
        if j == right:
            color1 = 'magenta'


        fn_vertical = anim(ip_fn=z_numeric, x=t, y=linesV, i=frame)

        line_grapher(fn_vertical.real, fn_vertical.imag, color1)

  
        
    
    fig.update_layout(
                      template='plotly_dark',
                      yaxis=dict(scaleanchor="x", scaleratio=1),
                      autosize=False, # lbz tested true
                      width=1000,
                      height=500,
                      showlegend=False,
                      dragmode='pan'
#                       hoverinfo='false'
                      )

    fig.show(config={'scrollZoom': True})
    
    return

def square(z_numeric, 
              limit_range,
              ticks, 
              fine, 
              frame):
    """
    Special case of rectangle, with all sides equal.
    Parameterized by the parameter limit_range.
    """

    
    
    left = -limit_range
    right = limit_range
    bottom = -limit_range
    top = limit_range  
    
    rectangle(z_numeric, 
              left, 
              right, 
              bottom, 
              top, 
              ticks, 
              fine, 
              frame)
    return
'''
def circle(z_numeric, 
              radius,
              ticks, 
              fine, 
              frame):

    fig.data = []
    
    color1 = 'green'
    color2 = 'red'
    # Horizontal Lines
    for j in np.linspace(0, radius, ticks):  
        for i in np.linspace(0, 2*np.pi, ticks):
             ones = np.ones(fine)
             t1 = j * ones
             t2 = i * ones
             x = t1*np.cos(t2)
             y = t1*np.sin(t2)


             fn_vertical = anim(ip_fn=z_numeric, x=x, y=y, i=frame)
    
             line_grapher(fn_vertical.real, fn_vertical.imag, color1)
    
      
             fn_horizontal = anim(ip_fn=z_numeric, x=x, y=y, i=frame)
    
             line_grapher(fn_horizontal.real, fn_horizontal.imag, color2)
        
    
    fig.update_layout(
                      template='plotly_dark',
                      yaxis=dict(scaleanchor="x", scaleratio=1),
                      autosize=False, # lbz tested true
                      width=1000,
                      height=500,
                      showlegend=False,
                      dragmode='pan'
#                       hoverinfo='false'
                      )

    fig.show(config={'scrollZoom': True})
    
    return  

'''

# next objetcs: circle, ellipse, annulusConcentric, annulusEccentric, annulusElliptical

# function for ipywidget to update on change of any parameters
def update_rectangle(function,
                     transformation,
                     left, 
                     right,
                     bottom, 
                     top,
                     ticks,
                     vertFreq = 1):
    '''
    Function that updates the rectangle plot.
    '''
    
#   fine ness of points, since its all numerical method
#   we need to choose the number of points
    fine = 50

#   The main input function from user
    fun = w_numeric(eval(function))

#   The main Grapher
    rectangle(z_numeric = fun, 
                 left = left, 
                 right = right, 
                 bottom = bottom,
                 top =top,
                 ticks = ticks,
                 fine = fine,
                 frame = transformation,
                 vertFreq = vertFreq)
    return

# function for ipywidget to update on change of any parameters
def update_square(function,transformation, limit_range, ticks):
    """
    Function that updates the square plot.
    """
    
#   fine ness of points, since its all numerical method
#   we need to choose the number of points
    fine = 50

#   The main input function from user
    fun = w_numeric(eval(function))

#   The main Grapher
    square(z_numeric = fun, 
                 limit_range = limit_range,
                 ticks = ticks,
                 fine = fine,
                 frame = transformation)
    return

"""
# function for ipywidget to update on change of any parameters
def update_circle(function,transformation, radius, ticks):
    
#   fine ness of points, since its all numerical method
#   we need to choose the number of points
    fine = 50

#   The main input function from user
    fun = w_numeric(eval(function))

#   The main Grapher
    circle(z_numeric = fun, 
                 radius = radius,
                 ticks = ticks,
                 fine = fine,
                 frame = transformation)
    return
"""