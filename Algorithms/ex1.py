import re

s = input("Enter your string: ")

#using RegEx to get the integers from the string
list = re.findall("\d", s)

res = []
for i in list:
    res.append(int(i))
print(f'res: {res}')
# numbs = [int(n) for n in list] #converting all elements in list into int.
# # print(numbs)
# # #converting list into string
# # numbs = ''.join(list)

result = []
i = 1
# for n in numbs:
#     # print('Type of numbs[n]',type(numbs[n]))
#     # print('numbs[n] is here',numbs[n])
#     # print('n is here: ',n)
#     if n < n+1:
#         result.append(n)
#         print(result)
#     else:
#         n += 1

for n in range(len(res)):
    if i <= 21:
        if res[n] < res[n+i]:
            result.append(res[n])
        else:
            result.clear()
        i+=1

    else:
        print('i is over 21')
print(result)
