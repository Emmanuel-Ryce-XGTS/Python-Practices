"""PART 5
Add A Key
To add a single key: value pair to a dictionary, we can use the syntax:

dictionary[key] = value
For example, if we had our menu dictionary from the first exercise:

menu = {"oatmeal": 3, "avocado toast": 6, "carrot juice": 5, "blueberry muffin": 2}

And we wanted to add a new item, "cheesecake" for 8 dollars, we could use:

menu["cheesecake"] = 8

Now, menu looks like:

{"oatmeal": 3, "avocado toast": 6, "carrot juice": 5, "blueberry muffin": 2, "cheesecake": 8}

Instructions
Checkpoint 1 Passed
1.
Create an empty dictionary called animals_in_zoo.

Checkpoint 2 Passed
2.
Walking around the zoo, you see 8 zebras. Add "zebras" to animals_in_zoo as a key with a value of 8.

Checkpoint 3 Passed
3.
The primate house was bananas! Add "monkeys" to animals_in_zoo as a key with a value of 12.

Checkpoint 4 Passed
4.
As you leave the zoo, you are saddened that you did not see any dinosaurs. Add "dinosaurs" to animals_in_zoo as a key with a value of 0.

Checkpoint 5 Passed
5.
Print animals_in_zoo."""



animals_in_zoo ={}

animals_in_zoo ={"zebras":8, "monkeys":12, "dinosaurs":0 }
print(animals_in_zoo)



"""PART 6 
Add Multiple Keys
If we wanted to add multiple key : value pairs to a dictionary at once, we can use the .update() method.

Looking at our sensors object from a previous exercise:

sensors = {"living room": 21, "kitchen": 23, "bedroom": 20}

If we wanted to add 3 new rooms, we could use:

sensors.update({"pantry": 22, "guest room": 25, "patio": 34})

This would add all three items to the sensors dictionary.

Now, sensors looks like:

{"living room": 21, "kitchen": 23, "bedroom": 20, "pantry": 22, "guest room": 25, "patio": 34}

Instructions
Checkpoint 1 Passed
1.
In one line of code, add two new users to the user_ids dictionary:

theLooper, with an id of 138475
stringQueen, with an id of 85739

Stuck? Get a hint
Checkpoint 2 Passed
2.
Print user_ids."""


user_ids = {"teraCoder": 9018293, "proProgrammer": 119238}

user_ids.update({"theLooper":138475 , "stringQueen": 85739})

print(user_ids)


"""PART 7
CREATING DICTIONARIES
Overwrite Values
We know that we can add a key by using the following syntax:

menu["banana"] = 3

This will create a key "banana" and set its value to 3. But what if we used a key that already has an entry in the menu dictionary?

In that case, our value assignment would overwrite the existing value attached to that key. We can overwrite the value of "oatmeal" like this:

menu = {"oatmeal": 3, "avocado toast": 6, "carrot juice": 5, "blueberry muffin": 2}
menu["oatmeal"] = 5
print(menu)

This would yield:

{"oatmeal": 5, "avocado toast": 6, "carrot juice": 5, "blueberry muffin": 2}

Notice the value of "oatmeal" has now changed to 5.

Instructions
Checkpoint 1 Passed
1.
Add the key "Supporting Actress" and set the value to "Viola Davis".

Checkpoint 2 Passed
2.
Without changing the definition of the dictionary oscar_winners, change the value associated with the key "Best Picture" to "Moonlight".

"""


oscar_winners = {"Best Picture": "La La Land", "Best Actor": "Casey Affleck", "Best Actress": "Emma Stone", "Animated Feature": "Zootopia"}

oscar_winners["Supporting Actress"] = "Viola Davis"

print(oscar_winners)
oscar_winners["Best Picture"] = "Moonlight"

print(oscar_winners)


"""PArt 8 
CREATING DICTIONARIES
Dict Comprehensions
Let’s say we have two lists that we want to combine into a dictionary, like a list of students and a list of their heights, in inches:

names = ['Jenny', 'Alexus', 'Sam', 'Grace']
heights = [61, 70, 67, 64]

Python allows you to create a dictionary using a dict comprehension, with this syntax:

students = {key:value for key, value in zip(names, heights)}
#students is now {'Jenny': 61, 'Alexus': 70, 'Sam': 67, 'Grace': 64}

Remember that zip() combines two lists into an iterator of tuples with the list elements paired together. This dict comprehension:

Takes a pair from the iterator of tuples
Names the elements in the pair key (the one originally from the names list) and value (the one originally from the heights list)
Creates a key : value item in the students dictionary
Repeats steps 1-3 for the entire iterator of pairs
Instructions
Checkpoint 1 Passed
1.
You have two lists, representing some drinks sold at a coffee shop and the milligrams of caffeine in each. First, create a variable called zipped_drinks that is an iterator of pairs between the drinks list and the caffeine list.


Stuck? Get a hint
Checkpoint 2 Passed
2.
Create a dictionary called drinks_to_caffeine by using a dict comprehension that goes through the zipped_drinks iterator and turns each tuple pair into a key:value item.
"""
drinks = ["espresso", "chai", "decaf", "drip"]
caffeine = [64, 40, 0, 120]
zipped_drinks = zip(drinks, caffeine)

# You can convert the iterator to a list if needed
zipped_drinks = list(zipped_drinks)

# Now, zipped_drinks contains pairs of (drink, caffeine) values
print(zipped_drinks)

# Create the dictionary using a dictionary comprehension
drinks_to_caffeine = {drink: caffeine for drink, caffeine in zipped_drinks}

# Now, drinks_to_caffeine contains the mapping of drinks to their caffeine levels
print(drinks_to_caffeine)



"""REVIEW PART 9 
Review
So far we have learned:

How to create a dictionary
How to add elements to a dictionary
How to update elements in a dictionary
How to use a dict comprehension to create a dictionary from two lists
Let’s practice these skills!

Instructions
Checkpoint 1 Passed
1.
We are building a music streaming service. We have provided two lists, representing songs in a user’s library and the amount of times each song has been played.

Using a dict comprehension, create a dictionary called plays that goes through zip(songs, playcounts) and creates a song:playcount pair for each song in songs and each playcount in playcounts.


Stuck? Get a hint
Checkpoint 2 Passed
2.
Print plays.

Checkpoint 3 Passed
3.
After printing plays, add a new entry to it. The entry should be for the song "Purple Haze" and the playcount is 1.

Checkpoint 4 Passed
4.
This user has caught Aretha Franklin fever and listened to “Respect” 5 more times. Update the value for "Respect" to be 94 in the plays dictionary.

Checkpoint 5 Passed
5.
Create a dictionary called library that has two key: value pairs:

key "The Best Songs" with a value of plays, the dictionary you created
key "Sunday Feelings" with a value of an empty dictionary
Checkpoint 6 Passed
6.
Print library."""

songs = ["Like a Rolling Stone", "Satisfaction", "Imagine", "What's Going On", "Respect", "Good Vibrations"]
playcounts = [78, 29, 44, 21, 89, 5]

# Step 1: Create a dictionary called "plays" using a dictionary comprehension
plays = {song: playcount for song, playcount in zip(songs, playcounts)}

# Step 2: Print the "plays" dictionary
print(plays)

# Step 3: Add a new entry for "Purple Haze" with a playcount of 1
plays["Purple Haze"] = 1

# Step 4: Update the playcount for "Respect" to 94
plays["Respect"] = 94

# Step 5: Create a dictionary called "library" with two key-value pairs
library = {
    "The Best Songs": plays,
    "Sunday Feelings": {}
}

# Step 6: Print the "library" dictionary
print(library)
