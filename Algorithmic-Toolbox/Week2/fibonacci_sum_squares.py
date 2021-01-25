# Uses python3
from sys import stdin

def get_fibonacci_huge_naive(n, m):
    if n <= 1:
        return n

    F = []
    for i in range(n + 1):
        if i == 0:
            F.append(0)
        elif i == 1:
            F.append(1)
        else:
            F.append((F[i - 1] + F[i - 2]) % m)
        if F[i - 1] == 0 and F[i] == 1 and i > 1:
            del F[i]
            del F[i - 1]
            
            index = n % len(F)
            return(F[index])
            
    return F[-1]

def fibonacci_sum_squares_naive(n):
    fib_num_height = get_fibonacci_huge_naive(n, 10)
    fib_num_width = get_fibonacci_huge_naive(n + 1, 10)
    return (fib_num_height * fib_num_width) % 10

if __name__ == '__main__':
    n = int(stdin.read())
    print(fibonacci_sum_squares_naive(n))
