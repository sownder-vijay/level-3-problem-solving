n = 10
lst = [2,4,6,8,9,10,12,14,18,22,55,67]
a = len(lst)//2
while True:
    if lst[a] == n:
        print(a)
        break
    elif lst[a] > n:
        a = a // 2
    elif lst[a] < n:
        a = a + (a//2)