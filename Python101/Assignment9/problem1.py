'''
Please find the following
vector: 1, 2, 4, 8, 16, …., 256
Please use
for loop to print this vector.
Please attach
a screenshot of the code(input) and output.
'''

vector = [] # empty list
def forLoop(): # define the function
    for i in range(1,257): # for loop iterates from 1 to 256
        vector.append(i) # adding i to the end of vector for each iteration
    return vector # return the vector

print(forLoop()) # calling the defined function
# print(f'vector: {vector}')