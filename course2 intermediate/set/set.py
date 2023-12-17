"""SETS"""


genre_results = ['rap', 'classical', 'rock', 'rock', 'country', 'rap', 'rock', 'latin', 'country', 'k-pop', 'pop', 'rap', 'rock', 'k-pop',  'rap', 'k-pop', 'rock', 'rap', 'latin', 'pop', 'pop', 'classical', 'pop', 'country', 'rock', 'classical', 'country', 'pop', 'rap', 'latin']

# Write your code below!
survey_genres = set(genre_results)

survey_abbreviated = {letters[0:3] for letters in survey_genres}
print(survey_abbreviated)



"""FROZENSETS"""
top_genres = ['rap', 'rock', 'pop']

# Write your code below!
frozen_top_genres  = frozenset(['rap', 'rock', 'pop'])

print(frozen_top_genres)


"""Adding to a Set"""
song_data = {'Retro Words': ['pop', 'warm', 'happy', 'electric']}

user_tag_1 = 'warm'
user_tag_2 = 'exciting'
user_tag_3 = 'electric'

# Write your code below!
tag_set = set(song_data['Retro Words'])

tag_set.add(user_tag_1)
tag_set.add(user_tag_2)
tag_set.add(user_tag_3)

song_data = {'Retro Words': tag_set}
print(song_data)



"""REMOVING FROM A SET pt 5"""

song_data_users = {'Retro Words': ['pop', 'onion', 'warm', 'helloworld', 'happy', 'spam', 'electric']}

print(song_data_users)
# Write your code below!

tag_set = set(song_data_users["Retro Words"])

print(tag_set)

tag_set.remove("onion")
tag_set.remove("helloworld")
tag_set.remove("spam")

song_data_users = {'Retro Words': tag_set}
print(song_data_users)


"""PART 6 remove tags"""
allowed_tags = ['pop', 'hip-hop', 'rap', 'dance', 'electronic', 'latin', 'indie', 'alternative rock', 'classical', 'k-pop', 'country', 'rock', 'metal', 'jazz', 'exciting', 'sad', 'happy', 'upbeat', 'party', 'synth', 'rhythmic', 'emotional', 'relationship', 'warm', 'guitar', 'fiddle', 'romance', 'chill', 'swing']

song_data_users = {'Retro Words': ['pop', 'explosion', 'hammer', 'bomb', 'warm', 'due', 'writer', 'happy', 'horrible', 'electric', 'mushroom', 'shed']}

# Write your code below!
tag_set = set(song_data_users["Retro Words"])

bad_tags = []
for tags in tag_set:
  if tags not in allowed_tags:
    bad_tags.append(tags)
    print(bad_tags)

for bad in bad_tags:
  tag_set.remove(bad)
  print(tag_set)

song_data_users['Retro Words'] = tag_set
print(song_data_users)


"""PART 8 SET UNION"""
song_data = {'Retro Words': ['pop', 'warm', 'happy', 'electronic'],
             'Wait For Limit': ['rap', 'upbeat', 'romance'],
             'Stomping Cue': ['country', 'fiddle', 'party'],
             'Lowkey Space': ['electronic', 'dance', 'synth']}

user_tag_data = {'Lowkey Space': ['party', 'synth', 'fast', 'upbeat'],
                 'Retro Words': ['happy', 'electronic', 'fun', 'exciting'],
                 'Wait For Limit': ['romance', 'chill', 'rap', 'rhythmic'], 
                 'Stomping Cue': ['country', 'swing', 'party', 'instrumental']}

# Write your code below!
new_song_data = {}

for key, val in song_data.items():
    song_tag_set = set(val)
    user_tag_set = set(user_tag_data[key])
    new_song_data[key] = song_tag_set | user_tag_set

print(new_song_data)
# """{'Retro Words': {'electronic', 'warm', 'exciting', 'happy', 'fun', 'pop'}, 'Wait For Limit': {'chill', 'rap', 'upbeat', 'romance', 'rhythmic'}, 'Stomping Cue': {'country', 'instrumental', 'party', 'fiddle', 'swing'}, 'Lowkey Space': {'synth', 'dance', 'party', 'upbeat', 'electronic', 'fast'}}


"""Part 9 set intersection"""
song_data = {'Retro Words': ['pop', 'warm', 'happy', 'electronic', 'synth'],
             'Wait For Limit': ['rap', 'upbeat', 'romance'],
             'Stomping Cue': ['country', 'fiddle', 'party'],
             'Lowkey Space': ['electronic', 'dance', 'synth', 'upbeat'],
             'Back To Art': ['pop', 'sad', 'emotional', 'relationship'],
             'Blinding Era': ['rap', 'intense', 'moving', 'fast'],
             'Down To Green Hills': ['country', 'relaxing', 'vocal', 'emotional'],
             'Double Lights': ['electronic', 'chill', 'relaxing', 'piano', 'synth']}

