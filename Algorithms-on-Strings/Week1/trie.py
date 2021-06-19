#Uses python3
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

    return tree

if __name__ == '__main__':
    patterns = sys.stdin.read().split()[1:]
    tree = build_trie(patterns)
    for node in tree:
        for c in tree[node]:
            print("{}->{}:{}".format(node, tree[node][c], c))
