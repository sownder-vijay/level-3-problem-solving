text = "PyThOn123"
u = 0
l = 0
d = 0
lower = "abcdefghijklmnopqrstuvwxyz"
upper = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
digits = "0123456789"
for i in range(len(text)):
  if text[i] in lower:
    l += 1
  if text[i] in upper:
    u += 1
  if text[i] in digits:
    d += 1
print(l, u, d)  
