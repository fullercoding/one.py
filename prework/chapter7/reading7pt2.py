#while loops

from http.client import responses
from operator import truediv
from turtle import end_fill


current_number =1 #starting point
while current_number <= 5: #finishing point(sets the standard for the loop)
    print(current_number)
    current_number +=1 #count from 1-5 
print("\n")

prompt = "\nTell me something, and I will repeat it back to you: "
prompt += "\nEnter 'quit' to end the program. "
message = "" 
while message != 'quit':
    message = input(prompt)
    print(message)
    if message != 'quit':
        print(message)

active = True
while active:
    message = input(prompt)

    if message == 'quit':
        active = False
    else:
        print(message)
#break to exit a loop


prompt = "\nPlease enter the name of a city you have visited:"
prompt += "\n(Enter 'quit' when you are finished.) "
while True:
    city = input(prompt)

    if city == 'quit':
        break
    else:
        print("I'd love to go to " + city.title() + "!")

current_number = 0
while current_number < 10:
    current_number += 1
    if current_number % 2 == 0:
        continue
    print(current_number)

x = 1 
while x <= 5: 
    print(x)
    x += 1

#7-4
prompt = "\nPlease enter in your favorite toppings for pizza: "
prompt += "\nEnter 'quit' when you are finished. "
while True:
    topping = input(prompt)
    
    if topping == 'quit':
        break
    else: 
        print(" I love " + topping.title() + "!")

#7-5 COME BACK AND FIX


unconfirmed_users = ['alice', 'brian', 'candace']
confirmed_users = []

while unconfirmed_users:
    current_user = unconfirmed_users.pop()

    print("verifying user: " + current_user.title())
    confirmed_users.append(current_user)
#Display confirmed users.
print("\nThe following users have been confirmed: ")
for confirmed_user in confirmed_users:
    print(confirmed_user.title())

#Removing all instances of a value in a list
pets = ['dog', 'cat', 'dog', 'goldfish', 'cat', 'rabbit', 'cat']
print(pets)

while 'cat' in pets:
    pets.remove('cat')
print(pets)

#filling a dictionary with USERS input
#set a flag to indicate the polling is active

polling_active = True

while polling_active:
    #prompt for the person's name and response
    name = input("\nWhat is your name? ")
    response = input("Which mountain would you like to climb someday? ")

    #Store the input responses
    responses[name] = response

    #find out if anyone else is going to take the poll
    repeat = input("Would you like to let another person respond? (yes/no) ")
    if repeat == 'no': 
        polling_active = False
        break
#Polling is complete, show results
print("\n ---Poll Results---")
for name, response in responses.items():
    print(name + " would you like to climb " + response + ".")
