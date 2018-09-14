num1 = 3.1425467389
num2 = 10.2903948
# Previous way
print('num1 is', num1, 'and num2 is', num2)

# New ways
# Format method
print('num1 is {0:.3f} and num2 is {1:.3f}'.format(num1,num2))

# Using F-Strings
print(f'num1 is {num1:.4f} and num2 is {num2:.4f}')
