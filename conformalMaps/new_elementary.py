import numpy as np
import plotly.graph_objs as go
import sympy as sym
from sympy import *

x, y = sym.symbols('x y', real=True)
I = i = sym.I
e = sym.exp

z = x + sym.I * y


class Rectangle:
    def __init__(self, left=-1, right=1, top=1, bottom=-1, fine=50, Hticks=10, Vticks=10, w=None):

        self.left = left
        self.right = right
        self.top = top
        self.bottom = bottom
        self.fine = fine
        self.Hticks = Hticks
        self.Vticks = Vticks
        self.z = x + sym.I * y

        self.x, self.y = sym.symbols('x y', real=True)

        if w is None:
            self.w = x + sym.I * y
        elif type(w) == str:
            self.w = self.evaluate(w)
        else:
            self.w = w

        self.w_sympy = self.w

        self.init_plotly(self.left, self.right, self.top, self.bottom, self.fine, self.Hticks, self.Vticks, self.w)

    def init_plotly(self, left, right, top, bottom, fine, Hticks, Vticks, w):

        self.transformed = self.matrix_generator(w=w, left=left, right=right, top=top, bottom=bottom, fine=fine,
                                                 Hticks=Hticks, Vticks=Vticks)

        self.traces = self.create_traces(self.transformed)

        self.fig = go.FigureWidget(data=self.traces)

        self.fig = self.fig.update_layout(
            template='plotly_dark',
            yaxis=dict(scaleanchor="x", scaleratio=1),
            autosize=False,
            width=900,
            height=500,
            showlegend=False,
            dragmode='pan')

    def matrix_generator(self, left, right, top, bottom, fine, Hticks, Vticks, w):

        self.X, self.Y = self.gen_coordinate_grid(left, right, top, bottom, fine, Hticks, Vticks)

        self.w = self.w_numeric(w)

        return self.plugin(w=self.w, X=self.X, Y=self.Y)

    def gen_coordinate_grid(self, left=None, right=None, top=None, bottom=None, fine=None, Hticks=None, Vticks=None):

        if left is None:
            left = self.left
        else:
            self.left = left

        if right is None:
            right = self.right
        else:
            self.right = right

        if top is None:
            top = self.top
        else:
            self.top = top

        if bottom is None:
            bottom = self.bottom
        else:
            self.bottom = bottom

        if fine is None:
            fine = self.fine
        else:
            self.fine = fine

        if Hticks is None:
            Hticks = self.Hticks
        else:
            self.Hticks = Hticks

        if Vticks is None:
            Vticks = self.Vticks
        else:
            self.Vticks = Vticks

        Hx, Hy = np.meshgrid(np.linspace(self.left, self.right, self.fine, dtype=complex),
                             np.linspace(self.bottom, self.top, self.Hticks, dtype=complex))
        Vx, Vy = np.meshgrid(np.linspace(self.left, self.right, self.Vticks, dtype=complex),
                             np.linspace(self.bottom, self.top, self.fine, dtype=complex))

        X = []
        Y = []

        X.extend(Hx)
        X.extend(np.transpose(Vx))

        Y.extend(Hy)
        Y.extend(np.transpose(Vy))

        return X, Y

    def w_numeric(self, w):
        return sym.lambdify((x, y), w, "numpy")

    def plugin(self, w, X, Y):

        matrix = X.copy()  # same shape as X or Y
        for j in range(len(X)):
            for k in range(len(X[j])):
                matrix[j][k] = w(X[j][k], Y[j][k])

            matrix[j] = np.array(matrix[j])

        # returns list of numpy arrays
        return matrix

    def create_traces(self, transformed_mat):

        traces = []
        for count, arr in enumerate(transformed_mat):
            if count == 0:
                color = 'blue'
            elif 0 < count < self.Hticks - 1:
                color = 'grey'
            elif count == self.Hticks - 1:
                color = 'red'
            elif count == self.Hticks:
                color = 'orange'
            elif self.Hticks < count < self.Vticks + self.Hticks - 1:
                color = 'green'
            elif count == self.Hticks + self.Vticks - 1:
                color = 'magenta'
            traces.append(go.Scatter(x=arr.real,
                                     y=arr.imag,
                                     line_color=color,
                                     hoverinfo='none',
                                     line=dict(shape='spline'),
                                     mode='lines'))

        return traces

    def over_write_traces(self, transformed_mat):

        with self.fig.batch_update():
            for count, tmp in enumerate(transformed_mat):
                self.fig.data[count].x = tmp.real
                self.fig.data[count].y = tmp.imag

    def add_new_data_to_traces(self, transformed_mat):

        with self.fig.batch_update():
            self.fig.data = []
            self.traces = self.create_traces(transformed_mat)
            self.fig.add_traces(self.traces)

    def anim(self, w, left, right, top, bottom, fine, Hticks, Vticks, frame, scale=100):

        return self.matrix_generator(w=(w - z) * (frame / scale) + z, left=left, right=right, top=top, bottom=bottom,
                                     fine=fine, Hticks=Hticks, Vticks=Vticks)

    def check_analytic(self, w = None):
        if w is None:
            f = self.w_sympy
        elif type(w) == str:
            f = self.w_sympy = self.evaluate(w)
        else:
            f = self.w_sympy = w

        u = sym.re(f)
        v = sym.im(f)

        cond1 = sym.diff(u, x) - sym.diff(v, y)
        cond2 = sym.diff(u, y) + sym.diff(v, x)

        if sym.simplify(cond1) == 0 and sym.simplify(cond2) == 0:
            print('The function is conformal, angles are preserved :)')
        else:
            print('The function is not conformal, angle are not preseverved ...')


    def evaluate(self, w):
        try:
            self.w_sympy = w
            return eval(w)
        except:
            # tmp = exc
            print("CHECK FUNCTION w AGAIN, USING PREVIOUS ENTERED w")
            self.w_sympy = self.w_sympy
            return self.w

    def updateFunc(self, w=None, left=None, right=None, top=None, bottom=None, fine=None, Hticks=None, Vticks=None,
                   frame=None, scale=100):

        if w is None:
            w = self.w

        elif type(w) == str:
            w = self.evaluate(w)

        if left is None:
            left = self.left

        if right is None:
            right = self.right

        if top is None:
            top = self.top

        if bottom is None:
            bottom = self.bottom

        if fine is None:
            fine = self.fine

        if Hticks is None:
            Hticks = self.Hticks

        if Vticks is None:
            Vticks = self.Vticks

        if type(w) == str:
            w = self.evaluate(w)

        if frame is None:
            self.frame = frame = 1

        self.same_args_for_w = True

        if self.right != right or self.left != left or self.top != top or self.bottom != bottom or self.fine != fine or self.Hticks != Hticks or self.Vticks != Vticks:
            self.same_args_for_w = False
            self.right = right
            self.left = left
            self.top = top
            self.bottom = bottom
            self.fine = fine
            self.Hticks = Hticks
            self.Vticks = Vticks

        if self.same_args_for_w:
            self.transformed = self.anim(w=w, left=left, right=right, top=top, bottom=bottom, fine=fine, Hticks=Hticks,
                                         Vticks=Vticks, frame=frame, scale=scale)
            self.over_write_traces(self.transformed)

        else:
            self.transformed = self.anim(w=w, left=left, right=right, top=top, bottom=bottom, fine=fine, Hticks=Hticks,
                                         Vticks=Vticks, frame=frame, scale=scale)
            self.add_new_data_to_traces(self.transformed)

    def show(self):
        return self.fig


