from optparse import Values
from sys import last_traceback
from threading import main_thread
from turtle import color


alien_0 = {'color': 'green', 'points': 5}
print(alien_0['color'])
print(alien_0['points'])
print("\n")

alien_0 = {'color': 'green'}
print(alien_0['color'])
print("\n")

alien_0 = {'color': 'green', 'points': 5}
new_points = alien_0['points']
print("You just earned " + str(new_points) + " points!")
print("\n")

alien_0 = {'color': 'green', 'points': 5}
print(alien_0)

alien_0['x_position'] = 0
alien_0['y position'] = 25
print(alien_0)

#Starting with an Empty Dictionary
alien_0 = {}

alien_0['color'] = 'green'
alien_0['points'] = 5

print(alien_0)
print("\n")

#Modifying Values in a Dictionary 
alien_0 = {'color': 'green'}
print("The alien is "+ alien_0['color'] + ".")

alien_0['color'] = 'yellow'
print("The alien is now " + alien_0['color'] + ".")
print("\n")

alien_0 = {'x_position': 0, 'y_position': 25, 'speed': 'medium'}
print("Original x-position: " + str(alien_0['x_position']))
# Move the alien to the right
# Determine how far to move the alien based on its current speed.
if alien_0['speed'] == 'slow':
    x_increment = 1
elif alien_0['speed'] == 'medium':
    x_increment = 2
else:
    x_increment = 3

# The new position is the old position plus the increment
alien_0['x_position'] = alien_0['x_position'] + x_increment

print("New x-position: " + str(alien_0['x_position']))
print("\n")

#Deleting key values, removes the key value permanetly 
alien_0 = {'color': 'green', 'points': 5}
print(alien_0)
del alien_0['points']
print(alien_0)
print("\n")

favorite_languages = {
    'jen': 'python',
    'sarah': 'c',
    'edward': 'ruby',
    'phil': 'python',
    }
print("Sarah's favorite langauge is " + favorite_languages['sarah'].title() + ".")

user_0 = {
    'username': 'efermi',
    'first': 'enrico',
    'last': 'fermi',
    }

for key, value in user_0.items():
    print("\nKey: " + key)
    print("Value: " + value)
print("\n")

#Why does this work??? Is it because python knows (k,V) formats in a "for loop" automatically to the dictionary???
for name, language in favorite_languages.items():
    print(name.title() + "'s favorite language is " + language.title() + ".")
print("\n")

for name in favorite_languages.keys():
    print(name.title())
print("\n")

#for cleaner code use
for name in favorite_languages:
    print(name.title())
print("\n")

friends = ['phil', 'sarah']
for name in favorite_languages.keys():
    print(name.title())

    if name in friends:
        print("Hi " + name.title() +
        ", I see your favorite language is " +
        favorite_languages[name].title() + "!")
    
    if 'erin' not in favorite_languages.keys():
        print("Erin, please take our poll")

for name in sorted(favorite_languages.keys()):
    print(name.title() + ", thank you for taking the poll")

print("\n")

print("The following languages have been mentioned:")
for language in favorite_languages.values():
    print(language.title())

print("\n")

print("The following languages have been mentioned:")
for language in set(favorite_languages.values()):
    print(language.title())


rivers = {
    'nile': 'egypt',
    'thames': 'england',
    'mississippi': 'america',
    }

for river, location in rivers.items():
    print("\nKey: " + river)
    print("Value: " + location)

#REMEMBER WE HAVE TO SORT THROUGH THE DICTIONARY TO PRODUCE 
for river in sorted(rivers.keys()):
    print("The " + river.title() + ", runs through " + location.title())

for river in sorted(rivers.keys()):
    print(river.title())

for location in sorted(rivers.values()):
    print(location.title())

print("\n")

#Nesting
alien_0 = {'color': 'green', 'points': 5}
alien_1 = {'color': 'yellow', 'points': 10}
alien_2 = {'color': 'red', 'points': 15}

aliens = [alien_0, alien_1, alien_2]

for alien in aliens:
    print(alien)

aliens = []

for alien_number in range(30):
    new_alien = {'color': 'green', 'points': 5, 'speed': 'slow'}
    aliens.append(new_alien)
#show first 5 aliens
for alien in aliens[:5]:
    print(alien)
print("...")

#show how many aliens have been created.
print("Total number of aliens:" + str(len(aliens)))

for alien in aliens[0:3]:
    if alien['color'] == 'green':
        alien['color'] = 'yellow'
        alien['speed'] = 'medium'
        alien['points'] = 10
    #expand loop and turn yellow aliens into red
    elif alien['color'] == 'yellow':
        alien['color'] = 'red'
        alien['speed'] = 'fast'
        alien['points'] = 15

#show the first 5 aliens
for alien in aliens[0:5]:
    print(alien)

print("\n")

#LISTS INSIDE OF DICITIONARY
pizza = {
    'crust': 'thick',
    'toppings': ['mushrooms', 'extra cheese'],
    }

#summarize the order.
print("You ordered a " + pizza['crust'] + "-crust pizza" + 
    "with the following toppings:")

for topping in pizza['toppings']:
    print("\t" + topping)

favorite_languages = {
    'jen': ['python','ruby'],
    'sarah': ['c'],
    'edward': ['ruby', 'go'],
    'phil': ['python', 'haskell'],
    }
for name, languages in favorite_languages.items():
    print("\n" + name.title() + "'s favorite languages are:")
    for language in languages:
        print("\t" + language.title())

#Dictionary inside of a Dictonary
#shy away from, it can get complicated and messy

users = {
    'aeinstein': {
        'first': 'albert',
        'last': 'einstein',
        'location': 'princeton',
        },
    'mcurie': {
        'first': 'marie',
        'last': 'curie',
        'location': 'paris',
        },
    }

for username, user_info in users.items():
    print("\nUsername: " + username)
    full_name = user_info['first'] + " " + user_info['last']
    location = user_info['location']

    print("\tFull name: " + full_name.title())
    print("\tLocation: " + location.title())

    people = {
    'jsmithson': {
        'first': 'john',
        'last': 'smithson',
        'height': 72,
        'weight': 195,
        'school': 'University of Nebraska',
        },
    'sucollins': {
        'first': 'susan',
        'last': 'collins',
        'height': 66,
        'weight': 135,
        'school': 'University of Dakota',
        }
    }
print(people['jsmithson'])
print(people['sucollins'])
