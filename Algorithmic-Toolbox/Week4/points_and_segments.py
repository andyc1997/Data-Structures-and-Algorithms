# Uses python3
import sys
import math
# Task. You are given a set of points on a line and a set of segments on a line. The goal is to compute, for
# each point, the number of segments that contain this point.
# Input Format. The first line contains two non-negative integers s and p defining the number of segments
# and the number of points on a line, respectively. The next s lines contain two integers a[i], b[i] defining
# the i-th segment [a[i], b[i]]. The next line contains p integers defining points x[1], x[2], . . . , x[p].
# Output Format. Output p non-negative integers k[0], k[1], . . . , k[p-1] where k[i] is the number of segments which
# contain x[i].

def merge(subarray_1, subarray_2):
    # A part of merge sort algorithm costs O(n)
    array_sorted = list()
    while len(subarray_1) > 0 and len(subarray_2) > 0:
        if subarray_1[0] <= subarray_2[0]:
            array_sorted.append(subarray_1.pop(0))
        else:
            array_sorted.append(subarray_2.pop(0))
    if len(subarray_1) > 0:
        array_sorted += subarray_1
    elif len(subarray_2) > 0:
        array_sorted += subarray_2
    return array_sorted

def merge_sort(array):
    # A standard implementation of merge sort in O(nlogn)
    n = len(array)
    if n == 1:
        return array
    m = math.floor(n/2)
    subarray_1 = merge_sort(array[:m])
    subarray_2 = merge_sort(array[m:])
    array_sorted = merge(subarray_1, subarray_2)
    return array_sorted

def modified_binary_search_inf(array, value, l, r): # Time complexity: O(logn)
    # Input: sorted ending points of segments
    # Return: the index of the largest ending points < point
    m = math.floor((l + r)/2)
    if value == array[m]:
        while value == array[m]:
            m -= 1
            if m < 0:
                return -1
        return m
    if l == r:
        if array[l] < value:
            return l
        return l - 1
    elif value < array[m]:
        return modified_binary_search_inf(array, value, l, m)
    else:
        return modified_binary_search_inf(array, value, m + 1, r)
    
def modified_binary_search_sup(array, value, l, r): # Time complexity: O(logn)
    # Input: sorted starting points of segments
    # Return: the index of the smallest starting points > point
    m = math.floor((l + r)/2)
    if value == array[m]:
        while value == array[m]:
            m += 1
            if m > len(array) - 1:
                return -1
        return m
    if l == r:
        if array[l] > value:
            return l
        return -1
    elif value > array[m]:
        return modified_binary_search_sup(array, value, m + 1, r)
    else:
        return modified_binary_search_sup(array, value, l, m)
    
def fast_count_segments(starts, ends, points):
    cnt = list()
    index_begin, index_stop = 0, len(starts) - 1
    sort_starts = merge_sort(starts)
    sort_ends = merge_sort(ends)
    for p in points:
        p_sup = modified_binary_search_sup(sort_starts, p, index_begin, index_stop) 
        p_inf = modified_binary_search_inf(sort_ends, p, index_begin, index_stop) 
        num_segment_above, num_segment_below = (len(starts) - p_sup)*(p_sup > -1), (p_inf + 1)*(p_inf > -1)
        num = len(starts) - (num_segment_above + num_segment_below)
        cnt.append(num)
    return cnt

if __name__ == '__main__':
    input = sys.stdin.read()
    data = list(map(int, input.split()))
    n = data[0]
    m = data[1]
    starts = data[2:2 * n + 2:2]
    ends   = data[3:2 * n + 2:2]
    points = data[2 * n + 2:]
    cnt = fast_count_segments(starts, ends, points)
    for x in cnt:
        print(x, end=' ')

