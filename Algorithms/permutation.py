letters = 'ABCDEFGHIJKLMNOPQSTUVWXYZ' 

user_input = int(input('Please enter n to do the permutations (1-26): '))
string = letters[0:user_input] #getting the letters/number from 1 to user_input
#The list starts from the beginning till before the userinput number
#Example: [0:4] -> a,b,c,d

result = [] #empty list

def permutation(a, left_letter, right_letter): #parameters: list, position, position
	if left_letter == right_letter:
		result.append(''.join(a))
	else:
		for j in range(left_letter, right_letter):
			a[left_letter], a[j] = a[j], a[left_letter] #swapping 
			permutation(a, left_letter + 1, right_letter) 
			a[left_letter], a[j] = a[j], a[left_letter] #swapping 

permutation(list(string), 0, len(string))

print('\n'.join(result))