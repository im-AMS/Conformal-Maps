from conformalMaps.grids import *
from conformalMaps.mappings import RectangleToEccentricAnnulus, RectangleToEllipticAnnulus, ConcentricAnnulusToEccentricAnnulus
from ipywidgets import widgets
from ipywidgets import HBox,VBox


rect = Rectangle()

left = widgets.FloatSlider(min=-10, max=10, value=-1, description='left')
bottom = widgets.FloatSlider(min=-10, max=10, value=-1, description='bottom')

top = widgets.FloatSlider(min=-10, max=10, value=1, description='top')
right = widgets.FloatSlider(min=-10, max=10, value=1, description='right')

fine = widgets.IntSlider(min = 20, max = 100, value=50, description='Fine')

Hticks = widgets.IntSlider(min = 2, max = 50, value=10, description='Hticks')
Vticks = widgets.IntSlider(min = 2, max = 50, value=10, description='Vticks')


function = widgets.Text( value = 'z**2' , description='w : ')

frame = widgets.FloatSlider(min=0, max=100, value=100, step = 5, description='anim')

play = widgets.Play(min= 0, max = 100, step = 5)
widgets.jslink((play, 'value'), (frame, 'value'))

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


rect.check_analytic()


sq = Square()

side = widgets.FloatSlider(min=0.01, max=10, value=1, description='side')

fine = widgets.IntSlider(min = 20, max = 100, value=50, description='Fine')

Hticks = widgets.IntSlider(min = 2, max = 50, value=10, description='Hticks')
Vticks = widgets.IntSlider(min = 2, max = 50, value=10, description='Vticks')


function = widgets.Text( value = 'z**2' , description='w : ')

frame = widgets.FloatSlider(min=0, max=100, value=100, step = 5, description='anim')

play = widgets.Play(min= 0, max = 100, step = 5)
widgets.jslink((play, 'value'), (frame, 'value'))


interactive_plot = widgets.interactive(sq.updateFunc,
                                       w = function,
                                       side = side,
                                       fine = fine,
                                      Hticks = Hticks,
                                      Vticks = Vticks,
                                      frame = frame
                                      )

# w1 = VBox([ left, right])
# w2 = VBox([top,bottom])
box1 = HBox([side, Hticks,Vticks])

box2 = HBox([function, fine])

anim_slider = HBox([play, frame])

w = VBox([box1, box2, anim_slider, sq.show()])

w


sq.check_analytic()


r = sym.sqrt(x**2+y**2)

f = x*(sym.sqrt(x**2+y**2-x**2*y**2))/r + sym.I*y*(sym.sqrt(x**2+y**2-x**2*y**2))/r # transforms unit square

sq2 = Square()

side = widgets.FloatSlider(min=0.01, max=10, value=1, description='side')

fine = widgets.IntSlider(min = 20, max = 100, value=50, description='Fine')

Hticks = widgets.IntSlider(min = 2, max = 50, value=10, description='Hticks')
Vticks = widgets.IntSlider(min = 2, max = 50, value=10, description='Vticks')


function = widgets.Text(  value = 'get_ipython().run_line_magic("s'", " %(f) , description='w : ')")

frame = widgets.FloatSlider(min=0, max=100, value=100, step = 5, description='anim')

play = widgets.Play(min= 0, max = 100, step = 5)
widgets.jslink((play, 'value'), (frame, 'value'))


interactive_plot = widgets.interactive(sq2.updateFunc,
                                       w = function,
                                       side = side,
                                       fine = fine,
                                      Hticks = Hticks,
                                      Vticks = Vticks,
                                      frame = frame
                                      )

# w1 = VBox([ left, right])
# w2 = VBox([top,bottom])
box1 = HBox([side, Hticks,Vticks])

box2 = HBox([function, fine])

anim_slider = HBox([play, frame])

w = VBox([box1, box2, anim_slider, sq2.show()])

w



sq2.check_analytic()


donut = Donut()

rin = widgets.FloatSlider(min=0, max=10, value=1, description='Rin')
rout = widgets.FloatSlider(min=1, max=20, value=3, description='Rout')

x0 = widgets.FloatSlider(min=-10, max=10, value=0, description='x0')
y0 = widgets.FloatSlider(min=-10, max=10, value=0, description='y0')

cticks = widgets.IntSlider(min = 2, max = 50, value=4, description='cticks')
rticks = widgets.IntSlider(min = 2, max = 50, value=4, description='rticks')

fine = widgets.IntSlider(min = 20, max = 100, value=50, description='Fine')

function = widgets.Text( value = 'z**2' , description='w : ')

frame = widgets.FloatSlider(min=0, max=100, value=100, step = 2, description='anim')

play = widgets.Play(min= 0, max = 100, step = 5)
widgets.jslink((play, 'value'), (frame, 'value'))

interactive_plot = widgets.interactive(donut.updateFunc,
                                       rin = rin,
                                       rout = rout,
                                       x0 = x0,
                                       y0 = y0,
                                       fine = fine,
                                       cticks = cticks,
                                       rticks = rticks,
                                       w = function,
                                       frame = frame)

radius = VBox([rin, rout])
offset = VBox([x0, y0])
ticks = VBox([cticks, rticks])
group = HBox([radius, offset,ticks])
animation = HBox([play, frame])

