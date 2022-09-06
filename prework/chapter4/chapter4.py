foods = ["pizza", "tacos","dim sum", "sushi"]

print(foods[1])

# for (PLACEMENT) in THE_LIST_WE_WANT_TO_lOOK_AT:
    #this is a code block
    #this code block
    #will run every item in the list

for food in foods:
    
    if food == "dim sum":
        continue
    print(f"I like {food} because they are yummy")

for index in range(len(foods)):
    print(index)
    print(foods[index])
# ENUMERATE IS HOW PYTHON GIVES A LIST OF STRINGS AN INDEX POSITION IN A FOR LOOP
print(list(enumerate(foods)))
for index,food in enumerate(foods):
    print(f"my no {index + 1} food is {food.title()}")


# LOOP OF THE INDEX
print(list(range(4)))
print(len(foods))