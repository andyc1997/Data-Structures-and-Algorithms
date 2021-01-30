# python3

import sys
import threading

def compute_height(n, parents):
    # Replace this code with a faster implementation
    max_height = 0
    for vertex in range(n):
        height = 0
        current = vertex
        while current != -1:
            height += 1
            current = parents[current]
        max_height = max(max_height, height)
    return max_height

class node:
    def __init__(self):
        self.child = []
        self.parent = None
        self.key = None
        
class tree:
    def __init__(self):
        self.root = None
        self.node = []

def get_height(tree, t_node):
    if t_node.child == []:
        return 0
    return 1 + max([get_height(tree, tree.node[t_node.child[i]]) for i in range(len(t_node.child))])

def fast_compute_height(n, parents):
    # Construct empty tree
    t = tree()
    # Construct node of tree and parent
    for i in range(n):
        t_node = node()
        t_node.key = i
        t_node.parent = parents[i]
        if t_node.parent == -1:
            t.root = t_node
            t.node.append(t.root)
        else:
            t.node.append(t_node)
    # Construct child of tree
    for i in range(n):
        parent_index = t.node[i].parent
        if parent_index != -1:
            parent_node = t.node[parent_index]
            parent_node.child.append(i)
    return get_height(t, t.root) + 1

def main():
    #f = open(r'C:\Users\user\Documents\Coursera (2020)\Data Structures\week1_basic_data_structures\mywork\21.txt', 'r')
    #data = list(f)
    #x = []
    #for i in range(len(data) - 1):
    #    x += data[i + 1].split()
    n = int(input())
    parents = list(map(int, input().split()))
    #n = int(data[0])
    #parents = list(map(int, x))
    print(fast_compute_height(n, parents))


# In Python, the default limit on recursion depth is rather low,
# so raise it here for this problem. Note that to take advantage
# of bigger stack, we have to launch the computation in a new thread.
sys.setrecursionlimit(10**7)  # max depth of recursion
threading.stack_size(2**30)   # new thread will get stack of such size
threading.Thread(target=main).start()
