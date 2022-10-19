import matplotlib
import matplotlib.pyplot as plt
import numpy as np
from matplotlib.gridspec import GridSpec
from matplotlib.ticker import IndexLocator
import utils


def main():
    matplotlib.use('TkAgg')
    fig = plt.figure(figsize=(15, 15))
    fig.set_facecolor('#eee')
    gs = GridSpec(nrows=1, ncols=2, figure=fig)

    first = plt.subplot(gs[0, 0])
    first.grid()
    first.xaxis.set_major_locator(IndexLocator(base=50, offset=0))
    first.yaxis.set_major_locator(IndexLocator(base=0.05, offset=0))

    second = plt.subplot(gs[0, 1])
    second.grid()
    second.xaxis.set_major_locator(IndexLocator(base=50, offset=0))
    second.yaxis.set_major_locator(IndexLocator(base=0.05, offset=0))
    N = 512
    fi = np.pi / 32

    f_1 = lambda x: np.sin(2 * np.pi * x / N)
    f_2 = lambda x: np.sin(2 * np.pi * x / N + fi)

    utils.draw(f_1, first)
    utils.draw(f_2, second)
    plt.show()


if __name__ == '__main__':
    main()
