# PART1 Welcome: Change Codecademy to your name in the script to the right. Run the code to see what it does!
# my_name = "Codecademy"
# print("Hello and welcome " + my_name + "!")

#RESULT Part1 

my_name = "Emmanuel Ryce"
print("Hello and welcome " + my_name + "!")


# PART2 Documentation is an important step in programming.
# Write a comment describing the first program you want to write!

#RESULT Part2]: Documentamos con valores asignados
print("\nHaremos una multiplicación \n")
valor = 7
multiplo = 7
total = valor * multiplo
print("El resultado de multiplicar: ", valor, "*", multiplo ,'es: ', total)

#RESULT Part2]: Documentamos con valores por medio de un input:
print("\nHaremos una multiplicación \n")
valor = int(input("ingresa un valor numerico: "))
multiplo = int(input("Ingresa el multiplo: "))
total = valor * multiplo
print("El resultado de multiplicar: ", valor, "*", multiplo ,'es: ', total)


#Part 3 Print the distinguished greeting “Hello world!”

#RESULT Part3
print("Hello World!")


#Part 4 
# Print the sum of 4 + 5.
# Print the result of subtracting 5 from 5.
# Multiply 3 by 5.
# Divide 10 by 2.

# Addition
print(4+5)

# Subtraction
print(5-5)

# Multiplication
print(3*5)

# Division
print(10/2)


"""# parte4"""
# Instructions
# Checkpoint 1 Passed
# 1. Print your name using the print() command.
print("Emmanuel Ryce")

# 2. If your print statement uses double-quotes ", change them to single-quotes '. 
# If it uses single-quotes ', change them to double-quotes ".
# Try running your code again after switching the type of quote-marks. Is anything different about the output?
print('Emmanuel Ryce')

"""Parte 5"""
#Update the variable meal to reflect each meal of the day before we print it.

# We've defined the variable "meal" here to the name of the food we ate for breakfast!
meal = "An english muffin"

# Printing out breakfast
print("Breakfast:")
print(meal)

# Now update meal to be lunch!
#meal = "Lunch"
meal = "Lunch"

# Printing out lunch
print("Lunch:")
print(meal)

# Now update "meal" to be dinner

# Printing out dinner
print("Dinner:")
print(meal)

"""Parte 6: Update the malformed strings in the workspace to all be strings."""
# print('This message has mismatched quote marks!")
# print(Abracadabra)

Abracadabra = ('This message has mismatched quote marks!')
print(Abracadabra)
"""Parte 7:
Create the following variables and assign integer numbers to them:
release_year and runtime.
# Define the rating_out_of_10 float variable below: 

# Define the release and runtime integer variables below:
"""

release_year = int(1)
runtime = int(10)

# Define the rating_out_of_10 float variable below: 
rating_out_of_10 = float(2)

"""parte 8 Calculation: Print out the result of this equation: 25 * 68 + 13 / 28 """

equation = 25 * 68 + 13 / 28
print(equation)

"""Parte 9 Changing Numbers: 
We create two variables and assign numeric values to them. 
Then we perform a calculation on them. This doesn’t update the variables! 
When we update the coffee_price variable and perform the calculations again, 
they use the updated values for the variable!
# """
#1. You’ve decided to get into quilting! To calculate the number of squares 
#you’ll need for your first quilt let’s create two variables: quilt_width and quilt_length.
#let’s make this first quilt 8 squares wide and 12 squares long.

quilt_width = 8
quilt_length = 12

#2. Print out the number of squares you’ll need to create the quilt!
quilt = quilt_width * quilt_length
print(quilt_width)
print(quilt_length)
print(quilt)

#3. It turns out that quilt required a little more material 
# than you have on hand! Let’s only make the quilt 8 squares long.
# How many squares will you need for this quilt instead?

uilt_length = 8
quilt = quilt_width * quilt_length
print(quilt)

"""Parte 9 Exponents: Since this operation is so related to multiplication, we use the notation **.

"""
"""1. # You really like how the square quilts from last exercise came out,
# and decide that all quilts that you make will be square from now on.

# Using the exponent operator, print out how many squares you’ll need for a 6x6 quilt,
# a 7x7 quilt, and an 8x8 quilt."""

