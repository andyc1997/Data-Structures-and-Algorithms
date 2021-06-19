#uses python3

import sys
import threading

# This code is used to avoid stack overflow issues
sys.setrecursionlimit(10**7) # max depth of recursion
threading.stack_size(2**26)  # new thread will get stack of such size

# A vertex with children and assigned weight
class Vertex:
    def __init__(self, weight):
        self.weight = weight
        self.children = []

def ReadTree():
    # Number of nodes
    size = int(input())
    
    # Weighting of vertices
    tree = [Vertex(w) for w in map(int, input().split())]
    
    for i in range(1, size):
        a, b = list(map(int, input().split()))
        # The subordination of vertices a and b is not unique
        # It is possible a is the parent of b 
        # or b is the parent of a
        tree[a - 1].children.append(b - 1)
        tree[b - 1].children.append(a - 1)
    
    return tree

def dfs(tree, vertex, parent):
    # A dynamic programming implementation
    # If the weights of vertex hasn't been updated:
    if weights[vertex] == -1:
        # If the vertex has exactly one child and not the root
        if len(tree[vertex].children) == 1 and parent != -1:
            # Return the weight directly
            weights[vertex] = tree[vertex].weight
        
        # It has more than one child or being the root
        else:
            # Current weighting of the vertex
            current_weight = tree[vertex].weight
            # Children
            for children in tree[vertex].children:
                # Avoid infinite loop due to two possible subordinations
                if children != parent:
                    # Grandchildren
                    for grandchildren in tree[children].children:
                        # Avoid inifinite loop due to two possible subordinations
                        if grandchildren != vertex:
                            # Add weights of grandchildren
                            current_weight += dfs(tree, grandchildren, children)
            
            # Weighting of the children vertex
            next_weight = 0
            # Children
            for children in tree[vertex].children:
                # Avoid infinite loop due to two possible subordinations
                if children != parent:
                    # Add weights of chilren
                    next_weight += dfs(tree, children, vertex)
            
            # Dynamic programming: Either current vertex + grandchildren or children
            weights[vertex] = max(current_weight, next_weight)
    
    return weights[vertex]

def MaxWeightIndependentTreeSubset(tree):
    # The number of nodes
    size = len(tree)
    
    # Handle trivial case: no nodes
    if size == 0:
        return 0
    
    # Global variable: container for the optimal weights
    global weights
    weights = [-1] * size
    
    # DFS + Dynamic programming
    return dfs(tree, 0, -1)


def main():
    tree = ReadTree()
    weight = MaxWeightIndependentTreeSubset(tree)
    print(weight)

# This is to avoid stack overflow issues
threading.Thread(target = main).start()
