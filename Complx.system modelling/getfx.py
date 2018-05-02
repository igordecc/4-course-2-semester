def defaul_equation(derivative_y, y):
    return derivative_y - y         # = 0   Ы

def basis_func(x, N_range):
    return x ** N_range

def approximate_solution(x_arg, N_range = 2):
    summ = 0
    for i in range(N_range + 1):
        summ += basis_func(x_arg, N_range)
    return summ


def approximate_derivative_solution(x_arg, N_range = 2):
    summ = 0
    for i in range(N_range + 1):
        summ += N_range * basis_func(x_arg, N_range-1)
    return summ

def get_R(x_arg, N_range = 2):
   R = defaul_equation(approximate_derivative_solution(x_arg, N_range), approximate_solution(x_arg, N_range))
   return R

