#TEMAS LISTS:
#1. What is a List?, 2. What can a List contain?, 3. Empty Lists
# 
# 4. List Methods

example_list = [1, 2, 3, 4]

#Using Append
example_list.append(5)
# print(example_list)

#Using Remove
example_list.remove(5)
# print(example_list)


"""#Ejemplo 5. Growing a List: Append
We can add a single element to a list using the .append() Python method.
"""
#orders = ["daisies", "periwinkle"]


orders = ["daisies", "periwinkle"]
print(orders)

orders.append("tulips")
print(orders)

orders.append("roses")
print(orders)


"""Ejemplo 6 Growing a List: Plus (+) 
When we want to add multiple items to a list, we can use + to combine two lists 
(this is also known as concatenation).
"""

#Results

orders = ["daisy", "buttercup", "snapdragon", "gardenia", "lily"]

# Create new orders here:

new_orders = orders + ["lilac", "iris"]
print("new_orders")

orders_combined = orders + new_orders
#broken_prices = [5, 3, 4, 5, 4] + 4
broken_prices = [5, 3, 4, 5, 4] + [4]

print(broken_prices)


"""Ejemplo 7 Accessing List Elements: 
Python lists are zero-indexed. This means that the first element in a list has index 0, rather than 1.
"""

#RESULT


employees = ["Michael", "Dwight", "Jim", "Pam", "Ryan", "Andy", "Robert"]

employee_four = employees[3]
print(employee_four)
print(employees[0])


"""Part 8. Accessing List Elements: Negative Index
We can use the index -1 to select the last item of a list, even when we don’t
know how many elements are in a list.
Use print to display both index5_element and last_element.

Note that they are equal to "cereal"!


"""
# RESULTS

shopping_list = ["eggs", "butter", "milk", "cucumbers", "juice", "cereal"]

print(shopping_list[-1])
last_element = shopping_list[-1]
index5_element = shopping_list[5]

print(last_element)
print(index5_element)
print(index5_element + last_element)



""" Part 9 Modifying List Elements

    Alisha realized she was already stocked with all the items we are selling. 
    She asked us to replace her with her friend Alex who just ran out.

Replace Alisha with Alex using a negative index.

Print garden_waitlist again to see the change!
    """
#Results

# Your code below:

garden_waitlist = ["Jiho", "Adam", "Sonny", "Alisha"]

garden_waitlist[1] = "Calla"
print(garden_waitlist)

garden_waitlist[-1] = "Alex"
print(garden_waitlist)


"""Part 10 Shrinking a List: Remove: 
We can remove elements in a list using the .remove() Python method.
"""
# We are in luck again! We actually found a spare case of "Mango" in our back storage.

# We won’t be needing to place two orders anymore.

# Let’s remove it from new_store_order_list using the .remove() method.


# Your code below: 

# Create a list
order_list = ["Celery", "Orange Juice", "Orange", "Flatbread"]

print(order_list)

order_list.remove("Flatbread") 

print(order_list)

# Print new_store_order_list to see the current list.

new_store_order_list = ["Orange", "Apple", "Mango", "Broccoli", "Mango"]

print(new_store_order_list) 

new_store_order_list.remove("Mango")
print(new_store_order_list) 

#LETS SEE WHat HAPPENS WHEN WE REMOVE A ITEM IS NOT ON THE LIST


new_store_order_list.remove("Onions")
print(new_store_order_list) 


"""Parte 11 Two-Dimensional (2D) Lists
As an example the tic tac toe
tic_tac_toe = [
            ["X","O","X"], 
            ["O","X","O"], 
            ["O","O","X"]
            ]

"""
heights = [["Jenny", 61], ["Alexus", 70], ["Sam", 67], ["Grace", 64], ["Vik", 68]]

print(heights)
ages = [["Aaron", 15], ["Dhruti", 16]]

print(ages)




""" Part 12 Accessing 2D Lists
Let’s return to our classroom heights example:


    Use double square brackets ([][]) to select Ellies test score from the list class_name_test.t
    This time only use negative indices!

Save it to the variable ellies_score.

Print the variable ellies_score to see the result.
    """
#Your code below:

class_name_test = [
["Jenny", 90],
["Alexus", 85.5],
["Sam", 83],
["Ellie", 101.5],
]

print(class_name_test)

sams_score = class_name_test[2][1]
print(sams_score)

ellies_score = class_name_test[-1][-1]
print(ellies_score)

"""Part 13 Modifying 2D Lists
Now that we know how to access two-dimensional lists, modifying the elements should come naturally.

"Kenny" likes to be called by his nickname "Ken". Modify the list using double brackets [][] 
to accommodate the change but only using negative indices.

Print incoming_class to see our change.

"""

#Your code below:

incoming_class = [
  ["Kenny", "American", 9],
  ["Tanya", "Ukrainian" , 9],
  ["Madison" ,"Indian" , 7],
]
print(incoming_class)

incoming_class[2][2] = 8

print(incoming_class)


incoming_class[-3][-3] = "Ken"

print(incoming_class)


"""Part 14 Review of lists

! One last thing, Maria received new customers, "Amit" and "Karim", 
the following 2d list contains their data:

[["Amit", "Large", True], ["Karim", "X-Large", False]]

Create a new variable customer_data_final. Combine our existing list customer_data 
with our new customer 2d list using + by adding it to the end of customer_data.

Print customer_data_final to see our final result."""

# Your code below: 

first_names = ["Ainsley", "Ben", "Chani", "Depak"]

preferred_size = ["Small", "Large", "Medium"]

preferred_size.append("Medium")

print(preferred_size)

customer_data = [
  ["Ainsley", "Small", True],
  ["Ben" , "Large" , False],
  ["Chani" , "Medium" , True],
  ["Depak" , "Medium" , False],
]
#print(customer_data)


customer_data[2][2] = False
#print(customer_data)

#customer_data[1][2] = 
customer_data[1].remove(False)
print(customer_data)

customer_data_final = [["Amit", "Large", True], ["Karim", "X-Large", False]]

customer_data_final = customer_data+ customer_data_final 

print(customer_data_final)


