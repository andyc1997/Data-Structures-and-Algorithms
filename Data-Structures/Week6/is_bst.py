#!/usr/bin/python3

import sys, threading

sys.setrecursionlimit(10**8) # max depth of recursion
threading.stack_size(2**27)  # new thread will get stack of such size

class TreeOrders:
    def read(self, arr):
        self.n = len(arr)
        self.key = [0 for i in range(self.n)]
        self.left = [0 for i in range(self.n)]
        self.right = [0 for i in range(self.n)]
        
        for i in range(self.n):
            a, b, c = arr[i]
            self.key[i] = a
            self.left[i] = b
            self.right[i] = c
          
    def InOrderTraversal(self, i, result):
        if i == -1:
            return None
        self.InOrderTraversal(self.left[i], result)
        result.append(self.key[i])
        self.InOrderTraversal(self.right[i], result)
        return result

    def inOrder(self):
        self.result = []
        # Finish the implementation
        # You may need to add a new recursive method to do that
        self.InOrderTraversal(0, self.result)
        return self.result

def check_result(l):
    for i in range(1, len(l)):
        if l[i - 1] > l[i]:
            return False
    return True

def IsBinarySearchTree(tree):
    # Implement correct algorithm here
    # Construct a tree from input
    bst = TreeOrders()
    bst.read(tree)
    result = bst.inOrder()
    return check_result(result)

def main():
    nodes = int(sys.stdin.readline().strip())
    #---------------------------------------------
    #nodes = 1
    #---------------------------------------------
    tree = []
    #---------------------------------------------
    #tree = [[5, 1, -1], [4, 2, -1], [3, -1, 3], [2, -1, -1]]
    #---------------------------------------------
    for i in range(nodes):
        tree.append(list(map(int, sys.stdin.readline().strip().split())))
    if nodes == 0:
        # Handle empty tree case
        print("CORRECT")
    elif IsBinarySearchTree(tree):
        print("CORRECT")
    else:
        print("INCORRECT")

threading.Thread(target=main).start()
#-----------------------------------------------------------
#if __name__ == '__main__':
#    main()
#-----------------------------------------------------------