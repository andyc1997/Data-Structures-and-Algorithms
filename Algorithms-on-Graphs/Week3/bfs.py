#Uses python3

import sys
import queue

def distance(adj, s, t):
    #write your code here
    n = len(adj) # Number of vertices
    inf = n + 1 # Distance between the origin and isolated points
    
    dist = [inf] * n # An initialized array containing distance of each vertex
    dist[s] = 0
    
    q_vertex = queue.Queue()
    q_vertex.put(s)
    
    while not q_vertex.empty():
        u = q_vertex.get()
        for v in adj[u]:
            if dist[v] == inf:
                q_vertex.put(v)
                dist[v] = dist[u] + 1
    
    if dist[t] != inf:
        return dist[t]
    else:
        return -1

if __name__ == '__main__':
    input = sys.stdin.read()
    data = list(map(int, input.split()))
    #data = [4, 4, 1, 2, 4, 1, 2, 3, 3, 1, 2, 4]
    #data = [5, 4, 5, 2, 1, 3, 3, 4, 1, 4, 3, 5]
    n, m = data[0:2]
    data = data[2:]
    edges = list(zip(data[0:(2 * m):2], data[1:(2 * m):2]))
    adj = [[] for _ in range(n)]
    for (a, b) in edges:
        adj[a - 1].append(b - 1)
        adj[b - 1].append(a - 1)
    s, t = data[2 * m] - 1, data[2 * m + 1] - 1
    print(distance(adj, s, t))
