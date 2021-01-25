# Uses python3
import sys

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


def fibonacci_sum_naive(n):
    if n <= 1:
        return n
    last_digit = get_fibonacci_huge_naive(n + 2, 10) - 1
    if last_digit < 0:
        last_digit += 10
    return(last_digit)

if __name__ == '__main__':
    input = sys.stdin.read()
    n = int(input)
    print(fibonacci_sum_naive(n))
