#!/usr/bin/python3
import sys, threading
sys.setrecursionlimit(10**7) # max depth of recursion
threading.stack_size(2**27)  # new thread will get stack of such size
# Task. You are given a binary tree with integers as its keys. You need to test whether it is a correct binary
# search tree. The definition of the binary search tree is the following: for any node of the tree, if its
# key is x, then for any node in its left subtree its key must be strictly less than x, and for any node in
# its right subtree its key must be greater than or euqal to x. In other words, smaller elements are to the
# left, and bigger elements are to the right. You need to check whether the given binary tree structure
# satisfies this condition. You are guaranteed that the input contains a valid binary tree. That is, it is a
# tree, and each node has at most two children.
# Input Format. The first line contains the number of vertices n. The vertices of the tree are numbered
# from 0 to n − 1. Vertex 0 is the root.
# The next n lines contain information about vertices 0, 1, ..., n−1 in order. Each of these lines contains
# three integers key[i], left[i] and right[i] — key[i] is the key of the i-th vertex, left[i] is the index of the left
# child of the i-th vertex, and right[i] is the index of the right child of the i-th vertex. If i doesn’t have
# left or right child (or both), the corresponding left[i] or right[i] (or both) will be equal to −1.
# Output Format. If the given binary tree is a correct binary search tree (see the definition in the problem
# description), output one word “CORRECT” (without quotes). Otherwise, output one word “INCORRECT”
# (without quotes).

class TreeOrders:
    def read(self, arr): # Read input and build tree, see tree-order.py
        self.n = len(arr)
        self.key = [0 for i in range(self.n)]
        self.left = [0 for i in range(self.n)]
        self.right = [0 for i in range(self.n)]
        
        for i in range(self.n):
            a, b, c = arr[i]
            self.key[i] = a
            self.left[i] = b
            self.right[i] = c
          
    def inOrderTraversal(self, i, result, warning): # Modified in-order traversal: warning list indicates if two elements are equal 
        if i == -1:
            return None
        if self.left[i] != -1: # If a node has left child and left child shares the same key as its parent, then it violates BST condition
            if self.key[self.left[i]] == self.key[i]:
                warning.append(1)
        self.inOrderTraversal(self.left[i], result, warning)
        result.append(self.key[i])
        self.inOrderTraversal(self.right[i], result, warning)
        return result, warning

def check_result(l): # A linear search to compare two elements if they violate BST conditions
    for i in range(1, len(l)):
        if l[i - 1] > l[i]:
            return False
    return True

def IsBinarySearchTree(tree):
    bst = TreeOrders()
    bst.read(tree)
    result, warning = bst.inOrderTraversal(0, list(), list())

    if len(warning) > 0: # If any violations are detected, return False
        return False
    return check_result(result) # Otherwise, check the results as usual

def main():
    nodes = int(sys.stdin.readline().strip())
    tree = []
    for i in range(nodes):
        tree.append(list(map(int, sys.stdin.readline().strip().split())))
    if nodes == 0: # trivial case
        print("CORRECT")
    elif IsBinarySearchTree(tree):
        print("CORRECT")
    else:
        print("INCORRECT")

threading.Thread(target=main).start()
