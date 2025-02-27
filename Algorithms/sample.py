def get_nth_key(dictionary, n):
    if n < 0:
        n += len(dictionary)
    for i, key in enumerate(dictionary.keys()):
        if i == n:
            return key
    raise IndexError("dictionary index out of range") 

dict = {'cheese1': '1', 'cheese2': '2', 'cheese3': '3', 'cheese4': '4'}
n = int(input('Enter the index of an item: '))
n -= 1
m = get_nth_key(dict, n)
print(m)