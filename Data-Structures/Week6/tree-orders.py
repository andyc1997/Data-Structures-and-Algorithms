# python3

import sys, threading
sys.setrecursionlimit(10**6) # max depth of recursion
threading.stack_size(2**27)  # new thread will get stack of such size

class TreeOrders:
    def read(self):
        self.n = int(sys.stdin.readline())
        self.key = [0 for i in range(self.n)]
        self.left = [0 for i in range(self.n)]
        self.right = [0 for i in range(self.n)]
        #---------------------------------------------
#        example_list = [0,7,2,10,-1,-1,20,-1,6,30,8,9,40,3,-1,50,-1,-1,60,1,-1,70,5,4,80,-1,-1,90,-1,-1]
        #---------------------------------------------
        for i in range(self.n):
          [a, b, c] = map(int, sys.stdin.readline().split())
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

    def preOrderTraversal(self, i, result):
        if i == -1:
            return None
        result.append(self.key[i])
        self.preOrderTraversal(self.left[i], result)
        self.preOrderTraversal(self.right[i], result)
        return result
    
    def preOrder(self):
        self.result = []
        # Finish the implementation
        # You may need to add a new recursive method to do that
        self.preOrderTraversal(0, self.result)
        return self.result

    def postOrderTraversal(self, i, result):
        if i == -1:
            return None
        self.postOrderTraversal(self.left[i], result)
        self.postOrderTraversal(self.right[i], result)
        result.append(self.key[i])
        return result
    
    def postOrder(self):
        self.result = []
        # Finish the implementation
        # You may need to add a new recursive method to do that
        self.postOrderTraversal(0, self.result)
        return self.result

def main():
    tree = TreeOrders()
    tree.read()
    print(" ".join(str(x) for x in tree.inOrder()))
    print(" ".join(str(x) for x in tree.preOrder()))
    print(" ".join(str(x) for x in tree.postOrder()))

#----------------------------------------------
#if __name__ == '__main__':
#    main()
#----------------------------------------------
threading.Thread(target=main).start()