class Square(Rectangle):
    def __init__(self, side=1, fine=50, Hticks=10, Vticks=10, w=None):
        super().__init__(left=-side, right=side, top=side, bottom=-side, fine=fine, Hticks=Hticks, Vticks=Vticks, w=w)

    def updateFunc(self, w=None, side=None, fine=None, Hticks=None, Vticks=None, frame=None, scale=100):
        if side is None:

            super().updateFunc(left=side, right=side, top=side, bottom=side, fine=fine, Hticks=Hticks, Vticks=Vticks,
                               w=w,
                               frame=frame, scale=scale)
        else:
            super().updateFunc(left=-side, right=side, top=side, bottom=-side, fine=fine, Hticks=Hticks, Vticks=Vticks,
                               w=w,
                               frame=frame, scale=scale)


class Donut(Rectangle):
    def __init__(self, w=None, rin=1, rout=2, fine=50, cticks=5, rticks=10, x0=0, y0=0):

        self.rin = rin
        self.rout = rout
        self.fine = fine
        self.cticks = cticks
        self.rticks = rticks
        self.x0 = x0
        self.y0 = y0

        self.x, self.y = sym.symbols('x y', real=True)

        if w is None:
            self.w = x + sym.I * y
        elif type(w) == str:
            self.w = self.evaluate(w)
        else:
            self.w = w

        self.w_sympy = self.w

        self.init_plotly(w=self.w, rin=self.rin, rout=self.rout, fine=self.fine, cticks=self.cticks, rticks=self.rticks,
                         x0=self.x0, y0=self.y0)

    def init_plotly(self, w, rin, rout, fine, cticks, rticks, x0, y0):
        self.transformed = self.matrix_generator(w=w, rin=rin, rout=rout, fine=fine, cticks=cticks, rticks=rticks,
                                                 x0=x0, y0=y0)

        self.traces = self.create_traces(self.transformed)

        self.fig = go.FigureWidget(data=self.traces)

        self.fig = self.fig.update_layout(
            template='plotly_dark',
            yaxis=dict(scaleanchor="x", scaleratio=1),
            autosize=False,
            width=900,
            height=500,
            showlegend=False,
            dragmode='pan')

    def matrix_generator(self, w, rin, rout, fine, cticks, rticks, x0, y0):
        self.X, self.Y = self.gen_coordinate_grid(rin=rin, rout=rout, fine=fine, cticks=cticks, rticks=rticks, x0=x0,
                                                  y0=y0)

        self.w = self.w_numeric(w)

        return self.plugin(w=self.w, X=self.X, Y=self.Y)

    def gen_coordinate_grid(self, rin=None, rout=None, fine=None, cticks=None, rticks=None, x0=None, y0=None):
        if rin is None:
            rin = self.rin
        else:
            self.rin = rin

        if rout is None:
            rout = self.rout
        else:
            self.rout = rout

        if fine is None:
            fine = self.fine
        else:
            self.fine = fine

        if cticks is None:
            cticks = self.cticks
        else:
            self.cticks = cticks

        if rticks is None:
            rticks = self.rticks
        else:
            self.rticks = rticks

        if x0 is None:
            x0 = self.x0
        else:
            self.x0 = x0

        if y0 is None:
            y0 = self.y0
        else:
            self.y0 = y0

        t = np.linspace(0, 2 * np.pi, fine, dtype=complex)
        r = np.linspace(rin, rout, cticks, dtype=complex)

        # circular X and Y coordinates
        Cx = [x0 + tmp * np.cos(t) for tmp in r]
        Cy = [y0 + tmp * np.sin(t) for tmp in r]

        # Radial lines from smaller circle to larger circle

        t = np.linspace(0, 2 * np.pi, rticks, dtype=complex, endpoint=False)

        cinx = x0 + rin * np.cos(t)
        ciny = y0 + rin * np.sin(t)

        coutx = x0 + rout * np.cos(t)
        couty = y0 + rout * np.sin(t)

        Rx = [np.linspace(tmp1, tmp2, fine, dtype=complex) for tmp1, tmp2 in zip(cinx, coutx)]
        Ry = [np.linspace(tmp1, tmp2, fine, dtype=complex) for tmp1, tmp2 in zip(ciny, couty)]

        X = []
        Y = []

        X.extend(Cx)
        X.extend(Rx)

        Y.extend(Cy)
        Y.extend(Ry)

        return X, Y

    def plugin(self, w, X, Y):
        matrix = X.copy()  # same shape as X or Y
        for j in range(len(X)):
            for k in range(len(X[j])):
                matrix[j][k] = w(X[j][k], Y[j][k])

            matrix[j] = np.array(matrix[j])

        return matrix

    def create_traces(self, transformed_mat):

        traces = []
        for count, arr in enumerate(transformed_mat):
            if count == 0:
                color = 'magenta'
            elif 0 < count < self.cticks - 1:
                color = 'green'
            elif count == self.cticks - 1:
                color = 'blue'
            elif count > self.cticks - 1:
                color = 'grey'

            traces.append(go.Scatter(x=arr.real,
                                     y=arr.imag,
                                     line_color=color,
                                     hoverinfo='none',
                                     line=dict(shape='spline'),
                                     mode='lines'))

        return traces

    def anim(self, w, rin, rout, cticks, rticks, x0, y0, fine, frame, scale=100):
        return self.matrix_generator(w=(w - (x + I * y)) * (frame / scale) + z, x0=x0, y0=y0, rin=rin, rout=rout,
                                     fine=fine,
                                     cticks=cticks, rticks=rticks)
        # return self.matrix_generator(w=(w - z) * (frame / scale) + z, x0=x0, y0=y0, rin=rin, rout=rout, fine=fine,
        #                              cticks=cticks, rticks=rticks)

    def updateFunc(self, w=None, rin=None, rout=None, fine=None, cticks=None, rticks=None, x0=None, y0=None, frame=None,
                   scale=100):
        if rin is None:
            rin = self.rin

        if rout is None:
            rout = self.rout

        if fine is None:
            fine = self.fine

        if cticks is None:
            cticks = self.cticks

        if rticks is None:
            rticks = self.rticks

        if x0 is None:
            x0 = self.x0

        if y0 is None:
            y0 = self.y0

        if w is None:
            w = self.w

        elif type(w) == str:
            w = self.evaluate(w)

        if frame is None:
            self.frame = frame = 1

        self.same_args_for_w = True

        if self.x0 != x0 or self.y0 != y0 or self.rticks != rticks or self.cticks != cticks or self.rin != rin or self.rout != rout or self.fine != fine:
            self.same_args_for_w = False
            self.rin = rin
            self.rout = rout
            self.fine = fine
            self.cticks = cticks
            self.rticks = rticks
            self.x0 = x0
            self.y0 = y0

        if self.same_args_for_w:
            self.transformed = self.anim(w=w, rin=rin, rout=rout, cticks=cticks, rticks=rticks, x0=x0, y0=y0,
                                         fine=fine, frame=frame)
            self.over_write_traces(self.transformed)

        else:
            self.transformed = self.anim(w=w, rin=rin, rout=rout, cticks=cticks, rticks=rticks, x0=x0, y0=y0,
                                         fine=fine, frame=frame)
            self.add_new_data_to_traces(self.transformed)


