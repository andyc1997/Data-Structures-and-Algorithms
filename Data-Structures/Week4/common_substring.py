# python3
import sys
from collections import namedtuple
Answer = namedtuple('answer_type', 'i j len')

def poly_hash(S, p, x): # Standard implementation of polynomial hashing
    hash_num = [0]
    x_mod_p = [1]
    for i in range(len(S)):
        x_mod_p.append((x * x_mod_p[-1]) % p) # x_mod_p stores a sequence of hashing functions from S[0] to S[len(S) - 1]
    for i in range(len(S)):
        hash_num.append((ord(S[i]) + x * hash_num[-1]) % p) # hash_num stores a sequence of hashes from H(S[0]) to H(S[0]...S[len(S) - 1])
    return hash_num, x_mod_p

def compare_length(s, t): # return s and t in which s is always the longer string
    len_s, len_t = len(s), len(t)
    if len_s < len_t:
        return t, s, True
    return s, t, False

class hash_table:
    def __init__(self):
        self.hash_table_1 = dict()
        self.hash_table_2 = dict()
    
    def update(self, start, length, h1, h2):
        tuple_update = tuple([start, length])
        if h1 in self.hash_table_1:
            self.hash_table_1[h1].append(tuple_update)
        else:
            self.hash_table_1.update({h1: [tuple_update]})
        tuple_update = tuple([start, length, h1])
        if h2 in self.hash_table_2:
            self.hash_table_2[h2].append(tuple_update)
        else:
            self.hash_table_2.update({h2: [tuple_update]})
    
    def clear_cache(self):
        self.hash_table_1 = dict()
        self.hash_table_2 = dict()
        
class hashed_string:
    def __init__(self, s):
        self.s = s
        self.p1, self.p2 = 263130836933693530167218012159999999, 8683317618811886495518194401279999999 # Or 10 ** 12 + 37, 10** 12 + 19 to avoid time limit exceed problem
        self.x1, self.x2 = 17, 37 # Use number with fewer digits to avoid memory limit exceed problem
        self.hash_num_1, self.x_mod_p_1 = poly_hash(s, self.p1, self.x1) 
        self.hash_num_2, self.x_mod_p_2 = poly_hash(s, self.p2, self.x2)
        
    def hashed_substring(self, start, length): # Return hashed value of substring started at i with length of j
        h1 = (self.hash_num_1[start + length] - self.x_mod_p_1[length] * self.hash_num_1[start]) % self.p1 # First hash for string 1
        h2 = (self.hash_num_2[start + length] - self.x_mod_p_2[length] * self.hash_num_2[start]) % self.p2 # Second hash for string 1
        return (h1, h2)

def match(hashed_s, hashed_t, len_s, len_t, hash_table_t, i, swap):
    for j in range(0, len_t - i + 1): # j is the position at which the substring starts
        h1, h2 = hashed_t.hashed_substring(j, i)
        hash_table_t.update(j, i, h1, h2)
    for j in range(0, len_s - i + 1):
        h1, h2 = hashed_s.hashed_substring(j, i) 
        if h1 in hash_table_t.hash_table_1.keys() and h2 in hash_table_t.hash_table_2.keys():
            index_s, index_t, length = j, hash_table_t.hash_table_1[h1][0][0], i
            answer = Answer(index_s, index_t, length)
            if swap == True:
                answer = Answer(index_t, index_s, length)
            hash_table_t.clear_cache()
            return answer
    hash_table_t.clear_cache()
    return Answer(0, 0, 0)
    
def solve(s, t):
    answer, answer_temp = Answer(0, 0, 0), Answer(0, 0, 0)
    hash_table_t = hash_table()
    s, t, swap = compare_length(s, t) # s is always longer than t
    len_s, len_t = len(s), len(t) # length of s and length of t
    hashed_s, hashed_t = hashed_string(s), hashed_string(t)
    
    left, right = 1, len(t) + 1
    while right >= left:
        mid = (left + right) // 2
        answer = match(hashed_s, hashed_t, len_s, len_t, hash_table_t, mid, swap)

        if answer != Answer(0, 0, 0):
            left = mid + 1
            answer_temp = answer
        else:
            right = mid - 1
    if answer_temp != answer and answer == Answer(0, 0, 0):
        return answer_temp
    return answer

for line in sys.stdin.readlines():
    s, t = line.split()
    ans = solve(s, t)
    print(ans.i, ans.j, ans.len)
