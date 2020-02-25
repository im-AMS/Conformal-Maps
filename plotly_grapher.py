""""
this module deals with the plotling of graph
"""

from imports import *
import symbolic_conversion as sc
# create a figure object
fig = go.Figure()


def main_grapher(x,y , color):

    fig.add_trace(go.Scatter(x = x , y = y ,line_color=color , line = dict(shape='spline'),mode='lines'))


def graph(z , limit_range,ticks , fine , frame):

#     clear all previous fig
    fig.data = []

    for j in np.linspace(-1 * limit_range, limit_range , ticks):
        ones = np.ones(fine)
        t = j * ones

        lines = np.linspace(-1 * limit_range, limit_range, fine)
        Re, Im = sc.w_numeric(z, frame)
# color for forizontal and vertical lines
        color1 = 'red'
        color2 = 'green'

        main_grapher( Re(t,lines) , Im(t,lines) , color1)

        main_grapher( Re(lines,t), Im(lines,t) , color2)

    fig.update_layout(showlegend=False,
                      template='plotly_dark',
                      yaxis=dict(scaleanchor="x", scaleratio=1)
                      )


    fig.show(config={'scrollZoom': True})
    # iplot(fig , config={'scrollZoom': True , 'displayModeBar': True})

