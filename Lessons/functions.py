# Practice with functions
def greet():
    print('Hello World')

greet()

def greet(name,time):
    print(f'Good {time} {name}, hope you are well')

name = input('Enter your name: ')
time = input('Enter the time of day: ')

greet(name, time)

def greet(name='Jose',time='Morning'):
    print(f'Good {time} {name}, hope you are well')

#name = input('Enter your name: ')
#time = input('Enter the time of day: ')

greet()

def area(radius):
    print(3.142 * radius * radius)

area(5)

def area(radius):
    return 3.142 * radius * radius

def vol(area,length):
    print(area * length)

radius = int(input('Enter a radius: '))
length = int(input('Enter a length: '))

# area_calc = area(radius)
# vol(area_calc,length)
vol(area(radius),length)
