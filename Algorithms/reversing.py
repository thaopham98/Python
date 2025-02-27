"""Reversing digits"""
n = -1234
rev_num = 0
"""Time complexity: O(n)"""
# while n > 0:
#     rev_num = (rev_num * 10) + (n % 10)
#     # print(f'rev_num: {rev_num}')
#     n = n // 10 #arounding to the floor
#     # print(f'n: {n}')
# print(f'Final rev_num: {rev_num}')

"""Time complexity: O(logn): Recursion"""
# base_pos = 1
# def reverseRecusion(n: int):
#     global rev_num
#     global base_pos
#     if (n > 0):
#         reverseRecusion((int) (n/10))
#         rev_num = rev_num + (n % 10) * base_pos
#         base_pos = base_pos * 10
#         return rev_num
# print(reverseRecusion(1234))



"""Reversing string"""
# s = 'hello'[::-1]
# print(f's: {s}')

"""Reversing negative digit"""
# positive = n
# if n < 0:
#     positive *= -1

# while positive > 0:
#     rev_num = rev_num*10 + positive%10
#     positive = positive// 10
#     # print(rev_num)

# if n < 0:
#     # print(rev_num)
#     # print('Negative')
#     rev_num *= -1
#     # print(rev_num)

# print(rev_num)


