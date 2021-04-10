# 03/11/2021

cars = ['bugatti', 'ferrari', 'tesla', 'lexus']
# making numerical list
# SYNTEX: range ([start], stop, [step])

for num in range(4):
    print(num)

nums = range(4)
nums2 = list(range(4))
print(nums)
print(nums2)

for num in nums2:
    print(f"number: {num}")
print()
print('range with start and stop')
for num in range(1, 4):
    print(f"number: {num}")
print()
print("range with start stop and step")
#              start stop step=interval
for num in range(2, 15, 2):
    print(num)

print()
print('print even numbers from 1 to 16')
evens = []

for num in range(0, 17, 2):
    print(num)
    evens.append(num)  # to add values in list
    print(evens)  # printing list as many times as we have range, only with + another #
print()
print(evens)

print()
print("Exercise2: print the squares of numbers from 10 to 20.")
squares = []
for num in range(10, 21):
    squares.append(num ** 2)

print(squares)
print(f"min(squres): {min(squares)}")
print(f"max(squres): {max(squares)}")
print(f"sum(squres): {sum(squares)}")

print()
print("Exercise3 using index")

len_cars = len(cars)

for car in cars:
    print(car)
    print(f"index of the {car} is {cars.index(car)}")

print()
print("looping using ind")
for ind in range(len_cars):  # or using len function range(len(cars))
    print(ind)
    print(f"index of the {cars[ind]} is {ind}")

print("_______________________________________________")
# list comprehension (only for appending)

squares = []
for num in range(10, 21):
    squares.append(num ** 2)
#   append(expresion)  +    for loop
squares = [num ** 2 for num in range(10, 21)]

print()
print("Execirs")
nums = []
for num in range(1, 1000001):
    nums.append(num)

print(f"smallest number: {min(nums)}")
print(f"biggest number: {max(nums)}")
print(f"sum number: {sum(nums)}")