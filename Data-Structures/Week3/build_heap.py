# python3


def build_heap(data):
    """Build a heap from ``data`` inplace.

    Returns a sequence of swaps performed by the algorithm.
    """
    # The following naive implementation just sorts the given sequence
    # using selection sort algorithm and saves the resulting sequence
    # of swaps. This turns the given array into a heap, but in the worst
    # case gives a quadratic number of swaps.
    #
    # TODO: replace by a more efficient implementation
    swaps = []
    for i in range(len(data)):
        for j in range(i + 1, len(data)):
            if data[i] > data[j]:
                swaps.append((i, j))
                data[i], data[j] = data[j], data[i]
    return swaps

class Heap():
    def __init__(self, arr):
        self.arr = arr
        self.swap = []
        
    def LeftChild(i):
        return 2 * i + 1
    
    def RightChild(i):
        return 2 * i + 2
    
    def Parent(i):
        return (i - 1) // 2

    def SiftDown(self, i):
        minIndex = i
        # Left
        l = Heap.LeftChild(i)
        if l < len(self.arr):
            if self.arr[l] < self.arr[minIndex]:
                minIndex = l
        # Right
        r = Heap.RightChild(i)
        if r < len(self.arr):
            if self.arr[r] < self.arr[minIndex]:
                minIndex = r
        # Update
        if i != minIndex:
            self.swap.append((i, minIndex))
            self.arr[i], self.arr[minIndex] = self.arr[minIndex], self.arr[i]
            Heap.SiftDown(self, minIndex)

def BuildHeap(arr):
    size = len(arr)
    heap = Heap(arr)
    
    for i in reversed(range(0, size // 2)):
        heap.SiftDown(i)
    return heap.swap

def main():
    n = int(input())
    data = list(map(int, input().split()))
    assert len(data) == n
    
    swap = BuildHeap(data)
    print(len(swap))
    if len(swap) > 0:
        for i, j in swap:
            print(i, j)
    #swaps = BuildHeap(data)

    #print(len(swaps))
    #for i, j in swaps:
    #    print(i, j)


if __name__ == "__main__":
    main()
