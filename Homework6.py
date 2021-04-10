# homework 6 chapter

print("++++++++++++++++++++++6.6+++++++++++++++++")
'''Use the code in favorite_languages.py (page 104).
•	 Make a list of people who should take the favorite languages poll. Include 
some names that are already in the dictionary and some that are not.
•	 Loop through the list of people who should take the poll. If they have 
already taken the poll, print a message thanking them for responding.
If they have not yet taken the poll, print a message inviting them to take 
the poll.
'''

favorite_languages = {
    'jen': 'python',
    'sarah': 'c',
    'edward': 'ruby',
    'phil': 'python',
}
names = ['Alex', 'sarah', 'phil', 'Olga', 'Mia']

for name in names:
    if name in favorite_languages:
        print(f"Thank you for taking poll, {name}")
    else:
        print(f"Please take a poll, {name}")

print("++++++++++++++++++++++6.7+++++++++++++++++")
'''6-7. People: Start with the program you wrote for Exercise 6-1 (page 102).
Make two new dictionaries representing different people, and store all three 
dictionaries in a list called people. Loop through your list of people. As you 
loop through the list, print everything you know about each person.'''

Alex = {'first_name': 'Alex', 'last_name': 'Mor', 'age': 23, 'city': 'Lima'}
Bob = {'first_name': 'Bob', 'last_name': 'Smith', 'age': 56, 'city': 'New York'}
Anna = {'first_name': 'Anna', 'last_name': 'Kon', 'age': 43, 'city': 'Moscow'}
Jen = {'first_name': 'Jen', 'last_name': 'Love', 'age': 65, 'city': 'Barcelona'}

people = [Alex, Bob, Anna, Jen]

for a in people:
    print(f"My fiend's first name is {a['first_name']}")
    print(f"{a['first_name']}'s last name is {a['last_name']}")
    print(f"{a['first_name']}'s age is {a['age']}")
    print(f"{a['first_name']} lives in {a['city']}")
    print("")

print("++++++++++++++++++++++6.8 1 version+++++++++++++++++")
'''Make several dictionaries, where the name of each dictionary is the 
name of a pet. In each dictionary, include the kind of animal and the owner’s 
name. Store these dictionaries in a list called pets. Next, loop through your list 
and as you do print everything you know about each pet.'''

bobik = {'type': 'dog', 'name': 'bobik', 'color': 'grey', 'age': 5, 'owner': 'Bob'}
sharik = {'type': 'dog', 'name': 'sharik', 'color': 'white', 'age': 1, 'owner': 'Jen'}
molly = {'type': 'cat', 'name': 'molly', 'color': 'black', 'age': 15, 'owner': 'Alex'}
shrek = {'type': 'snake', 'name': 'shrek', 'color': 'yellow', 'age': 7, 'owner': 'Phil'}

pets = [bobik, sharik, molly, shrek]

for pet in pets:
    print(f"This is {pet['type']}, this pet's name is {pet['name']}. "
          f"\n{pet['name']} is {pet['age']} years old and pet's color is {pet['color']}."
          f"\n{pet['name']} belongs to {pet['owner']}")
    print("")



print("++++++++++++ EX 6.8 2 version +++++++++++++++++++++++")
cat = {'name': 'mysya', 'age': 5, 'city': 'brooklyn'}
dog = {'name': 'gody', 'age': 2, 'city': 'paris'}
bird = {'name': 'mark', 'age': 3, 'city': 'tokyo'}

pets = {
    'cat': {'name': 'mysya', 'age': 5, 'city': 'brooklyn'},
    'dog': {'name': 'gody', 'age': 2, 'city': 'paris'},
    'bird': {'name': 'mark', 'age': 3, 'city': 'tokyo'}
}

for pet, details in pets.items():
    print("")
    print(pet)
    for key, value in details.items():
        print(key)
        print(value)

   # print(f"This is {pet['type']}, this pet's name is {pet['name']}. "
    #      f"\n{pet['name']} is {pet['age']} years old and pet's color is {pet['color']}."
      #    f"\n{pet['name']} belongs to {pet['owner']}")
  #  print("")

print("++++++++++++++++++++++6.9+++++++++++++++++")
'''Make a dictionary called favorite_places. Think of three 
names to use as keys in the dictionary, and store one to three favorite places 
for each person. To make this exercise a bit more interesting, ask some friends 
to name a few of their favorite places. Loop through the dictionary, and print 
each person’s name and their favorite places.'''

#                                              ind1     ind2
favorite_places = {'Alex': 'Spain', 'Jen': ['Arizona', 'Florida'], 'Bob': 'Thailand', 'Anna': 'India'}

for name, details in favorite_places.items():
    if name == 'Jen':
        print(f"{name}'s favorite places are"
              f"\n {favorite_places['Jen'][0]} and {favorite_places['Jen'][1]}")
    else:
        print(f"{name}'s favorite place is {details} ")



print("++++++++++++++++++++++6.10 +++++++++++++++++")
'''Modify your program from Exercise 6-2 (page 102) so 
each person can have more than one favorite number. Then print each person’s 
name along with their favorite numbers.'''

fav_num = {'Zack': [7, 3, 4, 5], 'Olga': [6, 7, 1, 3], 'Mia': [1, 5, 6, 8], 'Alex': [6, 8, 9, 6], 'Bob': [13, 12, 11, 14]}
for key, value in fav_num.items():
    print('________________________________')
    print(f"{key}'s favorite numbers: {fav_num[key][0]}, {fav_num[key][1]}, {fav_num[key][2]}, {fav_num[key][3]}")

print("++++++++++++++++++++++6.11 ???????????? +++++++++++++++++")
''' Make a dictionary called cities. Use the names of three cities as 
keys in your dictionary. Create a dictionary of information about each city and 
include the country that the city is in, its approximate population, and one fact 
about that city. The keys for each city’s dictionary should be something like 
country, population, and fact. Print the name of each city and all of the 
information you have stored about it.'''

cities = {
    'moscow': {'country': 'Russia', 'population': '15 millions', 'fact': 'beautiful city'},
    'ny': {'country': 'USA', 'population': '18 millions', 'fact': 'capital of the world'},
    'Barcelona': {'country': 'Spain', 'population': '8 millions', 'fact': 'best vacation'}

}

for name, details in cities.items(): # parent for loop
    print(f"City name is {name.title()}")
    #for key, value in details.items(): # child for loop
   if name == 'moscow':
       print(f"")

   moscow = cities['moscow']
    ny = cities['ny']
    bar = cities['Barcelona']
    print(moscow)



       # print(f"details key is: {key}")
    #    print(f"the population is {} ")
      #  print(f"details value is: {value}")

'''
for key, value in cities.items():
    print(key)
    print(f"the population is {cities['moscow']['population']} ")
    print(f"The city is located in country")
    print(f"The fact about city: fact")
    '''



print("++++++++++++++++flag ++++++++++++++++")
# examples of flags
count = 0
for letter in 'hello guys':
    if letter == 'l':
        count += 1
print(f"number of l's is : {count}")