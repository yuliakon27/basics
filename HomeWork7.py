print("++++++++++++++++++++++++++++7.1++++++++++++++++")
''' Write a program that asks the user what kind of rental car they 
would like. Print a message about that car, such as 
“Let me see if I can find you a Subaru.'''

number = input("What kind of rental car they would like?: ")
print(f"Let me see if i can find you a {number.title()}")

print("++++++++++++++++++++++++++++7.2++++++++++++++++")
'''Write a program that asks the user how many people 
are in their dinner group. If the answer is more than eight, 
print a message saying they’ll have to wait for a table. 
Otherwise, report that their table is ready'''

table = int(input("How many people are in your dinner group?: "))
if table > 8:
    print(f"You will have to wait for a table")
else:
    print(f"Your table is ready")

print("++++++++++++++++++++++++++++7.3 ++++++++++++++++")
'''Ask the user for a number, and then report whether the 
number is a multiple of 10 or not.'''

number = int(input("Please enter number: "))
if number % 10 == 0:
    print(f"number is a multiple of 10")
else:
    print(f"number is not a multiple of 10")

print("++++++++++++++++++++++++++++7.4++++++++++++++++")
''' Write a loop that prompts the user to enter a series of 
pizza toppings until they enter a 'quit' value. As they enter each topping, 
print a message saying you’ll add that topping to their pizza.'''


topping = None
while topping != 'quit' or topping != 'q':
    topping = input("Enter your topping:  ")
    if topping == 'quit' or topping == 'q':
        break
    else:
        print(f"You’ll add {topping} topping to the pizza")

print("++++++++++++++++++++++++++++7.5++++++++++++++++")
''' A movie theater charges different ticket prices depending on 
a person’s age. If a person is under the age of 3, the ticket is free; 
if they are between 3 and 12, the ticket is $10; 
and if they are over age 12, the ticket is $15. 
Write a loop in which you ask users their age, and then tell them the cost 
of their movie ticket'''


while True:  # incorrect whe i type 'q' it gives error
    age = int(input('Enter your age: '))
    if age == 'quit':
        break
    elif age < 3:
        print(f"The ticket is free for you")
    elif 3 <= age < 12:
        print(f"The ticket is $10 for you")
    else:
        print(f"The ticket is $15 for you")


print("++++++++++++++++++++++++++++7.6++++++++++++++++")
'''Write different versions of either Exercise 7-4 or Exercise 7-5 
that do each of the following at least once:
•	 Use a conditional test in the while statement to stop the loop.
•	 Use an active variable to control how long the loop runs.
•	 Use a break statement to exit the loop when the user enters a 'quit' value'''

topping = None
while topping != 'quit' or topping != 'q':
    topping = input("Enter your topping:  ")
    if topping == 'quit' or topping == 'q':
        break
    else:
        print(f"You’ll add {topping} topping to the pizza")


print("++++++++++++++++++++++++++++7.1++++++++++++++++")

