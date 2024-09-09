import time
import matplotlib.pyplot as plt


#fib2 linear time function
def fib2(n):
    if n == 0:
        return 0
    f = [0]*(n+1)
    f[0] = 0
    f[1] = 1
    for i in range(2, n+1):
        f[i] = f[i-1] + f[i-2]
    return f[n]

# X axis: Indices from 1 to 43
x = list(range(1, 44))

# Y axis: Time taken for the first 43 Fibonacci numbers for fib2
y = []

# Run fib2 one million times for each n and record the average time
for n in x:
    start_time = time.time()
    
    for _ in range(10**6):
        result = fib2(n)
    
    end_time = time.time()
    total_time = end_time - start_time
    average_time = total_time / 10**6
    
    y.append(average_time)
    print(f"Fibonacci({n}) = {result}, Average Time: {average_time} seconds")

# Create a scatter plot
plt.scatter(x, y, c="red")

# Add title and labels
plt.title("Average Time for Iterative Fibonacci Calculation (First 43 Numbers, 1M Executions Each)")
plt.xlabel("Index (n)")
plt.ylabel("Average Time (seconds)")

# Show the plot
plt.show()