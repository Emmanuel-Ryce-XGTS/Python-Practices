"""PART 7 Methods with Arguments


Methods can also take more arguments than just self:

class DistanceConverter:
  kms_in_a_mile = 1.609
  def how_many_kms(self, miles):
    return miles * self.kms_in_a_mile

converter = DistanceConverter()
kms_in_5_miles = converter.how_many_kms(5)
print(kms_in_5_miles)
# prints "8.045"

Above we defined a DistanceConverter class, instantiated it, and used it to convert 5 miles into kilometers. Notice again that even though .how_many_kms() takes two arguments in its definition, we only pass miles, because self is implicitly passed (and refers to the object converter).

Instructions
Checkpoint 1 Passed
1.
It’s March 14th (known in some places as Pi day) at Jan van High, and you’re feeling awfully festive. You decide to create a program that calculates the area of a circle.

Create a Circle class with class variable .pi. Set .pi to the approximation 3.14.

Checkpoint 2 Passed
2.
Give Circle an .area() method that takes two parameters: self and radius.

Return the area as given by this formula:

area = pi * radius ** 2


Stuck? Get a hint
Checkpoint 3 Passed
3.
Create an instance of Circle. Save it into the variable circle.

Checkpoint 4 Passed
4.
You go to measure several circles you happen to find around.

A medium pizza that is 12 inches across.
Your teaching table which is 36 inches across.
The Round Room auditorium, which is 11,460 inches across.
You save the areas of these three things into pizza_area, teaching_table_area, and round_room_area.

Remember that the .radius of a circle is half the diameter. We gave three diameters here, so halve them before you calculate the given circle’s area.


Hint
Given a certain diameter, calculate the area using

circle.area(diameter / 2)

"""

class Circle:
    pi = 3.14  # Class variable

    def area(self, radius):  # Method to calculate the area
        return Circle.pi * radius ** 2

# Create an instance of Circle
circle = Circle()

# Calculate the areas for the given circles
pizza_area = 12
teaching_table_area = 36
round_room_diameter = 11460

pizza_area = circle.area(pizza_area / 2)
teaching_table_area = circle.area(teaching_table_area / 2)
round_room_diameter = circle.area(round_room_diameter / 2)

print("Area of the pizza: ", pizza_area)
print("Area of the teaching table: ", teaching_table_area)
print("Area of the round room: ", round_room_diameter)


"""Python Constructors part 8
class Shouter:
  def __init__(self, phrase):
    # make sure phrase is a string
    if type(phrase) == str:

      # then shout it out
      print(phrase.upper())

shout1 = Shouter("shout")
# prints "SHOUT"

shout2 = Shouter("shout")
# prints "SHOUT"

shout3 = Shouter("let it all out")
# prints "LET IT ALL OUT"

Above, we’ve updated our Shouter class to take the additional parameter phrase. When we created each of our objects, we passed an argument to the constructor. The constructor takes the argument phrase and, if it’s a string, prints out the all-caps version of phrase.

Instructions
Checkpoint 1 Passed
1.
Add a constructor to our Circle class.

Since we seem more frequently to know the diameter of a circle, it should take the argument diameter.

It doesn’t need to do anything yet, just write pass in the body of the constructor.

Checkpoint 2 Passed
2.
Now have the constructor print out the message "New circle with diameter: {diameter}" when a new circle is created.

Create a circle teaching_table with diameter 36.

"""
class Circle:
    pi = 3.14  # Class variable

    def __init__(self, diameter):
         print(f"New circle with diameter: {diameter}")

# Create a circle teaching_table with diameter 36
teaching_table = Circle(36)




""" Instance variable part 9 
Instance Variables
We’ve learned so far that a class is a schematic for a data type and an object is an instance of a class, but why is there such a strong need to differentiate the two if each object can only have the methods and class variables the class has? This is because each instance of a class can hold different kinds of data.

The data held by an object is referred to as an instance variable. Instance variables aren’t shared by all instances of a class — they are variables that are specific to the object they are attached to.

Let’s say that we have the following class definition:

class FakeDict:
  pass

We can instantiate two different objects from this class, fake_dict1 and fake_dict2, and assign instance variables to these objects using the same attribute notation that was used for accessing class variables.

fake_dict1 = FakeDict()
fake_dict2 = FakeDict()

fake_dict1.fake_key = "This works!"
fake_dict2.fake_key = "This too!"

# Let's join the two strings together!
working_string = "{} {}".format(fake_dict1.fake_key, fake_dict2.fake_key)
print(working_string)
# prints "This works! This too!"

Instructions
Checkpoint 1 Passed
1.
In script.py we have defined a Store class. Create two objects from this store class, named alternative_rocks and isabelles_ices.

Checkpoint 2 Passed
2.
Give them both instance attributes called .store_name. Set alternative_rocks‘s .store_name to "Alternative Rocks". Set isabelles_ices‘s .store_name to "Isabelle's Ices".
"""

