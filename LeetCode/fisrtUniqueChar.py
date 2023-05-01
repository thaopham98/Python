def firstUniqueChar(str):
    '''Empty container to store the characters'''
    store = {}
    '''Looping thru the string'''
    for index in str:
        if index not in  store:
            store[index] = 1
        else:
            store[index] += 1
    
    for index in range(len(str)):
        if store[str[index]] == 1:
            return index
    return -1

samples = ['leetcode', 'banana', 'abaabba', 'aabbdf']
for sample in samples:
    print(firstUniqueChar(sample))
