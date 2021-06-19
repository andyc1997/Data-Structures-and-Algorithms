# python3
import sys

NA = -1
class Node:
    def __init__ (self):
        self.next = [NA] * 4
        self.patternEnd = False

def build_trie(patterns):
    tree = dict({0: dict()})
    node_idx = 0
    # write your code here
    for pattern in patterns:
        currentNode = 0
        for i in range(len(pattern)):
            currentSymbol = pattern[i]
            if currentSymbol in tree[currentNode]:
                currentNode = tree[currentNode][currentSymbol]
                if i == len(pattern) - 1:
                    tree[currentNode]['$'] = -1
            else:
                node_idx += 1
                tree.update({node_idx: dict()})
                tree[currentNode][currentSymbol] = node_idx
                currentNode = node_idx
                if i == len(pattern) - 1:
                    tree[currentNode]['$'] = -1
    #print(tree)
    return tree

def prefix_trie_matching(text, trie):
    text += '$'
    i = 0
    symbol = text[i]
    v = 0
    while True:
        if symbol in trie[v]:
            v = trie[v][symbol]
            if '$' in trie[v]:
                return True
            elif len(trie[v]) == 0:
                return True
            i += 1
            symbol = text[i]
        else:
            return False
        
def solve(text, n, patterns):
    trie = build_trie(patterns)
    result = []
    # write your code here
    j = 0
    while len(text) > j:
        if prefix_trie_matching(text[j:], trie) == True:
            result.append(j)
        j += 1
    print(trie)
    return result

#text = sys.stdin.readline().strip()
#n = int(sys.stdin.readline().strip())
#patterns = []
#for i in range(n):
#	patterns += [sys.stdin.readline().strip()]
#ans = solve(text, n, patterns)
#ans = solve('ACATA', 3, ['AT', 'A', 'AG'])
#ans = solve('ATTGTTTTCTCGAGCGC', 7, ['TAATA', 'AAGTGAGCAG', 'GCTCACATA', 'CCAC', 'C',
#                                     'GCC', 'TGTTCTTA'])
ans = solve('CCCCCCCCCCCCCCCCCA', 3, ['CA'])
sys.stdout.write(' '.join(map(str, ans)) + '\n')
