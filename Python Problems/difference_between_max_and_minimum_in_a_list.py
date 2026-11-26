arr = [10, 45, 5, 80, 25]
max = arr[0]
min = arr[0]
for x in arr:
  if max < x:
    max = x
  if min > x:
    min = x
diff = max-min
print(diff)
  