# Description: 
#   This is an implementation of hash table.
#   The input is hashed into an integer.
#   The integer is used as an table index of the input in the hash table.
#   The hash table is an array of list to avoid any collision.
# Input Type: string & int

table_size = 50
hash_table=[[] for m in range(table_size)]

def main():
    while (True):
        input1 = input(">>> Input: ")

        try:
            if check_hash_table(input1) is True:
                print('%s is in hash table!' % input1)
            else:
                print('add %s in hash table' % input1)
                add_to_hash_table(input1)
        except Exception, e:
            print(e)
            break

        con = input(">>> Continue[y/n]: ")
        print(con)
        if con != 'y':
            print('Table: %s' % hash_table)
            break


def check_hash_table(input_val):
    try:
        index = hash_function(input_val)
        if input_val in hash_table[index]:
            return True
        else:
            return False
    except Exception, e:
        raise e

def add_to_hash_table(input_val):
    try:
        index = hash_function(input_val)
        hash_table[index].append(input_val)
    except Exception, e:
        raise e
    
def hash_function(input_val):
    input_type = type(input_val)
    if input_type is str:
        index = 0
        for char in input_val:
            index += ord(char)
        index = index % table_size
    elif input_type is int:
        index = input_val % table_size
    else:
        raise Exception('unsupported type: %s' % input_type)
    return index

if __name__ == '__main__':
    main()
