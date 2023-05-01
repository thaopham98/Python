from typing import List
class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left = 0 #first element
        right = len(nums) - 1 #last element

        while left <= right:
            #finding the mid point
            mid = (left +right)//2
            if nums[mid] == target:
                return (f'Find the {target} at index {mid}')
            elif nums[mid] < target:
                print(f"{nums[mid]} < {target}. Moving the right")
                left = mid + 1
            else:
                print(f"{nums[mid]} > {target}. Moving the left")
                right = mid - 1

        return -1
        
t1 = Solution()
list = [-1,0,3,5,9,12]
print(t1.search(list, -1))