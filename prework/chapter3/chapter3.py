my_list = []
print(type(my_list))
my_list = list()
print(type(my_list))

numbers = [2,6,10,12.5,0]
print(numbers)
print(type(numbers))
print(numbers[1])
print(type(numbers[1]))
print(numbers[1]*2.5)
print(type(numbers[1]*2.5))

print(numbers[3])
print(type(numbers[3]))

foods = ["pizza", "tacos", "dim sum", "sushi"]
print(foods[1])
print(type(foods[1]))
print(foods[1].upper())

x = 12
y = 15.5
z = "Z"

random_list = [x, y, z]
print(random_list[0])
print(type(random_list[0]))

print(random_list[1])
print(type(random_list[1]))

print(random_list[2])
print(type(random_list[2]))

my_favorite_num = random_list[0]
print(my_favorite_num)

foods = ["pizza", "tacos", "dim sum", "sushi"]
foods.append("cheeseburger")
print(foods)

foods.insert(0, "pho")
print(foods)

foods.remove("pho")
print(foods)

foods = ["pizza", "tacos", "dim sum", "sushi"]
foods.append("pizza")
print(foods)

foods.remove("pizza")
print(foods)
foods.remove("pizza")
print(foods)

foods = ["pizza", "tacos", "dim sum", "sushi"]
print(foods)
del foods[1]
print(foods)

foods = ["pizza", "tacos", "dim sum", "sushi"]
print(foods)
print(foods.pop())
print(foods)

# method of the list calls called .sort
# built in function called sorted()

#sort is in place
foods = ["pizza", "tacos", "dim sum", "sushi"]
print(foods.sort())
print(foods)
print(foods.sort(reverse = True))
print(foods)

#sorted is out of place
foods = ["pizza", "tacos", "dim sum", "sushi"]
print(sorted(foods))
print(foods)
foods = sorted(foods)
print(foods)

foods = ["pizza", "tacos", "dim sum", "sushi"]
foods.reverse()
print(foods)

foods = ["pizza", "tacos", "dim sum", "sushi"]
foods