a = float(input("x : "))


def dydx(x, y):
    a = x+y
    return a


def main(x):
    y = 1
    h = 0.1
    b = 0
    while b < x:
        y = y+h*dydx(b, y)
        b = b+0.1
    y = round(y, 3)
    return y


def _test():
    assert main(4) == 85.519
    assert main(6) == 662.760


_test()
print(main(a))
