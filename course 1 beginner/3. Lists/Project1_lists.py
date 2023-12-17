"""Project Gradebook
You are a student and you are trying to organize your subjects and grades using Python. 
Let’s explore what we’ve learned about lists to organize your subjects and scores.
    """
    
"""LEARN PYTHON 3
Gradebook
You are a student and you are trying to organize your subjects and grades using Python. Let’s explore what we’ve learned about lists to organize your subjects and scores.

Tasks
8/10 complete
Mark the tasks as complete by checking them off
Create Some Lists:
1.
Create a list called subjects and fill it with the classes you are taking:

"physics"
"calculus"
"poetry"
"history"

Stuck? Get a hint
2.
Create a list called grades and fill it with your scores:

98
97
85
88

Stuck? Get a hint
3.
Manually (without any methods) create a two-dimensional list to combine subjects and grades. Use the table below as a reference to associated values.

Name	Test Score
"physics"	98
"calculus"	97
"poetry"	85
"history"	88

Assign the value into a variable called gradebook.


Hint
Remember the key components of a two-dimensional list:

A two-dimensional list begins and ends with square brackets ( [ and ] ). This is our “container” list that wraps all of our inner sublists.

Any number of sublists within the “container” list. These are our inner lists.

Each item is separated by a comma ( , ) both in the inner and outer lists.

#Outermost "container" list
example_2d_list = [
  #Innermost sublists
  ["First Sublist"], 
  ["Second Sublist"], 
  ["Third Sublist"]
]

4.
Print gradebook.

Does it look how you expected it would?


Stuck? Get a hint
Add More Subjects:
5.
Your grade for your computer science class just came in! You got a perfect score, 100!

Use the .append() method to add a list with the values of "computer science" and an associated grade value of 100 to our two-dimensional list of gradebook.


Hint
You can add a value to the end of a list with this syntax:

list.append(new_value)

new_value can represent any value, even a list!

6.
Your grade for "visual arts" just came in! You got a 93!

Use append to add ["visual arts", 93] to gradebook.


Stuck? Get a hint
Modify The Gradebook:
7.
Our instructor just told us they made a mistake grading and are rewarding an extra 5 points for our visual arts class.

Access the index of the grade for your visual arts class and modify it to be 5 points greater.


Stuck? Get a hint
8.
You decided to switch from a numerical grade value to a Pass/Fail option for your poetry class.

Find the grade value in your gradebook for your poetry class and use the .remove() method to delete it.


Hint
Your grade for poetry is an 85 and the value exists at gradebook[2]. Use the .remove() method on this sublist and provide the value you want to remove.

sublist.remove(value)

9.
Use the .append() method to then add a new "Pass" value to the sublist where your poetry class is located.


Stuck? Get a hint
One Big Gradebook!
10.
You also have your grades from last semester, stored in last_semester_gradebook.

Create a new variable full_gradebook that combines both last_semester_gradebook and gradebook using + to have one complete grade book.

Print full_gradebook to see our completed list."""
    
    
    
last_semester_gradebook = [["politics", 80], ["latin", 96], ["dance", 97], ["architecture", 65]]

# Your code below: 
subjects = ["physics" ,"calculus" ,"poetry" ,"history"]
print(subjects)

grades = [98, 97, 85, 88]
print(grades)

gradebook = [
  ["physics", 98],
  ["calculus", 97],
  ["poetry", 85],
  ["history", 88],
]
# gradebook = [subjects] + [grades]
print(gradebook)

gradebook.append(["computer science", 100])
print(gradebook)

gradebook.append(["visual arts", 93])
print(gradebook)

gradebook[5][1] = 98
print(gradebook)

# gradebook[2][1] = False
# print(gradebook)

gradebook[2].remove(85)
print(gradebook)


gradebook[2].append("Pass")
print(gradebook)

full_gradebook = last_semester_gradebook + gradebook

print(full_gradebook)
