# python3
from sys import stdin
import numpy as np
from scipy.optimize import linprog # For solution checking

# Global constant
EPS = 1e-9

class pivot:
    def __init__(self, r = None, c = None):
        self.r, self.c = r, c

class two_phase_simplex:
    # A program for implementing two phase simplex algorithm
    def __init__(self, n, m, A, b, c):
        # Store data
        # Default: max c^{T}x subjected to Ax <= b and x >= 0
        self.A, self.b, self.c = np.array(A, dtype = np.float64), np.array(b, dtype = np.float64), np.array(c, dtype = np.float64)
        
        # Number of decision variable: n
        # Number of linear constraints: m
        self.n, self.m = n, m
        
        # Initial status of the simplex tableau
        self.table = np.hstack([self.A, np.zeros([m, m])])
        
        # Initial status of the auxiliary objective function
        self.auxiliary = np.zeros((m + n, ))
        
        # Row index for auxiliary problem
        self.aux_rows = np.array([])
        self.ratio = None
        
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

    def get_pivot_col(self):
        # Return the pivotal column
        # The column with the index that objective function is associated with the largest positive coefficient
        return np.argmax(self.table[0])
    
    @staticmethod
    def get_pivot_row(ratio):
        # Return the pivotal row
        # The row with the smallest ratio b/a
        return np.argmax(-ratio[1:]) + 1
    
    def get_ratio(self, c):
        ratio = []
        for i, j in zip(self.b, self.table[:, c]):
            if j == 0:
                if i == 0:
                    ratio.append(0)
                else:
                    ratio.append(np.float('inf'))
            else:
                ratio.append(i/j)
        return np.array(ratio)
    
    def check_opt(self):
        # Check if all elements are positive in the objective function
        return next((False for c_i in self.table[0, :(self.m + self.n)] if c_i < 0), True)

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
                self.aux_rows = np.append(self.aux_rows, i + 1)
                self.table = np.hstack([self.table, new_col])
                self.auxiliary = np.append(self.auxiliary, -1)
                
        # Augment original table and vector for the objective function
        self.table = np.insert(self.table, 0, self.auxiliary, axis = 0)
        self.b = np.insert(self.b, 0, 0)
        self.ratio = np.zeros((self.b.shape[0], ))
    
    def trim_tableau(self):
        self.table = self.table[:, :(self.m + self.n)]
        self.table[0, :self.n] = self.c
    
    def gauss_jordan_elimination(self, p):
        # Implement Gauss-Jordan elimination given pivot element
        # Rescale by pivot factor
        scale_factor = self.table[p.r, p.c]
        self.table[p.r, :] /= scale_factor
        self.b[p.r] /= scale_factor
        # Eliminate all above pivot row
        # The first row is objective function, don't eliminate it
        i = p.r
        while i > 0:
            i -= 1
            multipler = self.table[i, p.c]
            self.table[i, :] -= multipler*self.table[p.r, :]
            self.b[i] -= multipler*self.b[p.r]
            
        # Eliminate all below pivot row
        i = p.r
        while i < self.m:
            i += 1
            multipler = self.table[i, p.c]
            self.table[i, :] -= multipler*self.table[p.r, :]
            self.b[i] -= multipler*self.b[p.r]
            
    def phase_I(self):
        # Eliminate artificial variable from the auxiliary objective function
        for i in self.aux_rows:
            self.table[0] -= self.table[int(i)]
            self.b[0] -= self.b[int(i)]
        
        while self.check_opt() == False:
            c = self.get_pivot_col()           
            ratio = self.get_ratio(c)
            r = self.get_pivot_row(ratio)
            p = pivot(r, c)
            self.gauss_jordan_elimination(p)
            
        # Feaibility condition
        
        # Discard artificial variables    
        self.trim_tableau()
        
        # Express the objective as nonbasic variables
        
    def phase_II(self):
        pass
    
def allocate_ads(n, m, A, b, c):
    simplex = two_phase_simplex(n, m, A, b, c)
    simplex.check_true_sol()
    
    simplex.create_slack()
    if simplex.check_mix():
        simplex.create_artficial()
        simplex.phase_I()
        
    # Debug printing
    # print(simplex.A, '\n')
    print(simplex.table, '\n', simplex.b)
    return 0, []

m, n = 3, 2  # list(map(int, stdin.readline().split()))
A = [[-3, -2], [-1, -4], [1, 1]]
# for i in range(n):
#   A += [list(map(int, stdin.readline().split()))]
b = [-3, -4, 5]  # list(map(int, stdin.readline().split()))
c = [5, 8]  # list(map(int, stdin.readline().split()))
anst, ansx = allocate_ads(n, m, A, b, c)

# if anst == -1:
#     print("No solution")
# if anst == 0:
#     print("Bounded solution")
#     print(' '.join(list(map(lambda x: '%.18f' % x, ansx))))
# if anst == 1:
#     print("Infinity")
