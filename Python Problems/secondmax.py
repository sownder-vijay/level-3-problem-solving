# GCD: Given two positive integers, find their greatest common divisor (GCD).
a = int(input())
b = int(input())
gcd =[]
if a > b:
    d1 = a
    d2 = b
else:
    d1 = b
    d2 = a
while True:
    r = d1%d2
    d2 = d1
    if r == 0:
            break
    gcd.append(r)

    
print("gcd:",gcd[-1])