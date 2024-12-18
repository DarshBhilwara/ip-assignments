import json
with open('addrbook.txt', 'r') as json_file:
    directory = json.load(json_file)


def one():
    name = input('Name : ')
    address = input('Address : ')
    phone = input('Phone : ')
    email = input('Email : ')
    if name in directory:
        print('Person already exists, changing name to name1 and so on.')
        c = 0
        while name in directory:
            c = c+1
            name = name+str(c)
    directory[name] = {'Address': address, 'Phone': phone, 'Email': email}


def two():
    nm = input('Name to delete : ')
    if nm in directory:
        del directory[nm]
    else:
        print('User does not exist')


def three():
    srch = input('Partial name to search for : ')
    matching = [x for x in directory if srch in x]
    if matching == []:
        print('No person found')
    else:
        for x in matching:
            print(x, ' : ', directory[x])


def four():
    what = input('Phone or Email : ')
    while what not in ['Phone', 'Email']:
        print("Input can only be 'phone' or 'email'.")
        what = input('Phone or Email : ')
    srch = input('Phone Number or Email to search for : ')
    matching = []
    for a, b in directory.items():
        if srch in b[what]:
            matching.append(a)
    for x in matching:
        print(x, ' : ', directory[x])


def main():
    while True:
        print()
        print('(1) Insert a new entry')
        print('(2) Delete an entry')
        print('(3) Find all the matching entries given a partial name')
        print('(4) Find the entry with a phone number of email')
        print('(5) Exit')
        print()
        a = input('Your Choice : ')
        print()
        if a == '1':
            one()
        elif a == '2':
            two()
        elif a == '3':
            three()
        elif a == '4':
            four()
        elif a == '5':
            with open('addrbook.txt', 'w') as json_file:
                json.dump(directory, json_file, indent=4)
            break
        else:
            print('Wrong Input')


main()
