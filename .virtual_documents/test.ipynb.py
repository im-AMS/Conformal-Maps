from conformalMaps.new_elementary import *
from ipywidgets import widgets
from ipywidgets import HBox,VBox


left = widgets.FloatSlider(min=-10, max=0, value=-1, description='left')
bottom = widgets.FloatSlider(min=-10, max=0, value=-1, description='bottom')

top = widgets.FloatSlider(min=0, max=10, value=1, description='top')
right = widgets.FloatSlider(min=0, max=10, value=1, description='right')

fine = widgets.IntSlider(min = 5, max = 50, value=10, description='Fine')

Hticks = widgets.IntSlider(min = 2, max = 50, value=5, description='Hticks')
Vticks = widgets.IntSlider(min = 2, max = 50, value=5, description='Vticks')


function = widgets.Text( value = 'z' , description='w : ')

rect = Rectangle()


interactive_plot = widgets.interactive(rect.updateFunc,
                                       w = function,
                                       left = left,
                                       right = right,
                                       top= top,
                                       bottom = bottom,
                                       fine = fine,
                                      Hticks = Hticks,
                                      Vticks = Vticks)


w1 = HBox([ left, right])
w2 = HBox([top,bottom])
w3 = HBox([Hticks,Vticks])
w4 = VBox([w1,w2,w3])

w5 = HBox([function, fine])

w = VBox([w4, w5, rect.show()])

w



