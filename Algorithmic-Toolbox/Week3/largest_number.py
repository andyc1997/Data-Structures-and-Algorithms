#Uses python3

import sys

def get_better(a, b):
    is_better = int(str(a) + str(b)) >= int(str(b) + str(a))
    return is_better

def largest_number(a):
    #write your code here
    res = ""
    a_copy = a.copy()
    while a_copy != []:
        max_number = 0
        for num in a_copy:
            if get_better(num, max_number):
                max_number = num
        res += max_number
        a_copy.remove(max_number)
        
            
    return res

if __name__ == '__main__':
    input = sys.stdin.read()
    data = input.split()
    a = data[1:]
    print(largest_number(a))
    
