class Course:
    def __init__(self, cname, credit, assessments, policy):
        self.cname = cname
        self.credit = credit
        self.assessments = assessments
        self.policy = policy
        self.students = {}

    def new(self, roll, marks):
        if roll not in self.students:
            self.students[roll] = Student(roll, marks)

    def real_policy(self):
        k = [sum(y.marks) for x, y in self.students.items()]
        realpolicy = []
        for x in self.policy:
            a = []
            x = float(x)
            less = x-2
            more = x+2
            a = [y for y in k if less <= y <= more]
            a.sort(reverse=True)
            if len(a) > 1:
                realless = a[0]
                realmore = a[1]
                for y in range(1, len(a)):
                    if abs(a[y] - a[y-1]) > abs(realmore - realless):
                        realless = min(a[y], a[y-1])
                        realmore = max(a[y], a[y-1])
                realcutoff = (realmore + realless) / 2
                realpolicy.append(realcutoff)
            elif len(a) == 1:
                realpolicy.append(a[0])
            else:
                realpolicy.append(x)

        self.policy = {'A': realpolicy[0], 'B': realpolicy[1],
                       'C': realpolicy[2], 'D': realpolicy[3], 'F': 0}

    def generate_summary(self):
        summary = {'A': 0, 'B': 0, 'C': 0, 'D': 0, 'F': 0}
        for student in self.students.values():
            total_marks = student.total_marks()
            gr = student.grade(self.policy)
            summary[gr] += 1
        return summary

    def print_grades(self):
        result = 'Roll No. \t Total Marks \t Grade\n'
        for student in self.students.values():
            total = student.total_marks()
            grade = student.grade(self.policy)
            result += f'{student.roll_no} \t {round(total, 2)} \t\t {grade}\n'
        return result


class Student:
    def __init__(self, roll_no, marks):
        self.roll_no = roll_no
        self.marks = marks

    def total_marks(self):
        return sum(self.marks)

    def grade(self, policy):
        total = self.total_marks()
        if total >= policy['A']:
            return 'A'
        elif total >= policy['B']:
            return 'B'
        elif total >= policy['C']:
            return 'C'
        elif total >= policy['D']:
            return 'D'
        elif total >= policy['F']:
            return 'F'


def create(courses, cname, credit, assessments, policy):
    if cname in courses:
        print('This course already exists.')
    else:
        courses[cname] = Course(cname, credit, assessments, policy)
    return courses


def upload(courses):
    a = open('marks.txt', 'r')
    b = a.readlines()
    d = [c[:-1] for c in b]
    for x in d:
        x = x.split(',')
        x = [float(y.strip()) for y in x]
        roll_no = str(int(x[0]))
        marks = x[1:]
        courses['IP'].new(roll_no, marks)
    return courses


def main(courses):
    while True:
        print()
        print('1. Generate a summary ')
        print('2. Print Grades of all the students')
        print('3. Grade of a student')
        print()
        w = input('Your Choice: ')
        print()
        if w == '1':
            print('Subject: ', courses['IP'].cname)
            print('Credits: ', courses['IP'].credit)
            print('Assessments and their weightage: ')
            for x, y in courses['IP'].assessments.items():
                print('\t', x, ':', y)
            print('Cutoff Policy: ')
            for x, y in courses['IP'].policy.items():
                print('\t', x, ':', y)
            print('Grading Summary: ')
            summary = courses['IP'].generate_summary()
            for a, b in summary.items():
                print('\t', a, ':', b)

        elif w == '2':
            print(courses['IP'].print_grades())
            f = open('out.txt', 'w')
            f.write(courses['IP'].print_grades())
            f.close()
            print()
            print("Written to file 'out.txt'")
            print()

        elif w == '3':
            roll = input('Roll Number: ')
            student = courses['IP'].students.get(roll)
            if student:
                print('Labs: \t\t', student.marks[0])
                print('Midsem: \t', student.marks[1])
                print('Assignments: \t', student.marks[2])
                print('Endsem: \t', student.marks[3])
                total = student.total_marks()
                print('Total Marks: \t', total)
                print('Grade: \t ', student.grade(courses['IP'].policy))
            else:
                print('Student not found.')
            print()

        elif w == '':
            break
        else:
            print('Wrong Input')
            print()


def _test():
    credit = 4
    assessments = dict([('labs', 30), ('midsem', 15),
                       ('assignments', 30), ('endsem', 25)])
    policy = [80, 65, 50, 40]
    courses = {}
    courses = create(courses, 'IP', credit, assessments, policy)
    student_data = [('1', [30, 15, 25, 20]), ('2', [30, 15, 30, 25]), ('3', [
        15, 10, 15, 10]), ('4', [5, 7, 10, 12])]
    for roll_no, marks in student_data:
        courses['IP'].new(roll_no, marks)
    courses['IP'].real_policy()
    summary = courses['IP'].generate_summary()
    assert summary['A'] == 2
    assert summary['B'] == 0
    assert summary['F'] == 1
    st = courses['IP'].students['1']
    assert st.grade(courses['IP'].policy) == 'A'
    st = courses['IP'].students['4']
    assert st.grade(courses['IP'].policy) == 'F'


_test()
credit = 4
assessments = dict([('labs', 30), ('midsem', 15),
                   ('assignmments', 30), ('endsem', 25)])
policy = [80, 65, 50, 40]
courses = {}
courses = create(courses, 'IP', credit, assessments, policy)
courses = upload(courses)
courses['IP'].real_policy()
main(courses)
