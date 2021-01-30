# python3
from random import randint

def read_input():
    return (input().rstrip(), input().rstrip())

def print_occurrences(output):
    print(' '.join(map(str, output)))

def get_occurrences(pattern, text):
    return [
        i 
        for i in range(len(text) - len(pattern) + 1) 
        if text[i:i + len(pattern)] == pattern
    ]

def poly_hash(S: str, p: int, x: int) -> int:
    """hash_num: int"""
    hash_num = 0
    for i in reversed(range(len(S))):
        hash_num = ((hash_num * x) + ord(S[i])) % p
    return hash_num

def precompute_hashes(T: str, P: int, p: int, x: int) -> list:
    """H: list, y: int"""
    last_index = len(T) - P
    H, S, y = (last_index + 1)* [0], T[last_index:len(T)], 1
    H[last_index] = poly_hash(S, p, x)
    for i in range(P):
        y = (y * x) % p
    for i in reversed(range(len(T) - P)):
        H[i] = (x * H[i + 1] + ord(T[i]) - y * ord(T[i + P])) % p
    return H

def rabin_karp(P: str, T: str) -> list:
    p = 10 ** 9 + 19
    x, result = randint(1, p - 1), list()
    p_hash = poly_hash(P, p, x)
    H = precompute_hashes(T, len(P), p, x)
    for i in range(len(T) - len(P) + 1):
        if p_hash != H[i]:
            pass
        if T[i:(i + len(P))] == P:
            result.append(i)
    return result
    
    
if __name__ == '__main__':
    print_occurrences(rabin_karp(*read_input()))

