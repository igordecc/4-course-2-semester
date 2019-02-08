def logistic_map(x, _lambda):
    x_new = x - _lambda * x ** 2
    return x_new

#TODO
#create logistic_map() function - CHECK
#plot bifurcation tree - NOT
#reveiw point's vicinity (x_0 = 0, _lambda = l_critical) - NOT
#NOTE l_critical can be the point of the first biffurcation

#plot bifurcation tree:
# - iterate for sertain _lambda
# - find stationar dots
# - mark on the plot
# -  - will use matplotlib library
# - repeat for all others _lambdas in interval [0;5]
