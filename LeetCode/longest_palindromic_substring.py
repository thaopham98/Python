def longestPalindrome( s: str) -> str:
    newStr = ''
    longest = 0

    for i in range(len(s)):

        # for ODD length str:
        left1, right1 = i, i
        # IN-BOUND and the chars are the same
        while left1 >= 0 and right1 < len(s) and s[left1] == s[right1] :
            # if the position is LARGER than longest
            if (right1 - left1 + 1) > longest:
                newStr = s[left1:right1+1] # Add that char to the list
                longest = right1 - left1 + 1 # update the longest
            # Moving outward to the next chars
            left1 -= 1
            right1 += 1

        # for EVEN length str:
        # IN-BOUND and the chars are the same
        left2, right2 = i, i + 1
        while left2 >= 0 and right2 < len(s) and s[left2] == s[right2]:
            if (right2 - left2 + 1) > longest:
                newStr = s[left2:right2+1] # Add that char to the list
                longest = right2 - left2 + 1 # update the longest
            left2 -= 1
            right2 += 1
    
    return newStr



def check(label, actual, expected_options):
    status = "OK" if actual in expected_options else "FAIL"
    print(f"[{status}] {label}: got {actual!r}, expected one of {expected_options!r}")

check("single char", longestPalindrome("a"), {"a"})
check("two same", longestPalindrome("cc"), {"cc"})
check("two diff", longestPalindrome("ac"), {"a", "c"})
check("odd length", longestPalindrome("babad"), {"bab", "aba"})
check("even length", longestPalindrome("cbbd"), {"bb"})
check("whole string", longestPalindrome("racecar"), {"racecar"})
check("repeated chars", longestPalindrome("aaaa"), {"aaaa"})

# o = "babad"
# o = "mhnhmdsvm"
# o = "ac"
# newstr = ''
# longest = 0

# for i in range(len(o)):

#     if len(o)%2==1: # ODD str
#         left, right = i, i
#     elif len(o)%2==0: # EVEN str
#         left, right = i, i + 1

#     # print(f"left: {left}, char: {o[left]}")
#     # print(f"left: {right}, char: {o[right]}")

#     # each while loop is basically a char, and check left and right of that char
#     while left >= 0 and right < len(o) and o[left]==o[right]:

#         # only update newStr and longest when the current char's index is larger than longest 
#         if right-left+1 > longest:
#             newstr = o[left:right+1]
#             # print(newstr)
#             longest = right - left + 1 

#         # moving to the next char
#         left = left - 1
#         right = right + 1
# print(f"Results: {newstr}")