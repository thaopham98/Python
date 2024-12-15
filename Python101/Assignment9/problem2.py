'''
Please find the
following vector: 1, 2, 4, 8, 16, …., 256
Please use
while loop to print this vector.
Please attach a screenshot of the code(input) and output.
'''
vector = [] # an empty list
i = 1 # variable to track the number of iteration
while i < 257: # while loop stops when i < 257
    # print(i) # display the value of i
    vector.append(i) # adding i to the end of vector for each iteration
    i = i + 1 # increase i by 1
print(vector) # display the content of vector