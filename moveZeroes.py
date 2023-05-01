from typing import List
class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        '''
        zero = 0
        if len(nums) <= 1:
            print(f'There \'s only 1 element in nums: ', nums)
        else:
            print(f'There \'s more than 1 element in nums: ', nums)
            """
            Looping through the nums
            """
            for i in nums.copy():
                if i is 0:
                    zero += 1
                    nums.remove(i)
            # print(f'Zero: {zero}')
            # print(f'Nums: {nums}')
            
            """
            Adding zeros to the end of nums.
            """
            n = 0
            while zero > 0:
                nums.append(0)
                zero -= 1
            print(f'Nums: {nums}')

            """
            Time complexity: 2n => O(n).
            """
        '''

        print(nums.count(0))
        nums = [ i for i in nums if i != 0]



test1 = Solution()
nums = [0,1,8,0,3,12]
# nums = [1,0]
# nums= [0,0,1]
# nums = [1]
# nums =[1,2]
# nums = [2,1]
test1.moveZeroes(nums)