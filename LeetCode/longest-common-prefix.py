"""
Write a function to find the longest common prefix 
string amongst an array of strings.
If there is no common prefix, return an empty string "".

"""

from typing import List
class Solution:

    def common_prefix(self,left, right):
        lcp = ''
        for i in range(min(len(left), len(right))):
            if left[i] != right[i]:
                return lcp
            lcp += left[i]
        return lcp
        
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if len(strs) == 0: 
            return ""
        elif len(strs) == 1:
            return strs[0]
        else:
            mid = len(strs) // 2
            left = self.longestCommonPrefix(strs[:mid])
            right = self.longestCommonPrefix(strs[mid:])
            return self.common_prefix(left,right)

strs = ["flower","flow","flight"]
test1 = Solution()
print(test1.longestCommonPrefix(strs))