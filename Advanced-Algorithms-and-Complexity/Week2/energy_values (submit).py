# python3
EPS = 1e-6
PRECISION = 20


# In[2]:


class Equation:
    def __init__(self, a, b):
        self.a = a
        self.b = b


# In[3]:


class Position:
    def __init__(self, column, row):
        self.column = column
        self.row = row


# In[4]:


def ReadEquation():
    size = int(input())
    a = []
    b = []
    for row in range(size):
        line = list(map(float, input().split()))
        a.append(line[:size])
        b.append(line[size])
    return Equation(a, b)

# For testing purposes:
def ReadEquationTest():
    #data = [[1, 0, 0, 0, 1], [0, 1, 0, 0, 5], [0, 0, 1, 0, 4], [0, 0, 0, 1, 3]]
    #data = [[1, 1, 3], [2, 3, 7]]
    #data = [[5, -5, -1], [-1, -2, -1]]
    data = [[1, 0, 0, 0, 1], [0, 0, 0, 1, 3], [0, 1, 0, 0, 5], [0, 0, 1, 0, 8]]
    size = len(data)
    a = []
    b = []
    for row in range(size):
        line = list(map(float, data[row]))
        a.append(line[:size])
        b.append(line[size])
    return Equation(a, b)


# In[5]:


def SelectPivotElement(a, b, used_rows, used_columns):
    # This algorithm selects the first free element.
    # You'll need to improve it to pass the problem.
    pivot_element = Position(0, 0)
    while used_rows[pivot_element.row]:
        pivot_element.row += 1
    while used_columns[pivot_element.column]:
        pivot_element.column += 1
        
    max_row = pivot_element.row
    if a[pivot_element.row][pivot_element.column] == 0:
        for below_row in range(pivot_element.row + 1, len(a)):
            if a[below_row][pivot_element.column] > a[max_row][pivot_element.column]:
                max_row = below_row
        a[pivot_element.row], a[max_row] = a[max_row], a[pivot_element.row]
        b[pivot_element.row], b[max_row] = b[max_row], b[pivot_element.row]
    return pivot_element


# In[6]:


def SwapLines(a, b, used_rows, pivot_element):
    a[pivot_element.column], a[pivot_element.row] = a[pivot_element.row], a[pivot_element.column]
    b[pivot_element.column], b[pivot_element.row] = b[pivot_element.row], b[pivot_element.column]
    used_rows[pivot_element.column], used_rows[pivot_element.row] = used_rows[pivot_element.row], used_rows[pivot_element.column]
    pivot_element.row = pivot_element.column;


# In[7]:


def ProcessPivotElement(a, b, pivot_element):
    # Write your code here
    # Scale elements in pivot row with pivot element = 1
    scaling_factor = a[pivot_element.row][pivot_element.column]
    a[pivot_element.row] = list(map(lambda x: x / scaling_factor, a[pivot_element.row]))
    b[pivot_element.row] /= scaling_factor
    # All zeros below pivot element
    size = len(a)
    if pivot_element.row + 1 < size:
        for non_pivot in range(pivot_element.row + 1, size):
            multiple = a[non_pivot][pivot_element.column]
            for column in range(pivot_element.column, len(a[0])):
                a[non_pivot][column] -= multiple * a[pivot_element.row][column]
            b[non_pivot] -= multiple * b[pivot_element.row]
    # All zeros above pivot element
    if pivot_element.row > 0:
        for above_pivot in range(0, pivot_element.row):
            multiple = a[above_pivot][pivot_element.column]
            for column in range(pivot_element.column, len(a[0])):
                a[above_pivot][column] -= multiple * a[pivot_element.row][column]
            b[above_pivot] -= multiple * b[pivot_element.row]
    pass


# In[8]:


def MarkPivotElementUsed(pivot_element, used_rows, used_columns):
    used_rows[pivot_element.row] = True
    used_columns[pivot_element.column] = True


# In[9]:


def SolveEquation(equation):
    a = equation.a
    b = equation.b
    size = len(a)
    
    used_columns = [False] * size
    used_rows = [False] * size
    for step in range(size):
        pivot_element = SelectPivotElement(a, b, used_rows, used_columns)
        SwapLines(a, b, used_rows, pivot_element)
        ProcessPivotElement(a, b, pivot_element)
        MarkPivotElementUsed(pivot_element, used_rows, used_columns)
    return b


# In[10]:


def PrintColumn(column):
    size = len(column)
    for row in range(size):
        print("%.20lf" % column[row])


# In[11]:


if __name__ == "__main__":
    equation = ReadEquation()
    solution = SolveEquation(equation)
    PrintColumn(solution)

