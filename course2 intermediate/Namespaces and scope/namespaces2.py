""" fUNCION DENTRO DE UNA FUNCION PART 3"""

def calc_paint_amount(width, height):

  square_feet = width * height
  # Write your code below!

  def calc_gallons():
    square_feet = ""
  return square_feet / 400
  calc_gallons()


print('Number of paint gallons needed: ')
print(str(calc_paint_amount(30,20)))


"""NON LOCAL """

walls = [(20, 9), (25, 9), (20, 9), (25, 9)]


def calc_paint_amount(wall_measurements):
  square_feet = 0

  def calc_square_feet():
    nonlocal square_feet

    for width, height in wall_measurements:
      square_feet += width * height

  def calc_gallons():
    return square_feet / 400

  calc_square_feet()

  return calc_gallons()


print('Number of paint gallons needed: ')
print(str(calc_paint_amount(walls)))



"""Global scope issues"""

paint_gallons_available = {
    'red': 50,
    'blue': 72,
    'green': 99,
    'yellow': 33
}

def print_available(color):

  print('There are ' + str(paint_gallons_available[color]) + ' gallons available of ' + color + ' paint.')


def print_all_colors_available():
  for color in paint_gallons_available:
    print(color)

print_available('red')
print_all_colors_available()
  
  
"""GLOBAL INSIDE A FUNCTION PART 6"""

def print_available(color):
  global paint_gallons_available
  paint_gallons_available = {
    'red': 50,
    'blue': 72,
    'green': 99,
    'yellow': 33
  }
  print('There are ' + str(paint_gallons_available[color]) + ' gallons available of ' + color + ' paint.')


print_available('red')
for color in paint_gallons_available:
  print(color)
  
  
  
  """SCOPE RESOlution. the legb rule ep 7"""
  
  color = 'green'

# Fix the function below:
def change_color(new_color):

  to_update = new_color
  color = to_update

  def disp_color():
    global color
    print('The original color was: ' + color)

  disp_color()

  print('The new color is: ' + color)


change_color('blue')



"""REVIEW PART 8 """

# Outer function
def function1():
  global var1
  var1 = 1
  var2 = 2
  # Inner function
  def function2():
    nonlocal var2
    global var3
    var2 += 1
    var3 = 3
    print(globals())
    print(locals())
  
  # Call inner function
  function2()

# Call outer function
function1()