def binary_search(arr, a):
  high = len(arr) - 1
  low = 0
  while low<=high:
    mid = (low + high) // 2
    if arr[mid] == a:
      return mid
    if arr[mid] > a:
      high = mid - 1
    if arr[mid] < a:
      low = mid + 1
  return -1
arr = ["apple", "banana", "orange", "apricot", "carrot"]
arr.sort()
a = input()
print(binary_search(arr, a))