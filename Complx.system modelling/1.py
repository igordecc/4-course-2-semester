def defaul_equation(derivative_y, y):
    return derivative_y - y         # = 0   Ы

def basis_func(x, N_range):
    return x ** N_range

def approximate_solution(x_arg, a_vector, N_range = 2):
    summ = 0
    for i in range(N_range + 1): ## N = [0,2]
        summ += a_vector[i] * basis_func(x_arg, N_range)
    return summ


def approximate_derivative_solution(x_arg, a_vector, N_range = 2):
    summ = 0
    for i in range(N_range + 1): ###########!!!!+-!!!!!!!!!!!!!!!!!!!
        summ += a_vector[i] * N_range * basis_func(x_arg, N_range-1)
    return summ

def find_Nevyazka(x_arg, a_vector, N_range = 2):
   x,y = 0,0
   return x,y
"""
method gausa
method progonki
method kramera
"""
#x,y = find_Nevyazka(x,a,n)

#x_array = [for i in range()]
