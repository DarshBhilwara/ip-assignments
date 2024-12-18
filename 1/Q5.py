def df(a, b, p):
    d = a-(b*p)
    d = 2.71828**d
    return d


def s(c, d, p):
    s = c+(d*p)
    s = 2.71828**s
    return s


def ds(a, b, c, d, p):
    while df(a, b, p) > s(c, d, p):
        p = (p*105)/100
    p = round(p, 2)
    k = df(a, b, p)
    k = round(k, 2)
    j = s(c, d, p)
    j = round(j, 2)
    return p, k, j


def _test():
    assert ds(10, 1.05, 1, 1.06, 1) == (4.32, 236.04, 264.86)
    assert ds(5, 1.01, 1, 1.02, 2) == (2.0, 19.69, 20.91)


_test()

a = float(input('a : '))
b = float(input('b : '))
c = float(input('c : '))
d = float(input('d : '))
p = float(input('Initial Price : '))


print('Equilibrium Price : ', ds(a, b, c, d, p)[0])
print('Supply at equilibrium : ', ds(a, b, c, d, p)[1])
print('Demand at equilibrium : ', ds(a, b, c, d, p)[2])
