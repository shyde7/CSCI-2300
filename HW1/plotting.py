import matplotlib.pyplot as plt
import time

def fib1(n):
    if n == 0:
        return 0
    if n == 1:
        return 1
    return fib1(n - 1) + fib1(n - 2)

# X axis: Indices from 1-43
x = list(range(1, 44))

# Initialize Y axis: This will store the time taken for each fib1 computation
y = []

# Loop through each n from 1 to 43
for n in x:
    # Start timing the fib1 execution
    start_time = time.time()
    
    result = fib1(n)

    print(f"Fibonacci({n}) = {result}")
    
    # End timing
    end_time = time.time()
    
    # Calculate the time taken for this execution
    time_taken = end_time - start_time

    # Print time taken to to 2 decimal places
    print(f"Time taken: {time_taken:.2f} seconds")    
    
    # Append the time taken to the y list
    y.append(time_taken)

# Create the scatter plot after the loop
plt.scatter(x, y, c="blue")

# Add title and labels
plt.title("Time Taken for Recursive Fibonacci Calculation (First 43 Numbers)")
plt.xlabel("Index (n)")
plt.ylabel("Time (seconds)")

# Show the plot
plt.show()