"""
Given an integer array `nums` and an integer `val`, remove all occurrences of `val` in nums in-place. 
The order of the elements may be changed. 
Then return the number of elements in `nums` which are not equal to `val`.

Consider the number of elements in `nums` which are not equal to `val` be `k`,
to get accepted, you need to do the following things:

Change the array `nums` such that the first `k` elements of `nums` contain the elements which are not equal to `val`.
The remaining elements of nums are not important as well as the size of `nums`.
Return `k`.

"""
from typing import List

def removeElement(nums: List[int], val: int) -> int:
    if len(nums) < 1: return len(nums)

    """
    Since it's an in-place type of problem -> 2-pointer method:
    - `write_index` pointer This index keeps track of where the next non-`val` element should go
    - `i` pointer iterates through the array
    """
    write_index = 0 # start position at 0 
    for i in range(len(nums)):
        """
        Move the element to the front, if ums[write_index] != val.
        A.K.A. reassign position
        """
        
        if nums[i] != val:
            # print(f'{nums[write_index]} != {val}') #display value
            nums[write_index] = nums[i] # move nums[i] to nums[write_index]
            # print(f'nums[write_index] = {nums[write_index]}')
            write_index += 1
    # print(f'nums: {nums}')
    # print(f'write_index: {write_index}')

    return write_index

# k = removeElement([3,2,2,3], 3)
k = removeElement([0,1,2,2,3,0,4,2], 2)
# k = removeElement([4,3],3)
# k = removeElement([1],1)
print(k)