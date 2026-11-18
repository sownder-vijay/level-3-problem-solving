# Count Occurrences: Given an array of integers and a target element,
# count the number of times the target occurs in the array.
lst = [10, 20, 30, 10, 10, 10, 20, 30, 40]
target = int(input())
cnt = 0
for i in range(len(lst)):
    if target == lst[i]:
        cnt += 1
print(cnt)
