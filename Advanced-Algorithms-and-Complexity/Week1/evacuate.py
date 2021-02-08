# python3
# coding: utf-8

# In[1]:


from queue import Queue


# In[2]:


class Edge:

    def __init__(self, u, v, capacity):
        self.u = u
        self.v = v
        self.capacity = capacity
        self.flow = 0

# This class implements a bit unusual scheme for storing edges of the graph,
# in order to retrieve the backward edge for a given edge quickly.
class FlowGraph:

    def __init__(self, n):
        # List of all - forward and backward - edges
        self.edges = []
        # These adjacency lists store only indices of edges in the edges list
        self.graph = [[] for _ in range(n)]

    def add_edge(self, from_, to, capacity):
        # Note that we first append a forward edge and then a backward edge,
        # so all forward edges are stored at even indices (starting from 0),
        # whereas backward edges are stored at odd indices.
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
        # To get a backward edge for a true forward edge (i.e id is even), we should get id + 1
        # due to the described above scheme. On the other hand, when we have to get a "backward"
        # edge for a backward edge (i.e. get a forward edge for backward - id is odd), id - 1
        # should be taken.
        #
        # It turns out that id ^ 1 works for both cases. Think this through!
        self.edges[id].flow += flow
        self.edges[id ^ 1].flow -= flow


# In[3]:


def read_data():
    vertex_count, edge_count = map(int, input().split())
    graph = FlowGraph(vertex_count)
    for _ in range(edge_count):
        u, v, capacity = map(int, input().split())
        graph.add_edge(u - 1, v - 1, capacity)
    return graph


# In[4]:


def read_data_path(path):
    # Read text data
    f = open(path, 'r')
    count = 0
    graph = None
    for line in f:
        if count == 0:
            vertex_count, edge_count = map(int, line.split())
            graph = FlowGraph(vertex_count)
        else:
            u, v, capacity = map(int, line.split())
            graph.add_edge(u - 1, v - 1, capacity)
        count += 1
    return graph


# In[5]:


def read_data_test(n, m, array):
    # Read hardcoded data
    vertex_count, edge_count = n, m
    graph = FlowGraph(vertex_count)
    for i in range(edge_count):
        u, v, capacity = array[(3 * i):(3 * (i + 1))]
        graph.add_edge(u - 1, v - 1, capacity)
    return graph


# In[6]:


def update_residual_graph(graph, X, edges, prev, from_, to):
    while to != from_:
        graph.add_flow(edges[to], X)
        to = prev[to]
    return graph


# In[7]:


def reconstruct_path(graph, from_, to, prev, edges):
    result = []
    X = 10000 + 1
    while to != from_:
        result.append(to)
        X = min(X, graph.get_edge(edges[to]).capacity - graph.get_edge(edges[to]).flow)
        to = prev[to]
    return [from_] + [u for u in reversed(result)], X, edges, prev


# In[8]:


def find_a_path(graph, from_, to):
    # initializing distance array
    dist = [False] * graph.size()
    dist[from_] = True
    # initialize previous array
    prev = [None] * graph.size()
    # initialize edges array
    edges = [None] * graph.size()
    # a queue containing vertices
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
    # Two cases: reachable and non-reachable
    if dist[to] == True:
        return reconstruct_path(graph, from_, to, prev, edges)
    else:
        return [], 0, [], []


# In[9]:


def max_flow(graph, from_, to):
    flow = 0
    # your code goes here
    while True:
        path, X, edges, prev = find_a_path(graph, from_, to)
        if len(path) == 0:
            return flow
        flow += X
        graph = update_residual_graph(graph, X, edges, prev, from_, to)
    return flow


# In[12]:


if __name__ == '__main__':
    #graph = read_data_test(5, 7, [1, 2, 2, 2, 5, 5, 1, 3, 6, 3, 4, 2, 4, 5, 1, 3, 2, 3, 2, 4, 1])
    #graph = read_data_test(4, 5, [1, 2, 10000, 1, 3, 10000, 2, 3, 1, 3, 4, 10000, 2, 4, 10000])
    #graph = read_data_test(6, 7, [1, 2, 1, 1, 3, 1, 2, 4, 1, 2, 5, 1, 3, 4, 1, 4, 6, 1, 5, 6, 1])
    #graph = read_data_path(r'C:\Users\user\Documents\Coursera (2020)\Advanced Algorithms and Complexity\Programming-Assignment-1\mywork\failed_case\10.txt')
    graph = read_data()
    print(max_flow(graph, 0, graph.size() - 1))

