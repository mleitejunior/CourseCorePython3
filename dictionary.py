dictionary = {'a' : 1, 'c' : 3}

print(dictionary)

dictionary['b'] = 2

print(dictionary)

colors = dict(aquamarine='#7FFFD4', sienna='#A0522D')

for key in colors:
    print(f'{key} => {colors[key]}')

for value in colors.values():
    print(value)

for key in colors.keys():
    print(key)

for key, value in colors.items():
    print(f'{key} => {value}')
