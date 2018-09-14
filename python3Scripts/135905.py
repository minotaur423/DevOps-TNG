import mymodule

# print(myfunction())  # Error!
print(mymodule.myfunction())

from mymodule import myfunction

print(myfunction())
