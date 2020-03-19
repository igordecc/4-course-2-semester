import numpy

N_POINTS = 128


def linear(n=N_POINTS):
    return numpy.linspace(1, n, n)


def linear_with_noise(n=N_POINTS, mean=0, std=1):
    base = numpy.linspace(-1, n // 10, n)
    noise = numpy.random.normal(mean, std, base.shape)
    return base + noise


def constant(n=N_POINTS):
    return numpy.ones(n)


def quadratic(n=N_POINTS):
    return [(i + 2)**2 - 3 for i in range(n)]


def white_noise(n=N_POINTS, mean=0, std=1):
    return numpy.random.normal(mean, std, size=n)


def logistic_map(n=N_POINTS, x0=0.1, r=4):
    def log_map(x, r):
        return r * x * (1 - x)

    x = [x0]
    for i in range(n):
        x.append(log_map(x[i], r))
    return x