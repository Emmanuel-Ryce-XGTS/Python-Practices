"""Iterator Objects: __iter__() and iter()"""
sku_list = [7046538, 8289407, 9056375, 2308597]

# Write your code below:
print(dir(sku_list))

sku_iterator_object_one  = sku_list.__iter__()

print(sku_iterator_object_one)

sku_iterator_object_two = iter(sku_list)
print(sku_iterator_object_two)


"""Iterator Objects:__next__() and next()
"""
dog_foods = {
  "Great Dane Foods": 4,
  "Min Pip Pup Foods": 10,
  "Pawsome Pup Foods": 8
}

# Write your code below:


dog_food_iterator  = iter(dog_foods) 


next_dog_food1 = next(dog_food_iterator)

print(next_dog_food1)

next_dog_food2 = dog_food_iterator.__next__()
next_dog_food3 = dog_food_iterator.__next__()

print(next_dog_food2)
print(next_dog_food3)
next(dog_food_iterator)



"""Iterators and For Loops"""

class CustomerCounter:
# Write your code below:
  def __iter__(self):
    self.count = 0 
    return self

  def __next__(self):
    self.count += 1
    if self.count > 100:
      raise StopIteration
    return self.count

customer_counter = CustomerCounter()

for customercount in customer_counter:
  print(customercount)
  
  
  """INFINITE ITERATOR COUNT"""
  
  #Write your code below:
import itertools

max_capacity = 1000
num_bags = 0

for i in itertools.count(start=13.5, step=13.5):
  if i >= max_capacity:
    break
  num_bags += 1
  print(num_bags)
  
  
"""Input-Dependent Iterator Chain"""
import itertools

great_dane_foods = [2439176, 3174521, 3560031]
min_pin_pup_foods = [6821904, 3302083]
pawsome_pup_foods = [9664865]

# Write your code below: 
all_skus_iterator = itertools.chain( great_dane_foods, min_pin_pup_foods, pawsome_pup_foods)


for number in all_skus_iterator:
  print(number)
  
  
  
  """Combinatoric Iterator: COmbinations"""
  
  import itertools

collars = ["Red-S","Red-M", "Blue-XS", "Green-L", "Green-XL", "Yellow-M"]

# Write your code below: 
collar_combo_iterator = itertools.combinations(collars, 3)
print(collar_combo_iterator)

for item in collar_combo_iterator:
  print(item)
  
  
  
"""Review"""
# Write your code below:
import itertools
cat_toys = [("laser",1.99, ), ("fountain", 5.99), ("scratcher", 10.99), ("catnip", 15.99)]
max_money = 15
options = []

cat_toy_iterator = iter(cat_toys)

print(next(cat_toy_iterator))
print(next(cat_toy_iterator))
print(next(cat_toy_iterator))
print(next(cat_toy_iterator))

toy_combos = itertools.combinations(cat_toys, 2)
for combo in toy_combos:
   toy1 = combo[0]
   cost_of_toy1 = toy1[1]
   toy2 = combo[1]
   cost_of_toy2 = toy2[1]

   if cost_of_toy1 + cost_of_toy2 <= max_money:
      options.append(combo)

print(options)


