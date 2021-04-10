# 3/20/2021 Nesting - list in a dictionary

countries = ['usa', 'russia', 'spain']
cities = ['ny', 'moscow', 'barcelona']
companies = ['level up', 'abc comp', 'ola com']
customers = [companies, cities, countries]

# multidimensional array
print(customers)
print(customers[0])  # access to first list
print(customers[0][0])  # access to first list, first index

print(f"printing barcelona: {customers[1][2]}")

# multidimensional numbers
multi_dim_nums = [
    [3, 9, 0],
    [2, 7, 1],
    [0, 1, 0]
]

print("+++++++ Nesting looping +++++++++++++++++++++++++++++++")
countries = ['usa', 'russia', 'spain']
cities = ['ny', 'moscow', 'barcelona']
companies = ['level up', 'abc comp', 'ola com']
customers = [companies, cities, countries]

for column in customers:
    print(column)
    for value in column:
        print(value.upper())

print("++++++++++++++++++++++++++++++++++++")
for city in customers[1]:
    print(city)

raws = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
columns = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
tests = [raws, columns]
"""
H/W to print multiplication table
for column in customers(1, 11):
    print(column)
    for value in column(1, 11):
        print(value.upper())
"""

print("+++++++++ list of dictionaries  ")
user_0 = {'name': 'john', 'age': 25, 'city': 'brooklyn'}
user_1 = {'name': 'jane', 'age': 20, 'city': 'paris'}
user_2 = {'name': 'mark', 'age': 35, 'city': 'tokyo'}

users = [user_1, user_2, user_0]

print("++++++++++++looping ")
print(users[0])  # access
# has to have the same keys !!!!
#    dic ind  -  kyes
print(users[0]['name'])
print(users[0]['age'])
print(users[0]['city'])
print(users[1]['city'])
print(")))))))))))))))))))))))))))))))))))))")
for user in users:
    print(user['name'], end=' || ')
    print(user['age'], end=' || ')
    print(user['city'])

print("++++++++++++ lists in dictionary +++++++++")

countries = ['usa', 'rissia', 'spain']
cities = ['ny', 'moscow', 'barcelona']
companies = ['level up', 'abc comp', 'ola com']

customers = {"companies": ['level up', 'abc comp', 'ola com'],
             "cities": ['ny', 'moscow', 'barcelona'],
             "countries": ['usa', 'russia', 'spain']
             }
print(customers['cities'])
print(customers['cities'][1])  # second elements from cities

print("++++++++++++ dictionary in a dictionary +++++++++")
user_0 = {'name': 'john', 'age': 25, 'city': 'brooklyn'}
user_1 = {'name': 'jane', 'age': 20, 'city': 'paris'}
user_2 = {'name': 'mark', 'age': 35, 'city': 'tokyo'}

users = {
    'user_0': {'name': 'john', 'age': 25, 'city': 'brooklyn'},
    'user_1': {'name': 'jane', 'age': 20, 'city': 'paris'},
    'user_2': {'name': 'mark', 'age': 35, 'city': 'tokyo'}
}
# dic
print(users)
# dic in dic
print(users['user_0'])
# dic in dic kye
print(users['user_0']['name'])

print('++++++++++++++++++++++++++++++++++++++===')

#    key        value
for username, details in users.items(): # parent for loop
    print(username)
   # print(details["name"])
    for key, value in details.items(): # child for loop
        print(f"details key is: {key}")
        print(f"details value is: {value}")

print("++++++++++++ EX 6.8+++++++++++++++++++++++")
cat = {'name': 'mysya', 'age': 5, 'city': 'brooklyn'}
dog = {'name': 'gody', 'age': 2, 'city': 'paris'}
bird = {'name': 'mark', 'age': 3, 'city': 'tokyo'}

pets = {
    'cat': {'name': 'mysya', 'age': 5, 'city': 'brooklyn'},
    'dog': {'name': 'gody', 'age': 2, 'city': 'paris'},
    'bird': {'name': 'mark', 'age': 3, 'city': 'tokyo'}
}


