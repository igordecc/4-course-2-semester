from multiprocessing import Pool
import os, time

print("out of main", ", procc id",os.getpid())

def hello(x):
    print("inside hello()")
    print("proccess id: ", os.getpid())
    time.sleep(3)
    return x**2

if __name__ == '__main__':
    p = Pool(6)
    pool_output = p.map(hello, range(6))

    print(pool_output)