magicans = ['alcie', 'david', 'carlina']
for magician in magicans:
    print(f"{magician.title()}, banger trick!")
    
    print(f"I cant wait for ur next banger trick! {magician.title()}\n")
print("Thanks for the show!")

even_numbers = list(range(2, 12, 4))
print(even_numbers)

squares =[]
for value in range(1,11):
    squares.append(value**2)
    print(squares)

#4.1
pizzas = ['margarita', 'chicken pizza', 'beef pizza']
for pizza in pizzas:
    print(f"I like {pizza} ")

print("\n I really love pizza\n")

#4.2

animals = ['lion', 'tiger', 'cheetah']
for animal in animals:
    print(animal)
    
for animal in animals:
    print(f"A {animal} would be dangerous to have")
print("\nNone of these animals would be safe to have in the house")

#4.3
for value in range(1,20):
    print(value)

#4.4,#4.5
print("\n")
millin = list(range(1,1000000))
print(min(millin))
print(max(millin))
print(sum(millin))

#4.6
print("\n")
odd_numbers = list(range(1,21,2))
for number in odd_numbers:
    print(number)
    
#4.7
print("\n")
multi = [value*3. for value in range(3,30)]
print(multi)

#4.8
print("\n")
cubes = []
for value in range(1,11):
    cube = value **2
    cubes.append(cube)
    
for cube in cubes:
    print(cube)
    
#4.9
cubes = [value**2 for value in range(1,11)]
print(cubes)



