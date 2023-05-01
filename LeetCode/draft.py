# lower = pow(-2, 31)
# upper = pow(2, 31) -1
# print(f'Lower bound: {lower}')
# print(f'Upper bound: {upper}')

# array = [-12, 1234, 1534236469, -2147483412, 0 ]    
    
import random

# max = random.randrange(1, 100)

# for number in range(1,11):
#     print(number)
def isBadVersion():
    badNumber = random.randrange(1,11)
    return badNumber
    # if n == badNumber:
    #     print(f'{n} is bad number')
    # else:
    #     print(f'{n} is NOT bad number')

print(isBadVersion())