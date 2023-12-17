def get_math_function(operation): #+ or -
    
    def add(n1,n2):
        return n1 + n2
    def sub(n1, n2):
        return n1 - n2
    
    if operation == "+":
        return add
    elif operation == "-":
        return sub    
    
add_function = get_math_function("+")
print( add_function)
print( add_function(4 , 6))

sub_function = get_math_function("-")
print( sub_function)
print( sub_function(4 , 6))





"""Decortators"""

def title_decorator(print_name_function):
    def wrapper():
        print("Professor:")
        print_name_function()
    return wrapper

@title_decorator
def print_my_name():
    print("Mike")
    
@title_decorator
def print_joes_name():
    print("Joe")
    
# decorated_function = title_decorator(print_joes_name)   
 
# decorated_function()
print_my_name()
    
    
    
"""decorators w/Parameters"""
def title_decorator(print_name_function):
    def wrapper(*args, **kwargs):
        print("Professor:")
        print_name_function(*args, *kwargs)
    return wrapper

# @title_decorator
def print_my_name(name, age):
    print("name" + "You are" + str(age))
     
print_my_name("Shelby" , 50)
