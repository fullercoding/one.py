#While loop
#while boolean:
    #code block
    #to run while condition is true

# +=1 
from urllib import response


height = 55
while height < 60:
    print(f"You are {height} inches tall \n too short to ride! ")
    print("Drink a potion ")
    height += 1 

print("thanks for coming")
print("\n")


heights = int(input("What is your height in inches?: "))
while heights < 60:
    heights += 1 
    if heights < 58 :
        continue
    print(f"You are {heights} inches tall \n too short to ride! ")
    print("Drink a potion ")
    
    if heights == 58:
        break

#while True
#useful for games

while True:
    response = input(" What do you want to do? Say hi [h], Say Goodbye [g] or quit?[q] ")
    if response.lower() == 'h':
        print("hello")
    elif response.lower() == 'g':
        print("goodbye")
    elif response.lower() == 'q':
        break
    else:
        print("invalid option")