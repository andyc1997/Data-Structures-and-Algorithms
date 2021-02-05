#Uses python3

import sys

def previsit(v, pre, clock):
    pre[v] = clock
    clock += 1
    return clock

def postvisit(v, post, clock):
    post[v] = clock
    clock += 1
    return clock

def explore(v, visit, adj, pre, post, clock, stack):
    visit[v] = 1
    clock = previsit(v, pre, clock)
    for w in adj[v]:
        if visit[w] == 0:
            clock = explore(w, visit, adj, pre, post, clock, stack)
    stack.append(v)
    clock = postvisit(v, post, clock)
    return clock

def dfs(adj):
    #write your code here
    n, clock = len(adj), 0
    pre, post, visit, stack = [0] * n, [0] * n, [0] * n, []
    for v in range(n):
        if visit[v] == 0:
            clock = explore(v, visit, adj, pre, post, clock, stack)
    return stack

def toposort(adj):
    #write your code here
    stack = dfs(adj)
    sorted_list = []
    n = len(stack)
    for i in range(n):
        sorted_list.append(stack.pop())
    return sorted_list

if __name__ == '__main__':
    input = sys.stdin.read()
    data = list(map(int, input.split()))
    n, m = data[0:2]
    data = data[2:]
    edges = list(zip(data[0:(2 * m):2], data[1:(2 * m):2]))
    adj = [[] for _ in range(n)]
    for (a, b) in edges:
        adj[a - 1].append(b - 1)
    order = toposort(adj)
    for x in order:
        print(x + 1, end=' ')

