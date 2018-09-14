"""
https://docs.python.org/3/reference/datamodel.html
object.__lt__(self, other)
object.__le__(self, other)
object.__eq__(self, other)
object.__ne__(self, other)
object.__gt__(self, other)
object.__ge__(self, other)

object.__add__(self, other)
object.__sub__(self, other)
object.__mul__(self, other)
object.__matmul__(self, other)
object.__truediv__(self, other)
object.__floordiv__(self, other)
object.__mod__(self, other)
object.__divmod__(self, other)
object.__pow__(self, other[, modulo])
object.__lshift__(self, other)
object.__rshift__(self, other)
object.__and__(self, other)
object.__xor__(self, other)
object.__or__(self, other)
"""
class Properties(object):

    def __init__(self, props):
        self.props = []
        if type(props) in (list,tuple):
            self.props.extend(props)

    def __add__(self, other):
        return Properties(self.props + other.props)

    def __sub__(self, other):
        return Properties([p for p in self.props if p not in other.props])

    def __str__(self):
        return f'Properties: {self.props}'

p1 = Properties(['red', 'round', 'small'])
p2 = Properties(['shiny', 'reflective', 'transparent'])
p3 = Properties(['small', 'round'])

print('p1: ' + str(p1))
print('p2: ' + str(p2))
print('p3: ' + str(p3))

print()

p4 = p1 + p2
print('p4: ' + str(p4))

print()

print('p4 - p3: ' + str(p4 - p3))
