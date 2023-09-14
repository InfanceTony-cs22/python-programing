# python-programing
def fibonacci(n):
    fib_series = []
    a, b = 0, 1
    for _ in range(n):
        fib_series.append(a)
        a, b = b, a + b
    return fib_series

# Change the value of 'n' to generate a different number of Fibonacci numbers
n = 10
result = fibonacci(n)
print(result)
