def lengthOfLastWord( s: str) -> int:
        space = ' '
        count = 0
        for n in reversed(s):
            if (n != space or s[-1] == ' '):
                # print(n)
                count += 1
            # else:
            #     return count
            return count
            

length = lengthOfLastWord('Hello World ')
print(length)