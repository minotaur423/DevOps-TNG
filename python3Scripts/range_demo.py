# The range function generates a sequence of integers
a_range = range(5)
print('a_range ->', a_range)
print('list(a_range) ->', list(a_range))
# It is often used to execute a "for" loop a number of times
for i in range(5):
    print(i, end=' ') # executed five times
print()
# It is similar to the slice function with a start, stop and step
a_range = range(10) # stop only
print('list(a_range) ->', list(a_range))
a_range = range(10, 16) # start and stop
print('list(a_range) ->', list(a_range))
a_range = range(10, -1, -1) # start, stop and step
print('list(a_range) ->', list(a_range))
