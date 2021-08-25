""""
This module deals with the plotling of graph.
"""

import numpy as np
import sympy as sym
from sympy import *
import plotly.graph_objects as go
from numba import jit

jit(nopython=True, parallel=True)

e = sym.E
pi = np.pi
i = sym.I
x, y = sym.symbols('x y', real=True)
# complex number of the form z = a + i b
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
    w : Numerical function, depending on real and imaginary part of z.

    """
    w = sym.lambdify((x, y), z, "numpy")
    return w


# define grid(horizontal and vertical lines), z defined above as x + iy
grid = w_numeric(z)


def anim(ip_fn, x, y, i):
    """
    Function which creates the cool frames for the slider.
    what it does is
    (input function - Grid) * i + Grid
    here grid is the function w=z
    """
    global grid
    """
    The idea behind this is that, we initially subtract the grid from the input function,
    then we add it back to the grid part by part. 
    i.e, add 0% (i = 0 => displays grid)
    add 100% (i = 1 => displays inp_fn) 
    """
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

    fig.add_trace(go.Scatter(x=x, y=y, line_color=color, hoverinfo='none',
                             line=dict(shape='spline'), mode='lines'))


# transformation of rectangular grid
def rectangle(z_numeric,
              left,
              right,
              bottom,
              top,
              ticks,
              fine,
              frame,
              vertFreq=1):
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
    """
    plotting "ticks" number of Horizontal Lines from range "left" to "right" with "fine" number of 
    points for each line 
    """
    for j in np.linspace(bottom, top, ticks):
        ones = np.ones(fine)

        # plotting "j"th Horizontal line
        t = j * ones

        linesH = np.linspace(left, right, fine)

        color2 = 'grey'

        if j == bottom:
            color2 = 'blue'
        if j == top:
            color2 = 'red'

        """
        to plot j th Horizontal line for "fine" number of points per line,'
        i.e, array of co-ordinates for j th line (x,y) ranges from
        x = [ left, right ]
        y = j 
        where length of x and y is "fine"
        """
        fn_horizontal = anim(ip_fn=z_numeric, x=linesH, y=t, i=frame)

        line_grapher(fn_horizontal.real, fn_horizontal.imag, color2)

    # Vertical Lines
    # similar logic applies to vertical lines as explained above.
    for j in np.linspace(left, right, vertFreq * ticks):

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
        autosize=False,  # lbz tested true
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


def circle(z_numeric,
                 radius,
                 fine,
                 frame,
                 x0,
                 y0):
    """

    Parameters
    ----------
    z_numeric: Numerical conplex function
    radius: radius of circle
    fine: number of points used to plot circle
    frame: anim frame
    x0: x coordinate for center of circle
    y0: y coordinate for center of circle


    :return: None
    """

    fig.data = []

    t = np.linspace(0, 2 * np.pi, fine)
    t2 = np.linspace(0, radius, fine)

    X = x0 + radius * np.cos(t)
    Y = y0 + radius * np.sin(t)

    fn_vertical = anim(ip_fn=z_numeric, x=X, y=Y, i=frame)

    color = "white"
    line_grapher(fn_vertical.real, fn_vertical.imag, color)
    
    
    
    for i in np.linspace(0.01*radius, 0.98*radius, 20):
           X = x0 + i * np.cos(t)
           Y = y0 + i * np.sin(t)
        
           fn_vertical = anim(ip_fn=z_numeric, x=X, y=Y, i=frame)
        
           color = "green"
           line_grapher(fn_vertical.real, fn_vertical.imag, color)
       
    for i in np.linspace(0, 2*np.pi, 20):
           X = x0 + t2 * np.cos(i)
           Y = y0 + t2 * np.sin(i)
        
           fn_vertical = anim(ip_fn=z_numeric, x=X, y=Y, i=frame)
        
           color = "red"
           line_grapher(fn_vertical.real, fn_vertical.imag, color)       
   

    fig.update_layout(
        template='plotly_dark',
        yaxis=dict(scaleanchor="x", scaleratio=1),
        autosize=False,  # lbz tested true
        width=1000,
        height=500,
        showlegend=False,
        dragmode='pan'
#                       hoverinfo='false'
    )

    fig.show(config={'scrollZoom': True})

    return

def concentricAnnulus(z_numeric,
                 innerRadius,
                 outerRadius,
                 fine,
                 frame,
                 x0,
                 y0):
    """
    This function describes a concentric annulus.
    
    Parameters
    ----------
    z_numeric: Numerical complex function
    innerRadius: radius of inner circle
    outerRadius: radius of outer circle
    fine: number of points used to plot circle
    frame: anim frame
    x0: x coordinate for center of circle
    y0: y coordinate for center of circle


    :return: None
    """

    fig.data = []

    t = np.linspace(0, 2 * np.pi, fine)
    t2 = np.linspace(innerRadius, outerRadius, fine)

    X1 = x0 + outerRadius * np.cos(t)
    Y1 = y0 + outerRadius * np.sin(t)

    fn_vertical = anim(ip_fn=z_numeric, x=X1, y=Y1, i=frame)

    color1 = "magenta"
    line_grapher(fn_vertical.real, fn_vertical.imag, color1)
    
    
    X2 = x0 + innerRadius * np.cos(t)
    Y2 = y0 + innerRadius * np.sin(t)

    fn_vertical = anim(ip_fn=z_numeric, x=X2, y=Y2, i=frame)

    color2 = "blue"
    line_grapher(fn_vertical.real, fn_vertical.imag, color2)    
    
    
    
    for i in np.linspace(1.01*innerRadius, 0.98*outerRadius, 20):
           X = x0 + i * np.cos(t)
           Y = y0 + i * np.sin(t)
        
           fn_vertical = anim(ip_fn=z_numeric, x=X, y=Y, i=frame)
        
           color = "green"
           line_grapher(fn_vertical.real, fn_vertical.imag, color)
       
    for i in np.linspace(0, 2*np.pi, 20):
           X = x0 + t2 * np.cos(i)
           Y = y0 + t2 * np.sin(i)
        
           fn_vertical = anim(ip_fn=z_numeric, x=X, y=Y, i=frame)
        
           color = "grey"
           line_grapher(fn_vertical.real, fn_vertical.imag, color)       
   

    fig.update_layout(
        template='plotly_dark',
        yaxis=dict(scaleanchor="x", scaleratio=1),
        autosize=False,  # lbz tested true
        width=1000,
        height=500,
        showlegend=False,
        dragmode='pan'
#                       hoverinfo='false'
    )

    fig.show(config={'scrollZoom': True})

    return


def single_circle(z_numeric,
                 radius,
                 fine,
                 frame,
                 x0,
                 y0):
    """
    This function describes the outer boundary of a circle


    Parameters
    ----------
    z_numeric: Numerical conplex function
    radius: radius of circle
    fine: number of points used to plot circle
    frame: anim frame
    x0: x coordinate for center of circle
    y0: y coordinate for center of circle


    :return: None
    """

    fig.data = []

    t = np.linspace(0, 2 * np.pi, fine)

    X = x0 + radius * np.cos(t)
    Y = y0 + radius * np.sin(t)

    fn_vertical = anim(ip_fn=z_numeric, x=X, y=Y, i=frame)

    color = "white"
    line_grapher(fn_vertical.real, fn_vertical.imag, color)

    fig.update_layout(
        template='plotly_dark',
        yaxis=dict(scaleanchor="x", scaleratio=1),
        autosize=False,  # lbz tested true
        width=1000,
        height=500,
        showlegend=False,
        dragmode='pan'
#                       hoverinfo='false'
    )

    fig.show(config={'scrollZoom': True})

    return



# function for ipywidget to update on change of any parameters
def update_rectangle(function,
                     transformation,
                     left,
                     right,
                     bottom,
                     top,
                     ticks,
                     vertFreq=1):
    """
    Function that updates the rectangle plot.
    """

    #   fine ness of points, since its all numerical method
    #   we need to choose the number of points/coordinates for each line
    fine = 50

    #   The main input function from user
    fun = w_numeric(eval(function))

    #   The main Grapher
    rectangle(z_numeric=fun,
              left=left,
              right=right,
              bottom=bottom,
              top=top,
              ticks=ticks,
              fine=fine,
              frame=transformation,
              vertFreq=vertFreq)
    return


# function for ipywidget to update on change of any parameters
def update_square(function, transformation, limit_range, ticks):
    """
    Function that updates the square plot.
    """

    #   fine ness of points, since its all numerical method
    #   we need to choose the number of points
    fine = 50

    #   The main input function from user
    fun = w_numeric(eval(function))

    #   The main Grapher
    square(z_numeric=fun,
           limit_range=limit_range,
           ticks=ticks,
           fine=fine,
           frame=transformation)
    return


def update_single_circle(
        function,
        transformation,
        radius,
        x0,
        y0):
    """
    function that updates single_circle plot
    """

    fine = 50

    fun = w_numeric(eval(function))
    single_circle(z_numeric=fun,
                 radius=radius,
                 fine=fine,
                 frame=transformation,
                 x0=x0,
                 y0=y0)

    return


def update_circle(
        function,
        transformation,
        radius,
        x0,
        y0):
    """
    function that updates circle plot
    """

    fine = 50

    fun = w_numeric(eval(function))
    circle(z_numeric=fun,
                 radius=radius,
                 fine=fine,
                 frame=transformation,
                 x0=x0,
                 y0=y0)

    return


def update_concentricAnnulus(
        function,
        transformation,
        innerRadius,
        outerRadius,
        x0,
        y0):
    """
    function that updates concentric annulus plot
    """

    fine = 50

    fun = w_numeric(eval(function))
    concentricAnnulus(z_numeric=fun,
                 innerRadius=innerRadius,
                 outerRadius=outerRadius,
                 fine=fine,
                 frame=transformation,
                 x0=x0,
                 y0=y0)

    return