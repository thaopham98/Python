"""
Write a function to find the longest common prefix 
string amongst an array of strings.
If there is no common prefix, return an empty string "".
"""

from typing import List
class Solution:

    ''' 
    Finding the Longest Common Prefix
    by comparing the characters
    '''
    def common_prefix(left, right): 
        lcp = '' # An empty container that stores the longest common prefix
        for i in range(min(len(left), len(right))):
            if left[i] != right[i]: # If the characters are different, 
                return lcp # returning the container, the Longest Common Prefix.
            lcp += left[i] # Adding characters to the empty container
        return lcp 
        
    '''
    Diving the strings using Divide and Conquer Algorithm
    ''' 
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if len(strs) == 0: 
            return ""
        elif len(strs) == 1:
            return strs[0]
        
        mid = len(strs) // 2
        left = self.longestCommonPrefix(strs[:mid])
        right = self.longestCommonPrefix(strs[mid:])
        return Solution.common_prefix(left,right)

strs = ["flower","flow","flight"]
test1 = Solution()
print(test1.longestCommonPrefix(strs))