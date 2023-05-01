"""
Write a function to find the longest common prefix 
string amongst an array of strings.
If there is no common prefix, return an empty string "".

"""

from typing import List
class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if len(strs) == 0 or len(strs) == 1:
            return ""
        
        # hash = {}
        # stack = []
        # Looping through the elements in the array
        # for e in range(len(strs[0])): # Looping through the 1st element in the array
        #     # print(e)
        #     print(strs[0][e])
        #     hash.append(e) # Appending to the hash table 
        """
        Appending the letters of the 1st word to hash table.

        Checking which letters in the next word are in the hash table more or not

        If yes, then append it to the a stack.

        If no, then pop it out of the stack.
        """
        

        


strs = ["flower","flow","flight"]
# strs = [] #empty list
test1 = Solution()
test1.longestCommonPrefix(strs)