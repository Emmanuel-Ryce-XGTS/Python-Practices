"""Part1 Reading a File
Computers use file systems to store and retrieve data.
Each file is an individual container of related information.
If you’ve ever saved a document, downloaded a song, or even sent an email you’ve created 
a file on some computer somewhere. Even script.py, the Python program you’re editing in the
learning environment, is a file.

"""
with open('welcome.txt', 'r') as text_file:


    text_data = text_file.read()

print(text_data)


"""Part 2, iterate on files:
with open('keats_sonnet.txt') as keats_sonnet:
  for line in keats_sonnet.readlines():
    print(line)
"""

with open('how_many_lines.txt') as lines_doc:
    # Step 2: Iterate through each line and print them
    for line in lines_doc.readlines():
        print(line)


"""PArt 3 Read trough lines"""
with open('just_the_first.txt') as first_line_doc:
  first_line = first_line_doc.readline()
  second_line = first_line_doc.readline()
  print(first_line)


"""Part 4, write a doc"""


with open('bad_bands.txt', 'w') as bad_bands_doc:
  bad_bands_doc.write("asime!")



"""Part 5 Append to a file"""
with open('cool_dogs.txt', 'a') as cool_dogs_file:
  cool_dogs_file.write("\n... June")
  cool_dogs_file.write("\n... Air Buddy is a Golden Retriever that plays basketball, which more than qualifies him for this list")


"""Printed to test the output"""
with open('cool_dogs.txt', 'r') as cool_dogs_file:
  contents = cool_dogs_file.read()

# Print the contents to the console
print(contents)




"""pART 6 What's With "with"?
fun_cities_file = open('fun_cities.txt', 'a')

# We can now append a line to "fun_cities".
fun_cities_file.write("Montréal")

# But we need to remember to close the file
fun_cities_file.close()

close_this_file = open('fun_file.txt')

setup = close_this_file.readline()
punchline = close_this_file.readline()

print(setup)
In script.py there’s a file object that doesn’t get closed correctly. Let’s fix it by changing the syntax!

Remove this line:

close_this_file = open('fun_file.txt')

And change it to use the with syntax from our previous exercises.

Remember to indent the rest of the body so that we don’t get an IndentError.
"""

with open('fun_file.txt') as close_this_file:
    setup = close_this_file.readline()
    punchline = close_this_file.readline()

# Print the setup
print(setup)


"""part 7 What Is a CSV File?
Text files aren’t the only thing that Python can read, but they’re the only thing that we don’t
need any additional parsing library to understand. CSV files are an example of a text file that 
impose a structure to their data. CSV stands for Comma-Separated Values and CSV files are usually 
the way that data from spreadsheet software (like Microsoft Excel or Google Sheets) is exported into 
a portable format. A spreadsheet that looks like the following

    """
with open('logger.csv') as log_csv_file:
  csv = log_csv_file.read()

  print(csv)
  
  
  
