#find the second maximum number in a list
def second_max(arr):
    max = arr[0]
    min = arr[0]
    for i in range(1, len(arr)):
        if arr[i] > max:
            max = arr[i]
        if arr[i] < min:
            min = arr[i]
    for j in range(len(arr)):
        if max!=arr[j] and min < arr[j]:
            min = arr[j]
    return min
arr = [-1, -1, -2, -3, -4]
print(second_max(arr))