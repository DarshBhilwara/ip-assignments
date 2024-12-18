import random
n = int(input('Final x : '))
m = int(input('Final y : '))


def rw(n, m):
    step = 0
    x = 0
    y = 0
    while True:
        d = random.random()
        if d < 0.5:
            if x < n:
                x = x+random.randint(0, 5)
            else:
                y = y+random.randint(0, 5)
        else:
            if y < m:
                y = y+random.randint(0, 5)
            else:
                x = x+random.randint(0, 5)
        step = step + 1
        if x > n and y > m:
            break
    return step


def av():
    a = 0
    b = 1
    steps = 0
    while True:
        a = a+1
        steps = steps + rw(n, m)
        c = b
        b = steps/a
        if abs(b-c)/c < 0.1:
            return b


print('The average steps are', av())
