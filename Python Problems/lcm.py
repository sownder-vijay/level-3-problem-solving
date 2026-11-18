a = int(input())
b = int(input())
if a > b:
    large = a
else:
    large = b
while True:
    if large%a == 0 and large%b == 0:
        break
    large = large + 1
print(large)
