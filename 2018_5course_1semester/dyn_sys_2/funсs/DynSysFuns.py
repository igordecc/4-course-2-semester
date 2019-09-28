#exercise 1
def resslerSystem(x, y, z, h = 0.01, a = .25, b = 0.15, r = 2.5  ):     #a = 0.2, b = 0.2, r = 5.7
    new_x = - y - z
    new_y = x + a*y
    new_z = b + (x-r)*z
    return x + h*new_x, y + h*new_y, z + h*new_z

#exercise 2
def hennonMap(x, y, z, h = 0.01, a = .25, b = 0.15  ):     #a = 0.2, b = 0.2, r = 5.7
    new_x = 1 - a*x**2 + b*y
    new_y = x
    new_z = 0
    return new_x, new_y, new_z
