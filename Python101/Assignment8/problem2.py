"""
Please develop a calculator using if (and elif) functions. 
The calculator calculates 12 × a OPS 7, where “OPS” is a operator that could be +, -, ×, or /. 
"""
''' Define calculator()'''
def calculator(v1, v2, ops):
    if ops == '+':
        return v1+v2
    elif ops == '-':
        return v1-v2
    elif ops == '*':
        return v1*v2
    elif ops == '/':
        return v1/v2
    else:
        return "Invalid input"

''' User inputs'''
v1 = int(input('Enter int 1: '))
v2 = int(input('Enter int 2: '))
ops = input('Enter one of the operators + - * / : ')

print(f'Result = {calculator(v1,v2,ops)}') # calling calculator()
