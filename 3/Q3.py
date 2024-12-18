import random

f = open('scores.txt', 'w')
f.close()


def fun1(x):
    a = []
    for k in x:
        k.strip()
        k.strip(';')
        k.strip(':')
        k.strip('.')
        k.strip(',')
        k.strip('-')
        a.append(k)
    a = [x.lower() for x in a]
    total = len(a)
    unique = len(set(a))
    f1 = unique/total
    return f1


def fun2(x):
    y = {}
    x = [b.lower() for b in x]
    lst = []
    for k in x:
        k.strip()
        k.strip(';')
        k.strip(':')
        k.strip('.')
        k.strip(',')
        k.strip('-')
        if k:
            if k not in y:
                y[k] = 1
            else:
                y[k] += 1
    m = list(sorted(y.items(), key=lambda item: item[1], reverse=True))
    top5 = 0
    for a in range(5):
        lst.append(m[a][0])
        top5 += m[a][1]
    total = len(x)
    lst = ' '.join(lst)
    f2 = top5/total
    return f2, lst


def fun3(x):
    length = 0
    bad = 0
    total = 0
    for k in x:
        if k:
            if '.' in k:
                total += 1
                if length < 5 or length > 35:
                    bad += 1
                length = 0
            else:
                length += 1
    f3 = bad/total
    return f3


def fun4(x):
    bad = 0
    for k in x:
        r = 0
        for y in k:
            if y in ['.', ',', ';', ':']:
                r = r+1
        if r > 1:
            bad += 1
    total = len(x)
    ret = bad/total
    return ret


def fun5(x):
    total = len(x)
    if total > 750:
        return 1
    else:
        return 0


def randword(x):
    a = []
    b = []
    for k in x:
        k.strip()
        k.strip(';')
        k.strip(':')
        k.strip('.')
        k.strip(',')
        k.strip('-')
        a.append(k)
    for p in range(5):
        q = random.randint(0, len(a)-1)
        b.append(a[q])
    b = ' '.join(b)
    return b


def _test():
    assert fun1(['hello', 'i', 'am', 'writing', 'this', 'as', 'i', 'am', 'the', 'first',
                 'person', 'to', 'write', 'this', 'bye', 'for', 'now']) == 0.8235294117647058
    assert fun2(['hello', 'i', 'am', 'writing', 'this', 'as', 'i', 'am', 'the', 'first', 'person',
                'to', 'write', 'this', 'bye', 'for', 'now']) == (0.47058823529411764, 'i am this hello writing')
    assert fun3(['hello', 'i', 'am', 'writing', 'this', 'as', 'i', 'am', 'the', 'first', 'person.', 'This', 'is', 'the', 'second', 'sentence.', 'a', 'bad', 'sentence.', 'this', 'is', 'another', 'bad', 'sentence', 'and', 'this', 'will', 'be', 'a', 'very', 'long', 'sentence', 'as', 'it',
                 'has', 'to', 'be', 'more', 'than', '35', 'words', 'which', 'means', 'that', 'that', 'is', 'a', 'very', 'long', 'sentence', 'and', 'i', 'cannot', 'write', 'extra', 'words', 'to', 'save', 'my', 'life.', 'this', 'is', 'the', 'last', 'sentence', 'in', 'the', 'paragraph.']) == 0.6
    assert fun4(['hi...']) == 1.0
    assert fun5(['hi...']) == 0


_test()


def main(n):
    for q in range(1, n+1):
        a = open(f'FILE{q}.txt', 'r')
        x = []
        for y in a:
            r = y[:len(y)-1]
            r = r.split()
            for k in r:
                x.append(k)
        f1 = fun1(x)
        f2 = fun2(x)
        f3 = fun3(x)
        f4 = fun4(x)
        f5 = fun5(x)
        rwords = randword(x)
        net = 4 + (f1*6) + (f2[0]*6) - f3 - f4 - f5
        net = round(net, 2)
        scr = open('scores.txt', 'a')
        scr.write(f'FILE{q}.txt \nScore : {net} \nFive most used words in descending order of usage : {
                  f2[1]} \nFive random words from the submission : {rwords} \n')
        a.close()
        scr.close()


n = int(input('Number of files : '))
main(n)
print()
print('Output written to "scores.txt"')
