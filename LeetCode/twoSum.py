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
        # table = {} #creating empty hash table
        # # #Looping through the array 
        # for num in range(len(nums)):
        #     # diff = target - nums[num]

        #     if target - nums[num] in table:
        #         return [table[target - nums[num]], num]
        #     table[nums[num]] = num

        # return []


        """Solution3: also use Hash Table"""
        table = {}

        for num in range(len(nums)):
            diff = target - nums[num]

            if diff in table:
                return [table[diff], num]

            table[nums[num]] = num

list = [2,7,11,15]
test1 = Solution()
print(test1.twoSum(list, 9))

test2 = Solution()
print(test2.twoSum([5,5], 10))