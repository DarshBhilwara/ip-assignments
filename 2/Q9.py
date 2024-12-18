def directory(words):
    megalist = []
    words.sort()
    for x in words:
        a = megalist
        for i in range(len(x)):
            for j in range(len(a)):
                if a[j][0] == x[i] and type(a[j]) is list:
                    a = a[j]
                    break
            else:
                a.append([x[i]])
                a = a[-1]
        if x not in a:
            a.insert(1, x)
    return megalist


def add(word, megalist):
    a = megalist
    for x in range(len(word)):
        for y in range(len(a)):
            if a[y][0] == word[x] and type(a[y]) is list:
                a = a[y]
                break
        else:
            a.append([word[x]])
            a = a[-1]
    if len(a) == 1:
        a.append(word)
        return "Added to directory"
    else:
        if type(a[1]) is list:
            a.insert(1, word)
            return "Added to directory"
        else:
            return "Word already exists"


def search(megalist):
    s = []
    ans = []
    for x in range(len(megalist)):
        if type(megalist[x]) is list:
            s.append(megalist[x])
            k = megalist[x]
            while s:
                k = s[-1]
                s.pop(-1)
                for y in range(len(k)):
                    if type(k[y]) is str and y != 0:
                        ans.append(k[y])
                    elif type(k[y]) is list:
                        s.append(k[y])
    return ans


def count(word, megalist):
    count = 0
    a = search(megalist)
    for x in a:
        if word in x:
            count = count+1
    return count


def find(first, megalist):
    a = megalist
    for i in range(len(first)):
        for j in range(len(a)):
            if a[j][0] == first[i] and type(a[j]) is list:
                a = a[j]
                break
        else:
            a = []
            break
    else:
        a = search(a)
        a.sort()
    return a


def dlt(word, megalist):
    a = megalist
    find = [0]*len(word)
    out = ''
    for i in range(len(word)):
        for j in range(len(a)):
            if a[j][0] == word[i] and type(a[j]) is list:
                a = a[j]
                find[i] += len(a)-1
                break
        else:
            out = "Word not in directory"
            break
    else:
        if a[1] != word:
            out = "Word not in directory"
        else:
            out = "Word deleted"
            a.pop(1)
            x = 0
            for i in range(len(word)-1, -1, -1):
                if find[i] == 1:
                    x = x+1
                else:
                    break
            x = len(word)-x
            a = megalist
            end = megalist
            if x != len(word):
                for i in range(x+1):
                    for j in range(len(a)):
                        if a[j][0] == word[i] and type(a[j]) is list:
                            end = a
                            a = a[j]
                end.remove(a)
    return out


def _test():
    n = directory(['hi', 'hell', 'hello', 'hell', 'naw'])
    assert add('new', n) == 'Added to directory'
    assert count('hell', n) == 2
    assert dlt('w', n) == 'Word not in directory'


_test()

words = input('Enter words to create directory : ').split()


def main():
    megalist = directory(words)
    while True:
        print()
        print('1. Print full directory')
        print('2. Print words starting from')
        print('3. Counting instances of a substring')
        print('4. Add a new word')
        print('5. Delete a word')
        print('6. Exit')
        print()
        q = int(input('Select your option : '))
        if q == 1:
            print(megalist)
        elif q == 2:
            m = input('Words starting from : ')
            print(find(m, megalist))
        elif q == 3:
            m = input('Substring :')
            print(count(m, megalist))
        elif q == 4:
            m = input('Word : ')
            print(add(m, megalist))
        elif q == 5:
            m = input('Word : ')
            print(dlt(m, megalist))
        elif q == 6:
            break
        else:
            print('Wrong Input')


main()
