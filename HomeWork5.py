# homework 5.6
age = int(input("Enter your age: "))
if age < 2:
    print(f"You are a baby!")
elif 2 <= age < 4:
    print("You are a toddler!")
elif 4 <= age < 13:
    print("You are a kid!")
elif 13 <= age < 20:
    print("You are a teenager!")
elif 20 <= age < 65:
    print("You are an adult!")
else:
    print("You are an elder!")
print("+++++++++++++++++++++++++++++")
#5.7
fruits = ['mango', 'apple', 'pineapple', 'orange', 'grapes', 'melon', 'watermelon']
if 'mango' in fruits:
    print(f"You are really like mango!")
else:
    print(f"Sorry, we do not it mango")
print("++++++++++++++++++++++")
fruit = 'apple'
if fruit in fruits:
    print(f"You are really like {fruit}!")
else:
    print(f"Sorry, we do not eat {fruit}!")

print('+++++++++++++++++++++++++++++++')
fruit2 = 'banana'
if fruit2 in fruits:
    print(f"You are really like {fruit2}!")
else:
    print(f"Sorry, we do not eat {fruit2}!")

print("+++++++++++++++++++++++++++++++++++")

for letter in "hello":
    print(letter)

print("+++++++++++++++++5.8 +++++++++++++++++++")
#5.8

users = ['admin', 'Eric', 'John', 'Mike', 'Anna']
for user in users:
    if user == 'admin':
        print(f"Hello {user}, would you like to see a report?")
    else:
        print(f"Hello {user}, thank you for logging in again!")

print("+++++++++++++EXE 5.9 ++++++++++++++++++++++++++++")
#5.9


users = []
if users:
    for user in users:
        if user == 'admin':
            print(f"Hello {user}, would you like to see a report?")
else:
    print(f"We need some users")

print("++++++++++++++EXE 5.10 +++++++++++++++++++++++++++")
#5.10
current_users = ['Bob', 'Nik', 'Olga', 'Alex', 'Maria']
new_users = ['Maria', 'Yulia', 'Bob', 'Steve', 'Zack', 'Nik']

for new_user in new_users:
    if new_user in current_users:
        print(f"\nThe name {new_user} is not available! \nPlease check your spelling.\n")
    else:
        print(f"Welcome to the club, {new_user}!")

# ?? Make sure your comparison is case insensitive. If 'John' has been used,
#'JOHN' should not be accepted.


print("+++++++++++++++++++++++++++++ EXE 5.11++++++++")
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]

for number in numbers:
    if number == 1:
        print(f"The correct writing is {number}st")
    elif number == 2:
        print(f"The correct writing is {number}nd")
    elif number == 3:
        print(f"The correct writing is {number}rd")
    else:
        print(f"The correct writing is {number}th")

print("+++++++++++++++++++++++EXE 5.12 +++++++++++++++++++")


new_users = ['Maria', 'Yulia', 'Bob', 'Steve', 'Zack', 'Nik']

for user in new_users:
    if user == 'steve':
        print('yes')
        break 
    else:
        print('no')
        break







