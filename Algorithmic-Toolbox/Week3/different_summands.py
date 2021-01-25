# Uses python3
import sys

def optimal_summands(n):
    summands = []
    n_sum = n
    choice = 1
    #write your code here
    while n_sum > 2*choice:
        summands.append(choice)
        n_sum -= choice
        choice += 1
    
    summands.append(n_sum)
    return summands

if __name__ == '__main__':
    input = sys.stdin.read()
    n = int(input)
    summands = optimal_summands(n)
    print(len(summands))
    for x in summands:
        print(x, end=' ')
