def populationatyr(gr, yr, b, d, lst):
    a = 0
    m = 0
    for j in lst:
        j = int(j)
        cr = gr-(m*b)
        for k in range(yr):
            incdec = j * (cr / 100)
            j = j + incdec
            cr = cr - d
        a = a + j
        m = m + 1
    return a


def main(gr, b, d, lst):
    yr = 0
    while populationatyr(gr, yr+1, b, d, lst) >= populationatyr(gr, yr, b, d, lst):
        yr = yr + 1
    out = round(populationatyr(gr, yr, b, d, lst))
    return yr, out


def _test():
    main(2.4, 0.4, 0.1, [50, 1450, 1400, 1700, 1500, 600, 1200]) == (13, 8574)


_test()
lst = list(input("List of initial populations : ").split())
gr = float(input("First growth rate : "))
b = float(input("Decline rate per group : "))
d = float(input("Decline rate per year : "))


print("Years taken to reach the threshold population are",
      main(gr, b, d, lst)[0])
print("The threshold population is", main(gr, b, d, lst)[1])
