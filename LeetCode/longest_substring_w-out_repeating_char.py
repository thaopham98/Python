## Given a string s, find the length of the longest substring
## without duplicate characters
## Constraints:
# 0 <= s.length <= 105
# s consists of English letters, digits, symbols and spaces.

def lenthOfLognestSubstring1(s: str):
    if len(s) <= 0:
        return 0
    
    if len(s) == 1:
        return 1

    # acting as a sliding window, both start at the first char and only move forward
    right_pointer = 0 # this will move first, allowing the "window" to expand when find unique char
    left_pointer = 0 #  only move until the duplicate is removed 

    # keeping track of the char in that window
    window = set()
    longest = 0
    while right_pointer < len(s):
        # check if the s[right_pointer] is in window or now
        while s[right_pointer] in window:
            # update leftpoint 1 step at the time while also remove the same char from set
            window.remove(s[left_pointer])
            left_pointer += 1

        window.add(s[right_pointer])
        longest = max(longest, right_pointer - left_pointer + 1)
        right_pointer += 1

    return longest

def lenthOfLognestSubstring2(s: str):
    left = 0
    last_seen = {}
    longest = 0

    for right in range(len(s)):
        ch = s[right]

        if ch in last_seen:
            left = max(left, last_seen[ch] + 1)

        last_seen[ch] = right
        longest = max(longest, right - left + 1)

    return longest
    

print(f"Test 1: {lenthOfLognestSubstring2(s = 'abcabcbb')}") #3

print(f"Test 2: {lenthOfLognestSubstring2(s = 'bbbbb')}") #1

print(f"Test 3: {lenthOfLognestSubstring2(s = 'pwwkew')}") #3

print(f"Test 4: {lenthOfLognestSubstring2(s = '')}") #0

print(f"Test 5: {lenthOfLognestSubstring2(s = 'a')}") #1

print(f"Test 6: {lenthOfLognestSubstring2(s = 'pwwkewkewt')}") # 4