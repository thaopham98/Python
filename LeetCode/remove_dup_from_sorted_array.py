"""
Given an integer array nums sorted in non-decreasing order, 
remove the duplicates in-place such that each unique element appears only once. 
The relative order of the elements should be kept the same. Then return the number of unique elements in nums.

Consider the number of unique elements of nums to be k, to get accepted, you need to do the following things:

Change the array nums such that the first k elements of nums contain the unique elements in the order they 
were present in nums initially.
The remaining elements of nums are not important as well as the size of nums.
Return k.
"""
from typing import List

def removeDuplicates(nums: List[int]) -> int:
    if len(nums) <= 1 :
        return len(nums)
    
    """
    Using 2-pointer: 
    - 1 pointer keeps track of the position of the NEXT UNIQUE element
    - 1 pointer iterates through the array
    """
    slow = 0 # track position of the next unique element

    for fast in range(1, len(nums)):
        if nums[slow] != nums[fast]:
            slow += 1
            nums[slow] = nums[fast]
    return slow + 1, nums


length = removeDuplicates([1, 1, 2, 2, 3, 4, 4])
print(length)


"""
Testings
"""
# nums = [1, 1, 2, 2, 3, 4, 4]
# slow = 0 # track position of the next unique element
# fast = 1 # iterate through the array
# for fast in range(1, len(nums)):
#     if nums[slow] != nums[fast]:
#         slow += 1
#         nums[slow] = nums[fast]
# print(nums)


# slow = 0 # track position of the next unique element
# fast = 1 # iterate through the array
# unique = [] # stores unique element of array

# for fast in range(1, len(nums)):
#     if nums[slow] != nums[fast]:
#         unique.append(nums[slow])
#         unique.append(nums[fast])
#     slow += 1
# print(unique)