def list_count(lst, n):
    if lst is None:
        return "Invalid"
    else:
        count = 0
        for i in range(0, len(lst)):
            if lst[i] == n:
                count += 1
        return count
lst = [10, 20, 30, 10, 20, 40, 30, 20]
n = int(input())
print(list_count(lst, n))