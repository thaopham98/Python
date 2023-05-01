coins=[] # Empty list

#Reading the text file
with open("input.txt", "r") as input_file: #Opening the file to read 
    for line in input_file: # Reading all the lines in text file
        line = int(line.replace('\n', '')) #Converting the lines into integer and removing \n of each line
        coins.append(line) #adding the integers to coins list
print('This is coins list: ', coins)

def factor3(coins, k): #tracking the index
  if len(coins) == 1 or len(coins) == 2: 
    return k
  
  #Finding the starting/stopping points
  first_mid = len(coins)//3 
  second_mid = (len(coins)//3)*2

  #Dividing into 3 parts
  left = coins[:first_mid] # [0:first_mid]
  middle = coins[first_mid:second_mid] #[first_mid:second_mid]
  right = coins[second_mid:] # [second_mid:0]

  #Comparing logic
  if sum(left) == sum(middle):
    return factor3(right, k+second_mid) #Rightside contents the fake coin
  elif sum(left) != sum(middle):
    if sum(left) < sum(middle):
      return factor3(left, k) #Leftside contents the fake coin
    else:
      return factor3(middle, k+first_mid) #Middle contents the fake coin
    
print('\nThe fake coin is in the index: ', 1+factor3(coins,0))
print('\n')