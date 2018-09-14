a = 15
if a < 15:
    print('a is less than 15') 

if a == 15: 
    print('a is equal to 15') 
else: 
    print('a is something other than 15') 

b = 'hello' 

if b == 'goodbye': 
    print(b) 
elif b == 'hello': 
    print(b + ', world!') 
else: 
    print('???') 

c = [1, 'hi' , 2, 'hello', 3, 'greetings', 3.14159]

print('\nsimple while loop:\n') 

#simple while loop 
while a > 0: 
    print(a, end=' ') 
    a -= 1

print('\nsimple for loop over a list:\n') 
#simple for loop over a list 
for i in c: 
    print(i, end=' ') 

print('\nwhile loop with break:\n') 
#while loop with break 
while a < 15: 
    if a == 7:
        break
    print(a, end=' ')
    a += 1

print()

print('\nfor loop with continue:\n') 
#for loop with continue 
for i in c: 
    if i == 3:
        continue
    print(i, end=' ')

print()
