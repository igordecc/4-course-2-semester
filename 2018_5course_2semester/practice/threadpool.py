from multiprocessing.pool import ThreadPool
import os, time
print("hi outside of main()", os.getpid())

def hello(x):
    print("inside hello()")
    print("proccess id: ", os.getpid())
    time.sleep(3)
    return x**2

if __name__ == '__main__':
    p = ThreadPool(6)
    pool_output = p.map(hello, range(6))

    print(pool_output)