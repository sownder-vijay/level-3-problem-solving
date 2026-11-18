n = int(input())
count = 0
for i in range(1, n+1, 1):
    if n % i == 0:
        count += 1
if n == 1:
    print("Not prime")
else:
    if count > 2:
        print("Not prime")
    else:
        print("Prime")