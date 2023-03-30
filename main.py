# python3

class Query:
    def __init__(self, query):
        self.type = query[0]
        self.number = int(query[1])
        if self.type == 'add':
            self.name = query[2]

def hash_func(number):
    ans=(2*number+3)%4
    return ans%5

def read_queries():
    n = int(input())
    return [Query(input().split()) for i in range(n)]

def write_responses(result):
    print('\n'.join(result))

def process_queries(queries):
    result = []
    # Keep list of all existing (i.e. not deleted yet) contacts.
    contacts = {}
    for cur_query in queries:
        number=cur_query.number
        if cur_query.type == 'add':
            # if we already have contact with such number,
            # we should rewrite contact's name
            hashed=hash_func(number)
            
            if hashed in contacts.keys():
           
                contacts[hashed][number]=cur_query.name

            else:
                contacts[hashed]={}
                contacts[hashed][number]=cur_query.name
            
            
        elif cur_query.type == 'del':
            hashed=hash_func(number)
            if hashed in contacts.keys():
                del(contacts[hashed][number])
        
        else:
            response = 'not found'
            hashed=hash_func(number)
            if hashed in contacts.keys():
                if number in contacts[hashed].keys():
                    response=contacts[hashed][number]
            result.append(response)
    return result

if __name__ == '__main__':
    write_responses(process_queries(read_queries()))

