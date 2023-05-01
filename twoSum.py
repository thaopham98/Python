from typing import List # for List[int]
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        """Solution 1: Using Bubble Sort"""
        # for i in range(len(nums)): #Traverse through all array elements
        #     for j in range(i+1,len(nums)): #Starting from i+1
        #         if nums[i] + nums[j] == target:
        #             # print(f'i: {list[i]} and j: {list[j]}')
        #             # print(f'i: {i}, j: {j}')
        #             return [i,j]

        """Solution 2: Using Hash Table dict()"""
        hashTable = {} # Creating an empty dict
        
        


test1 = Solution()
test1.twoSum(12, 31)
