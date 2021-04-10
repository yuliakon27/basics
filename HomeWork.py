#3.4
print('___________________________________________')
guest_list = ['Dasha', 'Lena', 'Sasha', 'Bob', 'Lenur', 'John', 'Chris']
print(f"Hi {guest_list[0].upper()}, i would like to invite you to dinner tomorrow")
print(f"Hi {guest_list[1].upper()}, i would like to invite you to dinner tomorrow")
print(f"Hi {guest_list[2].upper()}, i would like to invite you to dinner tomorrow")
print(f"Hi {guest_list[3].upper()}, i would like to invite you to dinner tomorrow")
print(f"Hi {guest_list[4].upper()}, i would like to invite you to dinner tomorrow")

print("__________________________________________")
#3.5
print(guest_list)
print(f"Unfortunately, the following guests are not able to make it tomorrow: {guest_list[3]}, {guest_list[5]}")
guest_list[3] = 'Anna'
guest_list[5] = 'Mike'
print(f"\nHi {guest_list[0].upper()}, i would like to invite you to dinner tomorrow!")
print(f"\nHi {guest_list[1].upper()}, i would like to invite you to dinner tomorrow!")
print(f"\nHi {guest_list[2].upper()}, i would like to invite you to dinner tomorrow!")
print(f"\nHi {guest_list[3].upper()}, i would like to invite you to dinner tomorrow!")
print(f"\nHi {guest_list[4].upper()}, i would like to invite you to dinner tomorrow!")
print(f"\nHi {guest_list[5].upper()}, i would like to invite you to dinner tomorrow!")
print(f"\nHi {guest_list[6].upper()}, i would like to invite you to dinner tomorrow!")

# 3.6
print('___________________________________________')
print(guest_list)
print(f"Dear friends, i would like to inform you that i found a beautiful place for us. "
      f"\nLet's see each other tomorrow at YUYU restaurant at 5.30pm")
guest_list.insert(0, 'Olga')
guest_list.insert(4, 'Alex')
guest_list.append('Lisa')
print(guest_list)

print(f"\nHi {guest_list[0].title()}, I would like to invite you for dinner tomorrow!"
      f"\n\tLet's meet at YUYU restaurant at 5.30pm tomorrow."
      f"\n\t\tLooking forward to see you!")
print(f"\nHi {guest_list[1].title()}, I would like to invite you for dinner tomorrow!"
      f"\n\tLet's meet at YUYU restaurant at 5.30pm tomorrow."
      f"\n\t\tLooking forward to see you!")
print(f"\nHi {guest_list[2].title()}, I would like to invite you for dinner tomorrow!"
      f"\n\tLet's meet at YUYU restaurant at 5.30pm tomorrow."
      f"\n\t\tLooking forward to see you!")
print(f"\nHi {guest_list[3].title()}, I would like to invite you for dinner tomorrow!"
      f"\n\tLet's meet at YUYU restaurant at 5.30pm tomorrow."
      f"\n\t\tLooking forward to see you!")
print(f"\nHi {guest_list[4].title()}, I would like to invite you for dinner tomorrow!"
      f"\n\tLet's meet at YUYU restaurant at 5.30pm tomorrow."
      f"\n\t\tLooking forward to see you!")
print(f"\nHi {guest_list[5].title()}, I would like to invite you for dinner tomorrow!"
      f"\n\tLet's meet at YUYU restaurant at 5.30pm tomorrow."
      f"\n\t\tLooking forward to see you!")
print(f"\nHi {guest_list[6].title()}, I would like to invite you for dinner tomorrow!"
      f"\n\tLet's meet at YUYU restaurant at 5.30pm tomorrow."
      f"\n\t\tLooking forward to see you!")
print(f"\nHi {guest_list[7].title()}, I would like to invite you for dinner tomorrow!"
      f"\n\tLet's meet at YUYU restaurant at 5.30pm tomorrow."
      f"\n\t\tLooking forward to see you!")
print(f"\nHi {guest_list[8].title()}, I would like to invite you for dinner tomorrow!"
      f"\n\tLet's meet at YUYU restaurant at 5.30pm tomorrow."
      f"\n\t\tLooking forward to see you!")
print(f"\nHi {guest_list[9].title()}, I would like to invite you for dinner tomorrow!"
      f"\n\tLet's meet at YUYU restaurant at 5.30pm tomorrow."
      f"\n\t\tLooking forward to see you!")

#3.7
print("_________________________________________________")
print(guest_list)
print(f'Dear friends, turned out I can invite only 2 people for dinner.')
popped_guest0 = guest_list.pop(0)
print(f'\nDear {popped_guest0}, I have to cancel your invitation.'
      f'\n\tI apologize for any inconvenience.')
popped_guest1 = guest_list.pop(0)
print(f'\nDear {popped_guest1}, I have to cancel your invitation.'
      f'\n\tI apologize for any inconvenience.')
popped_guest2 = guest_list.pop(0)
print(f'\nDear {popped_guest2}, I have to cancel your invitation.'
      f'\n\tI apologize for any inconvenience.')
popped_guest3 = guest_list.pop(0)
print(f'\nDear {popped_guest3}, I have to cancel your invitation.'
      f'\n\tI apologize for any inconvenience.')
popped_guest4 = guest_list.pop(0)
print(f'\nDear {popped_guest4}, I have to cancel your invitation.'
      f'\n\tI apologize for any inconvenience.\n')
popped_guest5 = guest_list.pop(0)
print(f'\nDear {popped_guest5}, I have to cancel your invitation.'
      f'\n\tI apologize for any inconvenience.\n')
popped_guest6 = guest_list.pop(0)
print(f'\nDear {popped_guest6}, I have to cancel your invitation.'
      f'\n\tI apologize for any inconvenience.\n')
popped_guest = guest_list.pop(0)
print(f'\nDear {popped_guest}, I have to cancel your invitation.'
      f'\n\tI apologize for any inconvenience.\n')

print(guest_list)

print(f"Dear {guest_list[0]}, I am happy to meet you at YUYU restaurant at 5.30pm")
print(f"Dear {guest_list[1]}, I am happy to meet you at YUYU restaurant at 5.30pm")

del guest_list[0]
del guest_list[0]
print(guest_list)