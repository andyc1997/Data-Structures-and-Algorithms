# python3

from collections import namedtuple

Bracket = namedtuple("Bracket", ["char", "position"])


def are_matching(left, right):
    return (left + right) in ["()", "[]", "{}"]


def find_mismatch(text):
    opening_brackets_stack = []
    if len(text) == 1:
        return 1
    
    for i, char in enumerate(text):
        if char in "([{":
            # Process opening bracket, write your code here
            opening_brackets_stack.append([char, i])
        if char in ")]}":
            # Process closing bracket, write your code here
            if len(opening_brackets_stack) == 0:
                return i + 1
            else:
                top = opening_brackets_stack.pop()
                if (top[0] == '[' and char != ']') or (top[0] == '(' and char != ')') or \
                (top[0] == '{' and char != '}'):
                    return i + 1
    if len(opening_brackets_stack) == 0:
        return('Success')
    else:
        return(opening_brackets_stack[0][1] + 1)
        
def main():
    text = input()
    mismatch = find_mismatch(text)
    # Printing answer, write your code here
    print(mismatch)

if __name__ == "__main__":
    main()
