#Uses python3

import sys

def explore(v, adj, visit):
    # Explore vertex
    visit[v] = 1
    for w in adj[v]:
        if visit[w] == 0:
            explore(w, adj, visit)
    return visit

def number_of_components(adj):
    result = 0
    #write your code here
    visit = len(adj) * [0]
    for v in range(len(adj)):
        if visit[v] == 0:
            visit = explore(v, adj, visit)
            result += 1
    return result

if __name__ == '__main__':
    input = sys.stdin.read()
    data = list(map(int, input.split()))
    n, m = data[0:2]
    data = data[2:]
    edges = list(zip(data[0:(2 * m):2], data[1:(2 * m):2]))
    adj = [[] for _ in range(n)]
    for (a, b) in edges:
        adj[a - 1].append(b - 1)
        adj[b - 1].append(a - 1)
    print(number_of_components(adj))
