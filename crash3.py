#Chapter 3: List

bikes = ['kawasaki', 'yamaha', 'harley davidson']
bikes[0] = 'BMW' #changed Kawasaki to bmw
print(bikes[-1].title())
print(bikes) 

print("Orginal list")
print(bikes)

print("\n Here is the sorted list")
print(sorted(bikes))





#3.1
names = ['afaq', 'ashir', 'arman', 'bæbs']
print(names[0].title())
print(names[1].title())
print(names[2].title())
print(names[3].title())

#3.2
print(f"Hi {names[0].title()}, how are you?")
print(f"Hi {names[1].title()}, how are you?")
print(f"Hi {names[2].title()}, how are you?")
print(f"Hi {names[3].title()}, how are you?")

#3.3
transport = ['tbane', 'car', 'bike']
message = "i would like to own a"
print(f"{message} {transport[1]}")

#3.4
invite_person = ['dad', 'mom', 'siblings']
print(f"Hi {invite_person[0].title()} to dinner")
print(f"Hi {invite_person[1].title()} to dinner")
print(f"Hi {invite_person[2].title()} to dinner")

#3.5
invite_person[2] = 'Grandparents'
print(f"Hi {invite_person[0].title()} to dinner")
print(f"Hi {invite_person[1].title()} to dinner")
print(f"Hi {invite_person[2].title()} to dinner")

#3.6
invite_person.append('Uncle')
invite_person.append('Cousin')
invite_person.append('Aunt')
print(f"Hi {invite_person[0].title()} to dinner")
print(f"Hi {invite_person[1].title()} to dinner")
print(f"Hi {invite_person[2].title()} to dinner")
print(f"Hi {invite_person[3].title()} to dinner")
print(f"Hi {invite_person[4].title()} to dinner")
print(f"Hi {invite_person[5].title()} to dinner")

#3.7
print("I just found out that i can only invite 2 people to dinner")

cancel = invite_person.pop()
print("Sorry " + cancel.title() + " not enough space")

cancel = invite_person.pop()
print("Sorry " + cancel.title() + " not enough space")

cancel = invite_person.pop()
print("Sorry " + cancel.title() + " not enough space")

cancel = invite_person.pop()
print("Sorry " + cancel.title() + " not enough space")

invited = invite_person[0]
print(invited.title() + " you are still invited")

invited = invite_person[1]
print(invited + " you are still invited")

del(invite_person[0])
del(invite_person[0])
print(invite_person)


#3.8

places = ['Japan', 'Korea', 'Palestine', 'Sveits','Nord-Norge']
print(places)

print("\nSorted list")
print(sorted(places))

print("\n Reversed List alpha")
print(sorted(places, reverse=True))

print("\n Normal reversed")
places.reverse()
print(places)

print("\n Sorted in aplha order")
places.sort(reverse=True)
print(places)






