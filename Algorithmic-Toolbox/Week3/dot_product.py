#Uses python3

import sys

def search_max(a):
    index = 0
    for i in range(len(a)):
        if a[i] > a[index] and i != index:
            index = i
    return index

def max_dot_product(a, b):
    #write your code here
    a_copy = a
    b_copy = b
    res = 0
    n = len(a_copy)
    for i in range(n):    
        a_index = search_max(a_copy)
        b_index = search_max(b_copy)
        
        res += a_copy[a_index] * b_copy[b_index]
        
        del a_copy[a_index]
        del b_copy[b_index]
    return res

if __name__ == '__main__':
    input = sys.stdin.read()
    data = list(map(int, input.split()))
    n = data[0]
    a = data[1:(n + 1)]
    b = data[(n + 1):]
    print(max_dot_product(a, b))
    
