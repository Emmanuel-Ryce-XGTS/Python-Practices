"""Adding by Index: Insert
The Python list method .insert() allows us to add an element to a specific index in a list.
"""
front_display_list = ["Mango", "Filet Mignon", "Chocolate Milk"]
print(front_display_list)

# Your code below: 

front_display_list.insert(0, "Pineapple")
print(front_display_list)

"""Removing by Index: Pop
The .pop() method takes an optional single input:

The index for the element you want to remove.
To see it in action, let’s consider a list called cs_topics
that stores a collection of topics one might study in a computer science program.
"""

data_science_topics = ["Machine Learning", "SQL", "Pandas", "Algorithms", "Statistics", "Python 3"]
print(data_science_topics)

# Your code below: 


data_science_topics.pop()
print(data_science_topics)

data_science_topics.pop(3)
print(data_science_topics)



# Your code below: 

number_list = range(9)
print(list(number_list))

"""Parte 4
Consecutive Lists: Range
Often, we want to create a list of consecutive numbers in our programs. 
For example, suppose we want a list containing the numbers 0 through 9:
my_list = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
my_range = range(10)
print(my_range)

"""# Your code below: 

number_list = range(9)
print(list(number_list))

zero_to_seven  = range(8)
print(list(zero_to_seven))


"""Parte 5 The Power of Range!
By default, range() creates a list starting at 0. However, if we call range()
with two inputs, we can create a list that starts at a different number.
For example, range(2, 9) would generate numbers starting at 2 and ending at 8 (just before 9):

my_list = range(2, 9)
print(list(my_list))
"""

# Your code below: 

range_five_three = range(5, 15, 3)
print(range_five_three)

# Your code below: 

range_diff_five  = range(0, 40, 5)
print(range_five_three)


"""Parte 6 Length
When we apply len() to a list, we get the number of elements in that list:

my_list = [1, 2, 3, 4, 5]

print(len(my_list))
# output 5
"""

long_list = [1, 5, 6, 7, -23, 69.5, True, "very", "long", "list", "that", "keeps", "going.", "Let's", "practice", "getting", "the", "length"]

big_range = range(2, 3000, 10)

# Your code below: 

long_list_len = len(long_list)
print(long_list_len)

big_range_length = len(big_range)
print(big_range_length)

big_range = range(2, 3000, 100)
big_range_length = len(big_range)
print(big_range_length)


"""
In Python, often we want to extract only a portion of a list. Dividing a list in such a manner is referred to as slicing.

Lets assume we have a list of letters:

letters = ["a", "b", "c", "d", "e", "f", "g"]

sliced_list = letters[1:6]
print(sliced_list)

Would output:

["b", "c", "d", "e", "f"]

"""

suitcase = ["shirt", "shirt", "pants", "pants", "pajamas", "books"]

beginning = suitcase[0:4]

# Your code below: 
print(beginning)
beginning = suitcase[0:2]
print(beginning)

middle = suitcase[2:4]
print(middle)

"""Parte 8 WORKING WITH LISTS IN PYTHON
Slicing Lists II
Slicing syntax in Python is very flexible. Let’s look at a few more problems we can tackle with slicing.

Take the list fruits as our example:

fruits = ["apple", "cherry", "pineapple", "orange", "mango"]

If we want to select the first n elements of a list, we could use the following code:

fruits[:n]

For our fruits list, suppose we wanted to slice the first three elements.

The following code would start slicing from index 0 and up to index 3. Note that the fruit at index 
3 (orange) is not included in the results.

print(fruits[:3])

Would output:

['apple', 'cherry', 'pineapple']
"""

suitcase = ["shirt", "shirt", "pants", "pants", "pajamas", "books"]

# Your code below: 

last_two_elements = suitcase[-2:]
print(last_two_elements )
# """['pajamas', 'books']

slice_off_last_three = suitcase[:-3]
print(slice_off_last_three)

# ['shirt', 'shirt', 'pants']"""

"""Counting in a List
In Python, it is common to want to count occurrences of an item in a list.

Suppose we have a list called letters that represents the letters in the word “Mississippi”:

letters = ["m", "i", "s", "s", "i", "s", "s", "i", "p", "p", "i"]
"""


"""Part 9 Counting in a List
In Python, it is common to want to count occurrences of an item in a list.

Suppose we have a list called letters that represents the letters in the word “Mississippi”:

letters = ["m", "i", "s", "s", "i", "s", "s", "i", "p", "p", "i"]

If we want to know how many times i appears in this word, we can use the list method called .count():

num_i = letters.count("i")
print(num_i)

Would output:

4

"""
votes = ["Jake", "Jake", "Laurie", "Laurie", "Laurie", "Jake", "Jake", "Jake", "Laurie", "Cassie", "Cassie", "Jake", "Jake", "Cassie", "Laurie", "Cassie", "Jake", "Jake", "Cassie", "Laurie"]

# Your code below: 
jake_votes = votes.count("Jake")
print(jake_votes)


