menu = [
    ('Samosa', 15),
    ('Idli', 30),
    ('Maggie', 50),
    ('Dosa', 70),
    ('Tea', 10),
    ('Coffee', 20),
    ('Sandwich', 35),
    ('ColdDrink', 25)
]
for k in menu:
    print(k[0], ':', k[1])
print()
mainlist = []
x = int(input('Number of items : '))
total_price = 0
total_no_of_item = 0
for b in range(x):
    a = input('Please order (<number of item> <name of item>) : ')
    y = a.split()
    mainlist.append(y)
print()
for a_list in mainlist:
    number_of_item = int(a_list[0])
    total_no_of_item += number_of_item
    name_of_item = a_list[1]
    for b in menu:
        if b[0] == name_of_item:
            price_of_item = b[1]
            break
        else:
            price_of_item = 0
    if price_of_item == 0:
        print('Wrong Input')
    price_of_n_items = number_of_item * price_of_item
    total_price += price_of_n_items
    print(name_of_item, ',', number_of_item, ', Rs', price_of_n_items)


def _test():
    assert len(mainlist[0]) == 2


_test()
print()
print('Total,', total_no_of_item, 'items, Rs.', total_price)
