""""
this module deals with the plotling of graph
"""

from imports import *
import symbolic_conversion as sc
# create a figure object
fig = go.Figure()


def line_grapher(x, y, color):

    fig.add_trace(go.Scatter(x=x, y=y, line_color=color,hoverinfo='none',
                             line=dict(shape='spline'), mode='lines'))




def graph(z_numeric, limit_range, ticks, fine, frame):
# clear prev data
    fig.data = []

    for j in np.linspace(-1 * limit_range, limit_range, ticks):
        ones = np.ones(fine)
        t = j * ones

        lines = np.linspace(-1 * limit_range, limit_range, fine)

        # Re, Im = sc.frames(z_numeric, i=frame)

        # color for forizontal and vertical lines
        color1 = 'green'
        color2 = 'red'

        fn_vertical = sc.anim(ip_fn=z_numeric, x=t, y=lines, i=frame)

        line_grapher(fn_vertical.real, fn_vertical.imag, color1)

        fn_horizontal = sc.anim(ip_fn=z_numeric, x=lines, y=t, i=frame)

        line_grapher(fn_horizontal.real, fn_horizontal.imag, color2)

    fig.update_layout(
                      template='plotly_dark',
                      yaxis=dict(scaleanchor="x", scaleratio=1),

                      autosize=False,
                      width=1000,
                      height=500,
                      showlegend=False,
                      dragmode='pan'
#                       hoverinfo='false'
                      )

    fig.show(config={'scrollZoom': True})
