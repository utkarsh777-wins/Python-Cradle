# import tensorflow as tf
# print(tf.__version__)
# # n = int(input())
# # for i in range(2, n+1):
# #     if n % i == 0:
# #         break
# # if i == n:
# #     print("prime")
# # else:
# #     print("not prime")
print("hello world!")
# Recursive function for Fibonacci series
def fibonacci(n):
    if n <= 0:
        return "Input should be a positive integer"
    elif n == 1:
        return 0
    elif n == 2:
        return 1
    else:
        return fibonacci(n-1) + fibonacci(n-2)

# Print Fibonacci series up to n terms
def print_fibonacci_series(n):
    series = []
    for i in range(1, n+1):
        series.append(fibonacci(i))
    return series

# Example: Fibonacci series of 10 terms
print(print_fibonacci_series(23))