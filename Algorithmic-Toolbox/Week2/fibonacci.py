# Uses python3
def calc_fib(n):
    F = []
    for i in range(n + 1):
        if i == 0:
            F.append(0)
        elif i == 1:
            F.append(1)
        else:
            F.append(F[i - 1] + F[i - 2])
    return F[-1]
n = int(input())
print(calc_fib(n))
