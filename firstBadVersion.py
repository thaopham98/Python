from typing import List
import random

class Solution:
    """Checking is the number is the bad version"""
    def firstBadVersion(self, n: int) -> int:
        badNumber = Solution.isBadVersion()
        if n == 1 and badNumber:
            return 1

        l = 1
        h = n

        while l <= h:
            m = l + (h - l)//2 # floor division

            if m == False: # good version
                l = m + 1
            else: # bad version
                #checking the number before m
                if m-1 == False: 
                    return m
                else:
                    h = m - 1

    


solution = Solution()
solution.firstBadVersion(5)