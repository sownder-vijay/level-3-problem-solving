arr = [45, 12, 67, 23, 9, 34]
min = arr[0]
sec_min = arr[0]
for x in arr:
  if min > x:
    min = x
for y in arr:
  if y == min:
    pass
  elif sec_min > y:
    sec_min = y
print(sec_min)