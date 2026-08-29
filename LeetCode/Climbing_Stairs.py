# You are climbing a staircase. It takes n steps to reach the top.

# Each time you can either climb 1 or 2 steps. In how many distinct ways can you climb to the top?

# Example 1:

# Input: n = 2
# Output: 2
# Explanation: There are two ways to climb to the top.
# 1. 1 step + 1 step
# 2. 2 steps

# Example 2:

# Input: n = 3
# Output: 3
# Explanation: There are three ways to climb to the top.
# 1. 1 step + 1 step + 1 step
# 2. 1 step + 2 steps
# 3. 2 steps + 1 step

# n = 4
# 1+1+1+1
# 2+1+1
# 1+2+1
# 1+1+2
# 2+2


# n = 5
# 1+1+1+1+1
# 

def climbStairs( n: int) -> int:

    # base cases
    s1 = 1 # step 1
    s2 = 2 # step 2

    # if n==2:
    #     return s2
    # elif n ==1:
    #     return s1

    #or
    if n<=2:
        return n

    # start the loop when n>2
    for i in range(3, n+1): # start the loop at i=3
        res = (s1)+(s2)
        s1= s2
        s2 = res

    return res
        

test1 = climbStairs(5)
print("result:",test1)