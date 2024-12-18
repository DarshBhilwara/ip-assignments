lst = []
while True:
    a = input('Course number, number of credits, grade received : ')
    if a == '':
        break
    course_no, number_of_credits, grade_received = a.split()
    if not course_no[0].isalpha() or not course_no[-1].isnumeric():
        print('Incorrect Course')
    elif number_of_credits not in ['1', '2', '4']:
        print('Incorrect Credit')
    elif grade_received not in ['A+', 'A', 'A-', 'B', 'B-', 'C', 'C-', 'D', 'F']:
        print('Improper Grade')
    else:
        number_of_credits = int(number_of_credits)
        lst.append([course_no, int(number_of_credits), grade_received])


def _test():
    assert len(lst) >= 1, 'Add atleast one course'
    assert len(lst[0]) == 3, 'you might have missed something'


_test()
sgpa = 0
tot_cred = 0
for x in lst:
    if x[2] == 'A+' or x[2] == 'A':
        grade = 10
    elif x[2] == 'A-':
        grade = 9
    elif x[2] == 'B':
        grade = 8
    elif x[2] == 'B-':
        grade = 7
    elif x[2] == 'C':
        grade = 6
    elif x[2] == 'C-':
        grade = 5
    elif x[2] == 'D':
        grade = 4
    elif x[2] == 'F':
        grade = 2
    else:
        grade = 0
    print(x[0], ' : ', x[2])
    sgpa += grade*x[1]
    tot_cred += x[1]
sgpa /= tot_cred
sgpa = round(sgpa, 2)
print('SGPA : ', sgpa)
