# Uses python3
import sys

def get_number_of_inversions(a, b, left, right):
    number_of_inversions = 0
    if right - left <= 1:
        return number_of_inversions
    ave = (left + right) // 2
    number_of_inversions += get_number_of_inversions(a, b, left, ave)
    number_of_inversions += get_number_of_inversions(a, b, ave, right)
    #write your code here
    left_list, right_list = a[left:ave].copy(), a[ave:right].copy()
    d = []
    while (left_list != []) & (right_list != []):
        left_first, right_first = left_list[0], right_list[0]
        if left_first <= right_first:
            d.append(left_first)
            del left_list[0]
        else:
            d.append(right_first)
            del right_list[0]
            number_of_inversions += len(left_list)
    if left_list == []:
        d += right_list
    elif right_list == []:
        d += left_list
    a[left:right] = d
    return number_of_inversions

if __name__ == '__main__':
    input = sys.stdin.read()
    n, *a = list(map(int, input.split()))
    b = n * [0]
    print(get_number_of_inversions(a, b, 0, len(a)))
