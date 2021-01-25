# Uses python3
import sys
from collections import namedtuple

Segment = namedtuple('Segment', 'start end')
def min_segments(segments):
    index = 0
    for i in range(len(segments)):
        if segments[i].end < segments[index].end and index != i:
            index = i
    return index

def optimal_points(segments):
    points = []
    segments_copy = segments.copy()
    anchor = 0
    for i in range(len(segments)):
        argmin_index = min_segments(segments_copy)
        s = segments_copy[argmin_index]
        if i == 0:
            anchor = s.end
            points.append(anchor)
        else:
            if not((s.start <= anchor) and (anchor <= s.end)):
                anchor = s.end
                points.append(anchor)
        
        del segments_copy[argmin_index]
    return points

if __name__ == '__main__':
    input = sys.stdin.read()
    n, *data = map(int, input.split())
    segments = list(map(lambda x: Segment(x[0], x[1]), zip(data[::2], data[1::2])))
    points = optimal_points(segments)
    print(len(points))
    print(*points)
