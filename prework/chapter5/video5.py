#Boolean can be two things ON or OFF | True or False
# 0 is always False 1 is always True
#print(bool(" ")) is False (empty string is False)
#Empty list are False, filled list are True

letter = "A"
print(ord("a"))
print(ord("b"))
print(letter < "B")
print("\n")

x = 8
y = 9
print(x == y)
print("\n")

height = 75

#must be 5ft tall to ride
#must be under 6ft tall

if height < 60:
    print("You are too short")
    print("I am sorry but get off the ride")
elif height > 72:
    print("You are too tall")
    print("Please get off the ride")
else:
     print("Enjoy the ride.")
print("Thank you for visiting")

