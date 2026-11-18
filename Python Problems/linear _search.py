#Linear Search: Given an array and a target element, find the index of the target element. If the element is not present, print -1.
def linear_search(lst,target):
    for i in range(len(lst)):
        if lst[i] == target:
            return i
    return -1
lst = [10, 20, 30, 40, 50, 60, 70, 80]
target = int(input())
print(linear_search(lst, target))
    