def binary_search(arr, a):
  low = 0
  high = len(arr) - 1
  
  while low<=high:
    mid = (low + high) // 2
    if arr[mid] == a:
      return mid
    elif arr[mid] > a:
      high = mid - 1
    elif arr[mid] < a:
      low = mid + 1
  return -1
arr = [10,20,30,40,50,60,70]
a = int(input())
print(binary_search(arr, a))
