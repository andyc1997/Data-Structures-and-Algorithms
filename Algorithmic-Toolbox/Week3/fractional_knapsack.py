# Uses python3
import sys
# Task. The goal of this code problem is to implement an algorithm for the fractional knapsack problem.
# Input Format. The first line of the input contains the number n of items and the capacity W of a knapsack.
# The next n lines define the values and weights of the items. The i-th line contains integers v[i] and w[i]—the
# value and the weight of i-th item, respectively.
# Output Format. Output the maximal value of fractions of items that fit into the knapsack.

# Greedy algorithm: Take the items with maximum v[j] to w[j] ratio until the capacity is full
# If the last item is removed, the remaining items also yield an optimal solution to the subproblem. So, this is a safe move
def avoid_zero(v, w):
    if w == 0: # v[j]/w[j] is undefined mathematically when w[j] = 0. Let assume the item does not exist, so return value 0
        return 0
    else: # Otherwise, do division
        return v / w 

def linear_search(weights, values):
    values_per_weights = [avoid_zero(v, w) for (w, v) in zip(weights, values)]  # A list with j-th index = v[j]/w[j], 0 if w[j] == 0. This procedure takes O(n)
    index = 0
    while weights[index] <= 0: # If the first item has 0 weights, shift by ignore it and proceed to the next item until weights[j] > 0
        index += 1
    for i in range(len(weights)): # Basic linear search with time complexity O(n)
        if values_per_weights[i] > values_per_weights[index]: 
            index = i
    return index
    
def get_optimal_value(capacity, weights, values):
    value = 0 # The original value of Knapsack problem is 0 because no items
    for i in range(len(weights)): # The outer loop takes O(n) and do linear search at cost O(n) at each loop, so total cost = O(n^2)
        if capacity == 0: # If capacity is 0, return default value which is 0
            return value 
        j = linear_search(weights, values) # A linear search for j-th item which has maximum ratio of values to weights
        a = min(weights[j], capacity) # Check if capacity is available for the entire j-th item, if not let take the part of j-th item for the remaining capacity
        value += a * values[j]/weights[j] # Accumulate the value
        weights[j] -= a # Reduce the current amount of j-th item by the amount taken
        capacity -= a # Reduce the current capacity of knapsacck as j-th item is included
    return value


if __name__ == "__main__":
    data = list(map(int, sys.stdin.read().split()))
    n, capacity = data[0:2]
    values = data[2:(2 * n + 2):2] 
    weights = data[3:(2 * n + 2):2]
    opt_value = get_optimal_value(capacity, weights, values)
    print("{:.10f}".format(opt_value))
