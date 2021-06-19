# python3
import sys
        
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
            else:
                node_idx += 1
                tree.update({node_idx: dict()})
                tree[currentNode][currentSymbol] = node_idx
                currentNode = node_idx
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
            if len(trie[v]) == 0:
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
    #print(trie)
    return result

text = sys.stdin.readline().strip()
n = int(sys.stdin.readline().strip())
patterns = []
for i in range(n):
    patterns += [sys.stdin.readline().strip()]
ans = solve(text, n, patterns)
#ans = solve('AAA', 1, ['AA'])
#ans = solve('AA', 1, ['T'])
#ans = solve('AATCGGGTTCAATCGGGGT', 3, ['ATCG', 'GGGT'])
#ans = solve('TCTGGGCCTAACCAACGGAGCTG', 2, ['TCTG', 'CTGG', 'TGGG','GGGC', 'GCTG'])  
sys.stdout.write(' '.join(map(str, ans)) + '\n')
