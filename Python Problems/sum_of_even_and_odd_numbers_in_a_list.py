arr = [12, 7, 9, 20, 15, 8]
even = 0
odd = 0
for x in arr:
  if x%2 == 0:
    even += x
  else:
    odd += x
print("Even: ", even)
print("Odd: ", odd)