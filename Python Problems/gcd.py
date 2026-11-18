import time
start_time = time.perf_counter()
a = int(input())
b = int(input())
count = 0
while True:
    r = a % b
    a = b
    b = r
    count += 1
    if r == 0:
        print("GCD: ",a)
        print(count)
        break
end_time = time.perf_counter()
execution_time = end_time - start_time
print(f"Execution time: {execution_time:.6f} seconds")
