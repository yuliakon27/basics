# comment line ctrl +/
# shift + f10

bin_num =bin(45)

#print(bin_num)

current_users = ['Bob', 'Nik', 'Olga', 'Alex', 'Maria']
current_users[2] = 'Yulia'
print(current_users)

current_users.insert(0, 'Lenya')
print(current_users)

print("++++++++++++++++ DEL ++++++++++++=")
del current_users[0]
print(current_users)
print("++++++++++++++++ REMOVE ++++++++++++=")
current_users.remove('Yulia')
print(current_users)
print("++++++++++++++++ pop ++++++++++++=")
current_users.pop()
print(current_users)
print("++++++++++++++++ pop + ind ++++++++++++=")
print(current_users)
name = current_users.pop(-1)
print(current_users)

print("++++++++++++++++ using pop value ++++++++++++=")
#name = current_users.pop(-1)
print(name)
print("++++++++++++++++ ++++++++++++=")
current_users.append('Maria')
current_users.append('Yulia')
current_users.append('Sveta')
current_users.append('Steve')
current_users.append('Maryann')
current_users.append('Victor')
current_users.append('Yana')
print(current_users)

print("++++++++++++++++SORTING TEMP ++++++++++++=")
print(sorted(current_users, reverse=True))

print("++++++++++++++++SORTING per ++++++++++++=")
current_users.sort()
print(current_users)
current_users.sort(reverse=True)
print(current_users)

print("++++++++++++++++ LEN ++++++++++++=")

print(len(current_users))
love = len(current_users)
print(love)

print("++++++++++++++++ changi ++++++++++++=")
#current_users[10] = 'love'
#print(current_users)

users = []
if users:
    for user in users:
        if user == 'admin':
            print(f"Hello {user}, would you like to see a report?")
        else:
            print(f"We need some users")