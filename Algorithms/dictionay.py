"""user_0={'username': 'efermi', 'first': 'enrico', 'last': 'fermi'}

#adding item into dictionary
user_0['number'] = '0'

for key, value in user_0.items():
    print("\nKey: "+key)
    print('\nValue: '+value)

#removing item from dictionary
del user_0['number']

for key, value in user_0.items():
    print("\nKey: "+key)
    print('\nValue: '+value)"""


closing = ')]}'
opening = '{[('
mixing = '{[()]}'
mixing1 = '{(}]]{[(})'
parens = {'(': ')', 
          '{': '}', 
          '[': ']'}

stack = []

for key in mixing1:
    # if key in parens:
    #     print(f'Not Found: {key} {parens[key]}')
        
    # else:
    # # print('Found.')
    # # print(type(i))
    #     # print(f'key: {key}, value: {parens[key]}')
    #     print(parens[key]) # displaying value 
# print(parens['['])
    # print(key in parens)
    value = 1
    if key in parens.keys():
        # print(f'{parens.get(key)} is in the string') 
        stack.append(key)
    else:
        # print(f'{key} is NOT in the string')
        if stack == []:
            print(False)
        
        a = stack.pop()
        print(f'a: {a}')

        if key != parens[a]:
            print(False)


        

