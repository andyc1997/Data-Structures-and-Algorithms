#Uses python3

import sys

sys.setrecursionlimit(200000)

def previsit(v, pre, clock):
    pre[v] = clock
    clock += 1
    return clock

def postvisit(v, post, clock):
    post[v] = clock
    clock += 1
    return clock

def explore(v, visit, radj, pre, post, clock, stack):
    visit[v] = 1
    clock = previsit(v, pre, clock)
    for w in radj[v]:
        if visit[w] == 0:
            clock = explore(w, visit, radj, pre, post, clock, stack)
    stack.append(v)
    clock = postvisit(v, post, clock)
    return clock

def simple_explore(v, visit, adj):
    visit[v] = 1
    for w in adj[v]:
        if visit[w] == 0:
            simple_explore(w, visit, adj)

def dfs(radj):
    n = len(radj)
    visit = [0] * n
    clock = 0
    pre, post = [0] * n, [0] * n
    stack = []
    for v in range(n):
        if visit[v] == 0:
            clock = explore(v, visit, radj, pre, post, clock, stack)
    return stack
            
def number_of_strongly_connected_components(adj, radj):
    result = 0
    #write your code here
    stack = dfs(radj)
    n = len(stack)
    visit = [0] * n
    for i in range(n):
        v = stack.pop()
        if visit[v] == 0:
            simple_explore(v, visit, adj)
            result += 1
    return result

if __name__ == '__main__':
    input = sys.stdin.read()
    data = list(map(int, input.split()))
    #data = [4, 4, 1, 2, 4, 1, 2, 3, 3, 1]
    n, m = data[0:2]
    data = data[2:]
    edges = list(zip(data[0:(2 * m):2], data[1:(2 * m):2]))
    adj = [[] for _ in range(n)]
    radj = [[] for _ in range(n)]
    for (a, b) in edges:
        adj[a - 1].append(b - 1)
        radj[b - 1].append(a - 1)
    print(number_of_strongly_connected_components(adj, radj))
