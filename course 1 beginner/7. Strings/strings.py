
"""Part 4 Concatenating Strings in a function"""
first_name = "Julie"
last_name = "Blevins"

def account_generator(first_name , last_name):
  
  concatened_first = first_name[0:3]
  concatened_last = last_name[0:3]
  print(concatened_first + concatened_last)
  return concatened_first + concatened_last

account_generator(first_name , last_name)


new_account = account_generator(first_name , last_name)

print(new_account)


"""parte 5 de 12 More and More String Slicing (How Long is that String?)"""
first_name = "Reiko"
last_name = "Matsuki"

def password_generator(first_name, last_name): 
  string1 = first_name[-3:]
  string2 = last_name[-3:]
  string3 = string1 + string2
  print(string3)
  return string3

names = password_generator("Emmanuel", "Ariadne")

temp_password = names
print(temp_password)


"""Part 6 Negative Indices"""


company_motto = "Copeland's Corporate Company helps you capably cope with the constant cacophony of daily life"

second_to_last = company_motto[-2]

print(second_to_last)

final_word = company_motto[-4:]

print(final_word)


"""Part7 Strings are Immutable:
first_name = "Bob"
last_name = "Daily"
#first_name[0] = "R"
Then, concatenate the string "R" with a slice of first_name that includes everything 
but the first character, "B", and save it to a new string fixed_first_name.
"""


first_name = "Bob"
last_name = "Daily"

first_name = "R" + first_name[1:3]
fixed_first_name = first_name

print(fixed_first_name)

"""Part 9 Escape Characters
Occasionally when working with strings, you’ll find that you want to include characters that already have a special meaning in python. For example let’s say I create the string

favorite_fruit_conversation = "He said, "blueberries are my favorite!""

favorite_fruit_conversation = "He said, \"blueberries are my favorite!\""

"""
# password = "theycallme"crazy"91"
password = "theycallme\"crazy\"91"


favorite_fruit_conversation = "He said, \"blueberries are my favorite!\""

favorite_fruit_conversation = "He said, \"blueberries are my favorite!\""



"""Part 9 Iterating through Strings
def print_each_letter(word):
  for letter in word:
    print(letter)
favorite_color = "blue"
print_each_letter(favorite_color)
# => 'b'
# => 'l'
# => 'u'
# => 'e'
# """

def get_length(word):

  letter = "letter"
  for letter in word:
    print(letter)
  return len(word)

favorite_color = "blue"
get_length(favorite_color) 

 

# def get_length(input_string):
#     count = 0
#     for char in input_string:
#         count += 1
#     return count

# # Test the function
# input_string = "Hello, world!"
# length = get_length(input_string)
# print("Length:", length)


"""Part 10 Strings and Conditionals (Part One)

favorite_fruit = "blueberry"
counter = 0
for character in favorite_fruit:
  if character == "b":
    counter = counter + 1
print(counter)
"""

def letter_check(word, letter):
    return letter in word

# Example usage:
word = "example"
letter = "a"
result = letter_check(word, letter)
print(result)  # This will print True since "a" is in "example"

"""Part 11 Strings and Conditionals (Part 2)
Here is what the syntax of in looks like:

letter in word

Here, letter in word is a boolean expression that is True if the string letter is in the string word. Here are some examples:

print("e" in "blueberry")
# => True
print("a" in "blueberry")
# => False
"""


def contains(big_string, little_string):
    return little_string in big_string

# Example usage:
big_string = "watermelon"
little_string = "melon"
result = contains(big_string, little_string)
print(result)  # This will print True

big_string = "watermelon"
little_string = "berry"
result = contains(big_string, little_string)
print(result)  # This will print False



def common_letters(string_one, string_two):
    common = []  # Initialize an empty list to store common letters
    
    # Iterate through the characters of the first string
    for char in string_one:
        # Check if the character is in the second string and not already in the common list
        if char in string_two and char not in common:
            common.append(char)  # Append the character to the common list
    
    return common

# Example usage:
result = common_letters("banana", "cream")
print(result)  # This will print ['a']
 





# def contains(big_string, little_string):
#   big_string = "little_string"
#   return true, little_string
#   little_string = "little_string"

# contains(big_string, little_string)
# print(contains(big_string , little_string))

# print("little_string" in big_string)
