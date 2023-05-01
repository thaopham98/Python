from typing import List
class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        if (len(nums) <= 1) or (0 not in nums):
            # print(f'There \'s only 1 element in nums: ', nums)
            return nums
        
        # print(f'There \'s more than 1 element in nums: ', nums)
        i,j = 0,0
        n = len(nums)
        while i < n:
            if nums[i] != 0:
                nums[i], nums[j] = nums[j], nums[i]
                j+=1
            i +=1
        return nums
        """
        Time complexity: O(n), n is length of nums.
        Space complexity: 0(1).
        """
        
test1 = Solution()
list = [[0,1,8,0,3,12], [1,0], [0,0,1], [1], [1,2], [2,1]]
for j in list:
    print(test1.moveZeroes(j))