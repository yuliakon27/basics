# lists (array)

odds = [1, 3, 5, 7, 9]
friends = ['jakson', 'said', 'lenur', 'tyson']

first_friend = friends[0]

# creating the empty list
# nums = list()  OR  nums = []
events = []

# accessing
print(f"friends[0]: {friends[0].upper()}")
print(f"friends[1]: {friends[1].capitalize()}")
print(f"friends[2]: {friends[2]}")
print(f"friends[3]: {friends[3]}")
# print(f"friends[4]: {friends[4]}") # out of range, this is no index 4 in the list

print(friends[-1])
print(friends[-3])

## adding elements:
# list.append(new_element)

# resetting the elements, to give new value. you can not add new record
friends[2] = 'mark'
print(friends[2])
# friends[7] = 'elon'
print(f"new list after resetting; {friends}")

# removing the element: by value OR index
friends.remove('mark')
friends.pop(2)
print(f"new list removing; {friends}")

print('--------------------------------------------')
cars = ['bugatti', 'ferrari', 'tesla', 'bmw']
print(f"i would like to own a {cars[0].title()} car")
print(f"i would like to own a {cars[1].title()} car")
print(f"i would like to own a {cars[2].title()} car")
print(f"i would like to own a {cars[3].title()} car")

# 3.4
print('___________________________________________')
guest_list = ['Dasha', 'Lena', 'Sasha', 'Bob', 'Lenur']
print(f"Hi {guest_list[0].upper()}, i would like to invite you to dinner tomorrow")
print(f"Hi {guest_list[1].upper()}, i would like to invite you to dinner tomorrow")
print(f"Hi {guest_list[2].upper()}, i would like to invite you to dinner tomorrow")
print(f"Hi {guest_list[3].upper()}, i would like to invite you to dinner tomorrow")
print(f"Hi {guest_list[4].upper()}, i would like to invite you to dinner tomorrow")

# HW 03/07/2021
names = ['Dasha', 'Lena', 'Anna', 'Nicole', 'Sasha', 'Bob', 'Lenur']  # it doesn't work if lowercapital
removed_names = []
removed_names.append('may')

removed_names.append(names.pop(0))  # you dont assign to variable you move it directly to another list

print(removed_names)

##### orgonazing list
print(names)
# changing the list ordering in asc
names.sort()
print(names)
# changing the list ordering in decending
names.sort(reverse=True)

cars = ['bmw', 'audi', 'toyota', 'subaru']
sorted_cars = sorted(cars)
print(sorted_cars)
print(cars)
cars.reverse()
print(cars)
