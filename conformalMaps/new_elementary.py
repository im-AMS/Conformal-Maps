import numpy as np
import plotly.graph_objs as go
import sympy as sym

x, y = sym.symbols('x y', real=True)

z = x + sym.I * y


class Rectangle:
    def __init__(self, left=-1, right=1, top=1, bottom=-1, fine=50, Hticks=5, Vticks=5, w=None):

        self.left = left
        self.right = right
        self.top = top
        self.bottom = bottom
        self.fine = fine
        self.Hticks = Hticks
        self.Vticks = Vticks

        self.x, self.y = sym.symbols('x y', real=True)

        if w is None:
            self.w = x + sym.I * y
        elif type(w) == str:
            self.w = eval(w)
        else:
            self.w = w

        self.init_plotly(self.left, self.right, self.top, self.bottom, self.fine, self.Hticks, self.Vticks, self.w)

    def init_plotly(self, left, right, top, bottom, fine, Hticks, Vticks, w):

        self.transformed = self.matrix_generator(w=w, left=left, right=right, top=top, bottom=bottom, fine = fine, Hticks=Hticks, Vticks=Vticks)

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

    def matrix_generator(self,left, right, top, bottom, fine, Hticks, Vticks, w):

        self.X , self.Y = self.gen_coordinate_grid(left, right, top, bottom, fine, Hticks, Vticks)

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
        traces = [go.Scatter(x=arr.real,
                             y=arr.imag,
                             line_color='red',
                             hoverinfo='none',
                             line=dict(shape='spline'),
                             mode='lines') for arr in transformed_mat]

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


    def updateFunc(self, w=None, left=None, right=None, top=None, bottom=None, fine=None, Hticks=None, Vticks=None):


        if w is None:
            w = self.w

        elif type(w) == str:
            w = eval(w)

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
            w = eval(w)

        same_args_for_w = True

        if self.right != right or self.left != left or self.top != top or self.bottom != bottom or self.fine != fine or self.Hticks != Hticks or self.Vticks!= Vticks:
            same_args_for_w = False

        if same_args_for_w:
            self.transformed = self.matrix_generator(w=w, left=left, right=right, top=top, bottom=bottom, fine=fine,
                                                     Hticks=Hticks, Vticks=Vticks)
            self.over_write_traces(self.transformed)

        else:
            self.transformed = self.matrix_generator(w=w, left=left, right=right, top=top, bottom=bottom, fine=fine,
                                                     Hticks=Hticks, Vticks=Vticks)
            self.add_new_data_to_traces(self.transformed)


    def show(self):
        return self.fig