"""
Global functions
"""

print(' -- Globals Namespace with empty script -- \n')
# Write Checkpoint 1 here: 

import random

first_name = "Jaya"
last_name = "Bodegard" 

def print_variables():
  random_number = random.randint(0,9)
  print(first_name)
  print(last_name)
  print(random_number)


# Write Checkpoint 2 here: 
print(globals())
global_variable = 'global'


def print_global():
  global_variable = "nested_global"
  nested_variable = "nested value" 

print(globals())

# Write Checkpoint 3 here: 




print(' \n -- Globals Namespace non-empty script -- \n')
# Write Checkpoint 4 here: 




"""Funciones integradas de python"""
 
global_variable = 'global'

def add(num1, num2):
  nested_value = 'Inside Function'   
  print(num1 + num2)

add(5, 10)  
global_variable = 'global'

def add(num1, num2):
  nested_value = 'Inside Function'   
  print(num1 + num2)
  print(locals())

add(5, 10)  

15
{'num1': 5, 'num2': 10, 'nested_value': 'Inside Function'}
  
 
23242526272829303132333435
global_variable = 'global'



print(' -- Local and global Namespaces with empty script -- \n')
# Write Checkpoint 1 here:

print(locals())
print(globals())
 
