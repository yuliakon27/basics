# 04/04/21

filepath = "C:\\dev\\basics\\data\\students.txt.py" # absolute path, only for windows.
# for mac and win use /

print(f"+++++++ reading ++++++++++++++")
''' with open pattern - open and close the file
by default read only mode
'''
# saving in a memory and give alias name
#            file         alias
with open(filepath) as students:
    contents = students.read() # fun return all the content of that file
    print(contents)

print(f"+++++++reading line by line++++++++++++++")
# reading line by line
with open(filepath) as students: # for loop lines
    for line in students:
     #   print(line) # will have empty space in between
        print(line)


print(f"+++++++making a list++++++++++++++")
# making a list
with open(filepath) as students: # for loop lines
    lines = students.readlines() # fun to make a list

print(lines)
print(lines[0]) # printing first ind in string
print(lines[-1]) # printing last ind in string

print("++++++++++++ looping ++++++++++++++++++++")
for line in lines:
    print(line.strip())

# reading from the file
print("++++++++++++ writing in file  ++++++++++++++++++++")
'''
w - write. it will create file if not exist, and override if exists 
a - append. it will add value to the end 
r - read. can only read file 

with open(filepath, 'a') as student:
    print("writing to the file")
    students.write("Ali")

# appending new file

print("program is complited")
'''
with open(filepath, 'a') as student:
    print("writing to the file")
    student.write("hello") # fun that writes in file

with open(filepath, 'r') as students:
    lines = students.readlines()
    print(lines)