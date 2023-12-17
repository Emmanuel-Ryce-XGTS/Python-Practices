"""Sal's Shipping
Sal runs the biggest shipping company in the tri-county area, Sal’s Shippers. 
Sal wants to make sure that every single one of his customers has the best, 
and most affordable experience shipping their packages.

In this project, you’ll build a program that will take the weight of a package
and determine the cheapest way to ship that package using Sal’s Shippers.

Sal’s Shippers has several different options for a customer to ship their package:

Ground Shipping, which is a small flat charge plus a rate based on the weight of your package.
Ground Shipping Premium, which is a much higher flat charge, but you aren’t charged for weight.
Drone Shipping (new), which has no flat charge, but the rate based on weight is
triple the rate of ground shipping.
"""
weight = 0.1
costs = 0
flat_charge = 0.00

#premium ground shipping prices

premium_ground_shipping = 125.00
print(f"The Premium ground shipping standard price is: {premium_ground_shipping} \n")

#Grounds Shipping

weight = 8.4
costs = 0
flat_charge = 0.00

#premium ground shipping prices
premium_ground_shipping = 125.00
print(f"The Premium ground shipping standard price is: {premium_ground_shipping} \n")
#premium ground shipping prices


#Grounds Shipping
# A package that weighs 8.4 pounds should cost $53.60 to ship with normal ground shipping:
# 8.4 lb×$4.00+$20.00=$53.60


if weight <= 2:
  costs = 1.50
  flat_charge = 20.00
  print("Your item is about 2 lb or less	" + "the cost is: $" + str(costs))

elif weight > 2 and weight <= 6:
  flat_charge = 20.00
  costs = 3.0
  print("Your item is Over 2 lb but less than or equal to 6 lb \n" + "The weight cost per pound is: $" + str(costs))

elif weight > 6 and weight <= 10:
  flat_charge = 20.00
  costs = 4.00
  print("Your item is Over 2 lb but less than or equal to 6 lb \n" + "the weight cost per pound is: $" + str(costs))

else:
  flat_charge = 20.00
  costs = 4.75
  print("Your item is Over 10 lb \n" + "The weight cost per pound is: \n$" + str(costs))

package_price = costs * weight + flat_charge

print("Your total cost from your weight is: $" + str(weight) + " multiplied by your cost " + str(costs) + " gives a total of: " + str(package_price))

print("\n\n")


#Drone Shipping
# A package that weighs 1.5 pounds should cost $6.75 to ship by drone:
#   1.5 lb×$4.50+$0.00=$6.75

drone_weight = 1.5
drone_costs = 0
flat_charge = 0.00

if drone_weight <= 2:
  drone_costs = 4.50
  flat_charge = 0
  print("Your item is about 2 lb or less	" + "the cost is: $ " + str(drone_costs))

elif drone_weight > 2 and drone_weight <= 6:
  flat_charge = 0
  drone_costs = 9.00
  print("Your item is Over 2 lb but less than or equal to 6 lb \n" + "The weight cost per pound is: $" + str(drone_costs))

elif drone_weight > 6 and drone_weight <= 10:
  flat_charge = 0
  drone_costs = 12.00
  print("Your item is Over 2 lb but less than or equal to 6 lb \n" + "the weight cost per pound is: $" + str(drone_costs))

else:
  flat_charge = 0
  drone_costs = 14.25
  print("Your item is Over 10 lb \n" + "The weight cost per pound is: \n$" + str(drone_costs))

drone_package_price = drone_costs * drone_weight + flat_charge

print("Your total cost from your weight is: $" + str(drone_weight) + " multiplied by your cost " + str(drone_costs) + " gives a total of: " + str(drone_package_price))