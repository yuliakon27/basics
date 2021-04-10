         #                                    ind1     ind2
favorite_places = {'Alex': 'Spain', 'Jen': ['Arizona', 'Florida'], 'Bob': 'Thailand', 'Anna': 'India'}

for name, details in favorite_places.items():
    if name == 'Jen':
        print(f"{name}'s favorite places are"
              f"\n {favorite_places['Jen'][0]} and {favorite_places['Jen'][1]}")
    else:
        print(f"{name}'s favorite place is {details} ")
