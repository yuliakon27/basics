# 3/20/2021 Looping in dictionaries

print(f"+++++++++++++++ 1 ++++++++++++++++++++")
# looping using keys:
fav_num = {'Zack': 7, 'Olga': 3, 'Mia': 1, 'Alex': 6, 'Bob': 13}
for key in fav_num:
    print('________________________________')
    print(f"key in this iteration is: {key}")
    print(f"value in this iteration is: {fav_num[key]}")

print("+++++++++++++ 2 ++++++++++++++++++++++++++++++")
#
for key in fav_num.keys():
    print('________________________________')
    print(f"key in this iteration is: {key}")
    print(f"value in this iteration is: {fav_num[key]}")

print("==============================")
# looking specific key in dictionaries
if 'Zack' in fav_num:
    print(f"Yes, it's here")
else:
    print(f"No, it's not here")


print("++++++++++++ 3 using .values() +++++++++++++++++++++++++++++++")

#   print(f"value in this iteration is: {fav_num[value]}") - cannot use

print("++++++++++++ 4 using .items() +++++++++++++++++++++++++++++++")
print(fav_num)
for key, value in fav_num.items():
    print('________________________________')
    print(f"key in this iteration is: {key}")
    print(f"value in this iteration is: {value}")


print("++++++++++++++++++++++++++++")
if 13 in fav_num.values():
    print(f"yes")

print("++++++++++++++++++++++++++++")
favorite_languages = {
 'jen': 'python',
 'sarah': 'c',
 'edward': 'ruby',
 'phil': 'python',
 }

for name in sorted(favorite_languages.keys()):
    print(f"{name}'s favorite language is {favorite_languages[name]}")

print("+++++++++EX 6.5+++++++++++++++++++")
rivers = {'nile': 'egypt', 'volga': 'russia', 'missuri': 'usa', 'ganga': 'india'}

for key, key in rivers.items():
    print(f"river "
          f"{key} is running in {key}")
