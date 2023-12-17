"""Functions 1 RECAP"""

tables = {
  1: ['Jiho', False],
  2: [],
  3: [],
  4: [],
  5: [],
  6: [],
  7: [],
}
print(tables)

# Write your code below: 


def assign_table(table_number, name, vip_status = False):
    # Update the tables dictionary with the new customer information
    tables[table_number] = [name, vip_status]

assign_table(6, "Yoni", False)

print(tables)

assign_table(name = "Martha", table_number = 3, vip_status = True)

print(tables)

assign_table(4, "Karla")

print(tables)


"""ARGS *args"""

order_items = "ABCD"
def print_order(*order_items):

  print(order_items) 

print_order("Orange Juice", "Apple Juice", "Scrambled Eggs", "Pancakes")


"""Working with ARGS"""
tables = {
  1: {
    'name': 'Jiho',
    'vip_status': False,
    'order': 'Orange Juice, Apple Juice'
  },
  2: {},
  3: {},
  4: {},
  5: {},
  6: {},
  7: {},
}
print(tables)

def assign_table(table_number, name, vip_status=False): 
  tables[table_number]['name'] = name
  tables[table_number]['vip_status'] = vip_status
  tables[table_number]['order'] = ''

# Write your code below: 

def assign_and_print_order(table_number, *order_items): 

  tables[table_number]['order'] = order_items

  for orders in order_items:
    print(orders)

assign_table(2, 'Arwa', True)


assign_and_print_order(2, "Steak", "Seabass", "Wine Bottle")

print(tables)



"""**KWARGS ARGUMENTS"""
tables = {
  1: {
    'name': 'Chioma',
    'vip_status': False,
    'order': {
      'drinks': 'Orange Juice, Apple Juice',
      'food_items': 'Pancakes'
    }
  },
  2: {},
  3: {},
  4: {},
  5: {},
  6: {},
  7: {},
}
print(tables)


# Write your code below: 
def assign_food_items(**order_items):
  print(order_items)

  food = order_items.get("food")
  drinks = order_items.get("drinks")
  print(food)
  print(drinks)

assign_food_items(food="mac & cheese", drinks= "soda")
# Example Call
assign_food_items(food='Pancakes, Poached Egg', drinks='Water')


"""PART 5 Working with **Kwargs"""

tables = {
  1: {
    'name': 'Chioma',
    'vip_status': False,
    'order': {
      'drinks': 'Orange Juice, Apple Juice',
      'food_items': 'Pancakes'
    }
  },
  2: {},
  3: {},
  4: {},
  5: {},
  6: {},
  7: {},
}

def assign_table(table_number, name, vip_status=False): 
  tables[table_number]['name'] = name
  tables[table_number]['vip_status'] = vip_status
  tables[table_number]['order'] = {}

assign_table(2, 'Douglas', True)
print('--- tables with Douglas --- \n', tables)

def assign_food_items(table_number, **order_items):
  food = order_items.get('food')
  drinks = order_items.get('drinks')
  tables[table_number]['order']['food_items'] = food
  tables[table_number]['order']['drinks'] = drinks

print('\n --- tables after update --- \n')

assign_food_items(2, food='Seabass, Gnocchi, Pizza' , drinks= 'Margarita, Water')

print(tables)





"""Function Arguments part 6 all together"""
# Write your code below: 
def single_prix_fixe_order(appetizer, *entrees, sides, **dessert_scoops):

    print(appetizer)
    print(entrees)
    print(sides)
    print(dessert_scoops)
  


single_prix_fixe_order("Baby Beets", "Salmon", "Scallops", sides="Mashed Potatoes", dessert_scoops="Vanilla, Cookies and Cream")


# Parte 7 FUNCTION ARGUMENTS
# Function Call Unpacking & Beyond

# my_num_list = [3, 6, 9]

# def sum(num1, num2, num3):
#   print(num1 + num2 + num3)

# sum(*my_num_list)

# Would output: 18




def calculate_price_per_person(total, tip, split):
  total_tip = total * (tip/100)
  split_price = (total + total_tip) / split
  print(split_price)

# Write your code below: 

table_7_total = [534.50, 20.0, 5]


def calculate_price_per_person():

  calculate_price_per_person(*table_7_total)


"""REVIEW
tables = {
  1: {
    'name': 'Jiho',
    'vip_status': False,
    'order': {
      'drinks': 'Orange Juice, Apple Juice',
      'food_items': 'Pancakes',
      'total': [534.50, 20.0, 5]
    }
  },
  2: {},
  3: {},
  4: {},
  5: {},
  6: {},
  7: {},
}

def assign_table(table_number, name, vip_status=False): 
  tables[table_number]['name'] = name
  tables[table_number]['vip_status'] = vip_status
  tables[table_number]['order'] = {}

def assign_food_items(table_number, **order_items):
  food = order_items.get('food')
  drinks = order_items.get('drinks')
  tables[table_number]['order']['food_items'] = food
  tables[table_number]['order']['drinks'] = drinks

def calculate_price_per_person(total, tip, split):
    total_tip = total * (tip/100)
    split_price = (total + total_tip) / split
    print(split_price)

"""