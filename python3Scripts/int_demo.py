x = 5
y = 10
y = 0xA # Hex
y = 0o12 # Octal
y = 0b1010 # binary
print('x =', x, ',', 'y =', y)
# Typical comparisons can be made
print('x == y =', x == y)
print('x != y =', x != y)
print('x >= y =', x >= y)
print('x > y =', x > y)
print('x <= y =', x <= y)
print('x < y =', x < y)
# The usual operators can be used:
print('x + y =', x + y)
print('x - y =', x - y)
print('x * y =', x * y)
print('x / y =', x / y)
# In Python 2, x / y users floor division like:
print('x // y =', x // y)
print('x % y =', x % y)
print('x ** y =', x ** y)
# There are several useful builtin functions:
print('divmod(x, y) =', divmod(x, y))
print('pow(x, y) =', pow(x, y))
print('abs(-x) =', abs(-x))
print('int(5.2) =', int(5.2))
print('int("0xff",16) =', int("0xff", 16))
print('float(x) =', float(x))
# Inline notation can also be used:
print('x = x + y =', end = ' ')
x += y
print(x)
print('x = x - y =', end = ' ')
x -= y
print(x)
print('x = x * y =', end = ' ')
x *= y
print(x)
print('x = x / y =', end = ' ')
x /= y
print(x)
# Multiple assignments can be done:
x, y = 4, 2
print('x =', x, ',' 'y =', y)
# Bitwise operators can be used:
print('Or: x | y =', x | y)
print('Xor: x ^ y =', x ^ y)
print('And: x & y =', x & y)
print('Left Shift: x << y =', x << y)
print('Right Shift: x >> y =', x >> y)
print('Inversion: ~x =', ~x)
