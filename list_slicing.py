# 03/13/2021
# working with part of list
cars = ['bugatti', 'ferrari', 'tesla', 'lexus']

# slice of the list list_name[start:stop] - start is inclusive, stop is exclusive values

#       inclusive : exclusive
for car in cars[1:3]:
    print(f"the car is: {car}")

print("____________________________________________________")
for car in cars[0:3]:
    print(f"the car is: {car}")

print("____________________________________________________")
for car in cars[:3]:
    print(f"the car is: {car}")

print("________________________________________________________")
for car in cars[0:]:
    print(f"the car is: {car}")
print("__________________________________________________")
for car in cars[:10]: # no out of index error
    print(f"the car is: {car}")
print("_______________copying______________")
# copying the list
cars2 = cars
print(f"cars: {cars}")
print(f"cars2: {cars2}")
print(f"+++++++++after apdaded++++++++++")
cars.append('bmw')
print(f"cars: {cars}")
print(f"cars2: {cars2}")

cars3 = cars[:]
print(f"cars: {cars}")
print(f"cars2: {cars2}")
print(f"cars3: {cars3}")
print("++++++++++++++++++++++++++++++++++")
cars3.append('audi')
print(f"cars: {cars}")
print(f"cars2: {cars2}")
print(f"cars3: {cars3}")
print("++++++++++++++++++++")
cars.append("toyta")
print(f"cars: {cars}")
print(f"cars2: {cars2}")
print(f"cars3: {cars3}")
print("+++++++++++++ exe 4.10++++++++++++++++++++++")
#exe 4.10
print(f"the first 3 items in the list are: {cars[:3]} ")
print(f"3 items in the middle of the list are: {cars[2:5]} ")
print(f"last 3 items in the list are: {cars[-3:]} ")

print("++++++++++++++++TUPLES+++++++++++++++++++++++")
#tuples - data strucure similar to list but can not be modified

cars_t = ("0", "1", "2","3", "4")
print(cars_t)
#cars_t.append("8") # cannot change
print(cars_t)

