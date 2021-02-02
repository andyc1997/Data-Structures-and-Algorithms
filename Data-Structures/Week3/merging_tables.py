# python3


class Database:
    def __init__(self, row_counts):
        self.row_counts = row_counts
        self.max_row_count = max(row_counts)
        n_tables = len(row_counts)
        self.ranks = [1] * n_tables
        self.parents = list(range(n_tables))
        self.symlinks = list(range(n_tables))

    def compare_max(self, k):
        if self.max_row_count < self.row_counts[k]:
            self.max_row_count = self.row_counts[k]
            
    def union(self, i, j):
        if self.ranks[i] > self.ranks[j]:
            self.parents[j] = i
            self.row_counts[i] += self.row_counts[j]
            self.row_counts[j] = 0
            self.compare_max(i)
        else:
            self.parents[i] = j
            self.row_counts[j] += self.row_counts[i]
            self.row_counts[i] = 0
            self.compare_max(j)
            if self.ranks[i] == self.ranks[j]:
                self.ranks[j] += 1
                
    def merge(self, src, dst):
        src_parent = self.get_parent(src)
        dst_parent = self.get_parent(dst)

        if src_parent == dst_parent:
            return False
        # merge two components
        # use union by rank heuristic
        self.union(src_parent, dst_parent)
        # update max_row_count with the new maximum table size
        # print('Row counts: ', self.row_counts, 'src: ', src, 'dst: ', dst)
        # print('Parents: ', self.parents)
        # print('Ranks: ', self.ranks)
        return True

    def get_parent(self, table):
        # find parent and compress path
        if table != self.parents[table]:
            self.parents[table] = self.get_parent(self.parents[table])
        return self.parents[table]


def main():
    n_tables, n_queries = map(int, input().split())
    counts = list(map(int, input().split()))
    assert len(counts) == n_tables
    db = Database(counts)
    for i in range(n_queries):
        dst, src = map(int, input().split())
        db.merge(src - 1, dst - 1)
        print(db.max_row_count)


if __name__ == "__main__":
    main()
