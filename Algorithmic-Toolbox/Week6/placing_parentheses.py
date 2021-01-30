# Uses python3
def evalt(a, b, op):
    if op == '+':
        return a + b
    elif op == '-':
        return a - b
    elif op == '*':
        return a * b
    else:
        assert False

def min_and_max(i, j, dataset, m, M):
    min_, max_ = 100, -100
    for k in range(i, j):
        op = dataset[2 * k + 1]
        a, b, c, d = evalt(M[i][k], M[k + 1][j], op), evalt(M[i][k], m[k + 1][j], op), evalt(m[i][k], M[k + 1][j], op), evalt(m[i][k], m[k + 1][j], op)
        min_, max_ = min(min_, a, b, c, d), max(max_, a, b, c, d)
    return(min_, max_)
    
def get_maximum_value(dataset):
    #write your code here
    n = len(dataset) // 2 + 1
    m, M = [n * [0] for i in range(n)], [n * [0] for i in range(n)]
    
    for i in range(len(dataset)):
        if i % 2 == 0:
            pos = i // 2
            m[pos][pos], M[pos][pos] = int(dataset[i]), int(dataset[i])
            
    for s in range(n - 1):
        for i in range(n - s - 1):
            j = i + s + 1
            m[i][j], M[i][j] = min_and_max(i, j, dataset, m, M)
    return M[0][n - 1]


if __name__ == "__main__":
    print(get_maximum_value(input()))