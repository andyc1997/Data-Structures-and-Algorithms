# python3
# -*- coding: utf-8 -*-
import itertools

#%% Default mapping 
n, m = map(int, input().split())
edges = [ list(map(int, input().split())) for i in range(m) ]

#%% Test case 1
# n, m = [3, 3]
# edges = [[1, 2], [2, 3], [1, 3]]

#%% Test case 2
# n, m = [4, 6]
# edges = [[1, 2], [1, 3], [1, 4], [2, 3], [2, 4], [3, 4]]

#%% Test case 3
# n, m = [5, 7]
# edges = [[1, 2], [1, 3], [1, 4], [1, 5], [2, 3], [3, 4], [4, 5]]

#%% Main program
vertex = range(1, n + 1)
color = range(1, 4)
naming_scheme = [[v + (c - 1)*max(vertex) for v in vertex] for c in color]

def empty_clause():
    return []

def print_clause(clause):
    for c in clause:
        c.append(0)
        print(" ".join(map(str, c)))

def varnum(i, j, naming_scheme = naming_scheme):
    # i: the i-th vertex, j: color j
    # variable x[i][j] means i-th vertex has color j
    # range of i: max 500
    # 1 <= varnum <= 3000, use 10*i + j when there is no constraint on varnum.
    return naming_scheme[j - 1][i - 1]

def create_adj_list(edges, n):
    # build an adjacency list
    adj_list = [set() for i in range(n)]
    for e in edges:
        adj_list[e[0] - 1].add(e[1] - 1)
        # adj_list[e[1] - 1].add(e[0] - 1)
    return adj_list

def printEquisatisfiableSatFormula():
    # Intialize variables
    adj_list = create_adj_list(edges, n)
    total_clause = empty_clause()
    
    # Trivial case
    # No edge
    if m == 0:
        total_clause = [[1]]
    
    else:
        # Exactly one vertex is colored and at least one vertex is colored
        clause = empty_clause() # Temporary clauses
        for v in vertex:
            literal = []
            for c in color:
                var = varnum(v, c)
                literal.append(var)
            clause.append(literal)
            for c in color:
                literal_temp = literal.copy()
                literal_temp.pop(c - 1)
                literal_temp = list(map(lambda x: -x, literal_temp))
                clause.append(literal_temp)
        total_clause += clause # Append to total clauses
        # print_clause(total_clause)
        
        # Adjacent vertices must be in different color
        clause = empty_clause() # Temporary clauses
        for (v, c) in itertools.product(vertex, color):
            literal = []
            first_pair = -varnum(v, c)
            if len(adj_list[v - 1]) > 0:
                for w in adj_list[v - 1]:
                    next_pair = -varnum(w + 1, c)
                    clause.append([first_pair, next_pair])
        total_clause += clause
    print('{} {}\n'.format(len(total_clause), 3000))
    print_clause(total_clause)
    
#%% Write output to .txt file for minisat, uncomment if necessary
    # with open('tmp.txt', 'w') as f:
    #     f.write('p cnf {} {}\n'.format(120000, len(total_clause)))
    #     for c in total_clause:
    #         c.append(0)
    #         f.write(" ".join(map(str, c)) + '\n')
    
printEquisatisfiableSatFormula()
