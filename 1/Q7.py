def gcd(x, y):
    if x > y:
        for i in range(1, y+1):
            if x % i == 0:
                if y % i == 0:
                    a = i
    else:
        for i in range(1, x+1):
            if x % i == 0:
                if y % i == 0:
                    a = i
    return a


def pnt(n):
    v = 0
    for a in range(1, n+1):
        for b in range(1, n+1):
            if gcd(a, b) == 1:
                v = v+1
    return v


def dnsty(n):
    a = pnt(n)/(n*n)
    return a


def main(p):
    a = 6/(3.14**2)
    n = 1
    while abs(dnsty(n)-a)/a > (p/100):
        n = n+1
    return n


def _test():
    assert main(20) == 4
    assert main(25) == 2


_test()
p = int(input('Percentage : '))
print(main(p))
