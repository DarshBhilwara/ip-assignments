def f(x):
    f = (x**3)-(10.5*(x**2))+(34.5*x)-35
    return f


def df(x):
    df = (3*(x**2)) - (21*x) + 34.5
    return df


def main(x):
    while f(x) != 0:
        if df(x) == 0:
            print('Newton Rhapson Method Fails.')
        else:
            x = x-(f(x)/df(x))
        x = round(x, 1)
    return x


def _test():
    assert main(5) == 5
    assert main(3) == 3.5


_test()
x0 = float(input("Initial Estimate : "))
print(main(x0), ' is a root.')
