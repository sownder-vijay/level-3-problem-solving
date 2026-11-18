# Maximum and Minimum in an Array: Given an array of integers, 
# find and print the maximum and minimum elements.
lst = [-9, -2, 30, -1, 50, 60]
a = lst[0]
for i in range(len(lst)):
    if a < lst[i]:
        a = lst[i]
print("max", a)
for j in range(len(lst)):
    if a > lst[j]:
        a = lst[j]
print("min", a)