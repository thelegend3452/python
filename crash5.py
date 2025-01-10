#if-statments
requested = 'pokemon'
if requested  != 'sonic':
    print("no i want to play pokemon")
    
    
answer  = 22
if answer != 22:
    print("Wrong")
else:
    print("Correct")
    
users = ['arman', 'ashir']
user = 'asmar'

if user not in users:
    print(f"{user.title()} is not banned")
    
    
age = 3
if age < 4:
    price = 0
elif age < 18:
    price = 25
else:
    price = 40
    
print(f"Your admission will cost us {price}")

requested_toppings = ['mushrooms', 'cheese']

if 'mushrooms' in requested_toppings:
    print('Adding mushrooms')
if 'cheese' in requested_toppings:
    print('Adding cheese')
if 'chicken' in requested_toppings:
    print('Adding chicken')
print(f"\nFinished making yoru pizza, {requested_toppings}")
    
#5.3
print('5.3')

alien_color ='red'

if 'red' == alien_color:
    print('The player just earned 5 points')
else:
    print('')
    
#5.4
print('\n5.4')

alien_color ='yellow'

if 'green' == alien_color:
    print('The player just earned 5 points')
else:
    print('You just earned 10 points')
    
if 'yellow' == alien_color:
    print('You just earned 5 points')
else:
    print('You just earned 10 points')
    
    
#5.5
print('\n5.5')
alien_color ='green'

if 'green' == alien_color:
    print('You earned 10 points')
elif 'yellow' == alien_color:
    print('you earned 5 points')
else:
    print('you earned 15 points')

#5.6
print('\n5.6')

age = 2

if age <2 :
    print('this person is a baby')
elif age < 4:
    print('this person is a toddler')
elif age <13 :
    print('this person is a kid')
elif age <20:
    print('this person is an teenager')
elif age <65:
    print('This person adult')
else:
    print('this is an elder')
    
#5.7
print('\n5.7')

favorite_fruits = ['apple', 'banana', 'orange']

if 'orange' in favorite_fruits:
    print('you really like oranges')
if 'pear' in favorite_fruits:
    print('You really like pears')
if 'apple' in favorite_fruits:
    print('You really like apples')
if 'banana' in favorite_fruits:
    print('You really like bananas')
if 'kiwi' in favorite_fruits:
    print('You really like kiwis')