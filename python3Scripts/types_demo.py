"""
order of operations: (PEDMAS)
() (Parenthesis)
** (Exponent)
~ + - (unary operations)
* / % // (Division, Multiplication)
+ - (Addition, Subtraction)
>> << (shift bitwise)
& (AND bitwise)
^ | (NOT, OR bitwise)
<= < > >= (Comparison)
<> == != (Equality)
= %= /= //= -= += **= (Assignment)
"""
amount = 163400
time = 57.5

rate =  amount / time
print('Rate: ' + str(rate))

bits = 16
size = 2 ** 16
print('Size: ' + str(size))

print('11 // 3: ' + str(11 // 3))   # Integer Division
print('11 / 3: ' + str(11 / 3))     # Float Division
print('11 % 3: ' + str(11 % 3))     # Modulus = Remainder
#print('11 / 0: ' + str(11 / 0))    # Division by zero! error!

# PEDMAS?
print(10 - 2 ** 2 / 2 + 5)
