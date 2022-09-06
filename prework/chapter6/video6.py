steve = {
    "name": "Steve",
    "weight": 155.5,
    "height": 70,
    "foods": ["country fried steak", "fried chicken", "collards"],
    "ice cream": {
        "vanilla": False,
        "chocolate": True,
        "coffee": False,
    },
10: "this has an interger key"
}
print(type(steve))

#name_of_dict[KEY]

print(steve["foods"])
print(type(steve["foods"]))
print(steve["foods"][1])
print(steve["ice cream"]["vanilla"])
print(steve[10])

#You can search a dictionary for specific keys with .get("...", "if found print this")
print(steve.get("name", "Candies not found"))

my_list = [1,2,3]
my_list[1] ="WOW"
print(my_list)

#update a dictionary with .update
steve.update({
    "candies":["snickers", "mars", "m&ms"]
})

print(steve)
#Delete with del
del steve["candies"]
print(steve)

for key in steve:
    print(key)
    print(type(key))
    print(steve[key])

print(steve.values())
for value in steve.values():
    print(value)
    print(type(value))
#print(steve.items()) items print out k:v as Tups

for key,value in steve.items():
    if isinstance(value,list):
        print(f"The list is at {key}")