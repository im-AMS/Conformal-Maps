from imports import *
import symbolic_conversion as sc
import plotly_grapher as pg
import time as t


numeric = sc.w_numeric(z**2)

# print(numeric(1,0))

pg.graph(z_numeric = numeric , limit_range = 2 , ticks = 5 , fine = 10 , frame = 1)

