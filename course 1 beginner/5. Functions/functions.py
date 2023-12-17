"""parte 1, 2, 3 intro."""

"Part4 - 5 definir"

def function_name():
  # functions tasks go here

  print("Walk 4 mins to 34th St Herald Square train station")
  print("Take the Northbound N, Q, R, or W train 1 stop")
  print("Get off the Times Square 42nd Street stop")
  print("Take lots of pictures!")
function_name()



# part 6 Parameters & Arguments
#Your code below:
def generate_trip_instructions(location):
  print("Looks like you are planning a trip to visit " + location)
  print("You can use the public subway system to get to " + location)
generate_trip_instructions("Central Park")
generate_trip_instructions("Grand Central Station")


#Part 7 multiple parameters:

# Write your code below: 
def calculate_expenses(plane_ticket_price, car_rental_rate, hotel_rate, trip_time):

  car_rental_total = car_rental_rate * trip_time
  hotel_total  = hotel_rate  * trip_time - 10

  print(car_rental_total + hotel_total + plane_ticket_price)

calculate_expenses(200, 100, 100, 5)

"""Part 8 Types of Arguments
In Python, there are 3 different types of arguments we can give a function.

"""

# Write your code below:
def trip_planner(first_destination, second_destination, final_destination = "Codecademy HQ"):
  print("Here is what your trip will look like!")
  print("First, we will stop in" ,first_destination, "then" ,second_destination, "and lastly", final_destination)
  
trip_planner("France", "Germany", "Denmark") 

trip_planner("Denmark", "France", "Germany")

trip_planner(first_destination = "Iceland", second_destination = "India", final_destination = "Germany")

trip_planner("Brooklyn", "Queens")


"""part 9 integrated functions"""

tshirt_price = 9.75
shorts_price = 15.50
mug_price = 5.99
poster_price = 2.00
max_price = 0
# Write your code below:
max_price = max(tshirt_price, shorts_price, mug_price, poster_price, max_price)

print(max_price)

min_price = min(tshirt_price, shorts_price, mug_price, poster_price, max_price)

print(min_price)

rounded_price = round(tshirt_price , 1)

print(rounded_price)


"""part 10 Variable Access"""
favorite_locations = "Paris, Norway, Iceland"
print("There are 3 locations")
  # This function will print a hardcoded count of how many locations we have.
def print_count_locations():
  favorite_locations = "Paris, Norway, Iceland"
  print("There are 3 locations")
    
# This function will print the favorite locations
def show_favorite_locations():
  print("Your favorite locations are: " + favorite_locations)

print_count_locations()
show_favorite_locations()


"""Parte 11 Return Functions"""

current_budget = 3500.75

def print_remaining_budget(budget):
  print("Your remaining budget is: $" + str(budget))

print_remaining_budget(current_budget)

# Write your code below: 

def deduct_expense(budget, expense):
  budget = budget - expense
  return budget

shirt_expense = 9

new_budget_after_shirt = deduct_expense(current_budget, shirt_expense)
print(type(new_budget_after_shirt))

print_remaining_budget(new_budget_after_shirt)
 

# def calculate_exchange_usd(us_dollars, exchange_rate):
#   return us_dollars * exchange_rate


# new_zealand_exchange = calculate_exchange_usd(100, 1.4)

# print("100 dollars in US currency would give you " + str(new_zealand_exchange) + " New Zealand dollars")


def top_tourist_locations_italy():
  first = "Rome"
  second = "Venice"
  third = "Florence"

  return first, second, third

most_popular1, most_popular2, most_popular3 = top_tourist_locations_italy()

print(most_popular1) 
print(most_popular2)
print(most_popular3)



# weather_data = ['Sunny', 'Sunny', 'Cloudy', 'Raining', 'Snowing']

# def threeday_weather_report(weather):
#   first_day = " Tomorrow the weather will be " + weather[0]
#   second_day = " The following day it will be " + weather[2]
#   third_day = " Two days from now it will be " + weather[2]
#   return first_day, second_day, third_day

# monday, tuesday, wednesday = threeday_weather_report(weather_data)

# print(monday)
# print(tuesday)
# print(wednesday)


def trip_planner_welcome(name):
  print("Welcome to tripplanner v1.0 " , name)

trip_planner_welcome("Frank")

def estimated_time_rounded(estimated_time):
  rounded_time = round(estimated_time)
  return rounded_time

print(estimated_time_rounded(2.5))
estimate = estimated_time_rounded(2.5)

def destination_setup(origin, destination, estimated_time, mode_of_transport = "Car"):
  print("Your trip starts off in" + origin + "And you are traveling to " + destination + " You will be traveling by " + mode_of_transport + "It will take approximately " + str(estimated_time) + " hours")

"""destination_setup(origin = "Colon" , destination = "Panama", estimated_time = estimate , mode_of_transport = "Bus")
"""

destination_setup(" Colon ", " Panama ", estimate, mode_of_transport = "Bus ")