user_recent_songs = {'Retro Words': ['pop', 'warm', 'happy', 'electronic', 'synth'],
                     'Lowkey Space': ['electronic', 'dance', 'synth', 'upbeat']}

# Write your code below!
tags_int = set(user_recent_songs["Retro Words"]) & set(user_recent_songs["Lowkey Space"])

recommended_songs = {}
for key, val in song_data.items():
    for tag in val:
        if tag in tags_int:
            if key not in user_recent_songs:
                recommended_songs[key] = val

print(recommended_songs)

""" PART 10 SET DIFFERENCE


Set Difference
Similar to how we can find elements in common between sets, we can also find unique elements in one set. To do so, the set or frozenset use the .difference() method or the - operator. This returns a set or frozenset, which contains only the elements from the first set which are not found in the second set. Similar to the other operations, the type of the first operand (a set or frozenset on the left side of the operator or method) determines if a set or frozenset is returned when finding the difference.

Take a look at the Venn diagram representing a difference operation that captures elements that are unique to set A:

Python Set Difference

Here is what finding a set difference looks like in Python:

# Given a set and frozenset of song tags for two python related hits
prepare_to_py = {'rock', 'heavy metal', 'electric guitar', 'synth'}

py_and_dry = frozenset({'classic', 'rock', 'electric guitar', 'rock and roll'})

# Find the elements which are only in prepare_to_py
only_in_prepare_to_py = prepare_to_py.difference(py_and_dry)
print(only_in_prepare_to_py)

Would Output:

{'heavy metal', 'synth'}

Alternativly, we can use the - operator:

# Find the elements which are only in py_and_dry
only_in_py_and_dry = py_and_dry - prepare_to_py
print(only_in_py_and_dry)

Would output:

frozenset({'rock and roll', 'classic'})

This operation also supports an updating version of the method. You can use .difference_update() to update the original set with the result instead of returning a new set or frozenset object.

Let’s see how we can apply this operation to our music application!"""







song_data = {'Retro Words': ['pop', 'warm', 'happy', 'electronic', 'synth'],
             'Wait For Limit': ['rap', 'upbeat', 'romance', 'relationship'],
             'Stomping Cue': ['country', 'fiddle', 'party'],
             'Lowkey Space': ['electronic', 'dance', 'synth', 'upbeat'],
             'Back To Art': ['pop', 'sad', 'emotional', 'relationship'],
             'Blinding Era': ['rap', 'intense', 'moving', 'fast'],
             'Down To Green Hills': ['country', 'relaxing', 'vocal', 'emotional'],
             'Double Lights': ['electronic', 'chill', 'relaxing', 'piano', 'synth']}

user_liked_song = {'Back To Art': ['pop', 'sad', 'emotional', 'relationship']}
user_disliked_song = {'Retro Words': ['pop', 'warm', 'happy', 'electronic', 'synth']}

# Write your code below!

tag_diff = set(user_liked_song["Back To Art"]) - set(user_disliked_song["Retro Words"])

print(tag_diff)

recommended_songs = {}

for key, val in song_data.items():
    for tag in val:
        if tag in tag_diff:
            if key not in user_liked_song and key not in user_disliked_song:
                recommended_songs[key] = val

print(recommended_songs)


"""Symmetric Difference part 11"""
user_song_history = {'Retro Words': ['pop', 'warm', 'happy', 'electronic', 'synth'],
                     'Stomping Cue': ['country', 'fiddle', 'party'],
                     'Back To Art': ['pop', 'sad', 'emotional', 'relationship'],
                     'Double Lights': ['electronic', 'chill', 'relaxing', 'piano', 'synth']}

friend_song_history = {'Lowkey Space': ['electronic', 'dance', 'synth', 'upbeat'],
                     'Blinding Era': ['rap', 'intense', 'moving', 'fast'],
                     'Wait For Limit': ['rap', 'upbeat', 'romance', 'relationship'],
                     'Double Lights': ['electronic', 'chill', 'relaxing', 'piano', 'synth']}

# Write your code below!
user_tags = set()
for key, val in user_song_history.items():
    user_tags.update(set(val))

# Checkpoint 2
friend_tags = set()
for key, val in friend_song_history.items():
    friend_tags.update(set(val))

# Checkpoint 3
unique_tags = user_tags ^ friend_tags
print(unique_tags)




"""REVIEW ...."""

music_tags = {'pop', 'warm', 'happy', 'electronic', 'synth', 'dance', 'upbeat'}

# Checkpoint 1
my_tags = frozenset(['pop', 'electronic', 'relaxing', 'slow', 'synth'])

# Checkpoint 2
frozen_tag_union = my_tags | music_tags
print(frozen_tag_union)

# Checkpoint 3
regular_tag_intersect = music_tags & my_tags
print(regular_tag_intersect)

# Checkpoint 4
frozen_tag_difference = my_tags - music_tags
print(frozen_tag_difference)

# Checkpoint 5
regular_tag_sd = music_tags ^ my_tags
print(regular_tag_sd)