class Store:
    def __init__(self):
        self.store_name = ""

# Create two Store objects
alternative_rocks = Store()
alternative_rocks.store_name = "Alternative Rocks"

isabelles_ices = Store()
isabelles_ices.store_name = "Isabelle's Ices"


"""PART 11
Attribute Functions
Instance variables and class variables are both accessed similarly in Python. This is no mistake, they are both considered attributes of an object. If we attempt to access an attribute that is neither a class variable nor an instance variable of the object Python will throw an AttributeError.

class NoCustomAttributes:
  pass

attributeless = NoCustomAttributes()

try:
  attributeless.fake_attribute
except AttributeError:
  print("This text gets printed!")

# prints "This text gets printed!"

What if we aren’t sure if an object has an attribute or not? hasattr() will return True if an object has a given attribute and False otherwise. If we want to get the actual value of the attribute, getattr() is a Python function that will return the value of a given object and attribute. In this function, we can also supply a third argument that will be the default if the object does not have the given attribute.

The syntax and parameters for these functions look like this:

hasattr(object, “attribute”) has two parameters:

object : the object we are testing to see if it has a certain attribute
attribute : name of attribute we want to see if it exists
getattr(object, “attribute”, default) has three parameters (one of which is optional):

object : the object whose attribute we want to evaluate
attribute : name of attribute we want to evaluate
default : the value that is returned if the attribute does not exist (note: this parameter is optional)
Calling those functions looks like this:

hasattr(attributeless, "fake_attribute")
# returns False

getattr(attributeless, "other_fake_attribute", 800)
# returns 800, the default value

Above, we checked if the attributeless object has the attribute .fake_attribute. Since it does not, hasattr() returned False. After that, we used getattr to attempt to retrieve .other_fake_attribute. Since .other_fake_attribute isn’t a real attribute on attributeless, our call to getattr() returned the supplied default value 800, instead of throwing an AttributeError.

Instructions
"""

can_we_count_it = [{'s': False}, "sassafrass", 18, ["a", "c", "s", "d", "s"]]

for element in can_we_count_it:
    if hasattr(element, 'count'):
        print(str(type(element)) + " has the count attribute!")
    else:
        print(str(type(element)) + " does not have the count attribute :(")


