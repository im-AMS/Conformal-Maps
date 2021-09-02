from conformalMaps.configs_for_jupyter import *
from conformalMaps.elementaryGeometry import fig
from conformalMaps.symbols import x, y, i, z, e
pi = np.pi


# ------------------Animation Speed (1 to 10)---------------
speed = 3.5





# since it is numerical computation, we need range to operate in
left = widgets.FloatSlider(min = -5 , max = 5 , value = -2 , description = "left",visibility = 'hidden')
right = widgets.FloatSlider(min = -5 , max = 5 , value = 2 , description = "right",visibility = 'hidden')
top = widgets.FloatSlider(min = -5 , max = 5 , value = 1 , description = "top",visibility = 'hidden')
bottom = widgets.FloatSlider(min = -5 , max = 5 , value = -1 , description = "bottom",visibility = 'hidden')

# change ticks slider to add or remove lines in the range
ticks = widgets.IntSlider(min = 2 , max = 40 , value = 20 , description = "Ticks")

# the input function w to draw conformal map
function = widgets.Text( value = 'exp(z)' , description='w : ')


# play button widget to animate
play = widgets.Play(min = 0 , max = 100 , value = 100, step= int(speed))

slider = widgets.IntSlider(min = 0 , max = 100 , value = 100,description = "anim")

# widgets.jslink((play, 'value'), (slider, 'value'))
    
# call all the variables in ipywidgets
interactive_plot = widgets.interactive(update_rectangle,
                                       function = function,
                                       transformation = slider,
                                       left =  left,
                                       right = right,
                                       bottom = bottom,
                                       top = top,
                                       ticks = ticks,
                                       vertFreq = 1,
                                       anim_scaler = 100)

# display the output
# display(interactive_plot)



# VBox([ HBox([play, slider]), fig])
# HBox([play, slider,fig])

# HBox([VBox([play,slider]),
#       fig])

# fig
# HBox([play, slider])
# fig
# interactive_plot
HBox([interactive_plot,fig])
# fig.show()


fig.data


# ------------------Animation Speed (1 to 10)---------------
speed = 3.5



# since it is numerical computation, we need range to operate in, given by limit_range
limit_range = widgets.FloatSlider(min = 0.1 , max = 10 , value = np.pi , description = "Limit Range",visibility = 'hidden')

# change ticks slider to add or remove lines in the range
ticks = widgets.IntSlider(min = 2 , max = 40 , value = 20 , description = "Ticks")

# the input function w to draw conformal map
function = widgets.Text( value = 'exp(z)' , description='w : ')

# play button widget to animate
play = widgets.Play(min = 0 , max = 100 , value = 100, step= int(speed))


    
# call all the variables in ipywidgets
interactive_plot = widgets.interactive(update_square,
                                       function = function, 
                                       transformation = play,
                                       limit_range=limit_range,
                                       ticks = ticks,
                                      anim_scaler=100)

# display the output
display(interactive_plot)








R1 = 4 # inner radius of target eccentric annulus
R2 = 7.6 # outer radius of target eccentric annulus
ep = 0.7 # relative eccentricity of target eccentric annulus

trans = RectangleToEccentricAnnulus(R1, R2, ep)



# since it is numerical computation, we need range to operate in, given by limit_range
limit_range = widgets.FloatSlider(min = 0.1 , max = 10 , value = np.pi , description = "Limit Range",visibility = 'hidden')

# change ticks slider to add or remove lines in the range
ticks = widgets.IntSlider(min = 2 , max = 40 , value = 11 , description = "Ticks")

# the input function w to draw conformal map
function = widgets.Text( value ='{0}'.format(trans.mapping(z)) , description='w : ')

# play button widget to animate
play = widgets.Play(min = 0 , max = 100 , value = 100, step=5)


    
# call all the variables in ipywidgets
interactive_plot = widgets.interactive(update_rectangle,
                                       function = function, 
                                       transformation = play,
                                       left =  trans.left,
                                       right = trans.right,
                                       bottom = trans.bottom,
                                       top = trans.top,
                                       ticks = ticks,
                                       vertFreq = 7,
                                       anim_scaler=100)

# display the output
display(interactive_plot)


a = 5 # half axis of outer ellipse

b = 3.6 # half axis of inner ellipse

