# python3

import sys
from random import randint

def poly_hash(S: str, p: int, x: int) -> int:
    hash_num = [0]
    x_mod_p = [1]
    for i in range(len(S)):
        x_mod_p.append((x * x_mod_p[-1]) % p)
    for i in range(len(S)):
        hash_num.append((ord(S[i]) + x * hash_num[-1]) % p)
    return hash_num, x_mod_p

class Solver:
    def __init__(self, s):
        self.s = s
        self.p1, self.p2 = 10 ** 9 + 17, 10 ** 9 + 37
        self.x1, self.x2 = randint(1, self.p1 - 1), randint(1, self.p2 - 1)
        self.hash_num_1, self.x_mod_p_1 = poly_hash(s, self.p1, self.x1)
        self.hash_num_2, self.x_mod_p_2 = poly_hash(s, self.p2, self.x2)
        
    def ask(self, a, b, l):
        #if len(self.s) < 1000:
        #    return self.s[a:(a + l)] == self.s[b:(b + l)]
        s1_h1 = (self.hash_num_1[a + l] - self.x_mod_p_1[l] * self.hash_num_1[a]) % self.p1
        s2_h1 = (self.hash_num_1[b + l] - self.x_mod_p_1[l] * self.hash_num_1[b]) % self.p1
        s1_h2 = (self.hash_num_2[a + l] - self.x_mod_p_2[l] * self.hash_num_2[a]) % self.p2
        s2_h2 = (self.hash_num_2[b + l] - self.x_mod_p_2[l] * self.hash_num_2[b]) % self.p2
        #print(s1_h1, s2_h1, s1_h2, s2_h2)
        return (s1_h1 == s2_h1) & (s1_h2 == s2_h2)
        
s = sys.stdin.readline()
q = int(sys.stdin.readline())
solver = Solver(s)
for i in range(q):
    a, b, l = map(int, sys.stdin.readline().split())
    print("Yes" if solver.ask(a, b, l) else "No")