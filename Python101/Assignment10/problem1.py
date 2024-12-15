"""
Creating the matrix
"""
m = [
    [1, 34, 22, 9, 8, 6],
    [5, 12, 23, 45, 12, 7],
    [41, 15, 35, 30, 11, 12],
    [32, 18, 12, 12, 13, 16],
    [60, 20, 8, 10, 22, 72]
]

"""
Nested loop through the matrix
"""
for r in m: # looping through the row first
    for c in r: # looping through the c in each r
        print(c)