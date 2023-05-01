def shift_alphabet(string):
    '''Loop, convert to ASCII, increase by 1, convert to character, store, join'''
    new = [] # empty container
    for char in string:
        '''Converting each characters to ASCII code, using ord(), and increasing by 1'''
        to_ascii = ord(char)+1

        '''
        If ASCII code > the ASCII code of 'z', 
        then assigning the ASCII code to the ASCII code of 'a'
        '''
        if to_ascii > ord('z'):
            to_ascii = ord('a')

        '''Converting the new ASCII codes back to letters, using chr() '''
        to_char = chr(to_ascii)
        # print(f'Char: {to_char}')

        '''Appending the shifted letters to a container'''
        new.append(to_char)

    '''Converting characters from list to string, using join() '''
    return ''.join(new)
    

str = 'abcz'
print(shift_alphabet(str))