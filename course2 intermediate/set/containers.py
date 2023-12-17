# Write your code below!
company_name = "erm"

company_location = 1 , 2


company_products = ["Juice","Cake","ICE", "Paper","Milk"]

company_data = {"name": company_name, "location": company_location, "products": company_products} 

print(company_data)
#{'name': 'erm', 'location': (1, 2), 'products': ['Juice', 'Cake', 'ICE', 'Paper', 'Milk']}

"""COLLECTIONS DEQUE"""

from helper_functions import process_csv_supplies
from collections import deque

# The first row is skipped since it only contains labels
csv_data = process_csv_supplies()[1:]

# Here is a sample of 2 elements in csv_data:
# [ ['nylon', '10', 'unimportant'], ['wool', '1', 'important'] ]

# Write your code below!
supplies_deque = deque()

for items in csv_data:
  if items[2] =="important":
    supplies_deque.appendleft(tuple(items))
  else:
    supplies_deque.append(tuple(items))

ordered_important_supplies = deque()

for _ in range(25):
    ordered_important_supplies.append(supplies_deque.popleft())

ordered_unimportant_supplies = deque()

for i in range(10):
  ordered_unimportant_supplies.append(supplies_deque.pop())

print(ordered_unimportant_supplies)



"""NAMED TUPPLE PART 4"""
from collections import namedtuple

clothes = [('t-shirt', 'green', 'large', 9.99),
           ('jeans', 'blue', 'medium', 14.99),
           ('jacket', 'black', 'x-large', 19.99),
           ('t-shirt', 'grey', 'small', 8.99),
           ('shoes', 'white', '12', 24.99),
           ('t-shirt', 'grey', 'small', 8.99)]

# Write your code below!
ClothingItem = namedtuple('ClothingItem', ['type', 'color', 'size' , 'price'])

new_coat = ClothingItem("coat", "black", "small", 14.99)

coat_cost = new_coat.price

updated_clothes_data = []

for clothesI in clothes:
  updated_clothes_data.append(ClothingItem(clothesI[0], clothesI[1], clothesI[2], clothesI[3]))

  print(updated_clothes_data)


"""DEFAULT DICT PART 5"""
from collections import defaultdict

site_locations = {'t-shirt': 'Shirts',
                  'dress shirt': 'Shirts',
                  'flannel shirt': 'Shirts',
                  'sweatshirt': 'Shirts',
                  'jeans': 'Pants',
                  'dress pants': 'Pants',
                  'cropped pants': 'Pants',
                  'leggings': 'Pants'
                  }
updated_products = ['draped blouse', 'leggings', 'undershirt', 'dress shirt', 'jeans', 'sun dress', 'flannel shirt', 'cropped pants', 'dress pants', 't-shirt', 'camisole top', 'sweatshirt']

# Write your code below!
validated_locations = defaultdict(lambda: 'TODO: Add to website')

validated_locations.update(site_locations)

for data in updated_products:
  site_locations[data] = validated_locations[data]

print(site_locations)


"""ORDERED DICT part 6"""

from collections import OrderedDict

# The first 15 orders are provided
order_data = [['Order: 1', 'purchased'],
              ['Order: 2', 'purchased'],
              ['Order: 3', 'purchased'],
              ['Order: 4', 'returned'],
              ['Order: 5', 'purchased'],
              ['Order: 6', 'canceled'],
              ['Order: 7', 'returned'],
              ['Order: 8', 'purchased'],
              ['Order: 9', 'returned'],
              ['Order: 10', 'canceled'],
              ['Order: 11', 'purchased'],
              ['Order: 12', 'returned'],
              ['Order: 13', 'purchased'],
              ['Order: 14', 'canceled'],
              ['Order: 15', 'purchased']]

# Write your code below!

orders = OrderedDict(order_data)
to_move = []
to_remove = []

for key, val in orders.items():
  if val == 'returned':
    to_move.append(key)
  elif val == 'canceled':
    to_remove.append(key)

for item in to_remove:
  orders.pop(item)

for item in to_move:
  orders.move_to_end(item)

print(orders)



