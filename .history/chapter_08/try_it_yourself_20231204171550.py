
# 8-1. Message: Write a function called display_message() that prints one sentence
# telling everyone what you are learning about in this chapter. Call the function,
# and make sure the message displays correctly.

# def display_message():
#     print("I love this book I'm learning about functions!")

# display_message()

# 8-2. Favorite Book: Write a function called favorite_book() that accepts one
# parameter, title. The function should print a message, such as One of my
# favorite books is Alice in Wonderland. Call the function, making sure to include
# a book title as an argument in the function call.

# def favorite_book(book_title):
#     print(f"One of my favorite books is {book_title.title()}")

# favorite_book('the never ending story')

# 8-3. T-Shirt: Write a function called make_shirt() that accepts a size and the
# text of a message that should be printed on the shirt. The function should print a
# sentence summarizing the size of the shirt and the message printed on it. Call the
# function once using positional arguments to make a shirt. Call the function a
# second time using keyword arguments.

# def make_shirt(shirt_size, shirt_text):
#     print(f'''Your shirt order is ready. Let's make sure we got it right...
#           size {shirt_size} message will read {shirt_text}''')


# make_shirt('Small', 'Yolo')
# make_shirt(shirt_size='Large', shirt_text='Paris')

# 8-4. Large Shirts: Modify the make_shirt() function so that shirts are large by
# default with a message that reads I love Python. Make a large shirt and a medium
# shirt with the default message, and a shirt of any size with a different message.

# def make_shirt(shirt_size='Large', shirt_text="I Love Python"):
#     print(f'''Your shirt order is ready. Let's make sure we got it right...
#           size {shirt_size} message will read {shirt_text}''')

# make_shirt()
# # Make a medium shirt with the default message
# make_shirt(shirt_size='Medium')

# # Make a shirt of any size with a different message
# make_shirt(shirt_text='Python is great', shirt_size='Small')

# 8-5. Cities: Write a function called describe_city() that accepts the name of a
# city and its country. The function should print a simple sentence, such as
# Reykjavik is in Iceland. Give the country parameter a default value. Call your
# function for three different cities, at least one of which is not in the default
# country.

# def describe_city(city_name, country='France',):
#     print(f"{city_name}, which is in {country} is a chill place to visit")

# describe_city("Paris")
# describe_city("Florance", country="Italy")
# describe_city("Varcie")

# 8-6. City Names: Write a function called city_country() that takes in the name
# of a city and its country. The function should return a string formatted like
# this: "Santiago, Chile". Call your function with at least three city-country pairs,
# and print the values that are returned.

# def city_country(city_name, country):
#     print(f''' "{city_name}, {country}" ''')

# city_country('Maputo', 'Mozambique')
# city_country('Austin', 'USA')
# city_country('Lagos', 'Nigeria')


# 8-7. Album: Write a function called make_album() that builds a dictionary
# describing a music album. The function should take in an artist name and an
# album title, and it should return a dictionary containing these two pieces of
# information. Use the function to make three dictionaries representing different
# albums. Print each return value to show that the dictionaries are storing the
# album information correctly. Use None to add an optional parameter to make_album()
# that allows you to store the number of songs on an album. If the calling line
# includes a value for the number of songs, add that value to the album's dictionary.
# Make at least one new function call that includes the number of songs on an album.

# def make_album(artist_name, album_title, number_of_songs=None):
#     album = {"artist": artist_name, "album": album_title}
#     if number_of_songs:
#         album["song_amount"] = number_of_songs
#     return album


# album_1 = make_album('Joan', 'Folk Glory', '7')
# album_2 = make_album('Joan', 'Folk Story 1')
# album_3 = make_album('Joan', 'Folk Forever')
# print(album_1, album_2, album_3)


# 8-8. User Albums: Start with your program from Exercise 8-7. Write a while loop
# that allows users to enter an album's artist and title. Once you have that
# information, call make_album() with the user's input and print the dictionary
# that's created. Be sure to include a quit value in the while loop.

# 8-9. Messages: Make a list containing a series of short text messages. Pass the
# list to a function called show_messages(), which prints each text message.

# 8-10. Sending Messages: Start with a copy of your program from Exercise 8-9.
# Write a function called send_messages() that prints each text message and moves
# each message to a new list called sent_messages as it's printed. After calling the
# function, print both of your lists to make sure the messages were moved correctly.

# 8-11. Archived Messages: Start with your work from Exercise 8-10. Call the
# function send_messages() with a copy of the list of messages. After calling the
# function, print both of your lists to show that the original list has retained its
# messages.

# 8-12. Sandwiches: Write a function called make_sandwich() that accepts a list of
# items a person wants on a sandwich. The function should have one parameter that
# collects as many items as the function call provides, and it should print a summary
# of the sandwich that’s being ordered. Call the function three times, using a
# different number of arguments each time.

# 8-13. User Profile: Start with a copy of user_profile.py from page 148. Build a
# profile of yourself by calling build_profile(), using your first and last names
# and three other key-value pairs that describe you.

# 8-14. Cars: Write a function that stores information about a car in a dictionary.
# The function should always receive a manufacturer and a model name. It should then
# accept an arbitrary
