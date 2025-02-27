with open('products.txt') as inputFile:
    contents = inputFile.read()
    print(contents)

    name = []
    number1 = []
    number2 = []

    #using REGLEX to sort the content
    for n in inputFile:
        name.append(n)