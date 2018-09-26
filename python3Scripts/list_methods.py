# Practice with list methods.
a = [1,2,3]
b = [4,5,6]

c = a + b
print(c)

s = 'a b c d e f'
z =  s.split()
print(z)

if 'a' in z:
    print("A is in z")
else:
    print("A is not in z")

if 'g' not in z:
    print("G is not in z")
else:
    print("G is in z")

for i in z:
    print(i)

q = [4,5,3,2,7]
q.sort()
print(q)
q.reverse()
print(q)
print(q.count(3))
print(q.index(7))
print(len(q))
print(min(q))
print(max(q))