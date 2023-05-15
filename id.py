def print_variable_description(var):
    print('value = ' + str(var))
    print('id = ' + str(id(var)))
    print('type = ' + str(type(var)))


a = 496
print('----- Var a')
print_variable_description(a)

b = 1729
print('----- Var b')
print_variable_description(b)

b = a
print('----- Var b')
print_variable_description(b)
