# Uses python3
import sys

def gcd_naive(a, b):
    if a == 0:
        return b
    elif b == 0:
        return a
    else:
        c, d = min(a, b), max(a, b)
        a, b = c, d % c
        return gcd_naive(a, b)
    
def lcm_naive(a, b):
    if (a != 0) or (b != 0):
        gcd = gcd_naive(a, b)
        return int((a * b) / gcd)
    else:
        return 0

if __name__ == '__main__':
    input = sys.stdin.read()
    a, b = map(int, input.split())
    print(lcm_naive(a, b))

