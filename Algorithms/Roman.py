# def romanToInt(string1: str) -> int:
#     dicts = {"I":1, "V":5, "X":10, "L":50, "C":100, "D":500, "M":1000}
#     # string1 = 'XII'
#     # n = len(string1)
#     # print(n)
#     numbers = []
#     for i in range(0, len(string1)): #Looping through a string
#         # print(string1[i]) #printing every characters of the string
#         # if string1[i] == 'I':
#         #     print(1)
#         # else:
#         #     print(-1)

#     #     if string1[i] in dicts:
#     #         # print(f'keys: {string1[i]}')
#     #         # print(f'values: {dicts.get(string1[i])}') #getting the values using keys
#     #         numbers.append(dicts.get(string1[i]))
            
#     #     else:
#     #         print(-1)
#     # print(f'numbers: {numbers}')
#     # print(f'Sum: {sum(numbers)}')
#         if dicts.get(string1[i]) < dicts.get(string1[i+1]):
#             print(f'{dicts.get(string1[i])} < {dicts.get(string1[i+1])}')
#             print(f'Smaller\n')
#         elif dicts.get(string1[i]) == dicts.get(string1[i+1]):
#             print(f'{dicts.get(string1[i])} == {dicts.get(string1[i+1])}')
#             print(f'Equal\n')
#         else:
#             print(f'{dicts.get(string1[i])} > {dicts.get(string1[i+1])}')
#             print(f'Larger\n')
        
# romanToInt("VI") #6
# romanToInt("IV") #4
# romanToInt("CDXLIII") #443

# class py_solution:
#     def roman_to_int(self, s):
#         rom_val = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
#         int_val = 0
#         for i in range(len(s)):
#             if i > 0 and rom_val[s[i]] > rom_val[s[i - 1]]:
#                 int_val += rom_val[s[i]] - 2 * rom_val[s[i - 1]]
#             else:
#                 int_val += rom_val[s[i]]
#         return int_val

# print(py_solution().roman_to_int('VI'))
# print(py_solution().roman_to_int('IV'))
# print(py_solution().roman_to_int('CDXLIII'))

roman = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
string = 'IV'
number = 0
print(f'Length of string: {len(string)}')
i = 0
while i<len(string): #going through even character in a string.
    if i+1<len(string): #making sure that it doesn't go out of range.
        if roman[string[i]] >= roman[string[i+1]]:
            number += roman[string[i]]
            i = i + 1
        else:
            number -= roman[string[i]]
            i = i + 1
    else: # at the last character
        number += roman[string[i]]
        break
print(f'Roman to integer: {number}')

# class Solution:
#     def romanToInt(self, s: str) -> int:
#         roman = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
#         number = 0
#         i = 0
#         while i<len(s): #going through even character in a string.
#             if i+1<len(s): #making sure that it doesn't go out of range.
#                 if roman[s[i]] >= roman[s[i+1]]:
#                     number += roman[s[i]]
#                     i = i + 1
#                 else:
#                     number -= roman[s[i]]
#                     i = i + 1
#             else: # at the last character
#                 number += roman[s[i]]
#                 break
#         return number

# roman = {'I':1,'V':5,'X':10,'L':50,'C':100,'D':500,'M':1000}
# class Solution:
#     def romanToInt(self, S: str) -> int:
#         ans = 0
#         for i in range(len(S)-1,-1,-1):
#             num = roman[S[i]]
#             if 4 * num < ans: ans -= num
#             else: ans += num
#         return ans