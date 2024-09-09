# Description: This program calculates the nth Fibonacci number using recursion.
import sys

#n = to input argument 
n = int(sys.argv[1])

def fib1(n):
    if n == 0:
        return 0
    if n == 1:
        return 1
    return fib1(n - 1) + fib1(n - 2)

print(fib1(n))