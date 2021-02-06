#Uses python3

import sys
import queue

def bipartite(adj, n, m):
    #write your code here
    is_bipartite = 1 # Boolean
    
    # Graph without edge
    if m == 0:
        return is_bipartite
    
    inf = n + 1 # Distance between the origin and isolated points
    s = 0 # Start at node with key 1
    
    dist = [inf] * n # An initialized array containing distance of each vertex
    dist[s] = 0
    
    q_vertex = queue.Queue()
    q_vertex.put(s)
    
    while not q_vertex.empty():
        u = q_vertex.get()
        for v in adj[u]:
            if dist[v] == inf:
                q_vertex.put(v)
                dist[v] = 1 - dist[u]
            else:
                if dist[v] == dist[u]:
                    is_bipartite = 0
                    break
    return is_bipartite

if __name__ == '__main__':
    input = sys.stdin.read()
    data = list(map(int, input.split()))
    #data = [4, 0]
    #data = [4, 4, 1, 2, 4, 1, 2, 3, 3, 1]
    #data = [5, 4, 5, 2, 4, 2, 3, 4, 1, 4]
    n, m = data[0:2]
    data = data[2:]
    edges = list(zip(data[0:(2 * m):2], data[1:(2 * m):2]))
    adj = [[] for _ in range(n)]
    for (a, b) in edges:
        adj[a - 1].append(b - 1)
        adj[b - 1].append(a - 1)
    print(bipartite(adj, n, m))
