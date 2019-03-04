def diff(fn,
         x,
         params,
         dx):
    return (fn(x + dx, params) - fn(x, params)) / dx

def logistic_map(x, _lambda):
    x_new = 1 - _lambda * x ** 2
    return x_new

def iterate(_lambda,
             fn,
             k,
             delta,
             x0):
    # iterate function for iterating 1 dimension map
    x_array = [fn(x0, _lambda)]
    for i in range(k):      #k+1, or not?
        x_array.append(fn(x_array[i],_lambda))
    if delta==0:
        return x_array
    else:
        return x_array[-delta:]