import sys
from termcolor import colored


dataset = [[96, 91], [96, 92], [96, 92], [97, 94], [98, 95], [100, 94], [100, 96], [102, 97], [103, 97], [104, 99],
[106, 101], [107, 101], [106, 102], [107, 102], [109, 104], [109, 106], [110, 107], [111, 108], [113, 107], [114,110]]


def greedy_knapsack(dataset, W):
    for i in range (len(dataset)):
        dataset[i].append(dataset[i][1]/dataset[i][0])
    dataset.sort(key = lambda x: x[2], reverse = True)
    total_weight = 0
    total_value = 0
    for i in range (len(dataset)):
        if total_weight + dataset[i][0] <= W:
            total_weight += dataset[i][0]
            total_value += dataset[i][1]
    return total_value
    
#recurrence: K(w,j) = max{K(w-wi,j-1)+vj,K(w,j-1)}
def dynamic_knapsack(dataset, W):
    #intialize all K(0,j) = 0
    #intialize all K(w,0) = 0
    
    #for j = 1 to n:
        #for w = 1 to W:
            #if wj > w: K(w,j) = K(w,j-1)
            #else: K(w,j) = max{K(w-wj,j-1)+vj,K(w,j-1)}
    #return K(W,n)
    
    n = len(dataset)
    K = [[0 for i in range (n+1)] for j in range (W+1)]    
    
    for j in range (1, n+1):
        for w in range (1, W+1):
            if dataset[j-1][0] > w:
                K[w][j] = K[w][j-1]
            else: 
                K[w][j]= max(K[w-dataset[j-1][0]][j-1]+dataset[j-1][1], K[w][j-1])
    return K[W][n] 
    
    

def main():
    
    greedy_W100 = greedy_knapsack(dataset, 100)
    dynamic_W100 = dynamic_knapsack(dataset, 100)
    
    greedy_W200 = greedy_knapsack(dataset, 200)
    dynamic_W200 = dynamic_knapsack(dataset, 200)
    
    greedy_W300 = greedy_knapsack(dataset, 300)
    dynamic_W300 = dynamic_knapsack(dataset, 300)
    
    print(colored("Greedy Algorithm", "red") + " vs " + colored("Dynamic Programming Algorithm", "green"))
    print("")
    print(colored("Greedy Algorithm for W = 100: " + str(greedy_W100), "red"))
    print(colored("Dynamic Programming Algorithm for W = 100: " + str(dynamic_W100), "green"))
    
    print("")
    print(colored("Greedy Algorithm for W = 200: " + str(greedy_W200), "red"))
    print(colored("Dynamic Programming Algorithm for W = 200: " + str(dynamic_W200), "green"))
    
    print("")
    print(colored("Greedy Algorithm for W = 300: " + str(greedy_W300), "red"))
    print(colored("Dynamic Programming Algorithm for W = 300: " + str(dynamic_W300), "green"))
    
main()    
    

