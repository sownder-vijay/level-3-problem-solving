arr = [10, 15, 30, 45, 22, 60, 7]
new_arr = []
for x in arr:
  if x%5 == 0 and x%3 == 0:
    new_arr.append(x)
print(new_arr)