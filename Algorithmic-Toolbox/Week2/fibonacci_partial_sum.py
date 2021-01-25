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
    
def fibonacci_partial_sum_naive(from_, to):
    if to == from_:
        return get_fibonacci_huge_naive(to, 10)
    else:
        if from_ == 0:
            return fibonacci_sum_naive(to)
        else:
            sum_ = fibonacci_sum_naive(to) - fibonacci_sum_naive(from_ - 1)
            return sum_ % 10


if __name__ == '__main__':
    input = sys.stdin.read();
    from_, to = map(int, input.split())
    print(fibonacci_partial_sum_naive(from_, to))