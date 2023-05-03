"""
Given a signed 32-bit integer x, return x with its digits reversed. If reversing x 
causes the value to go outside the signed 32-bit integer range [-2^31, 2^31 - 1], then return 0.
Assume the environment does not allow you to store 64-bit integers (signed or unsigned).

"""

from typing import List
class Solution:
    def reverse(self, x: int) -> int:
        """if x == 0:
            return x

        if x>0:
            #convert number to string 
            num_string = str(x)

            # use slicing to reverse 
            reversed_num = num_string[len(num_string)::-1]

            #output reversed number
            # print("Reversed Number is: " + reversed_num)
            return reversed_num
        else:
            positive = x *(-1)
            # print(positive)
            num_string = str(positive)
            # print(f'num_string: {num_string}')

            # use slicing to reverse 
            reversed_num = num_string[len(num_string)::-1]
            # print(f'reversed_num: {reversed_num}')
        
            str_num = int(reversed_num) * -1
            # print(str_num)
            
            return str_num"""
        
        rev_num = 0
        positive = x

        if x < 0: # if x is negative,
            positive *= -1 # making it positive without changing x.

        while positive > 0:
            rev_num = rev_num*10 + positive%10
            positive = positive // 10

        if x < 0: #if x is negative,
            rev_num *= -1 # after reversing change the number back to negative.

        if (pow(2,31)-1 <= rev_num) or (pow(-2,31) >= rev_num):
            return 0
        
        return rev_num
    
test1 = Solution()
array = [-12, 1234, 1534236469, -2147483412, 0 ,-2147483648]
for x in array :
    result = test1.reverse(x)
    print(result)