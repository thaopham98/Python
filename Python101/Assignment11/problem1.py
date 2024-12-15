"""
Please find the following series of numbers: 0, 4, 8, 12, 16, 20, 24, 28, 32, 36, ….
(add three more numbers here based on the trend)
Please use a function to output these 13 numbers.
(hint: use a loop function, and print i+3*i-4)

"""
# def extend_sequence(sequence, num_extrapolations=3):
#     difference = sequence[1] - sequence[0]
#     extended_sequence = sequence.copy()
#     for _ in range(num_extrapolations):
#         last_value = extended_sequence[-1]
#         extended_sequence.append(last_value + difference)
#     return extended_sequence
#
#
# # Example usage:
# original_sequence = [0, 4, 8, 12, 16, 20, 24, 28, 32, 36]
# # extended_sequence = extend_sequence(original_sequence, 3)
# # print(extended_sequence)
#
# def problem1(list):
#     for i in list:
#         print(i+3*i-4)
# problem1( extend_sequence(original_sequence, 3))

def generate_sequence(n):
  sequence = [] # empty list
  for i in range(n): # looping through the original list
    number = i + 3 * i - 4 # calculate the number
    sequence.append(number) # adding the number to the new list
  return sequence # return the new list after finish looping the original list

# Generate the first 13 numbers in the sequence
print(generate_sequence(13)) # calling the function and since we want it to display 13 values as input 
