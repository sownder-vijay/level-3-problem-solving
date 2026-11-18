def fizz_buzz(n):
    for i in range(n, 0, -1):
        if i%3 ==0 and i % 5 ==0:
            print("FizzBuzz")
        elif i%3 == 0:
            print("Fizz")
        elif i%5 == 0:
            print("Buzz")
        else:
           print(i)

n = int(input())
fizz_buzz(n)