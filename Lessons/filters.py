# Practice with filters
grades = ['A', 'B', 'F', 'C', 'F', 'A']

def remove_fails(grade):
    return grade != 'F'

# Three ways to get the same results
# 1. Filter
# print(list(filter(remove_fails, grades)))

# 2. for loop
# filtered_grades = []
# for grade in grades:
#     if grade != 'F':
#         filtered_grades.append(grade)
# print(filtered_grades)

# 3. Comprehension
print([grade for grade in grades if grade != 'F'])