trans = RectangleToEllipticAnnulus(b, a)


# change ticks slider to add or remove lines in the range
ticks = widgets.IntSlider(min = 2 , max = 40 , value = 11 , description = "Ticks")

vertFreq = widgets.IntSlider(min = 1 , max = 10 , value = 1 , description = "vertFreq")

# the input function w to draw conformal map
function = widgets.Text( value = '{0}'.format(trans.mapping(eval('z'))) , description='w : ')

# play button widget to animate
play = widgets.Play(min = 0 , max = 100 , value = 100, step=5)


    
# call all the variables in ipywidgets
interactive_plot = widgets.interactive(update_rectangle,
                                       function = function, 
                                       transformation = play,
                                       left = trans.left,
                                       right = trans.right,
                                       bottom = trans.bottom,
                                       top = trans.top,
                                       ticks = ticks,
                                       vertFreq = vertFreq,
                                       anim_scaler=100)

# display the output
display(interactive_plot)


function = widgets.Text( value = '(z+1)/(i-z)' , description='w : ')

innerRadius = widgets.FloatSlider(min = 0 , max = 5 , value = 3 , description = "radius")
outerRadius = widgets.FloatSlider(min = 6 , max = 10.0 , value = 7 , description = "radius")

# play button widget to animate
play = widgets.Play(min = 0 , max = 100 , value = 100, step=2)

x0 = widgets.FloatSlider(min = -3 , max = 3 , value = -0.08, description ="x0")
y0 = widgets.FloatSlider(min = -3 , max = 3 , value = 0.08, description ="y0")

interactive_plot = widgets.interactive(update_concentricAnnulus,
                                       function = function, 
                                       transformation = play,
                                       innerRadius=innerRadius,
                                       outerRadius=outerRadius,
                                       x0 = 0,
                                       y0 = 0,
                                      anim_scaler=100)

display(interactive_plot)   











function = widgets.Text( value = 'z**2' , description='w : ')
radius = widgets.FloatSlider(min = 0 , max = 10.0 , value = 1.08 , description = "radius")
# play button widget to animate
play = widgets.Play(min = 0 , max = 100 , value = 100, step=5)
x0 = widgets.FloatSlider(min = -3 , max = 3 , value = -0.08, description ="x0")
y0 = widgets.FloatSlider(min = -3 , max = 3 , value = 0.08, description ="y0")

interactive_plot = widgets.interactive(update_circle,
                                       function = function, 
                                       transformation = play,
                                       radius=radius,
                                       x0 = 0,
                                       y0 = 0,
                                      anim_scaler=100)

display(interactive_plot)                                       


function = widgets.Text( value = '(z+1)/(i-z)' , description='w : ')
innerRadius = widgets.FloatSlider(min = 0 , max = 5 , value = 3 , description = "radius")
outerRadius = widgets.FloatSlider(min = 6 , max = 10.0 , value = 7 , description = "radius")
# play button widget to animate
play = widgets.Play(min = 0 , max = 100 , value = 100, step=2)
x0 = widgets.FloatSlider(min = -3 , max = 3 , value = -0.08, description ="x0")
y0 = widgets.FloatSlider(min = -3 , max = 3 , value = 0.08, description ="y0")

interactive_plot = widgets.interactive(update_concentricAnnulus,
                                       function = function, 
                                       transformation = play,
                                       innerRadius=innerRadius,
                                       outerRadius=outerRadius,
                                       x0 = 0,
                                       y0 = 0,
                                      anim_scaler=100)

display(interactive_plot)          


function = widgets.Text( value = 'z+1/z' , description='w : ')
radius = widgets.FloatSlider(min = 0 , max = 10.0 , value = 1.08 , description = "radius")
# play button widget to animate
play = widgets.Play(min = 0 , max = 100 , value = 100, step=5)
x0 = widgets.FloatSlider(min = -3 , max = 3 , value = -0.08, description ="x0")
y0 = widgets.FloatSlider(min = -3 , max = 3 , value = 0.08, description ="y0")

interactive_plot = widgets.interactive(update_single_circle,
                                       function = function, 
                                       transformation = play,
                                       radius=radius,
                                       x0 = x0,
                                       y0 = y0,
                                      anim_scaler=100)

display(interactive_plot)     



