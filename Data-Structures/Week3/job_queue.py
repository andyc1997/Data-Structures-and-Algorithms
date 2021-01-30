# python3

from collections import namedtuple

AssignedJob = namedtuple("AssignedJob", ["worker", "started_at"])
#%%
class Heap():
    def __init__(self, arr):
        self.arr = arr
        self.thread = [i for i in range(len(arr))]
        
    def LeftChild(i):
        return 2 * i + 1
    
    def RightChild(i):
        return 2 * i + 2
    
    def Parent(i):
        return (i - 1) // 2
    
    def SiftUp(self, i):
        while (i > 0) & (self.arr[Heap.Parent(i)] > self.arr[i]):
            self.arr[Heap.Parent(i)], self.arr[i] = self.arr[i], self.arr[Heap.Parent(i)]
            i = Heap.Parent(i)
    
    def GetMin(self):
        return self.arr[0], self.thread[0]

    def ChangePriority(self, p):
        self.arr[0] += p
        Heap.SiftDown(self, 0)
        
    def SiftDown(self, i):
        minIndex = i
        # Left
        l = Heap.LeftChild(i)
        if l < len(self.arr):
            if self.arr[l] < self.arr[minIndex]:
                minIndex = l
            if (self.arr[l] == self.arr[minIndex]) & (self.thread[l] < self.thread[minIndex]):
                minIndex = l
        # Right
        r = Heap.RightChild(i)
        if r < len(self.arr):
            if self.arr[r] < self.arr[minIndex]:
                minIndex = r
            if (self.arr[r] == self.arr[minIndex]) & (self.thread[r] < self.thread[minIndex]):
                minIndex = r
        # Update
        if i != minIndex:
            self.arr[i], self.arr[minIndex] = self.arr[minIndex], self.arr[i]
            self.thread[i], self.thread[minIndex] = self.thread[minIndex], self.thread[i]
            Heap.SiftDown(self, minIndex)

#%% Modified assign_jobs
def pq_assign_jobs(n_workers, jobs):
    # TODO: replace this code with a faster algorithm.
    result = []
    next_free_time_heap = Heap([0] * n_workers)
    for i in range(len(jobs)):
        next_free_time, next_worker = next_free_time_heap.GetMin()
        result.append(AssignedJob(next_worker, next_free_time))
        next_free_time_heap.ChangePriority(jobs[i])
    return result

#%% Original assign_jobs
def assign_jobs(n_workers, jobs):
    # TODO: replace this code with a faster algorithm.
    result = []
    next_free_time = [0] * n_workers
    for job in jobs:
        next_worker = min(range(n_workers), key=lambda w: next_free_time[w])
        result.append(AssignedJob(next_worker, next_free_time[next_worker]))
        next_free_time[next_worker] += job
    return result

#%%
def main():
    n_workers, n_jobs = map(int, input().split())
    jobs = list(map(int, input().split()))
    assert len(jobs) == n_jobs

    assigned_jobs = pq_assign_jobs(n_workers, jobs)
    for job in assigned_jobs:
        print(job.worker, job.started_at)


if __name__ == "__main__":
    main()
