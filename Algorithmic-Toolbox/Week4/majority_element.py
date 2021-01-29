# Uses python3
import sys

def get_majority_element(a, left, right):
    if left + 1 == right:
        return a[left]
    #write your code here
    m = (left + right) // 2
    b = get_majority_element(a, left, m)
    c = get_majority_element(a, m, right)
    
    get_maj_list = [element for element in (b, c) if element != -1]

    for maj_element in get_maj_list:
        count = 0
        for i in range(left, right):
            if a[i] == maj_element:
                count += 1
        if count > (right - left) / 2:
            return maj_element
    return -1
 
if __name__ == '__main__':
    input = sys.stdin.read()
    n, *a = list(map(int, input.split()))
    if get_majority_element(a, 0, n) != -1:
        print(1)
    else:
        print(0)
