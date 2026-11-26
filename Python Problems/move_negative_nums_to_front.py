arr = [5, -2, 8, -9, 3, -1]
new_arr = []
for x in arr:
  if x < 0:
    new_arr.append(x)
for y in arr:
  if y > 0:
    new_arr.append(y)
print(new_arr)