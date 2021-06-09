# python3
from sys import stdin
import numpy as np
from scipy.optimize import linprog # For solution checking

# Global constant
EPS = 1e-6

class two_phase_simplex:
    # A program for implementing two phase simplex algorithm
    def __init__(self, n, m, A, b, c):
        # Store data
        # Default: max c^{T}x subjected to Ax <= b and x >= 0
        self.A, self.b, self.c = np.array(A), np.array(b), np.array(c)
        
        # Number of decision variable: n
        # Number of linear constraints: m
        self.n, self.m = n, m
        
        # Initial status of the simplex tableau
        self.table = np.hstack([self.A, np.zeros([m, m])])
    
    def check_true_sol(self):
        # Solve using scipy linear programming
        # Default: min c^{T}x subjected to Ax <= b and x >= 0
        true_sol = linprog(-self.c, self.A, self.b, method = 'simplex')
        
        # Check solutions
        if true_sol.status == 0:
            # Bounded solution and print the solution
            print('Bounded solution')
            print(' '.join(list(map(lambda x: '%.18f' % x, true_sol.x))))
            
        elif true_sol.status == 2:
            # No solution
            print('No solution')
            
        elif true_sol.status == 3:
            # Unbounded solution
            print('Infinity')
            
        else:
            # If something else unexpected occurs, print this line
            print('Unexpected')
            
    def check_mix(self):
        # There is a mixed condition if some b_i < 0 in the standard form of LP
        # The iterator: (True for b_i in self.b if b_i < 0) returns True only if some b_i in self.b < 0
        # Otherwise, it does not return anything
        # So, next(iterator, default = False) forces it to return False if none of b_i < 0
        return next((True for b_i in self.b if b_i < 0), False)

    def create_slack(self):
        # Create slack variables for each inequality constraint
        # (x_1, ..., x_n, w_1, ..., w_m) --> (x_1, ..., x_n, x_{n+1}, ..., x_{n+m}) 
        # The tableau = [A, I], I is the identity matrix
        for i in range(self.m):
            self.table[i][self.n + i] = 1
    
    def create_artficial(self):
        # Create artificial variables for some inequality constraint
        for i in range(self.m):
            # If b_i < 0 in the standard form of LP, we need an artificial variable for the i-th constraint
            if self.b[i] < 0:
                # Artificial variable for i-th constraint
                new_col = np.zeros([self.m, 1])
                new_col[i] = -1
                
                # Update
                self.table = np.hstack([self.table, new_col])
    
def allocate_ads(n, m, A, b, c):
    simplex = two_phase_simplex(n, m, A, b, c)
    
    simplex.create_slack()
    if simplex.check_mix():
        simplex.create_artficial()
    
    
    # Debug printing
    print(simplex.A, '\n')
    print(simplex.table, '\n')
    print(simplex.check_true_sol())
    return 0, []

m, n = 3, 2  # list(map(int, stdin.readline().split()))
A = [[-1, -1], [1, 0], [0, 1]]
# for i in range(n):
#   A += [list(map(int, stdin.readline().split()))]
b = [-1, 2, 2]  # list(map(int, stdin.readline().split()))
c = [-1, 2]  # list(map(int, stdin.readline().split()))
anst, ansx = allocate_ads(n, m, A, b, c)

if anst == -1:
    print("No solution")
if anst == 0:
    print("Bounded solution")
    print(' '.join(list(map(lambda x: '%.18f' % x, ansx))))
if anst == 1:
    print("Infinity")
