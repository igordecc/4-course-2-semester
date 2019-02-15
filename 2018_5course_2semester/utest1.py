import task1

def test_iterate():
    lmapfn = task1.logistic_map
    times = 100
    delta = 20
    x0 = 0.1
    _lambda = 2
    array = task1.iterate(_lambda, lmapfn, times, delta, x0)
    assert len(array) == delta


if __name__ == '__main__':
    test_iterate()
    print("All is good!")