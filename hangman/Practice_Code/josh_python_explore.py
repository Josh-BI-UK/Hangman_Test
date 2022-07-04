# my_name = 'Joshua'
# if len(my_name) < 3:
#     print(my_name)
# else:
#print('type letter')

# letter = input('select letter')
# word = 'apple'
# letters_in_word = list((word)*1)
# print(letters_in_word)
# letter_pos = letters_in_word.index(letter)
# print(letter_pos)

# string input
print('Please type a letter for input_a')
input_a = input()
 
# print type
# print('String test: ',type(input_a))
 
# integer input
print('Please type a letter for input_b')
input_b = input()
try:
    input_c = print(int(input_b))
except ValueError as ve: print('Integer test',input_b)
# print type
