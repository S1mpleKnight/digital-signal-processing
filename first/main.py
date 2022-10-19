import matplotlib
import matplotlib.pyplot as plt
from matplotlib.gridspec import GridSpec
from matplotlib.ticker import IndexLocator
import numpy as np
import utils

matplotlib.use('TkAgg')
fig = plt.figure(figsize=(15, 15))
fig.set_facecolor('#eee')
gs = GridSpec(ncols=4, nrows=3, figure=fig)

first = plt.subplot(gs[0, 0:2])
first.grid()
first.xaxis.set_major_locator(IndexLocator(base=250, offset=0))
first.yaxis.set_major_locator(IndexLocator(base=2, offset=0))

second = plt.subplot(gs[0, 2:4])
second.grid()
second.xaxis.set_major_locator(IndexLocator(base=250, offset=0))
second.yaxis.set_major_locator(IndexLocator(base=0.5, offset=0))

third = plt.subplot(gs[1, 0:2])
third.grid()
third.xaxis.set_major_locator(IndexLocator(base=250, offset=0))
third.yaxis.set_major_locator(IndexLocator(base=2, offset=0))

fourth = plt.subplot(gs[1, 2:4])
fourth.grid()
fourth.xaxis.set_major_locator(IndexLocator(base=150, offset=0))
fourth.yaxis.set_major_locator(IndexLocator(base=0.5, offset=0))

fifth = plt.subplot(gs[2, 0:4])
fifth.grid()
fifth.xaxis.set_major_locator(IndexLocator(base=100, offset=0))
fifth.yaxis.set_major_locator(IndexLocator(base=1, offset=0))

N = 2048

# First - a
A = 10
fi = [0, np.pi / 6, np.pi / 4, np.pi / 2, np.pi]
freq = 2
for phase in fi:
    utils.harmonic(A, freq, N, phase, first)

# First - b
A = 3
fi = np.pi / 2
frequencies = [5, 4, 2, 6, 3]
for freq in frequencies:
    utils.harmonic(A, freq, N, fi, second)

# First - c
amplitudes = [2, 3, 6, 5, 1]
fi = np.pi / 2
freq = 1
for A in amplitudes:
    utils.harmonic(A, freq, N, fi, third)

# Second
k = 5
A = [1, 1, 1, 1, 1]
f = [1, 2, 3, 4, 5]
fi = [0, np.pi / 4, np.pi / 6, 2 * np.pi, np.pi]
utils.polyharmonic(A, f, N, fi, k, fourth)

# Third
k = 5
A = [1, 1, 1, 1, 1]
f = [10, 20, 30, 40, 50]
fi = [0, np.pi / 4, np.pi / 6, 2 * np.pi, np.pi]
max_change = 0.2
utils.polyharmomic_linear(A, f, fi, max_change, N, k, fifth)

plt.show()
