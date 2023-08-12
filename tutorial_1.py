#1. Randomly select an element from a list
my_list = [1,2,3,4,5]
my_element = me_list[0]
#2. Generate a random number in 0/1
import random
random uniform = random.(0, 1)
#3. Use random in 0/1 to mask 50% of the words in a string
my_string = "Hello World!"
my_string = "H-l-o W-rl-!"
my_string[2] = "-"

for i in range(len)(my_string)):
  rand_number = random.uniform(0,1)
  if(rand_number<0.5):
    my_string[i] = "-"
#4. Use random in 0/1 to mask 70% of the words in a string
my_string = "Hello World!"
my_string = "H-l-o W-rl-!"
my_string[2] = "-"

for i in range(len)(my_string)):
  rand_number = random.uniform(0,1)
  if(rand_number<0.7):
    my_string[i] = "-"
#5. Turn a string into capital/lowercase letters
my_str = "Hello World"
my_str.upper()
my_stri.lower()
#6. Get an input from the user using the default input() method
my_string = input ()
#7. Check if an element is in a list/dictionary using the 'in' statement
my_string = "Hello World!"
if("w" in my_string):
  
#8. Remove an element from a list/dictionary
my_list = [23, 4, 7 , 1, 22, 23]
my_target = 7
for i in range(len(my_list)):
  if(my_list[i]==my_target):
#9. Load in memory the content of a text file
file = "Users/kamila/12345.txt"
f = open(file)
data = f.readlines()

#10. The use of enumerate() in a for loop
my_list = [23, 4, 7, 22, 33]

for element in my_list:
  print(element)
#11. Define a function that returns more than one element (introduce the idea of "tuple")
my_list = [23, 4, 7, 22, 33]
for idx, elem in enumerate (my_list):
  print (idx, elem)
  
# Exercise
# - take a random word as string e.g. "umbrella"
# - Iterate over all the characters in the string with a for-loop (with enumerate)
# - Use the character as key of a dictionary
# - For each key add a list as value that contains the positions/index
#     of that character in the string.
#
# e.g. for the word "umbrella" the dictionary should be: 
# {'u': [0], 'm': [1], 'b': [2], 'r': [3], 'e': [4], 'l': [5, 6], 'a': [7]}

my_string = "gemstone"
for idx, elem in enumerate(my_list):
  print(idx, elem)
my_dict = {'g': [0], 'e': [1, 7], 'm': [2], 's': [3], 't': [4], 'o': [5], 'n' [6]}
