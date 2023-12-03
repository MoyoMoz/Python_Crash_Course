# Try It Yourself
# 7-1. Rental Car: Write a program that asks the user what kind of rental car they would like.
# Let the user enter the kind of car they want, and then print a message like, "Let me see if
#  I can find you a Subaru."

# car_type = input("Type the model of car would you like:")
# print(f"I'm searcing for a {car_type} now")

# 7-2. Restaurant Seating: Write a program that asks the user how many people are in their dinner group.
# If the answer is more than eight, print a message telling them they'll have to wait for a table.
# Otherwise, report that their table is ready.

# number_of_people = input("\n Type the number of people at your table:  ")
# number_of_people = int(number_of_people)

# if number_of_people > 8:
#     print("\n \t your wait will be about 40min")
# else:
#     print("\n \t We have an open table please follow me")

# 7-3. Multiples of Ten: Ask the user for a number, and then report whether the number is a multiple of ten or not.

# number = input("\n Please type any number:  ")
# number = int(number)

# if number % 10 == 0:
#     print(f"\t \n your number is a multiple of 10")
# else:
#     print(f"\t \n Your number is not a multiple of 10")


# 7-4. Pizza Toppings: Write a loop that prompts the user to enter a series of pizza toppings until they enter a 'quit' value.
# As they enter each topping, print a message saying you’ll add that topping to their pizza.

# prompt = "Type your topping \n (when you are finished type quit) :  "

# while True:
#     topping = input(prompt)
#     if topping != quit:
#         print(f"I've added {topping} to you pizza")
#     else:
#         break

# 7-5. Movie Tickets: A movie theater charges different ticket prices depending on a person's age.
# If a person is under the age of 3, the ticket is free; if they are between 3 and 12, the ticket is $10;
# and if they are over age 12, the ticket is $15. Write a loop in which you ask users their age,
# and then tell them the cost of their movie ticket.

ticket_price = ""
age = input("what is your age? ")
age = int(age)
if age < 3:
    ticket_price = "your ticket is free"
elif age < 13:
    ticket_price = "your ticket is $10"
else:
    ticket_price = "your ticket is $15"
print(ticket_price)


# 7-6. Three Exits: Write different versions of either Exercise 7-4 or 7-5 that do each of the following at least once:
# - Use a conditional test in the while statement to stop the loop.
# - Use an active variable to control how long the loop runs.
# - Use a break statement to exit the loop when the user enters a 'quit' value.

# 7-7. Infinity: Write a loop that never ends, and run it.
# (To end the loop, press CTRL-C or close the window displaying the output.)
