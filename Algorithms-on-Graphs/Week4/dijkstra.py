#Uses python3

import sys
import queue

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

def distance(adj, cost, s, t):
    # Dijkstra's Algorithm
    n = len(adj) # Number of nodes
    inf = (10 ** 3) * n + 1 # Inreachable distance
    node = range(n)
    dist = [inf] * n
    
    # Initialize starting point and priority queue
    dist[s] = 0
    h = queue.PriorityQueue()
    H = Heap()
    
    # Heap sort
    for node_num, priority in zip(node, dist):
        h.put((priority, node_num))
    
    for i in range(n):
        H.Put(h.get())
    
    # Edge relaxation
    while not H.Empty():
        _, u = H.Pop()
        if len(adj[u]) > 0:
            for i in range(len(adj[u])):
                v = adj[u][i]
                if dist[v] > dist[u] + cost[u][i]:
                    dist[v] = dist[u] + cost[u][i]
                    H.ChangePriority((dist[v], v))
    if dist[t] != inf:
        return dist[t]
    return -1

if __name__ == '__main__':
    input = sys.stdin.read()
    data = list(map(int, input.split()))
    n, m = data[0:2]
    data = data[2:]
    edges = list(zip(zip(data[0:(3 * m):3], data[1:(3 * m):3]), data[2:(3 * m):3]))
    data = data[3 * m:]
    adj = [[] for _ in range(n)]
    cost = [[] for _ in range(n)]
    for ((a, b), w) in edges:
        adj[a - 1].append(b - 1)
        cost[a - 1].append(w)
    s, t = data[0] - 1, data[1] - 1
    print(distance(adj, cost, s, t))
