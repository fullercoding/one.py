prompt = "\nPlease tell me your age for the price of admission: "
prompt += "\nEnter 'quit' when you are finished. "
while True:
    age = (input(prompt))
    age = int()

    if age == 'quit':
        break
    if age <= 3:
        print("Your admission is free. Enjoy the show")
    if age <= 12:
        print("Your price is $10." )
    if age >= 13:
        ("Your price is $15. Enjoy the show")