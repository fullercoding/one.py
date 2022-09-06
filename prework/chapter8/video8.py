#function saves code for later
# def NAME_OF_FUNCTION(parameters):
    # these lines
    # belong
    #to the code block
    # FOR THE FUNCTION

from urllib import response


def hello():
    print("hello")
hello()
#is the same as
def hello():
    return "hello"
print(hello())

def hello(name, age):
    print(f"hello {name} you are {age} years old.")

hello('connor', 27)
#same as
def hello(name, age):
    print(f"hello {name} you are {age} years old.")
hello(age = 23, name = 'connor')

#default values is when YOU put in the parameter AND HAVE TO GO AT THE END
def hello(name, age=55):
    print(f"hello {name} you are {age} years old.")
hello(name = 'connor')




def say_hello(name,age):
    print(f"hello {name} you are age {age} years old")

def say_goodbye():
    print("Goodbye")

def greet_back(feeling):
    if feeling == "good":
        print("Awesome I feel good too")
    elif feeling == "bad":
        print("I am so sorry.")
    elif feeling == "stressed":
        print("Coding can be hard to learn")
    else:
        print("Well, have a good day")

#Driver code

while True:
    response = input("What do you want to do? Say hello [H] say Goodbye [G] talk to me [T], quit[Q]")
    if response.lower() == 'q':
        say_goodbye()
        break
    elif response.lower() == 'h': 
        n = input("What is your name? ")
        a = input("What is your age? ")
        say_hello(n,a)
    elif response.lower() == 'g':
        say_goodbye()
    elif response.lower() == 't':
        f = input("How are you today? ")
        greet_back(f)
    else:
        print("Invalid input")

def my_function(num):
    while num < 10:
        print(num)
        if num == 6:
            return
        num +=1 
my_function(0)
