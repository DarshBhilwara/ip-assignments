def monthdays(mon, yr):
    if mon == "January":
        monnum = 13
        days = 31
        yr = yr-1
    elif mon == "February":
        monnum = 14
        if yr % 4 == 0:
            days = 29
        else:
            days = 28
        yr = yr-1
    elif mon == "March":
        monnum = 3
        days = 31
    elif mon == "April":
        monnum = 4
        days = 30
    elif mon == "May":
        monnum = 5
        days = 31
    elif mon == "June":
        monnum = 6
        days = 30
    elif mon == "July":
        monnum = 7
        days = 31
    elif mon == "August":
        monnum = 8
        days = 31
    elif mon == "September":
        monnum = 9
        days = 30
    elif mon == "October":
        monnum = 10
        days = 31
    elif mon == "November":
        monnum = 11
        days = 30
    elif mon == "December":
        monnum = 12
        days = 31
    else:
        print("Wrong Input.")

    return monnum, yr, days


def monname(monnum):
    if monnum == 13:
        return "January"
    elif monnum == 14:
        return "February"
    elif monnum == 3:
        return "March"
    elif monnum == 4:
        return "April"
    elif monnum == 5:
        return "May"
    elif monnum == 6:
        return "June"
    elif monnum == 7:
        return "July"
    elif monnum == 8:
        return "August"
    elif monnum == 9:
        return "September"
    elif monnum == 10:
        return "October"
    elif monnum == 11:
        return "November"
    elif monnum == 12:
        return "December"
    else:
        return "Wrong"


def dow(mon, yr):
    monnum = monthdays(mon, yr)[0]
    yr = monthdays(mon, yr)[1]
    q = 1
    k = yr % 100
    j = yr // 100
    h = (q + (13 * (monnum + 1) // 5) + k + (k // 4) + (j // 4) + (5 * j)) % 7
    return h


def pr(mon, yr):
    days = monthdays(mon, yr)[2]
    yr = monthdays(mon, yr)[1]
    print("Mon Tue Wed Thu Fri Sat Sun")
    one = dow(mon, yr)

    print('    ' * one, end='')

    for c in range(1, days + 1):
        if c < 10:
            print(' ', c, end=' ')
        elif c == 10:
            print('', c, end=' ')
        else:
            print('', c, end=' ')

        if (c + one) % 7 == 0:
            print()


def main(mon, yr):
    pr(mon, yr)
    while True:
        print()
        monnum = monthdays(mon, yr)[0]
        yr = monthdays(mon, yr)[1]
        b = input("next/previous/exit : ")
        if b == 'next':
            if monnum == 14:
                monnum = 3
            elif monnum == 13:
                monnum = 14
                yr = yr + 1
            elif monnum == 12:
                monnum = 13
                yr = yr + 1
            else:
                monnum = monnum + 1
            mon = monname(monnum)
            pr(mon, yr)
        elif b == 'previous':
            if monnum == 3:
                monnum = 14
            elif monnum == 14:
                yr = yr - 1
                monnum = 13
            elif monnum == 13:
                monnum = 12
                yr = yr - 1
            else:
                monnum = monnum - 1

            mon = monname(monnum)
            pr(mon, yr)
        elif b == 'exit':
            break
        else:
            print('wrong input')


mon = input('Month : ')
yr = int(input('Year : '))
adbc = input('AD/BC (default AD) : ')
if adbc.lower() == 'bc':
    yr = ((-1)*yr)+1
main(mon, yr)
