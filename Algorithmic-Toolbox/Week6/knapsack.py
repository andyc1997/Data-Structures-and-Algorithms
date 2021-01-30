# Uses python3
import sys

def optimal_weight(W, w):
    # write your code here
    # Number of items
    n = len(w)
    # Value matrix
    value = [(n + 1) * [0] for i in range(W + 1)]
    for i in range(1, n + 1):
        for w_ in range(1, W + 1):
            value[w_][i] = value[w_][i - 1]
            if w[i - 1] <= w_:
                val = value[w_ - w[i - 1]][i - 1] + w[i - 1]
                if value[w_][i] < val:
                    value[w_][i] = val
    return value[w_][n]

if __name__ == '__main__':
    input = sys.stdin.read()
    W, n, *w = list(map(int, input.split()))
    print(optimal_weight(W, w))
