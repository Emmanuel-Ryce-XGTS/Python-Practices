#Parte 1 fue mas introduccion

#Parte 2 Boolean Expressions
#My dog is the cutest dog in the world.
example_statement = "Yes"

# Statement one: Dogs are mammals.
statement_one = "Yes"

# Statement two: My dog is named Pavel.
statement_two = "Yes" or "No"

# Statement three: Dogs make the best pets.
statement_three = "Yes" and "No"

# Statement four: Cats are female dogs.
statement_four = "Yes" or "No"


"""Part 3 Relational Operators: Equals and Not Equals: 
These operators compare two items and return True or False if they are equal or not.
Equals: ==
Not equals: !=
"""

# Statement one: (5 * 2) - 1 == 8 + 1
statement_one = True

# Statement two: 13 - 6 != (3 * 2) + 1
statement_two = False

# Statement three: 3 * (2 - 1) == 4 - 1
statement_three = True


"""Part 4 Boolean Variables
Boolean variables can be created in several ways. 
The easiest way is to simply assign True or False to a variable:

set_to_true = True
set_to_false = False

bool_one = 5 != 7 
bool_two = 1 + 1 != 2
bool_three = 3 * 3 == 9
print(bool_one)    # True

print(bool_two)    # False

print(bool_three)  # True
"""

#.Create a variable named my_baby_bool and set it equal to the string "true"

my_baby_bool = "true"

#Check the type of my_baby_bool using type(my_baby_bool).

print(type(my_baby_bool))

#Create a variable named my_baby_bool_two and set it equal to True.

my_baby_bool_two = True

#Check the type of my_baby_bool_two and make sure you successfully created a boolean variable. And print
print(type(my_baby_bool_two))



"""Parte 5 If Statement: 
Understanding boolean variables and expressions is essential because 
they are the building blocks of conditional statements.

# Enter a user name here, make sure to make it a string
user_name = 

if user_name = "Dave":
  print("Get off my computer Dave!")
"""

#Result:
# Enter a user name here, make sure to make it a string
user_name = "Dave"

if user_name == "Dave":
  print("Get off my computer Dave!")
  
# Crear otro condicional.

if user_name == "AngelaCatlady_87":
  print("I know it is you, Dave! Go away!")


"""Parte 6 Relational Operators II: 
> greater than
>= greater than or equal to
< less than
<= less than or equal to
"""

#Create an if statement that checks if x and y are equal, print the string below if so:

x = 20
y = 20

#RESULT
#Create an if statement that checks if x and y are equal, print the string below if so:


# Write the first if statement here:

if x == y:
    print("These numbers are the same")



# Write the second if statement here:
credits = 120

if credits >= 120:
        print("You have enough credits to graduate!")



"""Parte 7 Boolean Operators: and: 
There are three boolean operators that we will cover:
and
or
not
"""

# Statement one: (2 + 2 + 2 >= 6) and (-1 * -1 < 0)

# Statement two: (4 * 2 <= 8) and (7 - 1 == 6)

statement_one = (2 + 2 + 2 >= 6) and (-1 * -1 < 0)
print(statement_one)

statement_two = (4 * 2 <= 8) and (7 - 1 == 6)
print(statement_two)


credits = 120
gpa = 3.4

if credits >= 120 and gpa >= 2.0:
  print("You meet the requirements to graduate!")
  
  
"""Parte 8 Boolean Operators Or:

The boolean operator or combines two expressions into a larger expression 
that is True if either component is True.

"""
#Set the variables statement_one and statement_two equal to the 
# results of the following boolean expressions:

#S1(2 - 1 > 3) or (-5 * 2 == -10)

statement_one = (2 - 1 > 3) or (-5 * 2 == -10)

#S2 (9 + 5 <= 15) or (7 != 4 + 3)
statement_two = (9 + 5 <= 15) or (7 != 4 + 3)



#Write an if statement that checks if a student either has 120 or 
# more credits or a GPA 2.0 or higher, and if so prints:

credits = 118
gpa = 2.0

if credits >= 120 or gpa >=2.0:
  print("You have met at least one of the requirements.")
  
  
  
  """Parte 9 Boolean Operators Not:

Boolean Operators: not
The final boolean operator we will cover is not. This operator is straightforward: 
when applied to any boolean expression it reverses the boolean value.
So if we have a True statement and apply a not operator we get a False statement.

"""

  
# statement_one = not (4 + 5 <= 9)
statement_one = False

# statement_two = not (8 * 2) != 20 - 4
statement_two = True

print(statement_two)

credits = 120
gpa = 1.8

if not credits >= 120:
  print("You do not have enough credits to graduate.")

if not gpa >= 2.0:
  print("Your GPA is not high enough to graduate.")

if not credits >= 120 and not gpa >= 2.0:
  print("You do not meet either requirement to graduate!")


 
"""Parte 10 Else statement:
Calvin Coolidge’s Cool College has another request for you. 
They want you to add an additional check to a previous if statement. 
If a student is failing to meet one or both graduation requirements, they want it to print:
"""

credits = 120
gpa = 1.9

if (credits >= 120) and (gpa >= 2.0):
  print("You meet the requirements to graduate!")
  
  #Resolve
else:
  print("You do not meet the requirements to graduate.")
  
"""Parte 11 Else if statement:
Write an if/elif/else statement that:

If grade is 90 or higher, print "A"
Else if grade is 80 or higher, print "B"
Else if grade is 70 or higher, print "C"
Else if grade is 60 or higher, print "D"
Else, print "F"

"""
grade = 86

if grade >= 90:
  print("A")
elif grade >= 80:
  print("B")
elif grade >= 70:
  print("C")
elif grade >= 60:
  print("D")
else:
  print("F")
  
  
  
#Review of the control Flow

print("I have information for the following planets:\n")

print("   1. Venus   2. Mars    3. Jupiter")
print("   4. Saturn  5. Uranus  6. Neptune\n")
 
weight = 185
planet = 3

# Write an if statement below:
if planet == 1:
  weight = weight * 0.91
elif planet == 2:
  weight = weight * 0.38
elif planet == 3:
  weight = weight * 2.34
elif planet == 4:
  weight = weight * 1.06
elif planet == 5:
  weight = weight * 0.92
elif planet == 6:
  weight = weight * 1.19

print("Your weight:", weight)
