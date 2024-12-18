cx = float(input("Scaling parameter for x : "))
cy = float(input("Scaling parameter for y : "))
lst = eval(input('List with tuples : '))


def main(cx, cy, lst):
    matrix1 = [[x, y, 1] for x, y in lst]
    matrix2 = [[cx, 0, 0], [0, cy, 0], [1, 1, 1]]
    b = []
    for x in matrix1:
        a = [
            x[0]*matrix2[0][0]+x[1]*matrix2[0][1]+x[2]*matrix2[0][2],
            x[0]*matrix2[1][0]+x[1]*matrix2[1][1]+x[2]*matrix2[1][2],
            x[0]*matrix2[2][0]+x[1]*matrix2[2][1]+x[2]*matrix2[2][2],
        ]
        b.append(a)
    sol = [(k[0], k[1]) for k in b]
    return sol


def _test():
    assert main(1, 1, [(5, 4), (2, 4)]) == [(5.0, 4.0), (2.0, 4.0)]
    assert main(2, 4, [(1, 1)]) == [(2.0, 4.0)]


_test()
print(main(cx, cy, lst))
