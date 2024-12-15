'''
Please define an If function to find a minimum value of (a, b, c, d),
where a, b, c, d can be any number.
'''
import random  # including the random lib to generate 4 random variables.

''' Defining a function '''
def minValue(a, b, c, d):
    min = a  # Assuming the minimum value is a

    ''' Logic '''
    if b < min:
        min = b  # the current minimum value is b
    if c < min:
        min = c  # the current minimum value is c
    if d < min:
        min = d  # the current minimum value is d
    return min  # return the minimum value

'''
To avoid manually enter 4 inputs, randint() is utilized 
to get 4 random integers in a list comprehension
'''
a, b, c, d = [random.randint(1, 100) for _ in range(4)]  # assigns random ints (1-100) with a list comprehension
print(f"Random values: a={a}, b={b}, c={c}, d={d}")  # display the random results

print(f'Min value: {minValue(a, b, c, d)}')  # calling the minValue() with 4 ints and display the minimum value

'''
Manually enter inputs
'''
print(f'Min value: {minValue(56, 7, 212, 7234)}')