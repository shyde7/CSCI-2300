# Description: This program calculates the nth Fibonacci number using a bottom-up approach.
import sys

#n = to input argument
n = int(sys.argv[1])

# print the final result
def fib2(n):
    if n == 0:
        return 0
    f = [0]*(n+1)
    f[0] = 0
    f[1] = 1
    for i in range(2, n+1):
        f[i] = f[i-1] + f[i-2]
    return f[n]

print(fib2(n))