"""
You are given a large integer represented as an integer array digits, 
where each digits[i] is the ith digit of the integer. 
The digits are ordered from most significant to least significant in left-to-right order. 
The large integer does not contain any leading 0's.

Increment the large integer by one and return the resulting array of digits.
"""
def plusOne(digits: list[int]):

    if len(digits) < 1: return 1 # return 1 if the list is empty

    # Coverting list[int] to int, then convert int to string
    nums = str(int(''.join(map(str,digits)))+1)
    
    # convert int to string
    # print(f'{nums} is {type(nums)}')
    digits = []
    for n in range(len(nums)): # Loop through the string and append to the list
        digits.append(int(nums[n]))
    return digits

list = [1,2,3,4]
# print(int(''.join(map(str,list)))+1)
print(plusOne(list))

# list[-1] = list[-1]+1
# print(list[-1])
# print(list)