"""part 8 Reading a CSV File
Reading a CSV File
Recall our CSV file from our last exercise:

users.csv

Name,Username,Email
Roger Smith,rsmith,wigginsryan@yahoo.com
Michelle Beck,mlbeck,hcosta@hotmail.com
Ashley Barker,a_bark_x,a_bark_x@turner.com
Lynn Gonzales,goodmanjames,lynniegonz@hotmail.com

Even though we can read these lines as text without a problem, there are ways to access the data in a format better suited for programming purposes. In Python we can convert that data into a dictionary using the csv library’s DictReader object. Here’s how we’d create a list of the email addresses of all of the users in the above table:

import csv

list_of_email_addresses = []
with open('users.csv', newline='') as users_csv:
  user_reader = csv.DictReader(users_csv)
  for row in user_reader:
    list_of_email_addresses.append(row['Email'])

In the above code we first import our csv library, which gives us the tools to parse our CSV file. We then create the empty list list_of_email_addresses which we’ll later populate with the email addresses from our CSV. Then we open the users.csv file with the temporary variable users_csv.

We pass the additional keyword argument newline='' to the file opening open() function so that we don’t accidentally mistake a line break in one of our data fields as a new row in our CSV (read more about this in the Python documentation).

After opening our new CSV file we use csv.DictReader(users_csv) which converts the lines of our CSV file to Python dictionaries which we can use access methods for. The keys of the dictionary are, by default, the entries in the first line of our CSV file. Since our CSV’s first line calls the third field in our CSV “Email“, we can use that as the key in each row of our DictReader.

When we iterate through the rows of our user_reader object, we access all of the rows in our CSV as dictionaries (except for the first row, which we used to label the keys of our dictionary). By accessing the 'Email' key of each of these rows we can grab the email address in that row and append it to our list_of_email_addresses.

Instructions
Checkpoint 1 Passed
1.
Import the csv module.

Checkpoint 2 Passed
2.
Open up the file cool_csv.csv in the temporary variable cool_csv_file.

Checkpoint 3 Passed
3.
Using csv.DictReader read the contents of cool_csv_file into a new variable called cool_csv_dict.


Stuck? Get a hint
Checkpoint 4 Passed
4.
cool_csv.csv includes a cool fact about every person in the CSV.

For each row in cool_csv_dict print out that row’s "Cool Fact".
Recall our CSV file from our last exercise:

"""

import csv
list_of_email_addresses = []

with open('cool_csv.csv') as cool_csv_file:
  cool_csv_dict  = csv.DictReader(cool_csv_file)
  #cool_csv.csv includes a cool fact about every person in the CSV.

# For each row in cool_csv_dict print out that row’s "Cool Fact".


  for row in cool_csv_dict:
      print(row["Cool Fact"])


"""PART 9 Reading Different Types of CSV Files
I need to level with you, I’ve been lying to you for the past two exercises. Well, kind of. We’ve been acting like CSV files are Comma-Separated Values files. It’s true that CSV stands for that, but it’s also true that other ways of separating values are valid CSV files these days.

People used to call Tab-Separated Values files TSV files, but as other separators grew in popularity everyone realized that creating a new .[a-z]sv file format for every value-separating character used is not sustainable.

So we call all files with a list of different values a CSV file and then use different delimiters (like a comma or tab) to indicate where the different values start and stop.

Let’s say we had an address book. Since addresses usually use commas in them, we’ll need to use a different delimiter for our information. Since none of our data has semicolons (;) in them, we can use those.

addresses.csv

Name;Address;Telephone
Donna Smith;126 Orr Corner Suite 857\nEast Michael, LA 54411;906-918-6560
Aaron Osborn;6965 Miller Station Suite 485\nNorth Michelle, KS 64364;815.039.3661x42816
Jennifer Barnett;8749 Alicia Vista Apt. 288\nLake Victoriaberg, TN 51094;397-796-4842x451
Joshua Bryan;20116 Stephanie Stravenue\nWhitneytown, IA 87358;(380)074-6173
Andrea Jones;558 Melissa Keys Apt. 588\nNorth Teresahaven, WA 63411;+57(8)7795396386
Victor Williams;725 Gloria Views Suite 628\nEast Scott, IN 38095;768.708.3411x954

Notice the \n character, this is the escape sequence for a new line. The possibility of a new line escaped by a \n character in our data is why we pass the newline='' keyword argument to the open() function.

Also notice that many of these addresses have commas in them! This is okay, we’ll still be able to read it. If we wanted to, say, print out all the addresses in this CSV file we could do the following:

import csv

with open('addresses.csv', newline='') as addresses_csv:
  address_reader = csv.DictReader(addresses_csv, delimiter=';')
  for row in address_reader:
    print(row['Address'])

Notice that when we call csv.DictReader we pass in the delimiter parameter, which is the string that’s used to delineate separate fields in the CSV. We then iterate through the CSV and print out each of the addresses.

Instructions
"""
import csv