"""PART 11 SELF
Self
Since we can already use dictionaries to store key-value pairs, using objects for that purpose is not really useful. Instance variables are more powerful when you can guarantee a rigidity to the data the object is holding.

This convenience is most apparent when the constructor creates the instance variables using the arguments passed into it. If we were creating a search engine and wanted to create a class to hold each search entry, we could do so like this:

class SearchEngineEntry:
  def __init__(self, url):
    self.url = url

codecademy = SearchEngineEntry("www.codecademy.com")
wikipedia = SearchEngineEntry("www.wikipedia.org")

print(codecademy.url)
# prints "www.codecademy.com"

print(wikipedia.url)
# prints "www.wikipedia.org"

In the preceding code sample, we define a SearchEngineEntry class, which contains a constructor with two parameters, self and url. Inside the constructor body, we create an instance variable named self.url and assign it the value of the url parameter that is passed into the constructor.

We then create the codecademy instance of SearchEngineEntry by passing the URL as an argument to the constructor. After codecademy is defined, printing codecademy.url shows that the URL has been assigned to the url instance variable of codecademy. Similarly, wikipedia.url holds the value that was passed into the constructor when wikipedia was defined.

Since the self keyword refers to the object and not the class being called, we can define a .secure() method on the SearchEngineEntry class that returns the secure link to an entry.

class SearchEngineEntry:
  secure_prefix = "https://"
  def __init__(self, url):
    self.url = url

  def secure(self):
    return "{prefix}{site}".format(prefix=self.secure_prefix, site=self.url)

codecademy = SearchEngineEntry("www.codecademy.com")
wikipedia = SearchEngineEntry("www.wikipedia.org")

print(codecademy.secure())
# prints "https://www.codecademy.com"

print(wikipedia.secure())
# prints "https://www.wikipedia.org"

Above, we define our .secure() method to take just the one required argument, self. We access both the class variable self.secure_prefix and the instance variable self.url to return a secure URL.

This is the strength of writing object-oriented programs. We can write our classes to structure the data that we need and write methods that will interact with that data in a meaningful way.

Instructions
Checkpoint 1 Enabled
1.
In script.py you’ll find our familiar friend, the Circle class.

Even though we usually know the diameter beforehand, what we need for most calculations is the radius.

In Circle‘s constructor, set the instance variable self.radius to equal half the diameter that gets passed in.

Checkpoint 2 Step instruction is unavailable until previous steps are completed
2.
Define a new method .circumference() for your circle object that takes only one argument, self, and returns the circumference of a circle with the given radius by this formula:

circumference = 2 * pi * radius

Checkpoint 3 Step instruction is unavailable until previous steps are completed
3.
Define three Circles with three different diameters.

A medium pizza, medium_pizza, that is 12 inches across.
Your teaching table, teaching_table, which is 36 inches across.
The Round Room auditorium, round_room, which is 11,460 inches across.
Checkpoint 4 Step instruction is unavailable until previous steps are completed
4.
Print out the circumferences of medium_pizza, teaching_table, and round_room.
"""


class Circle:
    pi = 3.14

    def __init__(self, diameter):
        self.radius = diameter / 2  # Calculate the radius
        print("Creating circle with diameter {d}".format(d=diameter))

    def circumference(self):
        return 2 * Circle.pi * self.radius

# Create Circles with different diameters
medium_pizza = Circle(12)
teaching_table = Circle(36)
round_room = Circle(11460)

# Print out the circumferences
print("Circumference of medium pizza: {}".format(medium_pizza.circumference()))
print("Circumference of teaching table: {}".format(teaching_table.circumference()))
print("Circumference of round room: {}".format(round_room.circumference()))



"""Everything is an Object
Attributes can be added to user-defined objects after instantiation, so it’s possible for an object to have some attributes that are not explicitly defined in an object’s constructor. We can use the dir() function to investigate an object’s attributes at runtime. dir() is short for directory and offers an organized presentation of object attributes.

class FakeDict:
  pass

fake_dict = FakeDict()
fake_dict.attribute = "Cool"

print(dir(fake_dict))
# Prints ['__class__', '__delattr__', '__dict__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__gt__', '__hash__', '__init__()', '__init_subclass__', '__le__', '__lt__', '__module__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__', '__weakref__', 'attribute']

That’s certainly a lot more attributes than we defined! Python automatically adds a number of attributes to all objects that get created. These internal attributes are usually indicated by double-underscores. But sure enough, attribute is in that list.

Do you remember being able to use type() on Python’s native data types? This is because they are also objects in Python. Their classes are int, float, str, list, and dict. These Python classes have special syntax for their instantiation, 1, 1.0, "hello", [], and {} specifically. But these instances are still full-blown objects to Python.

fun_list = [10, "string", {'abc': True}]

type(fun_list)
# Prints <class 'list'>

print(dir(fun_list))
# Prints ['__add__', '__class__', [...], 'append', 'clear', 'copy', 'count', 'extend', 'index', 'insert', 'pop', 'remove', 'reverse', 'sort']

Above we define a new list. We check its type and see that’s an instantiation of class list. We use dir() to explore its attributes, and it gives us a large number of internal Python dunder attributes, but afterward, we get the usual list methods.

Instructions
Checkpoint 1 Enabled
1.
Call dir() on the number 5. Print out the results.


Stuck? Get a hint
Checkpoint 2 Step instruction is unavailable until previous steps are completed
2.
Define a function called this_function_is_an_object. It can take any parameters and return anything you’d like.

Checkpoint 3 Step instruction is unavailable until previous steps are completed
3.
Print out the result of calling dir() on this_function_is_an_object.

Functions are objects too!"""

# Call dir() on the number 5 and print the results
print(dir(5))

# Define a function called this_function_is_an_object
def this_function_is_an_object():
    pass  # This function can be empty for demonstration

