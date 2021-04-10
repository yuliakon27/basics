# 3/25/2021 functions with return statement  Return
def get_formatted_name(firstname: str, lastname: str):
    name = f"{firstname.title()} {lastname.title()}"
    return name
'''
def print_formatted_name(firstname: str, lastname: str):
    name = f"{firstname.title()} {lastname.title()}"
    print(name)

get_formatted_name('yulia', 'konyukhova')
print(get_formatted_name('yulia', 'konyukhova'))

def get_desc_of_what_you_want_to_get():
    return
def set_desc_of_what_you_want_to_get():
    pass
'''

# using different date structure
def print_username(users: list):
    for user in users:
        print(f"current user: {user}")

print_username(['john', 'mike', 'olga', 'victor', 'ruslan'])
