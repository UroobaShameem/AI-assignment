#program to swap four variables
a = 10
b = 67
c = 38
d = 55

print('before swapping')
print('a =', a, ' b =', b, ' c =', c, ' d =', d)

a, b, c, d = d, c, b, a
print('after swapping')
print('a =', a, ' b =', b, ' c =', c, ' d =', d)