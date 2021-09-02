import sympy as sym
import numpy as np

from conformalMaps.elementaryGeometry import update_rectangle, update_square, update_single_circle, update_circle, update_concentricAnnulus
from conformalMaps.mappings import RectangleToEccentricAnnulus, RectangleToEllipticAnnulus
import ipywidgets as widgets

from ipywidgets import VBox, HBox, Layout, AppLayout
from plotly.offline import init_notebook_mode, iplot

init_notebook_mode(connected=True)