# Print out the result of calling dir() on this_function_is_an_object
print(dir(this_function_is_an_object))



"""String Representation
One of the first things we learn as programmers is how to print out information that we need for debugging. Unfortunately, when we print out an object we get a default representation that seems fairly useless.

class Employee():
  def __init__(self, name):
    self.name = name

argus = Employee("Argus Filch")
print(argus)
# prints "<__main__.Employee object at 0x104e88390>"

This default string representation gives us some information, like where the class is defined and our computer’s memory address where this object is stored, but is usually not useful information to have when we are trying to debug our code.

We learned about the dunder method __init__(). Now, we will learn another dunder method called __repr__(). This is a method we can use to tell Python what we want the string representation of the class to be. __repr__() can only have one parameter, self, and must return a string.

In our Employee class above, we have an instance variable called .name that should be unique enough to be useful when we’re printing out an instance of the Employee class.

class Employee():
  def __init__(self, name):
    self.name = name

  def __repr__(self):
    return self.name

argus = Employee("Argus Filch")
print(argus)
# prints "Argus Filch"

We implemented the __repr__() method and had it return the .name attribute of the object. When we printed the object out it simply printed the .name of the object! Cool!

Instructions
Checkpoint 1 Passed
1.
Add a __repr__() method to the Circle class that returns

Circle with radius {radius}

Checkpoint 2 Passed
2.
Print out medium_pizza, teaching_table, and round_room."""


class Circle:
    pi = 3.14

    def __init__(self, diameter):
        self.radius = diameter / 2

    def circumference(self):
        return 2 * Circle.pi * self.radius

    def __repr__(self):
        return f"Circle with radius {self.radius}"

medium_pizza = Circle(12)
teaching_table = Circle(36)
round_room = Circle(11460)

print(medium_pizza)
print(teaching_table)
print(round_room)




"""
Review
So far we’ve covered what a data type actually is in Python. We explored what the functionality of Python’s built-in types (also referred to as primitives) are. We learned how to create our own data types using the class keyword.

We explored the relationship between a class and an object — we create objects when we instantiate a class, we find the class when we check the type() of an object. We learned the difference between class variables (the same for all objects of a class) and instance variables (unique for each object).

We learned about how to define an object’s functionality with methods. We created multiple objects from the same class, all with similar functionality, but with different internal data. They all had the same methods, but produced different output because they were different instances.

Take a moment to congratulate yourself, object-oriented programming is a complicated concept.

1.
Define a class named Student that will be our data model at Jan van Eyck High School and Conservatory.

Add a constructor for Student. Have the constructor take in two parameters: a name and a year. Save those two as attributes .name and .year.


Stuck? Get a hint
Checkpoint 2 Step instruction is unavailable until previous steps are completed
2.
Create three instances of the Student class:

Roger van der Weyden, year 10
Sandro Botticelli, year 12
Pieter Bruegel the Elder, year 8
Save them into the variables roger, sandro, and pieter.

Checkpoint 3 Step instruction is unavailable until previous steps are completed
3.
Create a Grade class, with .minimum_passing as an attribute set to 65.

Checkpoint 4 Step instruction is unavailable until previous steps are completed
4.
Give Grade a constructor. Take in a parameter score and assign it to self.score.

Checkpoint 5 Step instruction is unavailable until previous steps are completed
5.
In the body of the constructor for Student, declare self.grades as an empty list.

Checkpoint 6 Step instruction is unavailable until previous steps are completed
6.
Add an .add_grade() method to Student that takes a parameter, grade.

.add_grade() should verify that grade is of type Grade and if so, add it to the Student‘s .grades.

If grade isn’t an instance of Grade then .add_grade() should do nothing.

Checkpoint 7 Step instruction is unavailable until previous steps are completed
7.
Create a new Grade with a score of 100 and add it to pieter‘s .grades attribute using .add_grade().

Checkpoint 8 Step instruction is unavailable until previous steps are completed
8.
Great job! You’ve created two classes and defined their interactions. This is object-oriented programming! From here you could:

Write a Grade method .is_passing() that returns whether a Grade has a passing .score.
Write a Student method .get_average() that returns the student’s average score.
Add an instance variable to Student that is a dictionary called .attendance, with dates as keys and booleans as values that indicate whether the student attended school that day.
Write your own classes to do whatever logic you want!
"""