# Calculation of squares for:
# 6x6 quilt
quilt_length = 6
quilt_width = 6
quilt = quilt_length ** quilt_width
print(6 * 6) 
print("Calculation of squares for: 6x6 quilt:", 6 ** 6)
print("Calculation of squares for: 6x6 quilt:", quilt)
# 7x7 quilt
print(7 * 7) 
quilt_length = 7
quilt_width = 7
quilt = quilt_length ** quilt_width
print("Calculation of squares for: 7x7 quilt:", 7 ** 7)
print("Calculation of squares for: 7x7 quilt:", quilt)
# 8x8 quilt
print(8 * 8) 
quilt_length = 8
quilt_width = 8
quilt = quilt_length ** quilt_width
print("Calculation of squares for: 8x8 quilt:", 8 ** 8)
print("Calculation of squares for: 8x8 quilt:", quilt)


# How many squares for 6 people to have 6 quilts each that are 6x6?
print(6 ** 3 * 6) #1296


"""Part11 Modulo operator: Python offers a companion to the division operator called the modulo operator. 
The modulo operator is indicated by % and gives the remainder of a division calculation. 
If the two numbers are divisible, then the result of the modulo operation will be 0.

# Prints 4 because 29 / 5 is 5 with a remainder of 4
print(29 % 5)
 
# Prints 2 because 32 / 3 is 10 with a remainder of 2
print(32 % 3)
 
# Modulo by 2 returns 0 for even numbers and 1 for odd numbers
# Prints 0
print(44 % 2)
"""

#Here comes order #263! Find the remainder by calculating 263 modulo 11 and store the result in a variable called order_263_r.
#Print out order_263_r.


order_263_r = 263 % 11
print(order_263_r)
#Based on the value of order_263_r, should this order receive a coupon? Create a new variable called order_263_coupon and assign to it a value of "yes" if the order should get a coupon, otherwise "no".

order_263_coupon = "no"

#Here comes another order, #264! Find the remainder by calculating 264 modulo 11 and store the result in a variable called order_264_r.
#Print out order_264_r.


order_264_r = 264 % 11
print(order_264_r)

#Based on the value of order_264_r, should this order receive a coupon? Create a new variable called order_264_coupon and assign to it a value of "yes" if the order should get a coupon, otherwise "no".


order_264_coupon = "yes"


"""Part12 Concatenation: Using str() we can convert variables that are not strings to strings
and then concatenate them. But we don’t need to convert a number to a string for it to be an 
argument to a print statement."""

string1 = "The wind, "
string2 = "which had hitherto carried us along with amazing rapidity, "
string3 = "sank at sunset to a light breeze; "
string4 = "the soft air just ruffled the water and "
string5 = "caused a pleasant motion among the trees as we approached the shore, "
string6 = "from which it wafted the most delightful scent of flowers and hay."

# Define message below Results:
message = string1 + string2 + string3 + string4 + string5 + string6

#print(message)
print(message)

"""Part13 Plus Equals: Python offers a shorthand for updating variables. 
When you have a number saved in a variable and want to add to the current 
value of the variable, you can use the += (plus-equals) operator."""

total_price = 0

new_sneakers = 50.00

total_price += new_sneakers

nice_sweater = 39.00
fun_books = 20.00
# Update total_price here:
total_price += nice_sweater + fun_books #Este es el resultado que hice, suma
print("The total price is", total_price)


"""Part 14 Multi-line Strings: Python offers a solution: multi-line strings. 
By using three quote-marks (.".".". or ''') instead of one, we tell the program 
that the string doesn’t end until the next triple-quote. """

# #Instructions
# 1. Assign the string

# Stranger, if you passing meet me and desire to speak to me, why
#   should you not speak to me?
# And why should I not speak to you?

to_you = """Stranger, if you passing meet me and desire to speak to me, why
  should you not speak to me?
And why should I not speak to you?
"""

print(to_you)


"""Parte 15 Review: Create variables:

my_age
half_my_age
greeting
name
greeting_with_name
Assign values to each using your knowledge of division and concatenation!

"""

#RESULT
my_age = 24
half_my_age = my_age - 12
greeting = "E pra mim um prazer"
name = " Emmanuel"
greeting_with_name = greeting + " O meu nome e: " + name

print(greeting_with_name + " I am: " + str(my_age) + "years old, and: " + str(half_my_age) + ", I was a young boy off: " + str(half_my_age))