class Circle(Donut):

    def __init__(self, w=None, r=1, fine=50, cticks=5, rticks=10, x0=0, y0=0):
        super().__init__(w=w, rin=0, rout=r, fine=fine, cticks=cticks + 1, rticks=rticks, x0=x0, y0=y0)

    def updateFunc(self, w=None, r=None, fine=None, cticks=None, rticks=None, x0=None, y0=None, frame=None, scale=100):
        if cticks is None:
            super().updateFunc(w=w, rin=0., rout=r, fine=fine, cticks=cticks, rticks=rticks, x0=x0, y0=y0, frame=frame,
                               scale=scale)
        else:
            super().updateFunc(w=w, rin=0., rout=r, fine=fine, cticks=cticks + 1, rticks=rticks, x0=x0, y0=y0,
                               frame=frame, scale=scale)


class Single_circle(Circle):
    def __init__(self, w=None, r=1, fine=50, rticks=0, x0=0, y0=0):
        super().__init__(w=w, r=r, fine=fine, cticks=1, rticks=rticks, x0=x0, y0=y0)

    def updateFunc(self, w=None, r=None, rticks=None, x0=None, y0=None, frame=None):
        super().updateFunc(w=w, r=r, rticks=rticks, x0=x0, y0=y0, frame=frame, scale=100)
