age = 17
if age >=18:
    print("You are old enough to vote")
    print("Have you registered to vote yet?")
else:
    print("Sorry, you are too young to vote.")
    print("Please register to vote as soon as you turn 18!")

#ELIF

age = 12 
if age < 4:
    print("Your admission cost is $0.")
elif age < 18:
    print("Your admission cost is $5.")
else:
    print("Your admission cost is $10.")

age = 12

if age < 4:
    price = 0
elif age < 18:
    price = 5
else:
    price = 10
print("Your admission cost is $" + str(price) + ".")

age = 40

if age < 4:
    price = 0
elif age < 18:
    price = 5
elif age < 65:
    price = 10
else:
    price = 5

print("Your admission cost is $" + str(price) + ".")

requested_topping = ['mushrooms', 'extra cheese']

if 'mushrooms' in requested_topping:
    print("adding mushrooms.")
if 'pepperoni' in requested_topping:
    print("adding pepperoni")
if 'extra cheese' in requested_topping:
    print("adding extra cheese.")

print("\nFinished making your pizza!")

alien_color = ['red', 'blue', 'green', 'purple']

if 'red' in alien_color:
    print("Player Red has been awarded 5 points")
if 'blue' in alien_color:
    print("Player Blue has lost 5 points")
if 'purple' in alien_color:
    print("Player Purple has been awarded 0 points")

alien_colors = ['pink', 'orange', 'auburn']

if 'pink' in alien_colors:
    print("pink has been awarded 7 points")
if 'burgandy' in alien_colors:
    print("No points awarded to orange")
else:
    print("You have been awarded 10 points")

#Come back to this, why does it give attribute "adult, teen, kid, and toddler "\
    #solved, I was running if-if-if statements not if-elif-elif-elif-else
age = 25

if age <=2:
    print("This child is a baby.")
elif age <=4:
    print("This child is a toddler.")
elif age <=13:
    print("This child is a kid.")
elif age <=20:
    print("This person is a teen.")
elif age <65:
    print("This person is an adult.")
else:
    print("This person is an elder.")

favorite_fruits = ['bananas', 'oranges', 'strawberries']

if 'bananas' in favorite_fruits:
    print("I really like Bananas")
if 'oranges' in favorite_fruits:
    print("I really like Oranges")
if 'strawberries' in favorite_fruits:
    print("I really like Strawberries")
if 'strawberries' in favorite_fruits:
    print("I like them more than Bananas")
if 'oranges' in favorite_fruits:
    print("But not as much as Apples")
print("\n")
requested_toppings = ['mushrooms', 'green peppers', 'extra cheese']

for requested_topping in requested_toppings:
    print("Adding " + requested_topping + ".")

print("\nFinshed Making your pizza!!")
print("\n")

requested_toppings = ['mushrooms', 'green peppers', 'extra cheese']

for request_topping in requested_toppings:
    if request_topping == 'green peppers':
        print("sorry, we are out of green peppers right now.")
    else:
        print("Adding " + request_topping + ".")
print("\nFinished making your pizza!")
print("\n")

requested_toppings = []

if requested_toppings:
    for requested_topping in requested_toppings:
        print("Adding " + requested_topping + ".")
else:
    print("Are you sure you want a plain pizza?")
    print("\n")

available_toppings = ['mushrooms', 'olives', 'green peppers',
 'pepperoni', 'pineapple', 'extra cheese']
requested_toppings = ['mushrooms', 'french fries', 'extra cheese']
 
for requested_topping in requested_toppings:
    if requested_topping in available_toppings:
        print("Adding " + requested_topping + ".")
    else:
        print("Sorry, we don't have " + requested_topping + ".")

print("\nFinished making your pizza!")

Usernames = ['gamer123', '321Games', 'admin', 'xXHappyXx']
for user in Usernames:
    if user == "admin":
        print("Hello admin, would you you like to see a status report?")
    else:
        print("hello " + user + " thank you for logging in again.")

print('\n')

Usernames = []


if Usernames:
    for user in requested_toppings:
        print("Adding " + user + ".")
else:
    print("We need to find more users")
    print("\n")