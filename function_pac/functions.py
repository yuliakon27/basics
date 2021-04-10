# 3/21/2021 FUNCTION - block of  code

def greet_user(name):
    """docstring - describe the function"""
    print(f"Hello {name}")


#greet_user('Yulia')


def mutip(x, y):
    result = x * y
    print(result)


#mutip(10, 12)


def div(x, y):
    result = x // y
    print(result)


#div(120, 10)


def decribe_pet(name, type='cat'):
    """
    keyword parameter is type with default
    :param type: by default is cat, optional. has to be at the end
    :param name: is required paremetr
    :return:
    """
    print(f"I have a {type} and my pet name is {name.title()}")

#decribe_pet('love', "dog")
#decribe_pet( 'lazy')


# 3/25/2021
print("+++++++++++++++++++++++++++++++++++")
def favorite_book(title):
    print(f"one of my favorite book is {title}")

#favorite_book("land")


def multi_num(a, b):
    result = a*b
    print(f"Multiplication {a} by {b} is {result}")

#multi_num(10, 5)


'''
print(f"+++++++++++++++++++++++++++")
# how to swap 2 variable values
a = 45
b = 78

temp = a
a = b
b = temp
print("the value a : {}".format(a))
print("the value b : {}".format(b))
print('++++++++++++++++++++++++++++')

num1 = 'number one'
num2 = 'number two'
print(num1, num2)
num1, num2 = num2, num1
print(num1, num2)

print('++++++++++++++++++++++++++++')
'''