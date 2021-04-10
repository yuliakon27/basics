#03/13/2021
if 2 < 3:
    print(f"expession is true")
else:
    print(f"expression is false")
print("if statement is completed here")

print("+++++++++++++++++++++++++++++++++")
num1=20
num2=1
#if num1 < num2:
if num1 == num2:
    print("expression is true")
else:
    print("expression is false")
print("++++++++++++++++++++++++++")
msg = True
if msg:
    print("expression is true")
else:
    print(" expression is false")

print("++++++++++++++++++++++++++++++")
msg = input("enter true/false here: ")
if msg:
    print("expression is true")
else:
    print(" expression is false")

print("+++++++++++++++++++++++++++++")
msg = input("enter the number: ")
if msg.strip() != '':
    print(f"this message was entered: \n'{msg}'")
else:
    print(f"whitespace")
print("+++++++++++++++++++++++++")

msg = input("enter the number: ")
if msg.strip() == '':
    print(f"this message was entered: \n'{msg}'")
else:
    print(f"whitespace")

print("+++++++++++++++++++++++++++++++++")
cars = ['bugatti', 'ferrari', 'tesla', 'lexus']
if 'tesla' in cars:
    print(f"we have tesla in stock")
else:
    print("we don't have it")

ask = input("enter model: ")
if ask in cars:
    print(f"we have {ask} in stock")
else:
    print(f"we don't have {ask} in stock")

print("+++++++++++++++++++++=")

if 'sat' in "today in saturday":
    print(f"yes")
else:
    print(f"no")