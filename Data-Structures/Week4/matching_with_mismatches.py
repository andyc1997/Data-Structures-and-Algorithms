# python3
import sys
def poly_hash(S, p, x): # Standard implementation of polynomial hashing
    hash_num = [0]
    x_mod_p = [1]
    for i in range(len(S)):
        x_mod_p.append((x * x_mod_p[-1]) % p) # x_mod_p stores a sequence of hashing functions from S[0] to S[len(S) - 1]
    for i in range(len(S)):
        hash_num.append((ord(S[i]) + x * hash_num[-1]) % p) # hash_num stores a sequence of hashes from H(S[0]) to H(S[0]...S[len(S) - 1])
    return hash_num, x_mod_p

class hashed_string:
    def __init__(self, s):
        self.s = s # input string
        self.p1, self.p2 = 263130836933693530167218012159999999, 8683317618811886495518194401279999999 # Or 10 ** 12 + 37, 10** 12 + 19 to avoid time limit exceed problem
        self.x1, self.x2 = 17, 37 # Use number with fewer digits to avoid memory limit exceed problem
        self.hash_num_1, self.x_mod_p_1 = poly_hash(s, self.p1, self.x1) # Do polynomial hashing two times with different primes, it costs O(length(string))
        self.hash_num_2, self.x_mod_p_2 = poly_hash(s, self.p2, self.x2)
        
    def hashed_substring(self, start, end): # Return hashed value of substring started at i with length of j, it costs O(1)
        length = end - start + 1
        h1 = (self.hash_num_1[start + length] - self.x_mod_p_1[length] * self.hash_num_1[start]) % self.p1 # First hash for string 1
        h2 = (self.hash_num_2[start + length] - self.x_mod_p_2[length] * self.hash_num_2[start]) % self.p2 # Second hash for string 1
        return (h1, h2)

def modified_bs(hashed_p, hashed_t, pattern, substr_text, i, mismatch_count, left, right, k):
    if right >= left:
        mid = (left + right) // 2
        # print(i, left, right, mid, substr_text, pattern)
        if substr_text[mid] != pattern[mid]:
            mismatch_count += 1
            # print(i + left, i + mid - left)
            # print(i + mid + 1, i + right - mid - 1)
        if hashed_t.hashed_substring(i + left, i + mid - 1) != hashed_p.hashed_substring(left, mid - 1):
            # print(hashed_t.hashed_substring(i + left, i + mid - 1), hashed_p.hashed_substring(left, mid - 1))
            mismatch_count = modified_bs(hashed_p, hashed_t, pattern, substr_text, i, mismatch_count, left, mid - 1, k)
        if hashed_t.hashed_substring(i + mid + 1, i + right) != hashed_p.hashed_substring(mid + 1, right):
            # print(hashed_t.hashed_substring(i + mid + 1, i + right), hashed_p.hashed_substring(mid + 1, right))
            mismatch_count = modified_bs(hashed_p, hashed_t, pattern, substr_text, i, mismatch_count, mid + 1, right, k)
        if mismatch_count > k:
            return mismatch_count
    return mismatch_count

def solve(k, text, pattern):
    len_p, len_t, results = len(pattern), len(text), list()
    hashed_t, hashed_p = hashed_string(text), hashed_string(pattern)
    # print(hashed_t.hash_num_1)
    for i in range(0, len_t - len_p + 1):
        substr_text, mismatch_count = text[i:(i + len_p)], 0
        left, right = 0, len_p - 1
        mismatch_count = modified_bs(hashed_p, hashed_t, pattern, substr_text, i, mismatch_count, left, right, k)
        # print('substring of text:', substr_text, 'pattern:', pattern, 'Mismatches', mismatch_count, 'Tolerance:', k)
        if mismatch_count <= k:
            results.append(i)
        # print('Results:', results)
    return results

for line in sys.stdin.readlines():
    k, t, p = line.split()
    ans = solve(int(k), t, p)
    print(len(ans), *ans)

#%% debug case
# data = ['0 ababab baaa', '1 ababab baaa', '1 xabcabc ccc', '2 xabcabc ccc', '3 aaa xxx']
# for line in data:
#     k, t, p = line.split()
#     ans = solve(int(k), t, p)
#     print(len(ans), *ans)
