# Uses python3
def edit_distance(s, t):
    #write your code here
    # Build zero matrix
    common = 0
    D = [(len(t) + 1) * [0] for i in range(len(s) + 1)]
    # Initialize variable
    for i in range(1, len(s) + 1):
        D[i][0] = i
    for i in range(1, len(t) + 1):
        D[0][i] = i
    for j in range(1, len(t) + 1):
        for i in range(1, len(s) + 1):
            insertion = D[i][j - 1] + 1
            deletion = D[i - 1][j] + 1
            match = D[i - 1][j - 1]
            mismatch = D[i - 1][j - 1] + 1
            if s[i - 1] == t[j - 1]:
                D[i][j] = min(insertion, deletion, match)
            else:
                D[i][j] = min(insertion, deletion, mismatch)
    i, j = len(s), len(t)
    count = 0
    while (i != 0) | (j != 0):
        if (i > 0) & (D[i][j] == D[i - 1][j] + 1):
            #print([s[i - 1], '-'])
            count += 1
            i -= 1
        elif (j > 0) & (D[i][j] == D[i][j - 1] + 1):
            count += 1
            #print(['-', t[j - 1]])
            j -= 1
        else:
            #print([s[i - 1], t[j - 1]])
            if s[i - 1] != t[j - 1]:
                count += 1
            else:
                common += 1
            i -= 1
            j -= 1
    return common

if __name__ == "__main__":
    #print(edit_distance(input(), input()))
    print(edit_distance("2783", "5287"))
