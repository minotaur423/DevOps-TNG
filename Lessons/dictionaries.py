def belt_count(dictionary):
    belts = list(dictionary.values())
    for belt in set(belts):
        num = belts.count(belt)
        print(f'There are {num} {belt} belts')

# Practice with dictionaries.
# def ninja_intro(dictionary):
#     for key, val in dictionary.items():
#         print(f'I am {key} and I am a {val} belt')

ninja_belts = {}

while True:
    ninja_name = input('Enter a ninja name: ')
    ninja_belt = input('Enter a belt color: ')
    ninja_belts[ninja_name] = ninja_belt

    another = input('Add another? (y/n) ')
    if another.upper() == 'Y':
        continue
    else:
        break

# ninja_intro(ninja_belts)
belt_count(ninja_belts)
