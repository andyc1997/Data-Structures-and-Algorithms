#Uses python3
import sys
import math

class Heap():
    def __init__(self):
        self.arr = []
        self.track = dict()
        #self.poptime = 0
        
    def Put(self, item):
        # item: (node_name, node_priority_value)
        self.arr.append(item)
        node, index = item[1], len(self.arr) - 1
        self.track.update({node: index})
    
    def LeftChild(i):
        return 2 * i + 1
    
    def RightChild(i):
        return 2 * i + 2
    
    def Parent(i):
        return abs(i - 1) // 2
    
    def SiftUp(self, i):
        # As long as it is not the root and its parent has a key greater than its key
        while (i > 0) & (self.arr[Heap.Parent(i)][0] > self.arr[i][0]):     
            node_1, node_2 = self.arr[Heap.Parent(i)][1], self.arr[i][1]
            
            index_node_1, index_node_2 = self.track.get(node_1), self.track.get(node_2)
            self.track[node_1], self.track[node_2] = index_node_2, index_node_1
            
            self.arr[Heap.Parent(i)], self.arr[i] = self.arr[i], self.arr[Heap.Parent(i)]
            i = Heap.Parent(i)
        
    def SiftDown(self, i):
        minIndex = i
        # Left
        l = Heap.LeftChild(i)
        if l < len(self.arr):
            if self.arr[l][0] < self.arr[minIndex][0]:
                minIndex = l
        # Right
        r = Heap.RightChild(i)
        if r < len(self.arr):
            if self.arr[r][0] < self.arr[minIndex][0]:
                minIndex = r
        # Update
        if i != minIndex:
            node_1, node_2 = self.arr[i][1], self.arr[minIndex][1]
            
            index_node_1, index_node_2 = self.track.get(node_1), self.track.get(node_2)
            self.track[node_1], self.track[node_2] = index_node_2, index_node_1
            
            self.arr[i], self.arr[minIndex] = self.arr[minIndex], self.arr[i]
            Heap.SiftDown(self, minIndex)
    
    def Pop(self):
        result = None
        if len(self.arr) > 1:
            result = self.arr[0]
            self.arr[0] = self.arr[-1] # O(1) time
            del self.arr[-1] # O(1) time
            node = self.arr[0][1]
            self.track[node] = 0
            self.track.pop(result[1])
            #self.poptime += 1
            Heap.SiftDown(self, 0)
            
        elif len(self.arr) == 1:
            result = self.arr[0]
            self.arr.pop()
            self.track.pop(result[1])
            
        return result
    
    def ChangePriority(self, item):
        key, node = item
        node_index = self.track[node] #- self.poptime
        old_key = self.arr[node_index][0]
        self.arr[node_index] = item
        if key >= old_key:
            Heap.SiftDown(self, node_index)
        else:
            Heap.SiftUp(self, node_index)
        
    def Empty(self):
        return len(self.arr) == 0
    
def compute_distance(x_0, y_0, x_1, y_1):
    return math.sqrt((x_0 - x_1) ** 2 + (y_0 - y_1) ** 2)

def minimum_distance(x, y):
    result = 0. # Initialize results
    n = len(x) # Number of vertices
    adj = [[0] * n for i in range(n)] # List of distance
    
    # Compute distance
    for i in range(n):
        for j in range(n):
            if i == j:
                adj[i][j] = 0.
            elif i > j:
                dist = compute_distance(x[i], y[i], x[j], y[j])
                adj[i][j] = dist
                adj[j][i] = dist
    
    #write your code here
    inf = (10 ** 3) * 200
    cost = [inf] * n

    # Pick starting point
    cost[0] = 0
    
    # Initialize Min-heap
    H = Heap()
    for i in range(n):
        H.Put((cost[i], i))
    
    while not H.Empty():
        weight, u = H.Pop()
        result += weight
        for z in range(len(adj[u])):
            if (z in H.track) and (cost[z] > adj[u][z]):
                cost[z] = adj[u][z]
                H.ChangePriority((cost[z], z))
    
    return result


if __name__ == '__main__':
    input = sys.stdin.read()
    data = list(map(int, input.split()))
    #data = [4, 0, 0, 0, 1, 1, 0, 1, 1]
    #data = [5, 0, 0, 0, 2, 1, 1, 3, 0, 3, 2]
    n = data[0]
    x = data[1::2]
    y = data[2::2]
    print("{0:.9f}".format(minimum_distance(x, y)))
