arr = [4, 7, 9, 12, 16, 20, 25, 30]
new_arr = []
for x in arr:
  a = 1
  b = 1
  while b<=x:
    b = a * a
    if b==x:
      new_arr.append(x)
    a+=1
print(new_arr)
      
        
    