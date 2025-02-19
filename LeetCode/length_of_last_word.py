"""
Given a string `s` consisting of words and spaces, return the length of the last word in the string.
"""

def lengthOfLastWord( s: str) -> int:
    
    """
    Handling empty OR all-space string
    """
    if len(s) == 0 or s.isspace(): # Check for all spaces OR empty string
        return 0 

    found_last_word = False
    count = 0

    """
    since this is about the last word of a string, we can just start at the end of the string
    using `reversed()`
    """

    for n in reversed(s):
        if n != ' ': # skipping/ingoring the ' ' when counting the string 
            found_last_word = True # signaling the it finds non-space char
            count += 1 # start counting the non-space char
        elif found_last_word: # # If you've already found the last word AND hit a space
            break # the loop break/stop
        
    return count            
            
print(lengthOfLastWord(' fad sgfdf s '))