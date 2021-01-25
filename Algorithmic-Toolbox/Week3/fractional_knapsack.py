# Uses python3
import sys

def avoid_zero(v, w):
    if w == 0:
        return 0
    else:
        return v / w

def linear_search(weights, values):
    values_per_weights = [avoid_zero(v, w) for (w, v) in zip(weights, values)]
    index = 0
    while weights[index] <= 0:
        index += 1
    
    for i in range(len(weights)):
        if values_per_weights[i] > values_per_weights[index]:
            index = i
    return index
    
def get_optimal_value(capacity, weights, values):
    value = 0
    
    # write your code here
    for i in range(len(weights)):
        if capacity == 0:
            return value 
        j = linear_search(weights, values)
        a = min(weights[j], capacity)
        value += a * values[j]/weights[j]
        weights[j] -= a
        capacity -= a
    return value


if __name__ == "__main__":
    data = list(map(int, sys.stdin.read().split()))
    n, capacity = data[0:2]
    values = data[2:(2 * n + 2):2]
    weights = data[3:(2 * n + 2):2]
    opt_value = get_optimal_value(capacity, weights, values)
    print("{:.10f}".format(opt_value))
