# python3
# Task. In this task your goal is to implement a hash table with lists chaining. You are already given the
# number of buckets m and the hash function. It is a polynomial hash function. 
# Your program should support the following kinds of queries:
# 1. add string — insert string into the table. If there is already such string in the hash table, then just ignore the query.
# 2. del string — remove string from the table. If there is no such string in the hash table, then just ignore the query.
# 3. find string — output “yes" or “no" (without quotes) depending on whether the table contains string or not.
# 4. check i — output the content of the i-th list in the table. Use spaces to separate the elements of the list. If i-th list is empty, output a blank line.
# Input Format. There is a single integer m in the first line — the number of buckets you should have. The next line contains the number of queries N. 
# It’s followed by N lines, each of them contains one query in the format described above.
# Output Format. Print the result of each of the find and check queries, one result per line, in the same
# order as these queries are given in the input.

class Query:
    def __init__(self, query):
        self.type = query[0]
        if self.type == 'check':
            self.ind = int(query[1])
        else:
            self.s = query[1]

class QueryProcessor:
    _multiplier = 263
    _prime = 1000000007

    def __init__(self, bucket_count):
        self.bucket_count = bucket_count
        self.elems = dict()

    def _hash_func(self, s):
        ans = 0
        for c in reversed(s):
            ans = (ans * self._multiplier + ord(c)) % self._prime
        return ans % self.bucket_count

    def write_search_result(self, was_found):
        print('yes' if was_found else 'no')

    def write_chain(self, chain):
        print(' '.join(chain))

    def read_query(self):
        return Query(input().split())

    def process_query(self, query):
        if query.type == "check":
            if query.ind in self.elems:
                self.write_chain(reversed(self.elems[query.ind]))
            else:
                self.write_chain('')
        else:
            hashed_string = self._hash_func(query.s)
            ind = -1
            if hashed_string in self.elems:
                if query.s in self.elems[hashed_string]:
                    ind = self.elems[hashed_string].index(query.s)

            if query.type == 'find':
                self.write_search_result(ind != -1)
            elif query.type == 'add':
                if ind == -1:
                    if hashed_string in self.elems:
                        self.elems[hashed_string].append(query.s)
                    else:
                        self.elems.update({hashed_string: [query.s]})
            else:
                if ind != -1:
                    self.elems[hashed_string].pop(ind)

    def process_queries(self):
        n = int(input())
        for i in range(n):
            self.process_query(self.read_query())

if __name__ == '__main__':
    bucket_count = int(input())
    proc = QueryProcessor(bucket_count)
    proc.process_queries()
