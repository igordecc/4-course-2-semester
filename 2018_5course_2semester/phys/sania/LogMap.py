ITER = 1024


def log_map(x, r):
    return r * x * (1 - x)


def do_map(
        itter_n=ITER,
        x_array=[0.1],
        r=4):
    for i in range(itter_n):
        x_array.append(log_map(x_array[i], r))
    return x_array
