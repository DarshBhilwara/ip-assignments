def create(courses, cname, credit, assessments, policy):
    if cname in courses:
        print('This course already exists.')
    else:
        courses[cname] = {'credits': credit,
                          'assessments': assessments, 'policy': policy}
    return courses


def upload(courses):
    a = open('marks.txt', 'r')
    marks = {}
    b = a.readlines()
    d = [c[:-1] for c in b]
    for x in d:
        x = x.split(',')
        x = [float(y.strip()) for y in x]
        marks[str(int(x[0]))] = x[1:]
    courses['IP']['marks'] = marks
    return courses


def real(courses, policy):
    marks = courses['IP']['marks']
    k = [sum(y) for x, y in marks.items()]
    realpolicy = []
    for x in policy:
        a = []
        less = x-2
        more = x+2
        for y in k:
            if less <= y <= more:
                a.append(y)
        a.sort(reverse=True)
        if len(a) > 1:
            realless = a[0]
            realmore = a[1]
            for y in range(1, len(a)):
                if abs(a[y]-a[y-1]) > abs(realmore-realless):
                    realless = min(a[y], a[y-1])
                    realmore = max(a[y], a[y-1])
            realcutoff = (realmore+realless)/2
            realpolicy.append(realcutoff)
            realpolicy.sort(reverse=True)
        elif len(a) == 1:
            realpolicy.append(a[0])
        else:
            realpolicy.append(x)

    policy = {'A': realpolicy[0], 'B': realpolicy[1],
              'C': realpolicy[2], 'D': realpolicy[3], 'F': 0}
    return policy


def main(courses):
    while True:
        print()
        print('1. Generate a summary ')
        print('2. Print Grades of all the students')
        print('3. Grade of a student')
        print()
        w = input('Your Choice : ')
        print()
        if w == '1':
            print('Subject : ', cname)
            print('Credits : ', credit)
            print('Assessments and their weightage : ')
            for x, y in courses['IP']['assessments'].items():
                print('\t', x, ':', y)
            print('Cutoff Policy : ')
            for x, y in courses['IP']['policy'].items():
                print('\t', x, ':', y)
            print('Grading Summary : ')
            k = []
            for x, y in courses['IP']['marks'].items():
                a = 0
                for i in y:
                    a += i
                k.append(a)
            summary = {'A': 0, 'B': 0, 'C': 0, 'D': 0, 'F': 0}
            for y in k:
                if y >= courses['IP']['policy']['A']:
                    summary['A'] += 1
                elif y >= courses['IP']['policy']['B']:
                    summary['B'] += 1
                elif y >= courses['IP']['policy']['C']:
                    summary['C'] += 1
                elif y >= courses['IP']['policy']['D']:
                    summary['D'] += 1
                elif y >= courses['IP']['policy']['F']:
                    summary['F'] += 1
            for x, y in summary.items():
                print('\t', x, ':', y)

        elif w == '2':
            print()
            k = []
            result = ''
            for i, j in courses['IP']['marks'].items():
                marks = 0
                for m in j:
                    marks += m
                k.append(marks)
            result += 'Roll No. \t Total Marks \t Grade \n'
            a = 0
            for x, y in courses['IP']['marks'].items():
                if k[a] >= courses['IP']['policy']['A']:
                    gr = 'A'
                elif k[a] >= courses['IP']['policy']['B']:
                    gr = 'B'
                elif k[a] >= courses['IP']['policy']['C']:
                    gr = 'C'
                elif k[a] >= courses['IP']['policy']['D']:
                    gr = 'D'
                elif k[a] >= courses['IP']['policy']['F']:
                    gr = 'F'
                result += f'{x} \t {k[a]} \t\t {gr} \n'
                a += 1
            print(result)
            f = open('out.txt', 'w')
            f.write(result)
            f.close()
            print()
            print("Written to file 'out.txt'")
            print()
        elif w == '3':
            print()
            roll = input('Roll Number : ')
            if roll in courses['IP']['marks']:
                print('Labs : \t\t', courses['IP']['marks'][roll][0])
                print('Midsem : \t', courses['IP']['marks'][roll][1])
                print('Assignments : \t', courses['IP']['marks'][roll][2])
                print('Endsem : \t', courses['IP']['marks'][roll][3])
                total = courses['IP']['marks'][roll][0]+courses['IP']['marks'][roll][1] + \
                    courses['IP']['marks'][roll][2] + \
                    courses['IP']['marks'][roll][3]
                print('Total Marks : \t', total)
                if total >= courses['IP']['policy']['A']:
                    gr = 'A'
                elif total >= courses['IP']['policy']['B']:
                    gr = 'B'
                elif total >= courses['IP']['policy']['C']:
                    gr = 'C'
                elif total >= courses['IP']['policy']['D']:
                    gr = 'D'
                elif total >= courses['IP']['policy']['F']:
                    gr = 'F'
                print('Grade : \t ', gr)
            else:
                print()
                print('Student not found.')
            print()
        elif w == '':
            break
        else:
            print('Wrong Input')
            print()


def _test():
    courses = {}
    cname = 'IP'
    credit = 4
    assessments = {'labs': 30, 'midsem': 15, 'assignments': 30, 'endsem': 25}
    policy = [80, 65, 50, 40]
    courses = create(courses, cname, credit, assessments, policy)
    assert 'IP' in courses
    assert courses['IP']['credits'] == 4


_test()

cname = 'IP'
credit = 4
assessments = dict([('labs', 30), ('midsem', 15),
                   ('assignmments', 30), ('endsem', 25)])
policy = [80, 65, 50, 40]
courses = {}
courses = create(courses, cname, credit, assessments, policy)
courses = upload(courses)
courses['IP']['policy'] = real(courses, policy)
main(courses)
