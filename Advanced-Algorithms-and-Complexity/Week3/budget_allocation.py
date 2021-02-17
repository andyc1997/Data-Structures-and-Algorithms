# python3
from sys import stdin
from itertools import product

class Clause:
    # A standard class of clause
    def __init__(self, numvar):
        # initialize the clause with an empty list
        self.clause = list()
        self.m = 0
        self.n = numvar

    def update_count(self):
        self.m = len(self.clause)

    def empty_clause(self):
        # A method to determine if the clause is empty
        return len(self.clause) == 0

    def print_clause(self):
        # A method for printing clause to SAT solver
        print(str(self.m) + ' ' + str(self.n))
        for clause in self.clause:
            clause.append(0)
            print(' '.join(map(str, clause)))

def get_nonzero(arr):
    # Find at most 3 nonzero coefficients in each inequality
    results = list()
    for i, coef in enumerate(arr):
        if coef != 0:
            results.append((i, coef))
    return len(results), results

def build_truthtable(arr, size, const, C):
    table = list(product([False, True], repeat = size))
    for t in table:
        temp = list(zip(t, arr))
        s = sum([b * coef[1] for (b, coef) in temp])
        if s > const:
            c = [((-1) ** b) * (coef[0] + 1) for (b, coef) in temp]
            C.clause.append(c)

n, m = list(map(int, stdin.readline().split()))
A = []
for i in range(n):
    A += [list(map(int, stdin.readline().split()))]
b = list(map(int, stdin.readline().split()))
C = Clause(m)

for i, coef in enumerate(A):
    size, nonzero_coef = get_nonzero(coef)
    if size == 0:
        continue
    build_truthtable(nonzero_coef, size, b[i], C)

if C.empty_clause():
    C.clause.append([1, -1])
C.update_count()
C.print_clause()