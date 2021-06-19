#uses python3

import sys
import threading

# This code is used to avoid stack overflow issues
sys.setrecursionlimit(10**6) # max depth of recursion
threading.stack_size(2**26)  # new thread will get stack of such size


class Vertex:
    def __init__(self, weight):
        self.weight = weight
        self.children = []

def DebugReadTree():
    size = 5
    data = [1, 5, 3, 7, 5]
    tree = [Vertex(w) for w in data]
    edges = [[5, 4], [2, 3], [4, 2], [1, 2]]
    for i in range(1, size):
        a, b = edges[i - 1]
        tree[a - 1].children.append(b - 1)
        tree[b - 1].children.append(a - 1)
    return tree

def ReadTree():
    size = int(input())
    tree = [Vertex(w) for w in map(int, input().split())]
    for i in range(1, size):
        a, b = list(map(int, input().split()))
        tree[a - 1].children.append(b - 1)
        tree[b - 1].children.append(a - 1)
    return tree

def dfs(tree, vertex, parent):
    for child in tree[vertex].children:
        if child != parent:
            dfs(tree, child, vertex)
    if weights[vertex] == -1:
        if len(tree[vertex].children) == 0:
            if vertex != 0:
                weights[vertex] = tree[vertex].weight


def MaxWeightIndependentTreeSubset(tree):
    size = len(tree)
    if size == 0:
        return 0
    global weights
    weights = [-1] * size
    return dfs(tree, 0, -1)


def main():
    tree = DebugReadTree();
    weight = MaxWeightIndependentTreeSubset(tree);
    print(weight)

# This is to avoid stack overflow issues
threading.Thread(target=main).start()
