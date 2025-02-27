colors = ["red", "green", "blue", "purple"]
print('For loop 1:')
for i in range(1,len(colors)):
    print(colors[i], end=' ')

print('\n\nFor loop 2:')
j = 0
for j in range(j+1, len(colors)):
    print(colors[j], end=' ')

print('\n\nFor loop 3:')
d = 1
for e in range(d+1, len(colors)-1):
    print(colors[e], end=' ')

print('\nhello','world', sep=' & ')