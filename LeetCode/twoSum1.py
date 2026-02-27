from typing import List
class Solution:
    def twoSum(self, numbers: List[int], target: int) :
        table = {} #creating empty hash table
        #Looping through the array 
        for i in range(len(numbers)): 
            x = target - i 
            #Comparing if x is in the list or not
            if x in numbers:
                return[table[x],i]

            else:
                table[numbers[i]] = i
test1 = Solution()
list = [2,7,11,15]
print(test1.twoSum(list,9))
