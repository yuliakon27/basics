# 03/14/2021 if statement mupltiple conditions
num = 2
if num >= 1:
    print(f'number is greater than 1')
else:
    print(f"number is lesss than 1")

# expression AND/OR expression AND/OR expression

#OR:
#exp OR exp = True OR False = True

print('++++++++++++++++++++++++++++++++++++++++++++++++++++++++')
# AND:
num = 20
if num >= 1 and num <= 10:
    print(f"number is equal or greater than 1 and less than 10")
else:
    print(f"number is less than 1 ")


#age = int(input('enter the visitors age: '))
age = 3
if 0 <= age <= 4:
    print("your admission cost is $0")
elif 4 < age <= 18:
    print("your admission cost is $5")
elif 18 <= age < 140:
    print("your admission cost is $10")
else:
    print("invalid age")


#age = int(input('enter the visitors age: '))
price = 0
if age < 4:
    price = 0
elif age < 18:
    price = 5
elif age < 140:
    price = 10
else:
    print("invalid number")
print(f"your admission cost is ${price}.")

print("++++++++++++++++++++++++++++++++++++++++++++++++++++++")

# ex. 5.3
print("ex 5.3")
alien_color = 'green'
    #= input("enter the alien color (green, yellow, red): ")
if alien_color == 'green':
    print(f"you  just earned 5 points")
elif alien_color == 'yellow':
    print(f"you just earned 2 points")
elif alien_color == 'red':
    print(f"you just earned 10 points")
else:
    print("no points, take a rest!")

#H/W 5.6, 5.7

print("+++++++++++++++++++++++++++++++++++++++++++++++++++")

friends =[] # empty list returns False
if friends:
    print("good for you, i can be your friend")
else:
    print("go out and meet people")

print("+++++++++++++++++++++++++++++++++++++++++++++++++++++")
available_toppings = ['mushrooms', 'olive', 'green peppers', 'pineapple', 'extra cheese']
requested_toppings = ['mushrooms', 'extra cheese', 'french fries']

for requested_topping in requested_toppings:
    if requested_toppings in available_toppings:
        print(f"i am adding {requested_toppings}")
    else:
        print(f"sorry, we don't have {requested_toppings}")

print("+++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
# exe
#1. implement sum() with for loop
#2. FuzzBuzz, assume user enters number > 0
#   print FUZZ if the number is dividable by 3
#   print BUZZ if the number is dividable by 5
#   print FUZZBUZZ if the nu is dividable by 3 and 5

# palindrome (mom, dad, madam, kayak)
#for letter in "hello":
#    print(letter)

fizzbuzz = int(input(f"enter number: "))
if fizzbuzz % 3 == 0 and fizzbuzz % 5 == 0:
    print("fizzbuzz")
elif fizzbuzz % 3 == 0:
    print("fizz")
elif fizzbuzz % 5 == 0:
    print("buzz")
else:
    print("")

