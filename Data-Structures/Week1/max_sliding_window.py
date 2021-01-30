# python3

class stack():
    

def max_sliding_window_naive(sequence, m):
    maximums, minimums = [], []
    for i in range(len(sequence) - m + 1):
        #maximums.append(max(sequence[i:i + m]))
        if i == 0:
            maximums.append(max(sequence[i:i + m]))
            minimums.append(min(sequence[i:i + m]))
        else:
            if (sequence[i - 1] == maximums[-1]):
                if sequence[i - 1] > sequence[i + m - 1]:
                    maximums.append(max(sequence[i:i + m]))
                else:
                    maximums.append(sequence[i + m - 1])
            elif maximums[-1] < sequence[i + m - 1]:
                maximums.append(sequence[i + m - 1])
            else:
                maximums.append(maximums[-1])
            
    return maximums

if __name__ == '__main__':
    n = int(input())
    input_sequence = [int(i) for i in input().split()]
    assert len(input_sequence) == n
    window_size = int(input())

    print(*max_sliding_window_naive(input_sequence, window_size))

