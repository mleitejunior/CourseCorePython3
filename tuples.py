t = ("Norway", 4.93, 3)

print(t)

print(t[0])
print(t[2])

print(t + (333.0, 256e9))

is_no_tuple = (391)

print(type(is_no_tuple))

is_tuple = (391,)

print(type(is_tuple))

print(type(()))


def minmax(items):
    return min(items), max(items)


is_tuple_too = 1,1,1,4,6,19
print(type(is_tuple_too))
print(minmax(is_tuple_too))

#UNPACKING
lower, upper = minmax(is_tuple_too)
print(lower)
print(upper)

a = 'jelly'
b = 'bean'
a,b = b, a
print(a)
print(b)

converted_to_tuple = tuple([123, 345, 232])
print(type(converted_to_tuple))
string_to_tuple = tuple("Marcelo")
print(string_to_tuple)
print('m' in string_to_tuple)
print('M' in string_to_tuple)
