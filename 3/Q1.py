a = int(input())


def up(a, b=0):
    if a == 1:
        return
    print(a*'* ', end='')
    print(4*(b)*' ', end='')
    print(a*'* ')
    up(a-1, b+1)


def down(a, b=1):
    if a == 0:
        return
    print(b*'* ', end='')
    print(4*(a-1)*' ', end='')
    print(b*'* ')
    down(a-1, b+1)


def _test():
    assert a > 0, 'input could only be a positive integer'
    assert up(1, 0) == None


_test()
up(a, 0)
print(end='')
down(a, 1)
