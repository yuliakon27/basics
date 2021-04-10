# 03/04/2021 strings

#
fname = 'john smith'
print(fname)
print(fname.upper())
msg = "we are looking. at strings functions in python"
print(msg.replace('.', '!!').title())
print(fname.lower())

# concatenation
msg1 = fname.upper() + '. ' + msg
print(msg1)

# working with whiespaces in string
print(fname.upper() + "msg1 = fname.upper() + '. '+ msg , " + msg)
msg2 = fname.upper() + '. ' + msg
msg3 = '\n\t\t\t' + fname.upper() + ', ' + msg2
print(msg3)
print(msg3.strip())  # to remove all whitespaces
print(msg3.strip() + "!!!!")

# fstring
msg4 = f"\n\t\t\t {fname.upper()} ,  {msg2}"
print(msg4)

# Intergers

num = 456
num2 = 600
print(f"num + num2 = {num + num2}")
print(f"num - num2 = {num - num2}")
print(f"num * num2 = {num * num2}")
print(f"num / num2 = {num / num2}")

print(int(16 / 2))

