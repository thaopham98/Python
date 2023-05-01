"""
Given a string s containing just the characters 
'(', ')', '{', '}', '[' and ']', 
determine if the input string is valid.

An input string is valid if:

Open brackets must be closed by the same type of brackets.
Open brackets must be closed in the correct order.
Every close bracket has a corresponding open bracket of the same type.

"""
from typing import List
class Solution:
    def isValid(self, s: str) -> bool:
        if len(s) % 2 != 0 or len(s)<1:
            return False
        
        dict = {'(' : ')', 
                '[' : ']', 
                '{' : '}'}
        
        stack = [] # Keeping track of openning bracket. FIFO order

        for i in s:
            """
            Checking if the bracket is open/close
            """
            if i in dict.keys(): # Opening brackets goes here
                # print(f'opening bracket: {i} {s[i]}')
                # print(f'i in dict: {i} {dict[i]}')
                stack.append(i) # appending the i to stack
            else: # Closing brackets goes here
                # print(f'closing bracket: {i} {s[i]}')
                # print(f'i not in dict.')

                if stack == []: # No openning bracket
                    # print(f'Stack is empty == No openning bracket')
                    return False
                
                last_e = stack.pop() # FIFO order 

                if i != dict[last_e]: # Comparing the input bracket with the bracket of the stack's element
                    # print(f'{i} && {dict[last_e]}')
                    # print(f'No matching close bracket')
                    return False
                
        """
        Return True if stack is empty, 
        Return False if stack is not empty.
        """
        return stack == []
        print(f'\tStack: {stack}')
        
test_cases = ['()', '', '(}', '(){}[]', '{[()]}', ')]}', ']', 'asdfhkasd', '234', '((' ]
"""TRUE, FALSE, FALSE, TRUE, TRUE, FALSE, FALSE, FALSE, FALSE, FALSE"""

test1=Solution()
for case in test_cases:
    # print(f'{case}: {test1.isValid(case)}\n')
    print(f'{test1.isValid(case)}\n', end="")