"""Part 10 
Sorting Lists I
Often, we will want to sort a list in either numerical (1, 2, 3, …) or alphabetical (a, b, c, …) order.

We can sort a list using the method .sort().

Suppose that we have a list of names:

names = ["Xander", "Buffy", "Angel", "Willow", "Giles"]

Let’s see what happens when we apply .sort():

names.sort()
print(names)

Would output:

['Angel', 'Buffy', 'Giles', 'Willow', 'Xander']
"""

# Checkpoint 1 & 2
addresses = ["221 B Baker St.", "42 Wallaby Way", "12 Grimmauld Place", "742 Evergreen Terrace", "1600 Pennsylvania Ave", "10 Downing St."]
addresses.sort()
print(addresses)

# Checkpoint 3
names = ["Ron", "Hermione", "Harry", "Albus", "Sirius"]
names.sort()


# Checkpoint 4 & 5
cities = ["London", "Paris", "Rome", "Los Angeles", "New York"]
sorted_cities = cities.sort()
print(sorted_cities)

sorted_cities = cities.sort(reverse = True)
print(sorted_cities)


"""Part 11 Sorting Lists II
A second way of sorting a list in Python is to use the built-in function sorted().

The sorted() function is different from the .sort() method in two ways:

It comes before a list, instead of after as all built-in functions do.
It generates a new list rather than modifying the one that already exists.
Let’s return to our list of names:

names = ["Xander", "Buffy", "Angel", "Willow", "Giles"]

Using sorted(), we can create a new list, called sorted_names:

sorted_names = sorted(names)
print(sorted_names)

This yields the list sorted alphabetically:

['Angel', 'Buffy', 'Giles', 'Willow', 'Xander']

Note that using sorted did not change names:

print(names)

Would output:

['Xander', 'Buffy', 'Angel', 'Willow', 'Giles']
"""


games = ["Portal", "Minecraft", "Pacman", "Tetris", "The Sims", "Pokemon"]

# Your code below:
games_sorted = sorted(games)
print(games)
print(games_sorted)


"""Review
In this lesson, we learned how to:

Add elements to a list by index using the .insert() method.
Remove elements from a list by index using the .pop() method.
Generate a list using the range() function.
Get the length of a list using the len() function.
Select portions of a list using slicing syntax.
Count the number of times that an element appears in a list using the .count() method.
Sort a list of items using either the .sort() method or sorted() function.
As you go through the exercises, feel free to use print() to see changes when not explicitly asked to do so.

Instructions
Checkpoint 1 Passed
1.
Our friend Jiho has been so successful in both the flower and grocery business that she has decided to open a furniture store.

Jiho has compiled a list of inventory items into a list called inventory and wants to know a few facts about it.

First, how many items are in the warehouse?

Save the answer to a variable called inventory_len.


Stuck? Get a hint
Checkpoint 2 Passed
2.
Select the first element in inventory. Save it to a variable called first.


Hint
If we wanted to select the second element in inventory, we would use:

second = inventory[1]

Remember that Python lists are zero-indexed.

Checkpoint 3 Passed
3.
Select the last element from inventory. Save it to a variable called last.


Stuck? Get a hint
Checkpoint 4 Passed
4.
Select items from the inventory starting at index 2 and up to, but not including, index 6.

Save your answer to a variable called inventory_2_6.


Stuck? Get a hint
Checkpoint 5 Passed
5.
Select the first 3 items of inventory. Save it to a variable called first_3.


Stuck? Get a hint
Checkpoint 6 Passed
6.
How many 'twin bed's are in inventory? Save your answer to a variable called twin_beds.


Stuck? Get a hint
Checkpoint 7 Passed
7.
Remove the 5th element in the inventory. Save the value to a variable called removed_item.


Stuck? Get a hint
Checkpoint 8 Passed
8.
There was a new item added to our inventory called "19th Century Bed Frame".

Use the .insert() method to place the new item as the 11th element in our inventory.


Hint
Since lists in Python of zero_indexed, the 11th element will be at index 10.

Checkpoint 9 Passed
9.
Sort inventory using the .sort() method or the sorted() function.

Remember, the sorted() function doesn’t change the original list — it creates a new list with the elements properly sorted. If you use sorted() you’ll have to set inventory equal to the value returned by sorted().

Print inventory to see the result."""

inventory = ["twin bed", "twin bed", "headboard", "queen bed", "king bed", "dresser", "dresser", "table", "table", "nightstand", "nightstand", "king bed", "king bed", "twin bed", "twin bed", "sheets", "sheets", "pillow", "pillow"]

inventory_len = len(inventory)

first = inventory[1]

last = inventory[-1]

inventory_2_6 = inventory[2:6]

first_3 = inventory[:3]

twin_beds = inventory.count("twin bed")

removed_item = inventory.pop(4)

inventory.insert(10, "19th Century Bed Frame")

inventory = sorted(inventory)

