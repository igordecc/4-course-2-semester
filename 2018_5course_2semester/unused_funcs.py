import matplotlib.pyplot

def scale(x_scale_point,
          y_scale_point,
          x_scale_coefficient,
          y_scale_coefficient,
          xmin,
          xmax,
          ymin,
          ymax
          ):
    #Universal scaling funtion

    # xmin = .5
    # xmax = 1.8
    # ymin = -1
    # ymax = 1
    # x_scale_point = 1.4
    # y_scale_point = 0
    # x_scale_coefficient = 1
    # y_scale_coefficient = 0.5
    # # scaling point
    # # x_scale_point = 1.1
    # # y_scale_point = DON'T SCALE

    # nxmin, nxmax = xmin * x_scale_coefficient, xmax * x_scale_coefficient
    # nymin, nymax = ymin * y_scale_coefficient, ymax * y_scale_coefficient

    x_proportions = x_scale_point -  xmin, xmax - x_scale_point
    n_x_proportions = [ i * x_scale_coefficient for i in x_proportions ]
    n_xmin, n_xmax = x_scale_point - n_x_proportions[0], x_scale_point + n_x_proportions[1]

    y_proportions = y_scale_point - ymin, ymax - y_scale_point
    n_y_proportions = [i * y_scale_coefficient for i in y_proportions]
    n_ymin, n_ymax = y_scale_point - n_y_proportions[0], y_scale_point + n_y_proportions[1]

    return matplotlib.pyplot.axis(n_xmin, n_xmax, n_ymin, n_ymax)

