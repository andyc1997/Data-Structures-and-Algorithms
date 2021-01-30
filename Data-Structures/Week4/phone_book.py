# python3
def hash_num(number):
    a, b, p, m = 34, 2, 10 ** 8 + 19, 200000
    return ((a * number + b) % p) % m

class Query:
    def __init__(self, query):
        self.type = query[0]
        self.number = int(query[1])
        self.hash_number = hash_num(self.number)
        if self.type == 'add':
            self.name = query[2]
            
def read_queries():
    n = int(input())
    return [Query(input().split()) for i in range(n)]

def write_responses(result):
    print('\n'.join(result))

def process_queries_fast(queries):
    result, contacts = list(), dict()
    for cur_query in queries:
        # Add a new contact to hash table
        if cur_query.type == 'add':
            # If hash number is already in the dictionary
            if cur_query.hash_number in contacts:
                # If query phone number appears in the list, update name
                for contact in contacts.get(cur_query.hash_number):
                    if contact.number == cur_query.number:
                        contact.name = cur_query.name
                        break
                # if query phone number does not appear in the list, append it
                else:
                    contacts[cur_query.hash_number].append(cur_query)
            # if hash number does not appear in the dictionary
            else:
                contacts.update({cur_query.hash_number: list()})
                contacts[cur_query.hash_number].append(cur_query)
        # Del a contact in the dictionary
        elif cur_query.type == 'del':
            if cur_query.hash_number in contacts:
                for i in range(len(contacts.get(cur_query.hash_number))):
                    if contacts[cur_query.hash_number][i].number == cur_query.number:
                        contacts[cur_query.hash_number].pop(i)
                        break
        # Find a contact in the dictionary
        else:
            response = 'not found'
            if cur_query.hash_number in contacts:
                for contact in contacts[cur_query.hash_number]:
                    if contact.number == cur_query.number:
                        response = contact.name
                        break
            result.append(response)
    return result
                
def process_queries(queries):
    result = []
    # Keep list of all existing (i.e. not deleted yet) contacts.
    contacts = []
    for cur_query in queries:
        if cur_query.type == 'add':
            # if we already have contact with such number,
            # we should rewrite contact's name
            for contact in contacts:
                if contact.number == cur_query.number:
                    contact.name = cur_query.name
                    break
            else: # otherwise, just add it
                contacts.append(cur_query)
        elif cur_query.type == 'del':
            for j in range(len(contacts)):
                if contacts[j].number == cur_query.number:
                    contacts.pop(j)
                    break
        else:
            response = 'not found'
            for contact in contacts:
                if contact.number == cur_query.number:
                    response = contact.name
                    break
            result.append(response)
    return result

if __name__ == '__main__':
    write_responses(process_queries_fast(read_queries()))

