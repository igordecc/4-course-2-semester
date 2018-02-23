import matplotlib.pyplot as pp

def f(x, y, lambd):
        return (lambd - x**x)*y - x

def g(x, y, lambd):
        return y

def method_euler(x0, y0, f, h, lambd):
        return y0 + h*f(x0,y0,lambd)


def calc_phase_point(x0,y0,lambd,h,N):
        xarr = [x0]
        yarr = [y0]
        for i in range(N):
                y0 = method_euler(x0, y0, f, h, lambd)
                x0 = x0 + h * g(x0, y0, lambd)
                #print(x0, y0)
                if (type(y0) is complex)or(type(x0) is complex)or(abs(y0) > 10) or (abs(x0) > 10):
                        break
                yarr.append(y0)
                xarr.append(x0)
        pp.plot(xarr, yarr)
        return None



if __name__ == '__main__':
        lambd = 1
        h = 0.01        #length of 1 step
        N = 1000        #numberof steps
        for x0 in range(-5,6):
                for y0 in range(-5,6):
                        calc_phase_point(x0, y0, lambd, h, N)
        pp.show()
        #myfile = open('D:/text.txt', 'w')
        #myfile.write(str(x0) + ' ' + str(y0) + '\n') ################realize file write
        #myfile.close()
