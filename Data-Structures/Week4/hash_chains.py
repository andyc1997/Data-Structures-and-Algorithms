# python3

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
        # store all strings in one list
        self.elems = dict()
        #self.elems = []

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
            # use reverse order, because we append strings to the end
            #self.write_chain(cur for cur in reversed(self.elems)
            #            if self._hash_func(cur) == query.ind)
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
#            try:
#                ind = self.elems.index(query.s)
#            except ValueError:
#                ind = -1
            if query.type == 'find':
                self.write_search_result(ind != -1)
            elif query.type == 'add':
                if ind == -1:
                    if hashed_string in self.elems:
                        self.elems[hashed_string].append(query.s)
                    else:
                        self.elems.update({hashed_string: [query.s]})
                    #self.elems.append(query.s)
            else:
                if ind != -1:
                    self.elems[hashed_string].pop(ind)
                    #self.elems.pop(ind)

    def process_queries(self):
        n = int(input())
        for i in range(n):
            self.process_query(self.read_query())

if __name__ == '__main__':
    bucket_count = int(input())
    proc = QueryProcessor(bucket_count)
    proc.process_queries()
