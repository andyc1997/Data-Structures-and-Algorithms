# python3
import sys
# Task. You are given a string S and you have to process n queries. Each query is described by three integers
# i, j, k and means to cut substring S[i...j] (i and j are 0-based) from the string and then insert it after the
# k-th symbol of the remaining string (if the symbols are numbered from 1). If k = 0, S[i...j] is inserted
# in the beginning. See the examples for further clarification.
# Input Format. The first line contains the initial string S.
# The second line contains the number of queries q.
# Next q lines contain triples of integers i, j, k.
# Output Format. Output the string after all q queries.

class Rope:
    def __init__(self, s): # Input string
        self.s = s
        
    def result(self): # Return results
        return self.s
    
    def process(self, i, j, k): # A naive solution
        substr = self.s[i:j + 1] # Substring defined in the problem
        self.s = self.s[:i] + self.s[j + 1:]
        if k == 0:
            self.s = substr + self.s
        else:
            self.s = self.s[:k] + substr + self.s[k:] 

rope = Rope(sys.stdin.readline().strip())
q = int(sys.stdin.readline())
for _ in range(q):
    i, j, k = map(int, sys.stdin.readline().strip().split())
    rope.process(i, j, k)
print(rope.result())

# Remark: I haven't figured out how to implement a splay tree to solve this problem. So, I use naive solution at the moment
