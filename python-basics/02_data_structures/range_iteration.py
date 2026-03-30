# range_iteration.py
# Topic: range and iteration

"""
This file demonstrates:
- iteration over a list
- iteration with range()
- iteration with index
"""

lst = [10, 20, 30]

# iterate directly over values
print("Iterate over values:")
for item in lst:
    print(item)

# iterate using range
print("Iterate using range:")
for i in range(3):
    print(i)

# iterate using index
print("Iterate over list with index:")
for i in range(len(lst)):
    print(i, lst[i])
