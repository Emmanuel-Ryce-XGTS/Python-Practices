"""part1 intro printing one by one, part2 intro with loops"""

"""Part 4 
for temp in range(6):
  print("Loop is on iteration number " + str(temp + 1))

Would output:

Loop is on iteration number 1
Loop is on iteration number 2
Loop is on iteration number 3
Loop is on iteration number 4
Loop is on iteration number 5
Loop is on iteration number 6
"""
#RESULT
promise = "I will finish the python loops module!"

for i in range(5):
  print(promise + " " + str(i + 1))
  

"""Part 5 While countdown
"""
countdown = 10

while countdown >= 0:
  print(countdown)
  countdown -= 1
print("We have liftoff!")



"""part 6 While Loops: Lists

python_topics = ["variables", "control flow", "loops", "modules", "classes"]

#Your code below: 
ingredients = ["milk", "sugar", "vanilla extract", "dough", "chocolate"]
length = len(ingredients)
index = 0

while index < length:
  print(ingredients[index])
  index += 1
  
  #
Output-only Terminal
Output:
milk
sugar
vanilla extract
dough
chocolate
"""

python_topics = ["variables", "control flow", "loops", "modules", "classes"]

#Your code below: 
length = len(python_topics)
print(length)

index = 0

while index < length:
  print("I am learning about" + python_topics[index])
  index += 1

"""Part 7 Infinite Loops
We’ve iterated through lists that have a discrete beginning and end. However, let’s consider this example:

my_favorite_numbers = [4, 8, 15, 16, 42]

for number in my_favorite_numbers:
  my_favorite_numbers.append(1)
"""

"""Part 8 Loop Control: Break
Loops in Python are very versatile. Python provides a set of control statements 
that we can use to get even more control out of our loops.
"""
dog_breeds_available_for_adoption = ["french_bulldog", "dalmatian", "shihtzu", "poodle", "collie"]
dog_breed_I_want = "dalmatian"

for dog_breed in dog_breeds_available_for_adoption:
  print(dog_breed)
  if dog_breed == dog_breed_I_want:
      print("They have the dog I want!")
      break
  
  

"""Part 9 Continue Loops:
for i in big_number_list:
  if i <= 0:
    continue
  print(i)

This would produce the output:

1
2
4
5
2
"""

ages = [12, 38, 34, 26, 21, 19, 67, 41, 17]

for i in ages:
  if i >= 21:
    print(i)
  continue




"""NESTED LOOPS:
for team in project_teams:
  # Loop elements in each sublist
  for student in team:
    print(student)
['Ava', 'Samantha', 'James']
['Lucille', 'Zed']
['Edgar', 'Gabriel']
Ava
Samantha
James
Lucille
Zed
Edgar
Gabriel
    """

sales_data = [[12, 17, 22], [2, 10, 3], [5, 12, 13]]

scoops_sold = 0

for location in sales_data:
  print(location)
  for element in location:
    scoops_sold += element
print(scoops_sold)


"""List Comprehensions: Introduction

To start, let’s say we had a list of integers and wanted to create a list where each element is doubled. We could accomplish this using a for loop and a new list called doubled:

numbers = [2, -1, 79, 33, -45]
doubled = []

for number in numbers:
  doubled.append(number * 2)

print(doubled)

Would output:

[4, -2, 158, 66, -90]

Let’s see how we can use the power of list comprehensions to solve these types of problems in one line. Here is our same problem but now written as a list comprehension:

numbers = [2, -1, 79, 33, -45]
doubled = [num * 2 for num in numbers]
print(doubled)

Let’s break down our example in a more general way:

new_list = [<expression> for <element> in <collection>]

In our doubled example, our list comprehension:

Takes an element in the list numbers
Assigns that element to a variable called num (our <element>)
Applies the <expression> on the element stored in num and adds the result to a new list called doubled
Repeats steps 1-3 for every other element in the numbers list (our <collection>)
Our result would be the same:

[4, -2, 158, 66, -90]


"""


# numbers = [2, -1, 79, 33, -45]
# doubled = []

# for number in numbers:
#   doubled.append(number * 2)

# print(doubled)


# numbers = [2, -1, 79, 33, -45]
# doubled = [num * 2 for num in numbers]
# print(doubled)




#MY CODE
grades = [90, 88, 62, 76, 74, 89, 48, 57]

# scaled_grades = sorted(grades)

# print(scaled_grades)


# for scaled_grades in grades:
#   scaled_grades = scaled_grades + 10
#   print(scaled_grades)

scaled_grades = [grade + 10 for grade in grades]
print(scaled_grades)



# Recorremos cada calificación en la lista original
for grade in grades:
    # Ajustamos la calificación sumándole 10 y la agregamos a la nueva lista
    adjusted_grade = grade + 10
    scaled_grades.append(adjusted_grade)

# Mostramos las listas originales y la nueva lista ajustada
print("Calificaciones originales:", grades)
print("Calificaciones ajustadas:", scaled_grades)


"""Parte 12 List Comprehensions: Conditionals 



# numbers = [2, -1, 79, 33, -45]
# negative_doubled = [num * 2 for num in numbers if num < 0]
# print(negative_doubled)

# numbers = [2, -1, 79, 33, -45]
# only_negative_doubled = []

# for num in numbers:
#   if num < 0: 
#     only_negative_doubled.append(num * 2)

# print(only_negative_doubled) 
# #OUTPUT [-2, -90]


# numbers = [2, -1, 79, 33, -45]
# # only_negative_doubled = []

# # for num in numbers:
# #   if num < 0: 
# #     only_negative_doubled.append(num * 2)

# # print(only_negative_doubled) 
# doubled = [num * 2 if num < 0 else num * 3 for num in numbers ]
# print(doubled)

numbers = [2, -1, 79, 33, -45]

no_if   = [num * 2 for num in numbers]
if_only = [num * 2 for num in numbers if num < 0]
if_else = [num * 2 if num < 0 else num * 3 for num in numbers]

print(no_if)
print(if_only)
print(if_else)

"""


heights = [161, 164, 156, 144, 158, 170, 163, 163, 157]



can_ride_coaster = []

can_ride_coaster = [i for i in heights if i >= 161]
print(can_ride_coaster)

#Part 13 Reviews

# Your code below:
single_digits = [0,1,2,3,4,5,6,7,8,9]

squares = []
cubes = []
for digits in single_digits:
  print(digits)
  squares.append(digits**2)
  # squares.append(digits*digits)
  print(squares)
  cubes.append(digits**3)
  print(cubes)
