def fac(x):
    a = 1
    for y in range(1, x+1):
        a = a*y
    return a


def sin(x):
    a = 0
    x = (x*3.14)/180
    for y in range(10):
        a = a + (((-1)**y)*(x**((2*y)+1)))/fac((2*y)+1)
    return a


def cos(x):
    a = 0
    x = (x*3.14)/180
    for y in range(10):
        a = a + ((-1)**y)*(x**(2*y))/fac(2*y)
    return a


def main(angle, dist):
    hypo = dist/cos(angle)
    length = hypo*sin(angle)
    hypo = round(hypo, 2)
    length = round(length, 2)
    return hypo, length


def _test():
    assert main(30, 40) == (46.18, 23.08)
    assert main(37, 4) == (5.01, 3.01)


_test()
a = int(input('Angle in degrees : '))
d = int(input('Horizontal distance from the person to the base of the pole : '))

print("The distance to the tip of the pole is ", main(a, d)[0])
print('The height of the pole is', main(a, d)[1])
