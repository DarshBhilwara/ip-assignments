def main(a):
    assert 0 <= a <= 99, 'Number should be between 0 and 99'
    b = a % 10
    c = a//10
    if c == 0 and b == 0:
        return 'zero', ''
    elif c == 1:
        if b == 0:
            return 'ten', ''
        elif b == 1:
            return 'eleven', ''
        elif b == 2:
            return 'twelve', ''
        elif b == 3:
            return 'thirteen', ''
        elif b == 4:
            return 'fourteen', ''
        elif b == 5:
            return 'fifteen', ''
        elif b == 6:
            return 'sixteen', ''
        elif b == 7:
            return 'seventeen', ''
        elif b == 8:
            return 'eighteen', ''
        elif b == 9:
            return 'nineteen', ''
    else:
        if c == 2:
            return 'twenty', ones(a)
        elif c == 3:
            return 'thirty', ones(a)
        elif c == 4:
            return 'forty', ones(a)
        elif c == 5:
            return 'fifty', ones(a)
        elif c == 6:
            return 'sixty', ones(a)
        elif c == 7:
            return 'seventy', ones(a)
        elif c == 8:
            return 'eighty', ones(a)
        elif c == 9:
            return 'ninety', ones(a)
        elif c == 0:
            return ones(a), ''


def ones(a):
    b = a % 10
    if b == 0:
        return ''
    if b == 1:
        return 'one'
    elif b == 2:
        return 'two'
    elif b == 3:
        return 'three'
    elif b == 4:
        return 'four'
    elif b == 5:
        return 'five'
    elif b == 6:
        return 'six'
    elif b == 7:
        return 'seven'
    elif b == 8:
        return 'eight'
    elif b == 9:
        return 'nine'


def _test():
    assert main(15) == ('fifteen', '')
    assert main(0) == ('zero', '')
    assert main(65) == ('sixty', 'five')


_test()

a = int(input('Please enter number : '))
print(main(a)[0], main(a)[1])
