import numpy as np


def harmonic(A, f, N, fi, chart):
    x = np.arange(0, N + 1, 1)
    y = (A * np.sin(((2 * np.pi * f * x) / N) + fi))
    chart.plot(x, y)


def polyharmonic(A, f, N, fi, harmonics_am, chart):
    x = np.arange(0, N + 1, 1)

    def y():
        result = 0
        for i in range(harmonics_am):
            result += (A[i] * np.sin(((2 * np.pi * f[i] * x) / N) + fi[i]))
        return result

    chart.plot(x, y())


def polyharmomic_linear(A, f, fi, max_change, N, harmonics_am, chart):
    x = np.arange(0, N + 1, 1)

    def increase_linear_law(start, x):
        return max_change * start * x + start

    def y():
        result = 0
        for i in range(harmonics_am):
            result += increase_linear_law(A[i], x / N) * np.sin(((2 * np.pi * increase_linear_law(f[i], x / N) * x) / N) + increase_linear_law(fi[i], x / N))
        return result

    chart.plot(x, y())
