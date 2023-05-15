import datetime
import math

# String is immutable
name = ' '.join(["Marcelo", "Leite", "Junior"])
print(name)

name_partitioned = name.partition('Leite')
print(name_partitioned)

# Using _ to define unused variables
origin, _, destination = 'Seattle-Boston'.partition('-')

print('The age of {0}, if {1}, right {0}?'.format('Jim', 32))

print('The age of {} is {}'.format('Fred', 11))

print('Galactic position x = {pos[0]}, y = {pos[1]}, z = {pos[2]}'.format(pos=(12.0, 0.0, 123.0)))

print('Math constants: pi={m.pi:.3f}, e={m.e:.3f}'.format(m=math))

value = 4 * 20
print('The value is {value}'.format(value=value))

# PEP 498: Literal String Interpolation (f-strings)

print(f'one plus one is {1 + 1}')
print(f'The value is {value}')
print(f'The current time is {datetime.datetime.now()}')
print(f'The current time is {datetime.datetime.now().isoformat()}')
print(f'Math constants: pi={math.pi:.3f}, e={math.e:.3f}')
