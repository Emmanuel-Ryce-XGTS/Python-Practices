"""
    Review
Great work! I hope you are now starting to see the potential of strings and how they can be used to solve a huge variety of problems.

In this lesson you learned:

A string is a list of characters.
A character can be selected from a string using its index string_name[index]. These indices start at 0.
A ‘slice’ can be selected from a string. These can be between two indices or can be open-ended, selecting all of the string from a point.
Strings can be concatenated to make larger strings.
len() can be used to determine the number of characters in a string.
Strings can be iterated through using for loops.
Iterating through strings opens up a huge potential for applications, especially when combined with conditional statements.
Let’s put your new skills to the test!
    
    
# Define the username_generator function
def username_generator(first_name, last_name):
    # Take the first three letters of the first name and the first four letters of the last name
    username = first_name[:3] + last_name[:4]
    return username

# Define the password_generator function
def password_generator(user_name):
    password = ""  # Initialize an empty string for the password
    
    # Iterate through the indices of user_name
    for i in range(len(user_name)):
        # Add the letter at the previous index to the password
        password += user_name[i-1]
    
    return password

# Example usage:
first_name = "Abe"
last_name = "Simpson"
user_name = username_generator(first_name, last_name)
temporary_password = password_generator(user_name)

print("Username:", user_name)
print("Temporary Password:", temporary_password)

    """
    
# Define the username_generator function
def username_generator(first_name, last_name):
    # Take the first three letters of the first name and the first four letters of the last name
    username = first_name[:3] + last_name[:4]
    return username

# Define the password_generator function
def password_generator(user_name):
    password = ""  # Initialize an empty string for the password
    
    # Iterate through the indices of user_name
    for i in range(len(user_name)):
        # Add the letter at the previous index to the password
        password += user_name[i-1]
    
    return password

# Example usage:
first_name = "Abe"
last_name = "Simpson"
user_name = username_generator(first_name, last_name)
temporary_password = password_generator(user_name)

print("Username:", user_name)
print("Temporary Password:", temporary_password)
