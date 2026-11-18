#print the minimum number from the list
#print invalid if the list is none or empty
def maximum_number(lst):
    if lst is None or len(lst) == 0:
        return "Invalid"
    else:
        small = lst[0]
        for i in range(1, len(lst)):
            if small > lst[i]:
                small = lst[i]
        return small
lst = [10, 20, 30, 40, 100, 50, 60, 70, 80]
print(maximum_number(lst))