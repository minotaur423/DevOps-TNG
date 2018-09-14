# The only two instance of the boolean class are True or False
x = 1
print('bool(x) =', bool(x))
y = 0
print('bool(y) =', bool(y))
# The bool class is a subclass of 'int'
# Zero values are considered False, non-zero True
# Values considered False in Python
if not None: print('None is False')
if not False: print('False is False')
if not (0 or 0.0 or 0j): print('Zero is False')
if not ('' or [] or ()): print('Empty sequences are False')
if not ({} or set([])): print('Empty mappings are False')
# Boolean Or returns first True, or last False value:
print('True or False returns', True or False)
print('1 or 0 returns', 1 or 0)
print('None or 0 returns', None or 0)
# Boolean And returns first False, or last True value:
print('True and False returns', True and False)
print('1 and 0 returns', 1 and 0)
print('None and 0 returns', None and 0)
# Boolean Not returns False if opearand is True:
print('Not True returns', not True)
print('Not 1 returns', not 1)
print('Not "text" returns', not "text")
# Boolean Not returns True if opearand is False:
print('Not False returns', not False)
print('Not 0 returns', not 0)
print('Not "" returns', not "")
