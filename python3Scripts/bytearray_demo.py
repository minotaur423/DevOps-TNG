# The bytearray class provides a mutable sequence
# Values must be integers from 0-255 to represent a byte
empty_array = bytearray()
null_array = bytearray(11)
ints_array = bytearray((84, 114, 97, 100, 101, 109, 97, 114, 107, 32, 194, 174))
str_array =  bytearray('Trademark ®', 'utf-8')
bytes_array = bytearray(b'Trademark \xc2\xae')
print('bytes_array =', bytes_array)
print('bytes_array.decode() ->', bytes_array.decode())
str_literal = 'Trademark ®'
# A bytearray sequence behaves similar to a string
print('str_literal.count("T") ->', str_literal.count('T'))
print('str_literal.index("T") ->', str_literal.index('T'))
# However, byte values are used instead of string values
print('bytes_array.count(0x54) ->', bytes_array.count(0x54))
print('bytes_array.index(0x54) ->', bytes_array.index(0x54))
# Bytearray objects have methods to mutate them
bytes_array.append(32)
print('bytes_array =', bytes_array)
bytes_array.extend((194, 174))
print('bytes_array =', bytes_array)
print('bytes_array.decode() ->', bytes_array.decode())
bytes_array.remove(0x54)
print('bytes_array=', bytes_array)
bytes_array.insert(0, 0x54)
print('bytes_array =', bytes_array)
bytes_array.pop()
bytes_array.pop()
print('bytes_array.decode() ->', bytes_array.decode())
