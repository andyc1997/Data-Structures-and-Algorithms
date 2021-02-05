#Uses python3

import sys

def explore(v, adj, visit):
    # Explore vertex
    visit[v] += 1
    for w in adj[v]:
        if visit[w] < 2:
            explore(w, adj, visit)
    return visit

def reach(adj, x, y):
    #write your code here
    visit = len(adj) * [0]
    result = explore(x, adj, visit)
    if result[y] > 1:
        return 1
    return 0

def acyclic(adj):
    for i in range(len(adj)):
        bool_cycle = reach(adj, i, i)
        if bool_cycle == 1:
            return 1
    return 0

if __name__ == '__main__':
    input = sys.stdin.read()
    #data = [5, 7, 1, 2, 2, 3, 1, 3, 3, 4, 1, 4,2, 5, 3, 5]#
    data = list(map(int, input.split()))
    #data = [4, 4, 1, 2, 4, 1, 2, 3, 3, 1]
    n, m = data[0:2]
    data = data[2:]
    edges = list(zip(data[0:(2 * m):2], data[1:(2 * m):2]))
    adj = [[] for _ in range(n)]
    for (a, b) in edges:
        adj[a - 1].append(b - 1)
    print(acyclic(adj))
