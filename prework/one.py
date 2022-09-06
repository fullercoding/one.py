#Question 1
#Write a function to print "hello_USERNAME!" USERNAME is the input of the function. 
# The first line of the code has been defined as below. def hello_name(user_name):

from ast import Num
from cgi import print_form
from operator import truediv


def hello_name(user_name):
    print("hello_" + user_name + "!" )
hello_name("USERNAME")
print("\n")

#Write a python function, first_odds that prints the odd numbers from 1-100 and returns nothing
def first_odds():
    for num in range(0,101):
     if num % 2 != 0:
        print(num)
first_odds()

#Please write a Python function, max_num_in_list to return the max number of a given list. 
# The first line of the code has been defined as below.

def max_num_in_list(a_list):
    max = a_list[0:]
    for num in a_list:
        max = num
    return max
print(max_num_in_list([500,5000,111,44,27,10000,1000001]))

# Write a function to return if the given year is a leap year. A leap year is divisible by 4, 
# but not divisible by 100, unless it is also divisible by 400. 
# The return should be boolean Type (true/false).

#!!!!!STUCK on line 37, come back, figure out division issue!!!!!
def is_leap_year():
    print(2012 % 4)
    if 2014 % 4 == 0:
        print (True)
    if 2014 % 100 != 0:
        print (False)
    elif 2014 % 400 == 0:
        print (False)
print(is_leap_year()) 

# Write a function to check to see if all numbers in list are consecutive numbers. 
# For example, 
# [2,3,4,5,6,7] are consecutive numbers, 
# but [1,2,4,5] are not consecutive numbers. The return should be boolean Type.

#Incomplete, I've seen this before, but cannot find resource
def is_consecutive(a_list):
    for list in range[:20]:
       if a_list +1:
        return True
    else:
            return False
is_consecutive()
    