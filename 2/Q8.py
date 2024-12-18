import re
alice_schedule = eval(input('Alice : '))
bob_schedule = eval(input('Bob : '))
cameron_schedule = eval(input('Cameron : '))


def name(nm_schedule):
    nm = []
    minutes = []
    for x in nm_schedule:
        k = re.split(r':|-', x)
        k = [int(r) for r in k]
        nm.append(k)
    for x in nm:
        start = x[0]*60+x[1]
        end = x[2]*60+x[3]
        assert start < end, 'Starting time could not be less than ending time'
        assert 540 <= start <= 1020, 'time should be between 9:00 to 17:00'
        assert 540 <= end <= 1020, 'time should be between 9:00 to 17:00'
        minutes.append((start, end))
    minutes.sort()
    return minutes


alice = name(alice_schedule)
cameron = name(cameron_schedule)
bob = name(bob_schedule)


def common(first, second):
    start = max(int(first[0]), int(second[0]))
    end = min(int(first[1]), int(second[1]))
    if end-start >= 30:
        return (start, end)
    return None


def main(alice, bob, cameron):
    slots = []
    albob = []
    for x in alice:
        for y in bob:
            k = common(x, y)
            if k:
                albob.append(k)
    for a in cameron:
        for b in albob:
            k = common(a, b)
            if k:
                slots.append(k)
    if slots == []:
        sol = ['No common slots available.']
    else:
        sol = [f"30 minutes time slot between {start // 60}:{start % 60:02d}-{end //
                                                                              60}:{end % 60:02d}" for start, end in slots]
    return sol


def _test():
    assert main(["15:00-16:00", "12:00-13:15"], ["14:00-14:30", "12:30-13:30"],
                ["09:00-10:00", "15:30-16:30"]) == ['No common slots available.']


_test()

pr = main(alice, bob, cameron)
for x in pr:
    print(x)
