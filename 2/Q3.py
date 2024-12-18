import json
with open('in3.txt', 'r') as json_file:
    directory = json.load(json_file)
min = len(directory)
max = 0
min_arr = []
max_arr = []
for x, y in directory.items():
    c = 0
    for z, k in y.items():
        c += int(k)
    if c == max:
        max_arr.append(x)
    if c > max:
        max = c
        max_arr = []
        max_arr.append(x)
    if c == min:
        min_arr.append(x)
    if c < min:
        min = c
        min_arr = []
        min_arr.append(x)
print()
print("Person with maximum signatures")
for x in max_arr:
    print(x)
print()
print("Person with minimum signatures")
for x in min_arr:
    print(x)
