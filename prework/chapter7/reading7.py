#input function

message = input("Tell me something, and I will repeat it back to you: ")
print("hi charlie")
print("\n")

name = input("please enter your name: ")
print("Hello, " + name + "!")

#prompts

prompt = "If you tell us who you are we can personalize the message you see."
prompt += "\nWhat is your first name? "

name = input(prompt)
print("\nHello, " + name + "!")

age = input("How old are you? ")
#when the user inputs their age, the inputed interger will be turned 
# to a string. so then it becomes
age = (int(input("How old are you? ")))
age >= 18

height = int(input("How tall are you, in inches?"))
if height >= 36:
    print("\nYou're tall enough to ride!")
else:
    print("\nYou'll be able to ride when you're a little older.")

number = int(input("Enter a number, and I'll tell you if it's even or odd: "))
if number % 2 == 0:
 print("\nThe number " + str(number) + " is even.")
else:
 print("\nThe number " + str(number) + " is odd.")
 