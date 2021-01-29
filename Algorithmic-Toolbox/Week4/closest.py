#Uses python3
import sys
import math
import itertools
from collections import deque

def merge(subarray_1, subarray_2, key):
    # A part of merge sort algorithm costs O(n)
    subarray_1 = deque(subarray_1)
    subarray_2 = deque(subarray_2)
    array_sorted = list()
    while len(subarray_1) > 0 and len(subarray_2) > 0:
        if subarray_1[0][key] <= subarray_2[0][key]:
            array_sorted.append(subarray_1.popleft())
        else:
            array_sorted.append(subarray_2.popleft())
    if len(subarray_1) > 0:
        array_sorted += subarray_1
    elif len(subarray_2) > 0:
        array_sorted += subarray_2
    return array_sorted

def merge_sort(array, key):
    # A standard implementation of merge sort in O(nlogn)
    n = len(array)
    if n == 1:
        return array
    m = math.floor(n/2)
    subarray_1 = merge_sort(array[:m], key)
    subarray_2 = merge_sort(array[m:], key)
    array_sorted = merge(subarray_1, subarray_2, key)
    return array_sorted

def zip_point(x, y):
    # Return a list: [(x[0], y[0]), ...(x[n], y[n])]
    return list(zip(x, y))

def euclidean_dist(point_l, point_r):
    # Return the Euclidean distance between two points
    sq_dist = (point_l[0] - point_r[0]) ** 2 + (point_l[1] - point_r[1]) ** 2
    return math.sqrt(sq_dist)

def get_point_in_strip(point, mid_point, min_dist):
    missing_point = list()
    for i in range(len(point)):
        p = point[i]
        if abs(p[0] - mid_point[0]) < min_dist:
            missing_point.append(p)
    return missing_point 

def checking(point_strip, guess_dist):
    n = len(point_strip)
    if n == 0:
        return guess_dist
    min_dist = guess_dist
    point_sorted_y = merge_sort(point_strip, 1)
    
    for i in range(0, n):
        point = point_sorted_y[i]
        point_compare = point_sorted_y[i + 1:min(i + 7, n)]
        for p in point_compare:
            d = euclidean_dist(point, p)
            if d < min_dist:
                min_dist = d        
    return min_dist

def split_halves(point):
    n = len(point)
    m = math.floor(n/2)
    min_dist = 10 ** 18
    
    if n <= 3:
        for point_l, point_r in itertools.combinations(point, r = 2):
            d = euclidean_dist(point_l, point_r)
            if d < min_dist:
                min_dist = d
        return min_dist

    min_dist_1 = split_halves(point[:m])
    min_dist_2 = split_halves(point[m:])
    min_dist = min(min_dist_1, min_dist_2)
    point_strip = get_point_in_strip(point, point[m], min_dist)
    min_dist = checking(point_strip, min_dist)
    return min_dist

def minimum_distance(x, y):
    point = zip_point(x, y)
    point_sorted_x = merge_sort(point, 0)
    min_dist = split_halves(point_sorted_x)
    return min_dist

if __name__ == '__main__':
    input = sys.stdin.read()
    data = list(map(int, input.split()))
    n = data[0]
    x = data[1::2]
    y = data[2::2]
    print("{0:.9f}".format(minimum_distance(x, y)))