"""ChainMAp Parte 7"""
from collections import ChainMap
year_profit_data = [
    {'jan_profit': 15492.30, 'jan_holiday_profit': 2589.12},
    {'feb_profit': 17018.05, 'feb_holiday_profit': 3701.88},
    {'mar_profit': 11849.13},
    {'apr_profit': 9870.68},
    {'may_profit': 13662.34},
    {'jun_profit': 12903.54},
    {'jul_profit': 16965.08, 'jul_holiday_profit': 4360.21},
    {'aug_profit': 17685.69},
    {'sep_profit': 9815.57},
    {'oct_profit': 10318.28},
    {'nov_profit': 23295.43, 'nov_holiday_profit': 9896.55},
    {'dec_profit': 21920.19, 'dec_holiday_profit': 8060.79}
]

new_months_data = [
    {'jan_profit': 13977.85, 'jan_holiday_profit': 2176.43},
    {'feb_profit': 16692.15, 'feb_holiday_profit': 3239.74},
    {'mar_profit': 17524.35, 'mar_holiday_profit': 4301.92}
]

# Write your code below!

# Checkpoint #1
profit_map = ChainMap(*year_profit_data)

# Checkpoint #2
def get_profits(input_map):
    total_standard_profit = 0.0
    total_holiday_profit = 0.0

    for key in input_map.keys():
        if 'holiday' in key:
            total_holiday_profit += input_map[key]
        else:
            total_standard_profit += input_map[key]

    return total_standard_profit, total_holiday_profit

last_year_standard_profit, last_year_holiday_profit = get_profits(profit_map)

# Checkpoint #3
for item in new_months_data:
    profit_map = profit_map.new_child(item)

current_year_standard_profit, current_year_holiday_profit = get_profits(profit_map)

# Checkpoint #4
year_diff_standard_profit = current_year_standard_profit - last_year_standard_profit
year_diff_holiday_profit = current_year_holiday_profit - last_year_holiday_profit

print(year_diff_standard_profit)
print(year_diff_holiday_profit)


"""PART 10 USER DICT"""

from collections import UserDict

data = {'order_4829': {'type': 't-shirt', 'size': 'large', 'price': 9.99, 'order_status': 'processing'},
        'order_6184': {'type': 'pants', 'size': 'medium', 'price': 14.99, 'order_status': 'complete'},
        'order_2905': {'type': 'shoes', 'size': 12, 'price': 22.50, 'order_status': 'complete'},
        'order_7378': {'type': 'jacket', 'size': 'large', 'price': 24.99, 'order_status': 'processing'}}

# Write your code below!
class OrderProcessingDict(UserDict):

   def clean_orders(self):
        to_del = []

        for key, val in self.data.items():
            if val['order_status'] == 'complete':
                to_del.append(key)

        for item in to_del:
            del self.data[item]

# Checkpoint #2
process_dict = OrderProcessingDict(data)
process_dict.clean_orders()
print(process_dict)


"""USER LIST"""

from collections import UserList

data = [4, 6, 8, 9, 5, 7, 3, 1, 0]

# Write your code below!
class ListSorter(UserList):

  def append(self, item):
      self.data.append(item)
      self.data.sort()


sorted_list = ListSorter(data)
sorted_list.append(2)
print(sorted_list)


"""UserString parte 12"""
class SubtractString(UserString):

    def __sub__(self, other):
        if other in self.data:
            self.data = self.data.replace(other, '')

# Checkpoint #2
subtract_string = SubtractString(str_name)
subtract_string - str_word
print(subtract_string)



"""REVIEW"""


# Checkpoint #1
split_prices = deque()

#Checkpoint #2
for item in overstock_items:
  if item[1] > 20.0:
    split_prices.appendleft(item)
  else:
    split_prices.append(item)
print(split_prices)

# Checkpoint #3
ClothesBundle = namedtuple('ClothesBundle', ['bundle_items', 'bundle_price'])

# Checkpoint #4
bundles = []
while len(split_prices) >= 5:
  bundle_list = [split_prices.pop(), split_prices.pop(), split_prices.pop(), split_prices.popleft(),split_prices.popleft()]

  calc_price = sum(b[1] for b in bundle_list)
  bundles.append(ClothesBundle(bundle_list, calc_price))

# Checkpoint #5
promoted_bundles = []
for bundle in bundles:
  if bundle.bundle_price > 100:
    promoted_bundles.append(bundle)

# # Checkpoint #6
print(promoted_bundles)

# for bundle in promoted_bundles:
#   print(bundle)    