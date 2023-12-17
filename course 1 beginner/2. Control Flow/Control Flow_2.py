"""Magic 8-Ball
The Magic 8-Ball is a popular toy developed in the 1950s for fortune-telling or advice seeking.

Write a magic8.py Python program that can answer any “Yes” or “No” question with a different fortune each time it executes.

Magic 8-Ball, should I do this project?

We’ll be using the following 9 possible answers for our Magic 8-Ball:

Yes - definitely
It is decidedly so
Without a doubt
Reply hazy, try again
Ask again later
Better not tell you now
My sources say no
Outlook not so good
Very doubtful"""

# So far, the Magic 8-Ball provides 9 possible fortunes. 
# Try to add a few more possible answers to the program.


# What if the asker does not provide a name, such that the value of name is an empty string? 
# If the name string is empty, the output of the program looks like the following:


#What if the question string is empty? If the user does not provide any question, then the 
# Magic 8-Ball cannot provide a fortune, otherwise, the fabric of reality is at risk!

import random

name = "Emmanuel"
#question = "Yes" or "No"
question = ""

#print(name + " asks: " + question)

Answer = ""
random_number = random.randint(1, 13)

if question == "":
  print("No question was made")
  raise Exception("Some condition is not met, terminating the operation.")

else: 
  print("Asks: Is this true? " + question)

if name:
  print(name + " asks: Will I Win? " + question)
  print("The magic ball number is: " + str (random_number))
else: 
  print("Asks: Is this true? " + question)
  print("The magic ball number is: " + str (random_number))

if random_number == 1:
  Answer = "Yes - definitely"
elif random_number == 2:
  Answer = "It is decidedly so"
elif random_number == 3:
  Answer = "Without a doubt"
elif random_number == 4:
  Answer = "Reply hazy, try again"
elif random_number == 5:
  Answer = "Ask again later"
elif random_number == 6:
  Answer = "Better not tell you now"
elif random_number == 7:
  Answer = "My sources say no"
elif random_number == 8:
  Answer = "Outlook not so good"
elif random_number == 9:
  Answer = "Very doubtful"
elif random_number == 10:
  Answer = "Doubtfull"
elif random_number == 11:
  Answer = "Very bad"
else:
  Answer = "Error"
  
  
print("Magic 8-Ball's answer: " + Answer)


