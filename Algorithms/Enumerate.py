# enumerate(iterable, start=0)
# Iterable: any object that supports iteration
# Start: the index value from which the counter is to be started, by default it is 0
l1 = ["eat", "sleep", "repeat"]
s1 = "geek"
 
# creating enumerate objects
obj1 = enumerate(l1)
obj2 = enumerate(s1)
 
print ("Type:", type(obj1))
print (list(enumerate(l1)))

# changing start index to 2 from 0
print (list(enumerate(s1, 2)))

# changing start index to 15 from 0
print(f"The start index is 15: {list(enumerate(s1, 15))}")