with open('books.csv') as books_csv:

    books_reader = csv.DictReader(books_csv, delimiter='@')
    
    # Step 4: Create a list called isbn_list by iterating through books_reader
    isbn_list = [row['ISBN'] for row in books_reader]

# Now you have a list of ISBN numbers from the CSV file
print(isbn_list)




"""part 10 wRITING A CSV FILE


Writing a CSV File
Naturally if we have the ability to read different CSV files we might want to be able to programmatically create CSV files that save output and data that someone could load into their spreadsheet software. Let’s say we have a big list of data that we want to save into a CSV file. We could do the following:

big_list = [{'name': 'Fredrick Stein', 'userid': 6712359021, 'is_admin': False}, {'name': 'Wiltmore Denis', 'userid': 2525942, 'is_admin': False}, {'name': 'Greely Plonk', 'userid': 15890235, 'is_admin': False}, {'name': 'Dendris Stulo', 'userid': 572189563, 'is_admin': True}] 

import csv

with open('output.csv', 'w') as output_csv:
  fields = ['name', 'userid', 'is_admin']
  output_writer = csv.DictWriter(output_csv, fieldnames=fields)

  output_writer.writeheader()
  for item in big_list:
    output_writer.writerow(item)

In our code above we had a set of dictionaries with the same keys for each, a prime candidate for a CSV. We import the csv library, and then open a new CSV file in write-mode by passing the 'w' argument to the open() function.

We then define the fields we’re going to be using into a variable called fields. We then instantiate our CSV writer object and pass two arguments. The first is output_csv, the file handler object. The second is our list of fields fields which we pass to the keyword parameter fieldnames.

Now that we’ve instantiated our CSV file writer, we can start adding lines to the file itself! First we want the headers, so we call .writeheader() on the writer object. This writes all the fields passed to fieldnames as the first row in our file. Then we iterate through our big_list of data. Each item in big_list is a dictionary with each field in fields as the keys. We call output_writer.writerow() with the item dictionaries which writes each line to the CSV file.

Instructions
Checkpoint 1 Passed
1.
We have a list in the workspace access_log which is a list of dictionaries we want to write out to a CSV file.

Let’s start by importing the csv module.

Checkpoint 2 Passed
2.
Open up the file logger.csv in the temporary variable logger_csv. Don’t forget to open the file in write-mode.

Checkpoint 3 Passed
3.
Create a csv.DictWriter instance called log_writer. Pass logger_csv as the first argument and then fields as a keyword argument to the keyword fieldnames.

Checkpoint 4 Passed
4.
Write the header to log_writer using the .writeheader() method.

Checkpoint 5 Passed
5.
Iterate through the access_log list and add each element to the CSV using log_writer.writerow().


"""


import csv

# Step 2: Open the CSV file "logger.csv" in write-mode
with open('logger.csv', 'w') as logger_csv:
    # Step 3: Create a csv.DictWriter instance
    fields = ['time', 'address', 'limit']
    log_writer = csv.DictWriter(logger_csv, fieldnames=fields)
    
    # Step 4: Write the header
    log_writer.writeheader()
    
    # Step 5: Iterate through the access_log list and add each element to the CSV
    access_log = [{'time': '08:39:37', 'limit': 844404, 'address': '1.227.124.181'}, 
                 {'time': '13:13:35', 'limit': 543871, 'address': '198.51.139.193'}, 
                 {'time': '19:40:45', 'limit': 3021, 'address': '172.1.254.208'}, 
                 {'time': '18:57:16', 'limit': 67031769, 'address': '172.58.247.219'}, 
                 {'time': '21:17:13', 'limit': 9083, 'address': '124.144.20.113'}, 
                 {'time': '23:34:17', 'limit': 65913, 'address': '203.236.149.220'}, 
                 {'time': '13:58:05', 'limit': 1541474, 'address': '192.52.206.76'}, 
                 {'time': '10:52:00', 'limit': 11465607, 'address': '104.47.149.93'}, 
                 {'time': '14:56:12', 'limit': 109, 'address': '192.31.185.7'}, 
                 {'time': '18:56:35', 'limit': 6207, 'address': '2.228.164.197'}]
    
    for log_entry in access_log:
        log_writer.writerow(log_entry)

        print(log_entry)
        
        
