a_list = [1, 2, 3, 4, 5, 6]

print(a_list[-1])
print(a_list[-2])
print(a_list[-3])
print(a_list[0])

# Slice

print(a_list[1:3])
print(a_list[:3])
print(a_list[1:-1])
print(a_list[2:])

new_list = a_list[:]

print (new_list is a_list)
print (new_list == a_list)

copy_list = a_list.copy()
print(copy_list is a_list)

alternative_copy_list = list(a_list)
print(alternative_copy_list is a_list)

a = [[1, 2], [3, 4]]
b = a[:]

print(a is b)
print(a == b)
print(a[0] is b[0])

a[0] = [8, 9]
print(a[0])
print(b[0])

a[1].append(5)
print(a[1])
print(b[1])

u = 'O cravo brigou com a rosa'.split()
del u[3]
print(u)
u.remove('rosa')
print(u)
u.insert(0, 'Letra')
print(u)
print(' '.join(u))
u.reverse()
print(u)
u.sort()
print(u)
u.sort(reverse=True)
print(u)

h = 'gigantestiscas com muitas palavras O eu'.split()

h.sort(key=len)
print(h)
