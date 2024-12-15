'''
String Function with a string parameter
'''
#Defining the string function with a parameter
def strFunc(x):
    print(f"I'm learning {x}")

strFunc('Python') # calling the string function with a string

'''
Numeric Function with numeric parameters
'''
def numFunc(a, b):
    return a*b
print(numFunc(3,5.6)) # calling
print(numFunc(3.4,5.6)) # calling