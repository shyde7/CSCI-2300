import random
import matplotlib.pyplot as plt

# Task 1: Generate a random graph G(n, p)
def generateRandomGraph(n, p):
    # Initialize an empty graph as an adjacency list
    G = {i: [] for i in range(n)}
    
    # Iterate over each pair of vertices (i < j)
    for i in range(n):
        for j in range(i + 1, n):
            # Generate a random number q and add edge if q < p
            if random.random() < p:
                G[i].append(j)
                G[j].append(i)
    
    return G

# Task 2: BFS to find the size of the component starting from a given node
def bfs_component_size(graph, start, visited):
    queue = [start]
    visited[start] = True
    component = []
    
    while queue:
        node = queue.pop(0)
        component.append(node)
        
        for neighbor in graph[node]:
            if not visited[neighbor]:
                visited[neighbor] = True
                queue.append(neighbor)
    
    return component

# Check if there's a component of size >= t
def has_large_component(graph, t):
    visited = {node: False for node in graph}
    
    for node in graph:
        if not visited[node]:
            component = bfs_component_size(graph, node, visited)
            if len(component) >= t:
                return 1  # Found a component with at least t vertices
    
    return 0  # No large component found

# Task 3: Calculate percentage of large components
def percentageLargeComponents(n, t, c_values, num_graphs):
    results = []
    
    for c in c_values:
        p = c / float(n)
        count_large_components = 0
        
        for _ in range(num_graphs):
            G = generateRandomGraph(n, p)
            if has_large_component(G, t):
                count_large_components += 1
        
        # Calculate percentage of graphs with large components
        percentage = (count_large_components / num_graphs) * 100
        results.append((c, percentage))
    
    return results

# Parameters for Task 3
n = 40
t = 30
c_values = [i * 0.2 for i in range(1, 16)]  # c in range [0.2, 3.0]
num_graphs = 500

# Main function
def main():
    # Run the test
    percentages = percentageLargeComponents(n, t, c_values, num_graphs)

    # Plot the results
    c_vals, percentages_vals = zip(*percentages)
    plt.plot(c_vals, percentages_vals)
    plt.xlabel('c')
    plt.ylabel('Percentage of large components')
    plt.title('Percentage of graphs with a component of size >= 30')
    plt.show()

# Call the main function
if __name__ == "__main__":
    main()