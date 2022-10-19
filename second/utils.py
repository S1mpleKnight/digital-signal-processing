import numpy as np

delta_deviation = 0.707
delta_amplitude = 1
N = 512
K = 3 * N // 4


def get_deviation_a(f, M):
    x_sum = 0
    for i in range(M):
        x_sum += f(i) ** 2
    return np.sqrt(x_sum / (M + 1))


def get_deviation_b(f, M):
    x_sum_1 = 0
    x_sum_2 = 0
    for i in range(M):
        x_sum_1 += f(i) ** 2
        x_sum_2 += f(i)
    return np.sqrt(x_sum_1 / (M + 1) - (x_sum_2 / (M + 1)) ** 2)


def get_amplitude(f, M):
    cos_sum = 0
    sin_sum = 0
    for i in range(M):
        y = f(i)
        cos_sum += y * np.cos((2 * np.pi * i) / M)
        sin_sum += y * np.sin((2 * np.pi * i) / M)
    ampl = np.sqrt(((2 / M) * cos_sum) ** 2 + ((2 / M) * sin_sum) ** 2)
    return ampl


def draw(f, chart):
    deviation_1 = []
    deviation_2 = []
    amplitude = []
    x = range(K, 2 * N)
    for M in x:
        deviation_a = get_deviation_a(f, M)
        deviation_b = get_deviation_b(f, M)
        a = get_amplitude(f, M)
        d_1 = delta_deviation - deviation_a
        d_2 = delta_deviation - deviation_b
        d_a = delta_amplitude - a
        deviation_1.append(d_1)
        deviation_2.append(d_2)
        amplitude.append(d_a)

    chart.plot(x, deviation_1, label='deviation_1')
    chart.plot(x, deviation_2, label='deviation_2')
    chart.plot(x, amplitude, label='amplitude')
    chart.legend()
