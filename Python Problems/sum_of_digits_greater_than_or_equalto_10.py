arr = [19, 25, 34, 56, 82, 91]
lst = []
for x in arr:
  a = x%10
  b = x//10
  c = a+b
  if c >= 10:
    lst.append(x)
print(lst)
    