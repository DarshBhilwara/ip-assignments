import math
a = int(input('Enter Starting Time : '))
b = int(input('Enter Ending Time : '))


def v(t):
    v = (2000*(math.log((140000)/(140000-(2100*t)))))-(9.8*t)
    return v


def f2(t1, t2):
    s = 0
    for t in range(int(4*(t1)), int(4*(t2))):
        t = t/4
        v1 = v(t)
        v2 = v(t+0.25)
        s = s + (v2+v1)*0.125
    s = round(s, 2)
    return s


def _test():
    assert a < b, 'Ending time should not be less than starting time'
    assert f2(24, 25) == 676.10
    assert f2(5, 8) == 425.05


_test()
print(f2(a, b))
