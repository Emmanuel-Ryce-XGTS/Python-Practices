"""Formatting Methods"""

poem_title = "spring storm"
poem_author = "William Carlos Williams"

poem_title_fixed =  poem_title.title()

print(poem_title_fixed)
print(poem_title)

poem_author_fixed =  poem_author.upper()
print(poem_author)
print(poem_author_fixed)


"""part 2 Split Splitting Strings I"""

line_one = "The sky has given over"
print(line_one)
line_one_words = line_one.split()

print(line_one_words)

"""part 3 Split Splitting Strings II """

authors = "Audre Lorde,Gabriela Mistral,Jean Toomer,An Qi,Walt Whitman,Shel Silverstein,Carmen Boullosa,Kamala Suraiyya,Langston Hughes,Adrienne Rich,Nikki Giovanni"

author_names = authors.split(',')
print(author_names)

author_last_names = [name.split()[-1] for name in author_names]

print(author_last_names)


"""Splitting Strings III
We can also split strings using escape sequences. Escape sequences are used to 
indicate that we want to split by something in a string that is not necessarily
a character. The two escape sequences we will cover here are

"""
spring_storm_text = \
"""The sky has given over 
its bitterness. 
Out of the dark change 
all day long 
rain falls and falls 
as if it would never end. 
Still the snow keeps 
its hold on the ground. 
But water, water 
from a thousand runnels! 
It collects swiftly, 
dappled with black 
cuts a way for itself 
through green ice in the gutters. 
Drop after drop it falls 
from the withered grass-stems 
of the overhanging embankment.


\n Newline
\t Horizontal Tab
"""

spring_storm_lines = spring_storm_text.split('\n') 

print(spring_storm_lines)



"""Joining Strings
Now that you’ve learned to break strings apart using .split(), 
let’s learn to put them back together using .join(). .join() is essentially the opposite of .split(),
it joins a list of strings together with a given delimiter. The syntax of .join() is:

"""


reapers_line_one_words = ["Black", "reapers", "with", "the", "sound", "of", "steel", "on", "stones"]

print(reapers_line_one_words)

reapers_line_one = ' '.join(reapers_line_one_words)
print(' '.join(reapers_line_one_words))


my_munequita = ['My', 'Spanish', 'Harlem', 'Mona', 'Lisa']

print(my_munequita)

print(' '.join(my_munequita))
# => 'My Spanish Harlem Mona Lisa'


"""PArt 7 Joining Strings II
In the last exercise, we joined together a list of words using a space as the delimiter
to create a sentence. In fact, you can use any string as a delimiter to join together a 
list of strings. For example, if we have the list
"""

winter_trees_lines = ['All the complicated details', 'of the attiring and', 'the disattiring are completed!', 'A liquid moon', 'moves gently among', 'the long branches.', 'Thus having prepared their buds', 'against a sure winter', 'the wise trees', 'stand sleeping in the cold.']

winter_trees_full = '\n'.join(winter_trees_lines)

print(winter_trees_full)


"""Part8 Strip
Instructions
Checkpoint 1 Passed
1.
They sent over another list containing all the lines to the Audre Lorde poem, Love, Maybe. They want you to join together all of the lines into a single string that can be used to display the poem again, but this time, you’ve noticed that the list contains a ton of unnecessary whitespace that doesn’t appear in the actual poem.

First, use .strip() on each line in the list to remove the unnecessary whitespace and save it as a new list love_maybe_lines_stripped.


Stuck? Get a hint
Checkpoint 2 Enabled
2.
.join() the lines in love_maybe_lines_stripped together into one large multi-line string, love_maybe_full, that can be printed to display the poem.

Each line of the poem should show up on its own line.


Stuck? Get a hint
Checkpoint 3 Step instruction is unavailable until previous steps are completed
3.
Print love_maybe_full.

"""


love_maybe_lines = ['Always    ', '     in the middle of our bloodiest battles  ', 'you lay down your arms', '           like flowering mines    ','\n' ,'   to conquer me home.    ']

love_maybe_lines_stripped = [line.strip() for line in love_maybe_lines]

# Step 2: Join the stripped lines into one multi-line string
love_maybe_full = '\n'.join(love_maybe_lines_stripped)

# Step 3: Print the poem
print(love_maybe_full)



"""Parte 9 replace"""
toomer_bio = \
"""
Nathan Pinchback Tomer, who adopted the name Jean Tomer early in his literary career, was born in Washington, D.C. in 1894. Jean is the son of Nathan Tomer was a mixed-race freedman, born into slavery in 1839 in Chatham County, North Carolina. Jean Tomer is most well known for his first book Cane, which vividly portrays the life of African-Americans in southern farmlands.
"""

toomer_bio_fixed = toomer_bio.replace("Tomer", "Toomer")

print(toomer_bio_fixed)

"""parte 10 Find"""
god_wills_it_line_one = "The very earth will disown you"


disown_placement = god_wills_it_line_one.find("disown")

"""PArte 11 Format

def favorite_song_statement(song, artist):
  return "My favorite song is {} by {}.".format(song, artist)

print(favorite_song_statement("Smooth", "Santana"))
# => "My favorite song is Smooth by Santana."
"""
def poem_title_card(title, poet):
    return 'The poem "{}" is written by {}.'.format(title, poet)

# Example usage
title = "I Hear America Singing"
poet = "Walt Whitman"
result = poem_title_card(title, poet)
print(result)


""".format() II part 12
.format() can be made even more legible for other people reading your code by including keywords.
Previously, with .format(), you had to make sure that your variables appeared as arguments in the 
same order that you wanted them to appear in the string, which added unnecessary complications when writing code.
"""

def poem_description(publishing_date, author, title, original_work):
    poem_desc = "The poem {title} by {author} was originally published in {original_work} in {publishing_date}.".format(
        title=title, author=author, original_work=original_work, publishing_date=publishing_date)
    return poem_desc
author = "Shel Silverstein"
title = "My Beard"
original_work = "Where the Sidewalk Ends"
publishing_date = "1974"

my_beard_description = poem_description(publishing_date, author, title, original_work)

print(my_beard_description)


"""Part 13"""