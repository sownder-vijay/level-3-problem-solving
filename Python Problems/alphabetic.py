arr = [10, 18, 26, 80]
i = 0
j = 1
c = len(arr) - 1
a = arr[i]
b = arr[j]
while c!=j:
    r = a % b
    a = b
    b = r
    if r == 0:
        gcd = a
        i += 1
        j += 1
        b = arr[j]
print(gcd)