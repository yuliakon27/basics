# 3/21/2021 while loop
print("++++++++ incrementing the variable to reach upper boundary+++")
current_num = 1
while current_num <= 5:
    print(current_num)
    current_num += 1

print("++++++++ decrementing the variable to reach upper boundary+++")
current_num = 10
while current_num >= 5:
    print(current_num)
    current_num -= 1

print("====== game started===========")
# enter colors , green 15 points , yellow - 10
# red - 5, other colors or something else you loose
# q to quit the game

color = None
while color != 'quit' or color != 'q':
    color = input("Enter your color (green, yellow, red):  ")
    color = color.lower().strip() # we takr
    points = 0
    if color == 'quit' or color == 'q':
        break
    elif color == 'green':
        points = 15
    elif color == 'yellow':
        points = 10
    elif color == 'red':
        points = 5
    elif color == 'quit':
        break
 #   elif color == 'quit':
 #       print(f"Game is over")
    else:
        print(f"You earned nothing!")
    print(f"You won {points} points!")
print("closing the game")

print("++++++++++++++++flag ++++++++++++++++")
# examples of flags
count = 0
for letter in 'hello guys':
    if letter == 'l':
        count += 1
print(f"number of l's is : {count}")

