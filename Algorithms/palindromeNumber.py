def isPalindrome(x: int):
    rev_num = 0
    if x > 0:
        rev_num = (rev_num * 10) + (x % 10)
        x = x // 10
    elif x < 0:
        rev_num = (rev_num * 10) + (x%10)
        x = x // 10
    return rev_num
result = print(isPalindrome(-1234))