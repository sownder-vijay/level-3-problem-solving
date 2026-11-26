arr = [2, 4, 7, 9, 11, 15, 17, 20]
new_arr = []
for x in arr:
  count = 0
  for i in range(2,x):
    if x%i == 0:
      count += 1
  if count == 0:
    new_arr.append(x)
print(new_arr)
    