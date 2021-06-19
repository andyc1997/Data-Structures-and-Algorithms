# python3

# Set recursion limits
import sys
import threading
import queue

sys.setrecursionlimit(10**7)
threading.stack_size(2**26)

#%%
class strongly_connected_components:
    def __init__(self, adj, radj):
        # Adjacency list and reversed adjacency list
        self.adj = adj
        self.radj = radj
        self.n = len(radj)

        self.lifo_q = queue.LifoQueue()

        self.count = 0
        self.scc = list()
        self.num2scc = [None] * self.n

    def explore(self, v, visit):
        visit[v] = 1
        for w in self.radj[v]:
            if visit[w] == 0:
                self.explore(w, visit)
        self.lifo_q.put(v)

    def dfs(self):
        visit = [0] * self.n
        for u in range(self.n):
            if visit[u] == 0:
                self.explore(u, visit)

    def find_scc_members(self, v, visit, order):
        visit[v] = 1
        order.append(v)
        self.num2scc[v] = self.count
        for w in self.adj[v]:
            if visit[w] == 0:
                self.find_scc_members(w, visit, order)

    def assign(self):
        visit = [0] * self.n
        while self.lifo_q.qsize() > 0:
            u = self.lifo_q.get()
            if visit[u] == 0:
                order = list()
                self.find_scc_members(u, visit, order)
                self.scc.append(order)
                self.count += 1

#%%
class implication_graph:
    def __init__(self, n, clauses):
        # For each variable x, introduce two vertices
        self.n = n 
        self.adj = [set() for _ in range(2*n)]
        self.radj = [set() for _ in range(2*n)]
        self.clauses = clauses
    
    @staticmethod
    def get_node_index(left, right, n):
        if left > 0:
            if right > 0:
                return left - 1, right - 1
            else:
                return left - 1, n - 1 - right
        else:
            if right > 0:
                return n - 1 - left, right - 1
            else:
                return n - 1 - left, n - 1 - right
    
    def add_edges(self):
        left, right = None, None
        # Loop through each clauses
        for clause in self.clauses:
            if len(clause) > 1:
                left, right = clause
            else:
                left, right = clause[0], clause[0]
                
            # Add ~l[1] -> l[2] 
            _from, _to = self.get_node_index(-left, right, self.n)
            self.adj[_from].add(_to)
            self.radj[_to].add(_from)
            
            if left != right:
                # Add ~l[2] -> l[1]
                _from, _to = self.get_node_index(-right, left, self.n)
                self.adj[_from].add(_to)
                self.radj[_to].add(_from)
                
            
#%%

# Read input
# n, m = 4, 5
# clauses = [[1, 2], [2, 3], [3, 4], [-1, -3], [-2, -4]]

# n, m = 3, 3
# clauses = [[1, -3], [-1, 2], [-2, -3]]
    
# n, m = 10000, 10000
# clauses = [[1, 1]]
    
# n, m = 2, 4
# clauses = [[1, 2], [-1, 2], [-2, 1], [-1, -2]]

# n, m = 2, 4
# clauses = [[1, 2], [-1, 2], [2, -1], [-1, -2]]

# n, m = 8, 12 
# clauses = [[1, 4], [-2, 5], [3, 7], [2, -5], [-8, -2], [3, -1], [4, -3], [5, -4], 
#             [-3, -7], [6, 7], [1, 7], [-7, -1]]

# n, m = 2, 4
# clauses = [[1, 2], [-1, 2], [2, -1], [-1, -2]]

# n, m = 1, 2
# clauses = [[-1], [1]]

n, m = map(int, input().split())
clauses = [ list(map(int, input().split())) for i in range(m)]

def is_sat():  
    
    # Build implication graph
    imgraph = implication_graph(n, clauses)
    imgraph.add_edges()
    
    # Find strongly connected components
    scc = strongly_connected_components(imgraph.adj, imgraph.radj)
    scc.dfs()
    scc.assign()

    for i in range(n):
        # Get literal x[i] and ~x[i]
        left, right = imgraph.get_node_index(i + 1, -(i + 1), n)

        # If x[i] and ~x[i] are lying in the same SCC: return None
        if scc.num2scc[left] == scc.num2scc[right]:
            return None

    assign_literal = [None for _ in range(2 * n)]

    for group in scc.scc:
        for u in group:
            if assign_literal[u] == None:
                assign_literal[u] = True
                if u >= n:
                    assign_literal[u - n] = False
                else:
                    assign_literal[u + n] = False

    return assign_literal

#%%
def isSatisfiable(n, clauses):
    for mask in range(1<<n):
        result = [ (mask >> i) & 1 for i in range(n) ]
        formulaIsSatisfied = True
        for clause in clauses:
            clauseIsSatisfied = False
            if result[abs(clause[0]) - 1] == (clause[0] < 0):
                clauseIsSatisfied = True
            if result[abs(clause[1]) - 1] == (clause[1] < 0):
                clauseIsSatisfied = True
            if not clauseIsSatisfied:
                formulaIsSatisfied = False
                break
        if formulaIsSatisfied:
            return result
    return None

def main():
    result = is_sat()
    if result is None:
        print("UNSATISFIABLE")
    else:
        print("SATISFIABLE");
        print(" ".join(str(- i - 1 if not result[i] else i + 1) for i in range(n)))

threading.Thread(target=main).start()
