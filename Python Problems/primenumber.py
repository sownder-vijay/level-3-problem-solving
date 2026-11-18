# Prime Number: Given a positive integer n, check whether it is a prime number.
n = int(input())
cnt = 0
for i in range(1, n+1):
    if n%i == 0:
        cnt += 1
if cnt <= 2:
    print('Prime')
else:
    print('Not a Prime')