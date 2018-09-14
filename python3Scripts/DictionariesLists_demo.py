#list
l0 = []
l1 = [5,10,15,20]
l2 = [3, 'Hello', 77, 'World', 1.299]

print(f'l1: {l1}') 
l1.append(25) 
print(f'l1: {l1}') 

print(f'l2: {l2}') 
print(l2[1] + ', ' + l2[3]) 
print(f'l2[:2]: {l2[:2]}') 
print('l2[2:]: ' + str(l2[2:])) 

l2[0] = 6 
print(l2[0]) 

print(l1 + l2) 
print() 

#dictionary
d0 = {} 
d1 = {'greeting':'hello', 'place':'world'} 
d2 = {'first':9.95, 'second':10.01, 'third':10.23}

print(d1['greeting'] + ', ' + d1['place']) 
d1['place'] = 'Earth' 
print(d1) 

print(d2['first'])
print(d2['second'])
print(d2['third'])
d2['forth'] = 10.55 
print(d2) 
print(d2.keys()) 
print(d2.values())
