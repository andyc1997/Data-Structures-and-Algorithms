# python3
from queue import Queue


# In[22]:


class Edge:

    def __init__(self, u, v, capacity):
        self.u = u
        self.v = v
        self.capacity = capacity
        self.flow = 0


# In[23]:


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


# In[24]:


def construct_graph(n, m, adj_matrix):
    fix_capacity = 1
    vertex_count = n + m + 2
    graph = FlowGraph(vertex_count)
    # Construct source, indexed by 0
    source = 0
    # Edge between source and flights, indexed by 1, ..., n
    for flight in range(1, n + 1):
        graph.add_edge(source, flight, fix_capacity)
    # Edge between flights and crew, indexed by n + 1, ..., n + m + 1
    for i in range(n):
        for j in range(m):
            if adj_matrix[i][j] == 1:
                flight = i + 1
                crew = n + j + 1
                graph.add_edge(flight, crew, fix_capacity)
    # Edge between crew and sink, indexed by n + m + 2
    sink = n + m + 1
    for crew in range(n + 1, n + m + 2):
        graph.add_edge(crew, sink, fix_capacity)
    return graph


# In[25]:


def update_residual_graph(graph, X, edges, prev, from_, to):
    while to != from_:
        graph.add_flow(edges[to], X)
        to = prev[to]
    return graph


# In[26]:


def reconstruct_path(graph, from_, to, prev, edges):
    result = []
    X = 1 + 1
    while to != from_:
        result.append(to)
        X = min(X, graph.get_edge(edges[to]).capacity - graph.get_edge(edges[to]).flow)
        to = prev[to]
    return [from_] + [u for u in reversed(result)], X, edges, prev


# In[27]:


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


# In[28]:


def update_matching(matching, path, n):
    flight, crew = path[1], path[2] - (n + 1)
    matching[flight - 1] = crew
    return matching


# In[29]:


class MaxMatching:
    def read_data(self):
        #---------------------------------------------------------------------
        n, m = map(int, input().split())
        adj_matrix = [list(map(int, input().split())) for i in range(n)]
        #---------------------------------------------------------------------
        # n, m = 3, 4
        # adj_matrix = [[1, 1, 0, 1], [0, 1, 0, 0], [0, 0, 0, 0]]
        return adj_matrix

    def write_response(self, matching):
        line = [str(-1 if x == -1 else x + 1) for x in matching]
        print(' '.join(line))

    def find_matching(self, adj_matrix):
        # Replace this code with an algorithm that finds the maximum
        # matching correctly in all cases.
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


# In[30]:


if __name__ == '__main__':
    max_matching = MaxMatching()
    max_matching.solve()

