print("++++++++++8.3+++++++++++++++")
''': Write a function called make_shirt() that accepts a size and the 
text of a message that should be printed on the shirt. The function should print 
a sentence summarizing the size of the shirt and the message printed on it.
Call the function once using positional arguments to make a shirt. Call the 
function a second time using keyword arguments.'''


def make_shirt(size, text):
    print(f"The size of this T-Shirt is {size.upper()}, "
          f"\nand the message is: '{text}'")


make_shirt('m', 'Hello World!')

print("++++++++++8.4+++++++++++++++")
''' Modify the make_shirt() function so that shirts are large 
by default with a message that reads I love Python. Make a large shirt 
and a medium shirt with the default message, and a shirt of any size 
with a different message.'''


def make_shirt(size='large', text='I love Python'):
    print(f"The size of this T-Shirt is {size.upper()}, "
          f"\nand the message is: '{text}'")
make_shirt()

print("++++++++++8.5+++++++++++++++")
'''Write a function called describe_city() that accepts the name of
a city and its country. The function should print a simple sentence, such as 
Reykjavik is in Iceland. Give the parameter for the country a default value.
Call your function for three different cities, at least one of which is not in the 
default country.'''

def describe_city(name, country='usa'):
    print(f"{name} is in {country}")

describe_city('brooklyn', 'usa')
describe_city('moscow')

print("++++++++++8.6+++++++++++++++")
''' Write a function called city_country() that takes in the name 
of a city and its country. The function should return a string formatted 
like this:"Santiago, Chile"
Call your function with at least three city-country pairs, and print 
the value that’s returned.'''
def city_country(city, country):
    return
    print(f'"{city}, {country}"')

city_country('brooklyn', 'usa')
print("++++++++++8.4+++++++++++++++")
print("++++++++++8.4+++++++++++++++")
print("++++++++++8.4+++++++++++++++")
print("++++++++++8.4+++++++++++++++")
