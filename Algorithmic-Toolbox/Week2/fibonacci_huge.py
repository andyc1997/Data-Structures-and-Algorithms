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

if __name__ == '__main__':
    input = sys.stdin.read();
    n, m = map(int, input.split())
    print(get_fibonacci_huge_naive(n, m))
