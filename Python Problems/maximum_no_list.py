# print the maximum number from a list
#if the list is none or empty print invalid
def maximum_number(lst):
    if lst is None or len(lst) == 0:
        return "Invalid"
    else:
        max = lst[0]
        for i in range(1, len(lst)):
            if max < lst[i]:
                max = lst[i]
        return max
lst = [10, 20, 30, 40, 100, 50, 60, 70, 80]
print(maximum_number(lst))