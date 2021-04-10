# 3/18/2021 Dictionaries
# creating dic_name = {} or dic_name = dic{}

my_car = {"brand": "Ford", "model": "Mustang", "year": 1964, "car": "my car is beautiful"}
print(my_car['car'])

my_car['price'] = 12500
print(my_car)

print("++++++++++++++++++++++++++ UPDATING +++++++")
# UPDATing the values in dictionaries
my_car['price'] = 15000
print(my_car)


print("++++++++++++++++++++++++++ REMOVING +++++++")
# removing the values from dictinaries
del my_car['car']
print(my_car)

print("++++++++++++++++++++++++++ EXE 6.1  +++++++")

amigo ={'first_name': ['Larisa', 'Olga'], 'last_name': 'Mos', 'age': '88', 'city': 'moscow'}
print(f"my fiend first name is {amigo['first_name']  [1]  }")
print(f"my fiend last name is {amigo['last_name']}")
print(f"my fiend age is {amigo['age']}")

print("++++++++++++++++++++++++++ EXE 6.2  +++++++")
fav_num = {'Zack': 7, 'Olga': 3, 'Mia': 1, 'Alex': 6, 'Bob': 13}
print(f"Zack fav number is {fav_num['Zack']}")
print(f"Olga fav number is {fav_num['Olga']}")
print(f"Mia fav number is {fav_num['Mia']}")
print(f"Alex fav number is {fav_num['Alex']}")
print(f"Bob fav number is {fav_num['Bob']}")

### ??? do we have accese to key's value? or we have to manualy write it

print("++++++++++++++++++++++++++ EXE 6.2  +++++++")

glossary = {'List': 'is used to store multiple items in a single variable.',
            'Float': 'represents real numbers and is written with a decimal point.',
            'String': ' is a sequence of characters, once defined they cannot be changed.',
            'Variable': 'is container for storing data values.',
            'Function': 'is a block of code which only runs when it is called.'
            }
print(f"\nList - {glossary['List']}")
print(f"\nFloat - {glossary['Float']}")
print(f"\nString - {glossary['String']}")
print(f"\nVariable - {glossary['Variable']}")
print(f"\nFunction - {glossary['Function']}")