def regex(list):
    i = 0
    for word in list:
        print('\nRegex: ', word)
        if len(word) <= 1:
            print("There's only 1 or less letter: ", word)

        # print("There's more than 1 letter: ", word[i])
        if word[i] == word[-1]:
            print("Match")
        else:
            print('Not Match')

list1 = ['a','aa','babbab','an']
regex(list1)
print('\n')