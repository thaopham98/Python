"""
FizzBuzz. Print numbers from 1 to 100

    If it’s a multiplier of 3, print “Fizz”
    If it’s a multiplier of 5, print “Buzz”
    If both 3 and 5 — “Fizz Buzz"
    Otherwise, print the number itself
Example of output: 1, 2, Fizz, 4, Buzz, Fizz, 7, 8, Fizz, Buzz, 11, Fizz, 13, 14, Fizz Buzz
, 16, 17, Fizz, 19, Buzz, Fizz, 22, 23, Fizz, Buzz, 26, Fizz, 28, 29, Fizz Buzz, 31, 32, Fizz, 34, Buzz, Fizz, ...
"""
for i in range (1, 101):
    if i % 3 == 0 and i % 5 == 0 :
        print('Fizz Buzz')
    elif i % 3 == 0:
        print('Fizz')
    elif i % 5 == 0:
            print('Bizz')
    else:
        print(i)