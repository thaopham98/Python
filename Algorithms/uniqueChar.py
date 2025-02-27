char=[]
def uniqueChar(line): 
    for i in line:
        if i not in line:
            char.append(i)
        
    for i in char:
        print(i)
            

line = input("Please enter a line: ")
print(uniqueChar(line))
