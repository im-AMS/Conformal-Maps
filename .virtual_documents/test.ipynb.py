from conformalMaps.new_elementary import *
from ipywidgets import widgets
from ipywidgets import HBox,VBox


left = widgets.FloatSlider(min=-10, max=0, value=-1, description='left')
bottom = widgets.FloatSlider(min=-10, max=0, value=-1, description='bottom')

top = widgets.FloatSlider(min=0, max=10, value=1, description='top')
right = widgets.FloatSlider(min=0, max=10, value=1, description='right')

fine = widgets.IntSlider(min = 5, max = 50, value=10, description='Fine')

Hticks = widgets.IntSlider(min = 2, max = 50, value=10, description='Hticks')
Vticks = widgets.IntSlider(min = 2, max = 50, value=10, description='Vticks')


function = widgets.Text( value = 'z**2' , description='w : ')

frame = widgets.FloatSlider(min=0, max=100, value=100, step = 5, description='anim')

play = widgets.Play(min= 0, max = 100, step = 5)
# widgets.jslink((frame, 'value'), (play, 'value'))
widgets.jslink((play, 'value'), (frame, 'value'))

rect = Rectangle()


interactive_plot = widgets.interactive(rect.updateFunc,
                                       w = function,
                                       left = left,
                                       right = right,
                                       top= top,
                                       bottom = bottom,
                                       fine = fine,
                                      Hticks = Hticks,
                                      Vticks = Vticks,
                                      frame = frame
                                      )


w1 = VBox([ left, right])
w2 = VBox([top,bottom])
w3 = VBox([Hticks,Vticks])
w4 = HBox([w1,w2,w3])

w5 = HBox([function, fine])

anim_slider = HBox([play, frame])

w = VBox([w4, w5, anim_slider, rect.show()])

w



