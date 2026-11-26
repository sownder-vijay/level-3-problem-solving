arr = [4, 7, 2, 7, 4, 9]
for i in range(len(arr)):
  if arr[i] in arr[i+1:]:
    print(arr[i], end = " ")