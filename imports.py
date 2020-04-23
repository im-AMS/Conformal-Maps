""""
All the required lib
"""


import numpy as np
from sympy import *
import plotly.graph_objects as go
from plotly.offline import init_notebook_mode, iplot
#for faster computation
from numba import jit
jit(nopython=True , parallel=True)
# njit(fastmath=True,parallel=True)
#declare all the Sympy variable/functions
e = E
pi = np.pi
i = I
a ,  b = symbols('a b',real = true)
#complex number of the form z = a + i b
z= a + I* b

