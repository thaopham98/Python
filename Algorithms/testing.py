roman = {"I":1, "V":5, "X":10, "L":50, "C":100, "D":500, "M":1000}
array = []
number = 0
i = 0
a='IV'
# a = input('Enter a string: ')
# print(a.upper())
for i in range(len(a)):
    if i+1<len(a):
        if roman[a[i]] >= roman[a[i+1]]:
            number += roman[a[i]]
            i += 1
        else:
            number -= roman[a[i]]
            i += 1
    else:
        number += roman[a[i]]
print(number)