"""OBJECT ORIENTED PROGRAMMING PART 1 """

# Write your code below
class Employee:
  new_id  = 1

  def __init__(self):
    self.id = Employee.new_id
    Employee.new_id += 1
 
  def say_id(self):
    print("My id is {}".format(self.id))
    # print(f"My id is {self.id}")

e1 = Employee()
e1.say_id()

e2 = Employee()
e2.say_id()

e2 = e2.say_id()

print(e1 , e2)


"""Part 2 Inheritance"""

class Employee():
  new_id = 1
  def __init__(self):
    self.id = Employee.new_id
    Employee.new_id += 1

  def say_id(self):
    print("My id is {}.".format(self.id))

# Write your code below
class Admin(Employee):
  pass


e1 = Employee()
e2 = Employee()
e3 = Admin()
e3 = e3.say_id()

"""OVERWRITE"""
class Employee():
  new_id = 1
  def __init__(self):
    self.id = Employee.new_id
    Employee.new_id += 1

  def say_id(self):
    print("My id is {}.".format(self.id))

class Admin(Employee):
  # Write your code below
  
  def say_id(self):
    print("I am an Admin")

e1 = Employee()
e2 = Employee()
e3 = Admin()
e3.say_id()


"""PART 4 the super class"""

class Employee():
  new_id = 1
  def __init__(self):
    self.id = Employee.new_id
    Employee.new_id += 1

  def say_id(self):
    print("My id is {}.".format(self.id))

class Admin(Employee):
  def say_id(self):
    # Write your code below:
    super().say_id()

e1 = Employee()
e2 = Employee()
e3 = Admin()
e3.say_id()



"""PART 5 Multiple inerithance"""
class Employee():
  new_id = 1
  def __init__(self):
    self.id = Employee.new_id
    Employee.new_id += 1

  def say_id(self):
    print("My id is {}.".format(self.id))

class Admin(Employee):
  def say_id(self):
    super().say_id()
    print("I am an admin.")

# Write your code below
class Manager(Admin):
  def say_id(self):
    print("I am a Manager.")
    super().say_id()


e1 = Employee()
e2 = Employee()
e3 = Admin()
e4 = Manager()
e4.say_id()


"""PART 6 Multiple Inheritance: Part 2
class Animal:
  def __init__(self, name):
    self.name = name

class Dog(Animal):
  def action(self):
    print("{} wags tail. Awwww".format(self.name))

class Wolf(Animal):
  def action(self):
    print("{} bites. OUCH!".format(self.name))

class Hybrid(Dog, Wolf):
  def action(self):
    super().action()
    Wolf.action(self)

my_pet = Hybrid("Fluffy")
my_pet.action() # Fluffy wags tail. Awwww
                # Fluffy bites. OUCH!

"""

class Employee():
  new_id = 1
  def __init__(self):
    self.id = Employee.new_id
    Employee.new_id += 1

  def say_id(self):
    print("My id is {}.".format(self.id))

class User:
  def __init__(self, username, role="Customer"):
    self.username = username
    self.role = role

  def say_user_info(self):
    print("My username is {}".format(self.username))
    print("My role is {}".format(self.role))

# Write your code below
class Admin(Employee, User):
  def __init__(self):
    super().__init__()

    User.__init__(self, self.id, "Admin") 
    

  def say_id(self):
    super().say_id()
    print("I am an admin.")

e1 = Employee()
e2 = Employee()
e3 = Admin()
e3.say_user_info()



"""Polymorphism part 7

class Animal:
  def __init__(self, name):
    self.name = name

  def make_noise(self):
    print("{} says, Grrrr".format(self.name))

class Cat(Animal):

  def make_noise(self):
    print("{} says, Meow!".format(self.name))

class Robot:
  
  def make_noise(self):
    print("beep.boop...BEEEEP!!!")

an_animal = Animal("Bear")
my_pet = Cat("Maisy")
my_vacuum = Robot()
objects = [an_animal, my_pet, my_vacuum]
for o in objects:
  o.make_noise()
"""

class Employee():
  new_id = 1
  def __init__(self):
    self.id = Employee.new_id
    Employee.new_id += 1

  def say_id(self):
    print("My id is {}.".format(self.id))

class Admin(Employee):
  def say_id(self):
    super().say_id()
    print("I am an admin.")

class Manager(Admin):
  def say_id(self):
    super().say_id()
    print("I am in charge!")

# Write your code below
meeting = [Employee(), Admin(), Manager()]

for employees in meeting:
  employees.say_id()
  
  
"""PART 8 DUNDER METHODS"""
  


class Employee():
  new_id = 1
  def __init__(self):
    self.id = Employee.new_id
    Employee.new_id += 1

class Meeting:
  def __init__(self):
    self.attendees = []

  def __len__(self):
    return len(self.attendees)

  def __add__(self, employee):
    print("ID {} added.".format(employee.id))
    self.attendees.append(employee)

  # Write your code
  
    
e1 = Employee()
e2 = Employee()
e3 = Employee()
m1 = Meeting()
m1 + e1 
m1 + e2 
m1 + e3
print(len(m1))



"""Part 9 Abstract Decorators"""
from abc import ABC, abstractmethod

class AbstractEmployee(ABC):
  new_id = 1
  def __init__(self):
    self.id = AbstractEmployee.new_id
    AbstractEmployee.new_id += 1

  @abstractmethod
  def say_id(self):
    pass

# Write your code below
class Employee(AbstractEmployee):
    def say_id(self):
      print(self.id)
    

e1 = Employee()
e1.say_id()


"""OOP Pillar Encapsulation"""
class Employee():
    def __init__(self):
        self.id = None
        # Write your code below
        # self.id = None
        # self._id = None
        # self.__id = None


e = Employee()
print(dir(e))




"""GETTERS, SETTERS, DELETERS"""
class Employee():
  new_id = 1
  def __init__(self, name=None):
    self.id = Employee.new_id
    Employee.new_id += 1
    self._name = name

  # Write your code below
    def get_name(self):
      return self._name

    def set_name(self, namestring):
      self._name = namestring

    def del_name(self):
      del self._name

e1 = Employee("Maisy")
e2 = Employee()



e1 = Employee("Maisy")
e2 = Employee()
print(e1.get_name())

e2.set_name("Fluffy")
print(e2.get_name())

e2.del_name()
print(e2.get_name())



"""REVIEW"""
from abc import ABC, abstractmethod

class AbstractEmployee(ABC):
  new_id = 1
  def __init__(self):
    self.id = AbstractEmployee.new_id
    AbstractEmployee.new_id += 1

  @abstractmethod
  def say_id(self):
    pass

class User:
  def __init__(self):
    self._username = None

  @property
  def username(self):
    return self._username

  @username.setter
  def username(self, new_name):
    self._username = new_name

class Meeting:
  def __init__(self):
    self.attendees = []
  
  def __add__(self, employee):
    print("{} added.".format(employee.username))
    self.attendees.append(employee.username)

  def __len__(self):
    return len(self.attendees)

class Employee(AbstractEmployee, User):
    def __init__(self, username):
      super().__init__()
      User.__init__(self)
      self.username = username

    def say_id(self):
      print("My id is {}".format(self.id))
 
    def say_username(self):
      print("My username is {}".format(self.username))