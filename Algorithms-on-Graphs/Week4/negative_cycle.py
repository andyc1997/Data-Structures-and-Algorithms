#Uses python3

import sys


def negative_cycle(adj, cost):
    #write your code here
    n = len(adj)
    inf = (10 ** 3) * n + 1
    dist = [inf] * n
    
    for j in range(n): # Loop |V| - 1 times
        for u in range(n):
            if len(adj[u]) != 0:
                for i in range(len(adj[u])): # Loop |E| times
                    v = adj[u][i]
                    if dist[v] > dist[u] + cost[u][i]:
                        dist[v] = dist[u] + cost[u][i]
                        if (j == n - 1):
                            return 1
    return 0


if __name__ == '__main__':
    input = sys.stdin.read()
    data = list(map(int, input.split()))
    #data = [4, 4, 1, 2, -5, 4, 1, 2, 2, 3, 2, 3, 1, 1]
    n, m = data[0:2]
    data = data[2:]
    edges = list(zip(zip(data[0:(3 * m):3], data[1:(3 * m):3]), data[2:(3 * m):3]))
    data = data[3 * m:]
    adj = [[] for _ in range(n)]
    cost = [[] for _ in range(n)]
    for ((a, b), w) in edges:
        adj[a - 1].append(b - 1)
        cost[a - 1].append(w)
    print(negative_cycle(adj, cost))