w1 = VBox([group, HBox([fine, function]), animation, donut.show()])

w1


donut.check_analytic()


circle = Circle()

r = widgets.FloatSlider(min=0.1, max=10, value=1, description='R')


x0 = widgets.FloatSlider(min=-10, max=10, value=0, description='x0')
y0 = widgets.FloatSlider(min=-10, max=10, value=0, description='y0')

cticks = widgets.IntSlider(min = 2, max = 50, value=4, description='cticks')
rticks = widgets.IntSlider(min = 0, max = 50, value=4, description='rticks')

fine = widgets.IntSlider(min = 20, max = 100, value=50, description='Fine')

function = widgets.Text( value = 'z**2' , description='w : ')

frame = widgets.FloatSlider(min=0, max=100, value=100, step = 2, description='anim')

play = widgets.Play(min= 0, max = 100, step = 2)
widgets.jslink((play, 'value'), (frame, 'value'))

interactive_plot = widgets.interactive(circle.updateFunc,
                                       r = r,
                                       x0 = x0,
                                       y0 = y0,
                                       fine = fine,
                                       cticks = cticks,
                                       rticks = rticks,
                                       w = function,
                                       frame = frame)

radius = VBox([r, fine])
offset = VBox([x0, y0])
ticks = VBox([cticks, rticks])
group = HBox([radius, offset,ticks])
animation = HBox([play, frame])

w1 = VBox([group, function, animation, circle.show()])

w1
# display(interactive_plot,circle.show())


circle.check_analytic()


single = Single_circle(rticks=0)

r = widgets.FloatSlider(min=0.1, max=10, value=1.08, description='R')


x0 = widgets.FloatSlider(min=-10, max=10, value=-0.08, description='x0')
y0 = widgets.FloatSlider(min=-10, max=10, value=0.08, description='y0')

rticks = widgets.IntSlider(min = 0, max = 50, value=0, description='rticks')

fine = widgets.IntSlider(min = 20, max = 100, value=50, description='Fine')

function = widgets.Text( value = 'z+1/z' , description='w : ')

frame = widgets.FloatSlider(min=0, max=100, value=100, step = 2, description='anim')

play = widgets.Play(min= 0, max = 100, step = 2)
widgets.jslink((play, 'value'), (frame, 'value'))

interactive_plot = widgets.interactive(single.updateFunc,
                                       r = r,
                                       x0 = x0,
                                       y0 = y0,
                                       fine = fine,
                                       rticks = rticks,
                                       w = function,
                                       frame = frame)

radius = VBox([r, fine])
offset = VBox([x0, y0])
# ticks = VBox([cticks, rticks])
group = HBox([radius, offset,rticks])
animation = HBox([play, frame])

w1 = VBox([group, function, animation, single.show()])

w1


single.check_analytic()


R1 = 4 # inner radius of target eccentric annulus
R2 = 7.6 # outer radius of target eccentric annulus
ep = 0.7 # relative eccentricity of target eccentric annulus

trans = RectangleToEccentricAnnulus(R1, R2, ep)


rect = Rectangle()

left = widgets.FloatSlider(min=-10, max=10, value=-pi, description='left')
right = widgets.FloatSlider(min=-10, max=10, value=pi, description='right')

top = widgets.FloatSlider(min=-10, max=10, value=1.5, description='top')
bottom = widgets.FloatSlider(min=-10, max=10, value=0.8, description='bottom')


fine = widgets.IntSlider(min = 20, max = 100, value=50, description='Fine')

Hticks = widgets.IntSlider(min = 2, max = 50, value=10, description='Hticks')
Vticks = widgets.IntSlider(min = 2, max = 50, value=20, description='Vticks')


function = widgets.Text( value = '{0}'.format(trans.mapping(z)) , description='w : ')

frame = widgets.FloatSlider(min=0, max=100, value=100, step = 5, description='anim')

play = widgets.Play(min= 0, max = 100, step = 5)
# widgets.jslink((frame, 'value'), (play, 'value'))
widgets.jslink((play, 'value'), (frame, 'value'))

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




a = 5 # half axis of outer ellipse

b = 3.6 # half axis of inner ellipse

trans = RectangleToEllipticAnnulus(b, a)


rect = Rectangle()

left = widgets.FloatSlider(min=-10, max=10, value=-pi, description='left')
right = widgets.FloatSlider(min=-10, max=10, value=pi, description='right')

top = widgets.FloatSlider(min=-10, max=10, value=1.5, description='top')
bottom = widgets.FloatSlider(min=-10, max=10, value=0.8, description='bottom')


fine = widgets.IntSlider(min = 20, max = 100, value=50, description='Fine')

Hticks = widgets.IntSlider(min = 2, max = 50, value=10, description='Hticks')
Vticks = widgets.IntSlider(min = 2, max = 50, value=20, description='Vticks')


function = widgets.Text( value = '{0}'.format(trans.mapping(z)) , description='w : ')

frame = widgets.FloatSlider(min=0, max=100, value=100, step = 5, description='anim')

play = widgets.Play(min= 0, max = 100, step = 5)
# widgets.jslink((frame, 'value'), (play, 'value'))
widgets.jslink((play, 'value'), (frame, 'value'))

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


