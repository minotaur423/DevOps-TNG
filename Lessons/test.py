# Practice with modules and packagesself.
from classes4 import Planet

naboo = Planet('Naboo', 300000, 8, 'Naboo System')

print(f'Name: {naboo.name}')
# print(Planet.spin())
print(Planet.spin('a very high speed'))
