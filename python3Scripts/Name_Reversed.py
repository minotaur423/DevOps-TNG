# Solution 1
name = input('What is your first and last name? ')
words = name.split(" ")

for word in words:
    lastindex = len(word) -1
    for index in range(lastindex, -1, -1):
        print(word[index], end='')
    print(end=' ')
print(end='\n')
    
# Solution 2
first, last = name.split()
print(first[::-1], last[::-1])
