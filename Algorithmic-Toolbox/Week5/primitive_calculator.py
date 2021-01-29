# Uses python3
import sys
def dp_optimal_sequence(n):
    # Record minimum number of operations for each integer
    # Record a sequence of number leading to n
    MinOpt, rlist = [0] * n, []
    # No operation is needed for 1, so MinOpt[1 - 1] = 0
    MinOpt[0] = 0
    # Loop through 0 to n - 1, position of number 1 to n
    for i in range(n):
        next_list = [i + 1, 2 * (i + 1) - 1, 3 * (i + 1) - 1] 
        # When i = 0, next_list = [1, 1, 2]
        # When i = 1, next_list = [2, 3, 5]
        for next_pos in next_list:
            if next_pos < n:
                if MinOpt[next_pos] == 0:
                    MinOpt[next_pos] = MinOpt[i] + 1
                elif MinOpt[i] + 1 < MinOpt[next_pos]:
                    MinOpt[next_pos] = MinOpt[i] + 1
    rlist.append(n)
    count = MinOpt[-1] - 1
    while count >= 0:
        last_num = rlist[-1]
        memo = []
        memo.append(last_num - 2)
        if last_num % 2 == 0:
            memo.append(last_num // 2 - 1)
        if last_num % 3 == 0:
            memo.append(last_num // 3 - 1)
        min_index = 0
        for i in range(len(memo)):
            if (min_index != i) & (MinOpt[memo[min_index]] > MinOpt[memo[i]]):
                min_index = i
        rlist.append(memo[min_index] + 1)
        count -= 1
    return reversed(rlist)

def optimal_sequence(n):
    sequence = []
    while n >= 1:
        sequence.append(n)
        if n % 3 == 0:
            n = n // 3
        elif n % 2 == 0:
            n = n // 2
        else:
            n = n - 1
    return reversed(sequence)

input = sys.stdin.read()
n = int(input)
sequence = list(dp_optimal_sequence(n))
print(len(sequence) - 1)
for x in sequence:
    print(x, end=' ')
