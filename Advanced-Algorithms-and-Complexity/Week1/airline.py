# python3
from queue import Queue
# Task. The airline offers a bunch of flights and has a set of crews that can work on those flights. However,
# the flights are starting in different cities and at different times, so only some of the crews are able to
# work on a particular flight. You are given the pairs of flights and associated crews that can work on
# those flights. You need to assign crews to as many flights as possible and output all the assignments.
# Input Format. The first line of the input contains integers n and m — the number of flights and the number
# of crews respectively. Each of the next n lines contains 𝑚 binary integers (0 or 1). If the j-th integer
# in the i-th line is 1, then the crew number j can work on the flight number i, and if it is 0, then it cannot.
# Output Format. Output 𝑛 integers — for each flight, output the 1-based index of the crew assigned to
# this flight. If no crew is assigned to a flight, output −1 as the index of the crew corresponding to it.
# All the positive indices in the output must be between 1 and m, and they must be pairwise different,
# but you can output any number of −1’s. If there are several assignments with the maximum possible
# number of flights having a crew assigned, output any of them.

class Edge: # see evacuation.py
    def __init__(self, u, v, capacity):
        self.u = u
        self.v = v
        self.capacity = capacity
        self.flow = 0

class FlowGraph: # see evacuation.py
    def __init__(self, n):
        self.edges = []
        self.graph = [[] for _ in range(n)]

    def add_edge(self, from_, to, capacity):
        forward_edge = Edge(from_, to, capacity)
        backward_edge = Edge(to, from_, 0)
        self.graph[from_].append(len(self.edges))
        self.edges.append(forward_edge)
        self.graph[to].append(len(self.edges))
        self.edges.append(backward_edge)

    def size(self):
        return len(self.graph)

    def get_ids(self, from_):
        return self.graph[from_]

    def get_edge(self, id):
        return self.edges[id]

    def add_flow(self, id, flow):
        self.edges[id].flow += flow
        self.edges[id ^ 1].flow -= flow

def construct_graph(n, m, adj_matrix):
    fix_capacity = 1
    vertex_count = n + m + 2
    graph = FlowGraph(vertex_count)
    source = 0
    
    for flight in range(1, n + 1):
        graph.add_edge(source, flight, fix_capacity)

    for i in range(n):
        for j in range(m):
            if adj_matrix[i][j] == 1:
                flight = i + 1
                crew = n + j + 1
                graph.add_edge(flight, crew, fix_capacity)

    sink = n + m + 1
    for crew in range(n + 1, n + m + 2):
        graph.add_edge(crew, sink, fix_capacity)
    return graph

def update_residual_graph(graph, X, edges, prev, from_, to): # see evacuation.py
    while to != from_:
        graph.add_flow(edges[to], X)
        to = prev[to]
    return graph

def reconstruct_path(graph, from_, to, prev, edges): # see evacuation.py
    result = []
    X = 1 + 1
    while to != from_:
        result.append(to)
        X = min(X, graph.get_edge(edges[to]).capacity - graph.get_edge(edges[to]).flow)
        to = prev[to]
    return [from_] + [u for u in reversed(result)], X, edges, prev

def find_a_path(graph, from_, to): # see evacuation.py
    dist = [False] * graph.size()
    dist[from_] = True
    prev = [None] * graph.size()
    edges = [None] * graph.size()

    q = Queue()
    q.put(from_)
    while not q.empty():
        u = q.get()
        
        for id in graph.get_ids(u):
            to_edge_v = graph.get_edge(id)
            v = to_edge_v.v
            flow = to_edge_v.flow
            capacity = to_edge_v.capacity
            
            if (dist[v] == False) and (flow < capacity):
                q.put(v)
                dist[v] = True
                prev[v] = u
                edges[v] = id

    if dist[to] == True:
        return reconstruct_path(graph, from_, to, prev, edges)
    else:
        return [], 0, [], []

def update_matching(matching, path, n):
    flight, crew = path[1], path[2] - (n + 1)
    matching[flight - 1] = crew
    return matching

class MaxMatching:
    def read_data(self):
        n, m = map(int, input().split())
        adj_matrix = [list(map(int, input().split())) for i in range(n)]
        return adj_matrix

    def write_response(self, matching):
        line = [str(-1 if x == -1 else x + 1) for x in matching]
        print(' '.join(line))

    def find_matching(self, adj_matrix):
        n, m = len(adj_matrix), len(adj_matrix[0])
        from_, to = 0, n + m + 1
        matching = [-1] * n
        graph = construct_graph(n, m, adj_matrix)
        flow = 0
        
        while True:
            path, X, edges, prev = find_a_path(graph, from_, to)
            if len(path) == 0:
                return matching
            flow += X
            matching = update_matching(matching, path, n)
            graph = update_residual_graph(graph, X, edges, prev, from_, to)

    def solve(self):
        adj_matrix = self.read_data()
        matching = self.find_matching(adj_matrix)
        self.write_response(matching)

if __name__ == '__main__':
    max_matching = MaxMatching()
    max_matching.solve()

