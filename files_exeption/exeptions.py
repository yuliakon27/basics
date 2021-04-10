# you want to handle this errors
# handle situations where you expect certain errors

filepath = "C:\\dev\\basics\\data\\students.txt.py"

try:
    print(f"trying block started")
    with open(filepath, 'a') as student:
        print("writing to the file")
        student.write("hello") # fun that writes in file

    with open(filepath, 'r') as students:
        lines = students.readlines()
        print(lines)

except FileNotFoundError as err: # if there is this error in block, it will print msg
    print(err)
    print(f"Enter correct filepath")

print(f"programs is completed!")

print()





'''
try:

    code
    code

except filenotfounderror as err:
    print(err)
    print("enter correct file path, check your file path ")

try:
    print(5/0)
except  ZeroDivisionError as err:
    print("You can not divide by zero ")
'''

print(f"++++++++++++++++++++++++++++++++++++++++")
try:
    num = 5/5
    print(f"result  of this division is {num}")
except ZeroDivisionError as err:
    print(" you ca not divide by 0")
else: # this is dependent on try block , if try block executes else
    print("this is else block")
finally:
    print("i am a finally block, i am always executed whatever "
          "happens with try, expect or else block")
print(f"programs is completed!")
