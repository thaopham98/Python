class Solution:
    def isPalindrome(self, x: int) -> bool:

        """Solution 1: This solution doesn't convert the int to a string. """
        rev = 0
        n = x # performing operations on n instead of x. This way x'll not change.
        # print(f'This is rev: {rev}. This is n: {n}')
        if (x < 0): # if the number is negative
            # print("The number is negative.")
            return False
            
        while n: # Looping through every digit
            # print(f'Looping through n: {n}') 
            # print("The number is positive.")

            #Reversing the number.
            rev = rev * 10 + n % 10
            # print('This is rev: ', rev)
            n//=10 # updating n 
            # print('This is n: ',n)

        return x == rev # Comparing if the rev is the same as x.

        """Solution 2: This solution converts the int to a string."""
        # x = str(x) #Coverting x into a string.
        # if x == x[::-1] and not('-') in x: # Only when x is positive
        #     return True
        # return False


test1 = Solution()
print(test1.isPalindrome(121)) #Displaying what is returned.