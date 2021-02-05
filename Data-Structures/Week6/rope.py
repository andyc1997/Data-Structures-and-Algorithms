# python3
import sys
class Rope:
    def __init__(self, s):
        self.s = s
        
    def result(self):
        return self.s
    def process(self, i, j, k):
        # Write your code here
        substr = self.s[i:j + 1]
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

#%%
# rope = Rope('hlelowrold'.strip())
# data = ['1 1 2', '6 6 7']
# q = int('2')
# for s in data:
#     i, j, k = map(int, s.strip().split())
#     rope.process(i, j, k)
# print(rope.result())