"""PART 11 Reading a JSON File
CSV isn’t the only file format that Python has a built-in library for. We can also use Python’s file tools to read and write JSON. JSON, an abbreviation of JavaScript Object Notation, is a file format inspired by the programming language JavaScript. The name, like CSV is a bit of a misnomer — some JSON is not valid JavaScript (and plenty of JavaScript is not valid JSON).

JSON’s format is endearingly similar to Python dictionary syntax, and so JSON files might be easy to read from a Python developer standpoint. Nonetheless, Python comes with a json package that will help us parse JSON files into actual Python dictionaries. Suppose we have a JSON file like the following:

purchase_14781239.json

{
  'user': 'ellen_greg',
  'action': 'purchase',
  'item_id': '14781239',
}

We would be able to read that in as a Python dictionary with the following code:

json_reader.py

import json

with open('purchase_14781239.json') as purchase_json:
  purchase_data = json.load(purchase_json)

print(purchase_data['user'])
# Prints 'ellen_greg'

First we import the json package. We opened the file using our trusty open() command. Since we’re opening it in read-mode we just need to pass the file name. We save the file in the temporary variable purchase_json.

We continue by parsing purchase_json using json.load(), creating a Python dictionary out of the file. Saving the results into purchase_data means we can interact with it. We print out one of the values of the JSON file by keying into the purchase_data object.

Instructions
Checkpoint 1 Passed
1.
Let’s read a JSON file! Start by importing the json module.


Stuck? Get a hint
Checkpoint 2 Passed
2.
Open up the file message.json, saving the file object to the variable message_json.

Open the file in read-mode, without passing any additional arguments to open().


Stuck? Get a hint
Checkpoint 3 Passed
3.
Pass the JSON file object as an argument to json.load() and save the resulting Python dictionary as message.

Checkpoint 4 Passed
4.
Print out message['text']."""

import json

# Open the JSON file in read-mode
with open('message.json') as message_json:
    # Load the JSON content into a Python dictionary
    message = json.load(message_json)

# Print the value associated with the "text" key
print(message['text'])



"""Part 12 Writing a json file

Writing a JSON File
Naturally we can use the json library to translate Python objects to JSON as well. This is especially useful in instances where you’re using a Python library to serve web pages, you would also be able to serve JSON. Let’s say we had a Python dictionary we wanted to save as a JSON file:

turn_to_json = {
  'eventId': 674189,
  'dateTime': '2015-02-12T09:23:17.511Z',
  'chocolate': 'Semi-sweet Dark',
  'isTomatoAFruit': True
}

We’d be able to create a JSON file with that information by doing the following:

import json

with open('output.json', 'w') as json_file:
  json.dump(turn_to_json, json_file)

We import the json module, open up a write-mode file under the variable json_file, and then use the json.dump() method to write to the file. json.dump() takes two arguments: first the data object, then the file object you want to save.

Instructions
Checkpoint 1 Passed
1.
In your workspace, we’ve put a dictionary called data_payload. We want to save this to a file called data.json.

Let’s start by importing the json library.

Checkpoint 2 Passed
2.
Open a new file object in the variable data_json. The filename should be 'data.json' and the file should be opened in write-mode.


Stuck? Get a hint
Checkpoint 3 Passed
3.
Call json.dump() with data_payload and data_json to convert our data to JSON and then save it to the file data.json.


Hint
Using json.dump() with the file object as a second argument writes the resulting JSON to the file:

payload = {'message': 'OK'}
with open('file.json', 'w') as file_json:
  json.dump(payload, file_json)

"""

import json

data_payload = [
  {'interesting message': 'What is JSON? A web application\'s little pile of secrets.',
   'follow up': 'But enough talk!'}
]# 

with open('data.json', 'w') as data_json:
  json.dump(data_payload, data_json)
