# python3
from sys import stdin
import itertools
EPS = 1e-3
PRECISION = 20


# In[2]:


class Equation:
    def __init__(self, a_, b_):
        self.a_ = a_.copy()
        self.b_ = b_.copy()
        
class Position:
    def __init__(self, column, row):
        self.column = column
        self.row = row


# In[3]:


def SelectPivotElement(a_, b_, used_rows, used_columns):
    # This algorithm selects the first free element.
    # You'll need to improve it to pass the problem.
    pivot_element = Position(0, 0)
    while used_rows[pivot_element.row]:
        pivot_element.row += 1
    while used_columns[pivot_element.column]:
        pivot_element.column += 1
        
    max_row = pivot_element.row
    if a_[pivot_element.row][pivot_element.column] == 0:
        for below_row in range(pivot_element.row + 1, len(a_)):
            if abs(a_[below_row][pivot_element.column]) > abs(a_[max_row][pivot_element.column]):
                max_row = below_row
        a_[pivot_element.row], a_[max_row] = a_[max_row], a_[pivot_element.row]
        b_[pivot_element.row], b_[max_row] = b_[max_row], b_[pivot_element.row]
    return pivot_element

def SwapLines(a_, b_, used_rows, pivot_element):
    a_[pivot_element.column], a_[pivot_element.row] = a_[pivot_element.row], a_[pivot_element.column]
    b_[pivot_element.column], b_[pivot_element.row] = b_[pivot_element.row], b_[pivot_element.column]
    used_rows[pivot_element.column], used_rows[pivot_element.row] = used_rows[pivot_element.row], used_rows[pivot_element.column]
    pivot_element.row = pivot_element.column
    
def ProcessPivotElement(a_, b_, pivot_element):
    # Write your code here
    # Scale elements in pivot row with pivot element = 1
    scaling_factor = a_[pivot_element.row][pivot_element.column]
    a_[pivot_element.row] = list(map(lambda x: x / scaling_factor, a_[pivot_element.row]))
    b_[pivot_element.row] /= scaling_factor
    # All zeros below pivot element
    size = len(a_)
    if pivot_element.row + 1 < size:
        for non_pivot in range(pivot_element.row + 1, size):
            multiple = a_[non_pivot][pivot_element.column]
            for column in range(pivot_element.column, len(a_[0])):
                a_[non_pivot][column] -= multiple * a_[pivot_element.row][column]
            b_[non_pivot] -= multiple * b_[pivot_element.row]
    # All zeros above pivot element
    if pivot_element.row > 0:
        for above_pivot in range(0, pivot_element.row):
            multiple = a_[above_pivot][pivot_element.column]
            for column in range(pivot_element.column, len(a_[0])):
                a_[above_pivot][column] -= multiple * a_[pivot_element.row][column]
            b_[above_pivot] -= multiple * b_[pivot_element.row]
    pass

def MarkPivotElementUsed(pivot_element, used_rows, used_columns):
    used_rows[pivot_element.row] = True
    used_columns[pivot_element.column] = True


# In[4]:


def SolveEquation(equation):
    a_ = equation.a_.copy()
    b_ = equation.b_.copy()
    size = len(a_)
    used_columns = [False] * size
    used_rows = [False] * size
    for step in range(size):
        pivot_element = SelectPivotElement(a_, b_, used_rows, used_columns)
        if a_[pivot_element.row][pivot_element.column] == 0:
            return False
        SwapLines(a_, b_, used_rows, pivot_element)
        ProcessPivotElement(a_, b_, pivot_element)
        MarkPivotElementUsed(pivot_element, used_rows, used_columns)
    return b_


# In[5]:


def Evaluate(n, m, c, x):
    # Given solution, evaluate the value of the objective function
    opt_val = 0
    for c_i, x_i in zip(c, x):
        opt_val += c_i * x_i
    return opt_val


# In[6]:


def AppendEquations(n, m, A, b):
    for i in range(m):
        # For each variable, add constraint: x[i] >= 0
        temp_equation = [0] * m
        temp_equation[i] = -1
        A.append(temp_equation)
        b.append(0)
    max_cap = 10 ** 9
    temp_equation = [1] * m
    A.append(temp_equation)
    b.append(max_cap)
    return A, b


# In[7]:


def CreateSubset(n, m, A, b):
    collection = []
    for equations in itertools.combinations(zip(A, b), m):
        temp_a = [x[0].copy() for x in equations]
        temp_b = [x[1] for x in equations]
        collection.append(Equation(temp_a, temp_b))
    return collection


# In[8]:


def ChangeDataType(A, b):
    return [list(map(float, a)) for a in A], list(map(float, b))


# In[9]:


def CheckInequality(n, m, A, b, solution):
    status = True
    for lhs, rhs in zip(A[:-1], b[:-1]):
        status =  status & (Evaluate(n, m, lhs, solution) < (rhs + EPS))
    return status


# In[10]:


def CheckInfinity(n, m, equations):
    max_cap = 10 ** 9
    max_cap = float(max_cap)
    for j in equations.b_:
        if j == max_cap:
            return True
    return False


# In[11]:


def solve_diet_problem(n, m, A, b, c):  
    # Write your code here
    A, b = AppendEquations(n, m, A, b)
    A, b = ChangeDataType(A, b)
    collection = CreateSubset(n, m, A, b)
    solutions, opt_vals, store_equations = [], [], []
    for equations in collection:
#         print(equations.a_, equations.b_)
        solution = SolveEquation(equations)
#         print(solution)
        if solution == False:
            continue
        status = CheckInequality(n, m, A, b, solution)
#         print(Evaluate(n, m, c, solution), status)
        if status == True:
            opt_val = Evaluate(n, m, c, solution)
            store_equations.append(equations)
            solutions.append(solution)
            opt_vals.append(opt_val)
    max_index, max_value = 0, float(-10 ** 9)
    for index, value in enumerate(opt_vals):
        if value > max_value:
            max_value = value
            max_index = index
    zero_solution = [0] * m
    status = CheckInequality(n, m, A, b, zero_solution)
    if len(solutions) == 0:
        if status == True:
            return 0, zero_solution
        return -1, []
    elif CheckInfinity(n, m, store_equations[max_index]):
        return 1, []
    else:
        if (status == True) & (Evaluate(n, m, c, zero_solution) > opt_vals[max_index]):
            return 0, zero_solution
        return 0, solutions[max_index]


# In[12]:


# Testing section --------------------------------------------------
# n, m = 3, 3
# A = [[-46, -46, 14], [38, -14, -30], [23, 100, -86]]
# b = [-14867, -7071, -10179]
# c = [100, -30, -80]

# n, m = 3, 2
# A = [[-1, -1], [1, 0], [0, 1]]
# b = [-1, 2, 2]
# c = [-1, 2]


# In[13]:


n, m = list(map(int, stdin.readline().split()))
A = []
for i in range(n):
    A += [list(map(int, stdin.readline().split()))]
b = list(map(int, stdin.readline().split()))
c = list(map(int, stdin.readline().split()))
anst, ansx = solve_diet_problem(n, m, A, b, c)
if anst == -1:
    print("No solution")
if anst == 0:  
    print("Bounded solution")
    print(' '.join(list(map(lambda x : '%.18f' % x, ansx))))
if anst == 1:
    print("Infinity")

