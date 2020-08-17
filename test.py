import math

w = math.factorial(13)


def permutation(a, b):
    return (math.factorial(a) / math.factorial(a - b))


def combination(c, d):
    return (math.factorial(c) / math.factorial(c - d) / math.factorial(d))


pp = permutation(5, 5)
cc = combination(32, 16)

# %%

import numpy as np
import pandas as pd
import warnings
import sys
import os

warnings.filterwarnings("ignore", category=FutureWarning)

from bokeh.plotting import figure, show
from bokeh.io import output_notebook
from bokeh.layouts import row
from sklearn.datasets.samples_generator import make_blobs

# %%

X, y = make_blobs(n_samples=300, centers=4, cluster_std=0.40, random_state=0)


colormap = {0: 'red', 1: 'green', 2: 'blue', 3: 'yellow'}
colors = [colormap[i] for i in y]

plot_color = figure(plot_width=300, plot_height=300)
plot_color.scatter(X[:, 0], X[:, 1], color=colors)

plot_plain = figure(plot_width=300, plot_height=300)
plot_plain.scatter(X[:, 0], X[:, 1])

output_notebook()
show(row(plot_plain, plot_color))

# %%
print('test')