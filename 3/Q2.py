def record(file):
    f = open(file, 'r')
    a = f.readlines()
    f.close()
    a = [x[:-1] for x in a]
    a.pop(0)
    a = [x.split(', ') for x in a]
    dct = {}
    for x in a:
        if x[0] in dct:
            dct[x[0]]['type'].append(x[1])
            dct[x[0]]['gate'].append(x[2])
            dct[x[0]]['time'].append(x[3])
            dct[x[0]]['timeint'].append(tint(x[3]))
        else:
            dct[x[0]] = {'type': [x[1]], 'gate': [x[2]],
                         'time': [x[3]], 'timeint': [tint(x[3])]}
            if x[1] == 'ENTER':
                dct[x[0]]['present'] = ''
            else:
                dct[x[0]]['present'] = ' not'

    return dct


def tint(time):
    try:
        hour, min, sec = map(int, time.split(':'))
        ret = hour*3600 + min*60 + sec
        return ret
    except:
        return 0


def show(dct, name, time):
    if name in dct:
        now = dct[name]['present']
        a = ''
        for x in range(len(dct[name]['type'])):
            a += f"{name},{dct[name]['type'][x]},{dct[name]
                                                  ['gate'][x]}, {dct[name]['time'][x]}\n"
        b = f'Student is currently{now} in the campus.'
        a = a+b
        f = open('out2_1.txt', 'w')
        f.write(a)
        f.close()
        return 'Output written in file "out2_1.txt"'
    else:
        return 'Student not in record'


def number(dct, start, end):
    ent = []
    ext = []
    start = tint(start)
    end = tint(end)
    for x in dct:
        for y in range(len(dct[x]['timeint'])):
            if start <= dct[x]['timeint'][y] <= end:
                if dct[x]['type'][y] == 'ENTER':
                    ent.append(f"{x}, {dct[x]['gate'][y]}, {
                               dct[x]['time'][y]}")
                elif dct[x]['type'][y] == 'EXIT':
                    ext.append(f"{x}, {dct[x]['gate'][y]}, {
                               dct[x]['time'][y]}")
    a = '\n\nThe students who entered are : \n\n'
    a += '\n'.join(ent)
    a += '\n\nThe students who have exited are : \n\n'
    a += '\n'.join(ext)
    f = open('out2_2.txt', 'w')
    f.write(a)
    f.close()
    return "Output written to file 'out2_2.txt'"


def agate(dct, gateno):
    ent = 0
    ext = 0
    for x in dct:
        for y in range(len(dct[x]['gate'])):
            if dct[x]['gate'][y] == gateno:
                if dct[x]['type'][y] == 'ENTER':
                    ent += 1
                elif dct[x]['type'][y] == 'EXIT':
                    ext += 1
    return f'{ent} students have entered and {ext} students have left the campus from gate {gateno}'


def _test():
    assert tint('00:00:00') == 0
    assert tint('01:00:00') == 3600


_test()

file = 'sorted_data.txt'
dct = record(file)


def main():
    while True:
        print()
        print('1. Show record of a student.')
        print('2. Determine all students who entered or left campus in interval.')
        print('3. Find number of times students have entered or left from the gate.')
        print()
        a = input('Your Choice : ')
        if a == '1':
            name = input('Student Name : ')
            time = input('Current time : ')
            print(show(dct, name, time))
        elif a == '2':
            start = input('Starting Interval : ')
            end = input('Ending Interval : ')
            print(number(dct, start, end))
        elif a == '3':
            gateno = input('Gate Number : ')
            print(agate(dct, gateno))
        elif a == '':
            break
        else:
            print('Wrong Input')


main()
