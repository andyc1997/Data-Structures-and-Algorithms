# python3
from queue import Queue
class DirectedGraph:
    def __init__(self, stock_data):
        self.data = stock_data
        self.n = len(stock_data)
        self.adj_list = [[0]*self.n for _ in range(self.n)]

    def compare(self, i, j):
        status = False
        stock_1, stock_2 = self.data[i], self.data[j]
        if stock_1[0] < stock_2[0]:
            status = True
        if status is False:
            return False
        for (p_1, p_2) in zip(stock_1, stock_2):
            if p_1 >= p_2 and status is True:
                return False
        return True

    def build_graph(self):
        for i in range(self.n):
            for j in range(self.n):
                if i != j:
                    if self.compare(i, j):
                        self.adj_list[i][j] = 1

class Edge: # an edge object
    def __init__(self, u, v, capacity):
        self.u = u # edge from u
        self.v = v # edge to v
        self.capacity = capacity # capacity of edge
        self.flow = 0 # current flow of edge

class FlowGraph: # a network object
    def __init__(self, n):
        self.edges = [] # list of all edges (in both directions) in the graph
        self.graph = [[] for _ in range(n)] #  an adjacency list. index of the list is vertex. self.graph[index] contains the indices of edges in self.edge

    def add_edge(self, from_, to, capacity):
        # a method to add edge to graph
        forward_edge = Edge(from_, to, capacity) # edge for the network
        backward_edge = Edge(to, from_, 0) # edge for the residual network
        self.graph[from_].append(len(self.edges)) # even index for forward edges
        self.edges.append(forward_edge) # add edge to graph
        self.graph[to].append(len(self.edges)) # odd index for backward edges
        self.edges.append(backward_edge) # add edge to graph

    def size(self):
        # a method to calculate the size of graph in terms of vertices
        return len(self.graph)

    def get_ids(self, from_):
        # a method that returns indices in self.edges given with index vertex from_
        return self.graph[from_]

    def get_edge(self, id):
        # a method that returns the edge given the index in self.edges
        return self.edges[id]

    def add_flow(self, id, flow):
        # a method to add flow given indices in self.edges, and subtract the flow in the reversed edge
        self.edges[id].flow += flow
        self.edges[id ^ 1].flow -= flow # In python, id ^ 1 filps the last bit of binary representation of integer "id", e.g. 0001 ^ 1 = 0000 --> 0, 0100 ^ 1 = 0101 ---> 5


def update_residual_graph(graph, X, edges, prev, from_, to):  # update the residual graph after adding flow
    while to != from_:
        graph.add_flow(edges[to], X)  # add the flow X to edges in residual graph
        to = prev[to]
    return graph


def reconstruct_path(graph, from_, to, prev, edges):  # Standard implementation of the shortest path tree
    result = []
    X = 10000 + 1  # It is guaranteed that the capacity is at most 10000
    while to != from_:
        result.append(to)
        X = min(X, graph.get_edge(edges[to]).capacity - graph.get_edge(
            edges[to]).flow)  # find the minimum capacity in the s-t path
        to = prev[to]  # update index
    return [from_] + [u for u in reversed(result)], X, edges, prev


def find_a_path(graph, from_, to):  # Standard algorithm to find source-sink (s-t) path using breadth first search
    dist = [False] * graph.size()  # reachability of each node from the node with index "from_"
    dist[from_] = True  # of course the starting point is reachable to itself
    prev = [None] * graph.size()  # record the parent of each node
    edges = [None] * graph.size()  # record the index of edge in self.edges to reach from u to v
    q = Queue()
    q.put(from_)

    while not q.empty():
        u = q.get()
        for id in graph.get_ids(u):
            to_edge_v = graph.get_edge(id)  # get edges from u to v
            v = to_edge_v.v
            flow = to_edge_v.flow
            capacity = to_edge_v.capacity

            if (dist[v] == False) and (
                    flow < capacity):  # consider unvisited node with flow < capacity as reachable node in BFS
                q.put(v)
                dist[v] = True
                prev[v] = u
                edges[v] = id

    if dist[to] == True:  # if sink is reachable, we reconstruct the path using shortest path tree
        return reconstruct_path(graph, from_, to, prev, edges)
    else:
        return [], 0, [], []


def max_flow(graph, from_, to):  # Standard implementation of Edmonds-Karp algorithm
    flow = 0  # initialize the flow with 0 at the beiginning
    while True:
        path, X, edges, prev = find_a_path(graph, from_, to)  # find a s-t path
        if len(path) == 0:  # If there is no path: return flow
            return flow
        flow += X  # otherwise, add the minimum capacity X in the s-t path to flow and update the residual graph
        graph = update_residual_graph(graph, X, edges, prev, from_, to)
    return flow

class StockCharts:
    def read_data(self):
        n, k = map(int, input().split())
        stock_data = [list(map(int, input().split())) for i in range(n)]
        return stock_data

    def write_response(self, result):
        print(result)

    def min_charts(self, stock_data):
        n = len(stock_data)
        dag = DirectedGraph(stock_data)
        dag.build_graph()
        network = FlowGraph(2*(n + 1))
        source, sink, capacity = 0, 2*n + 1, 1

        for i in range(1, n + 1):
            network.add_edge(source, i, 1)
            for j in range(n + 1, 2*n + 1):
                if dag.adj_list[i - 1][j - (n + 1)] == 1:
                    network.add_edge(i, j, 1)
        for j in range(n + 1, 2*(n + 1)):
            network.add_edge(j, sink, 1)
        return n - max_flow(network, source, sink)
        # for new_stock in stock_data:
        #     added = False
        #     for chart in charts:
        #         fits = True
        #         for stock in chart:
        #             above = all([x > y for x, y in zip(new_stock, stock)])
        #             below = all([x < y for x, y in zip(new_stock, stock)])
        #             if (not above) and (not below):
        #                 fits = False
        #                 break
        #         if fits:
        #             added = True
        #             chart.append(new_stock)
        #             break
        #     if not added:
        #         charts.append([new_stock])

    def solve(self):
        stock_data = self.read_data()
        result = self.min_charts(stock_data)
        self.write_response(result)

if __name__ == '__main__':
    stock_charts = StockCharts()
    stock_charts.solve()
