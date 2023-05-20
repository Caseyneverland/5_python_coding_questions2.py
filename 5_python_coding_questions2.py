#QUESTION 1/example 1, using string concatenation:
def hello_name(user_name):
    print("Hello_" + user_name + "!")

hello_name("Casey")    

#example 2, using f-string formatting
def hello_name(user_name):
    print(f"hello_{user_name}!")

hello_name("Casey")

#example 3, using the 'format" method of strings:
def hello_name(user_name):
    print("hello_{}!".format(user_name))

hello_name("Casey")

#example 4, using the interpolation with the '%' operator:
def hello_name(user_name):
    print("hello_%s!" % user_name)

hello_name("Casey")

#in all of these variations, the 'hello_name' function takes 'user_name!'
#as input and prints the formatted string "hello_USERNAME!" where 'USERNAME'
#is the provided 'user_name'
#the output is hello_Casey!


#QUESTION 2/example 1: Using a for loop and a conditional check.
def first_odds():
    for number in range(1, 101):
        if number % 2 != 0:
            print(number)

first_odds()

#example 2:using the comprehension and 'join' function to print the numbers:
def first_odds():
    odds = [str(number) for number in range(1, 101) if number % 2 != 0]
    print("\n".join(odds))

first_odds()    

#example 3:using a while loop:
def first_odds():
    number= 1
    while number <= 100:
        print(number)
        number += 2

first_odds()
#the output is 1, 3, 5, 7, 9, 11, and all the way to 99. odd numbers only

#in all these variations, the 'first_odds' function prints the odd numbers from 1-100.
#the first two methods use a for loop or list comprehension to iterate over the range of numbers
#and check if each number is odd. The third method uses a whike loopp and increments 
#the number by two in each iteration to ensure only odd numbers are printed.
#you can call the function by simply invoking 'first_odds()':


#QUESTION 3/ Example 1: using a loop to find the maximum
def max_num_in_list(a_list):
    max_num = a_list[0]
    for num in a_list:
        if num > max_num:
            max_num = num
    return max_num

numbers = [4, 9, 2, 7, 5]
max_num = max_num_in_list(numbers)
print(max_num)


#example 2: using the 'max()' function with a key argument
def max_num_in_list(a_list):
    return max(a_list, key=lambda x: x)

numbers = [4, 9, 2, 7, 5]
max_num = max_num_in_list(numbers)
print(max_num)


#example 3:using the 'reduce' functiuon from the 'functools' module
from functools import reduce

def max_num_in_list(a_list):
    return reduce(lambda x, y: x if x > y else y, a_list)

numbers = [4, 9, 2, 7, 5,]
max_num = max_num_in_list(numbers)
print(max_num)

#example 4: using the 'sorted()' function to sort the list in descending order
#and returning the first element.
def max_num_in_list(a_list):
    sorted_list = sorted(a_list, reverse=True)
    return sorted_list[0]

numbers = [4, 9, 2, 7, 5]
max_num = max_num_in_list(numbers)
print(max_num)

#example 5: using a list comprehension with the 'max()' function
def max_num_in_list(a_list):
    return max([num for num in a_list])

numbers = [4, 9, 2, 7, 5]
max_num = max_num_in_list(numbers)
print(max_num)

#these are just a few of the ways to write the max_num_in_list function.
# #eacxh variation achieves the goal of finding the maximum number from a given 
# #list and returning it. 

#question 4: example 1, using logical operators
def is_leap_year(a_year):
    if a_year % 4 == 0 and (a_year % 100 != 0 or a_year % 400 == 0):
        return True
    else:
        return False

year = 2024
print(is_leap_year(year))
  
#Example 2: def is_a_leap_year(a-tear):
def is_leap_year(a_year):   
    return True if a_year % 4 == 0 and (a_year % 100 != 0 or a_year % 400 == 0) else False

year = 2024
print(is_leap_year(year))

#example 3: using a single return statement
def is_leap_year(a_year):
    return a_year % 4 ==0 and (a_year % 100 != 0 or a_year % 400 == 0)

year = 2024
print(is_leap_year(year))

#example 4:using a nested if_else statement
def is_leap_year(a_year):
    if a_year % 100 != 0 or a_year % 400 == 0:
        return True
    return False
year = 2024
print(is_leap_year(year))

#the variations of the 'is_leap_year' function all follow the logic that a leap 
#year is divisble by four, but not divisble by 100 ,unless it is also divisble by 400.
# The function returns 'True' if the given year is a leap year and 'False' otherwise. 


#question 5: Example 1 using a loop and range
def is_consecutive(a_list):
    n = len(a_list)
    if n <= 1:
        return True
    for i in range(1, n):
        if a_list[i] != a_list[i-1] + 1:
            return False
        return True
    
numbers = [2, 3, 4, 5, 6, 7]
print(is_consecutive(numbers))

#example 2: Using the 'all()' function with a list comprehension
def is_consecutive(a_list):
    return all(a_list[i] == a_list[i-1] + 1 for i in range(1, len(a_list)))

numbers = [2, 3, 4, 5, 6, 7]
print(is_consecutive(numbers))

#Example 3: using thge 'zip()' function with slicing
def is_consecutive(a_list):
    return all(a == b + 1 for a, b in zip(a_list[1:], a_list))

numbers = [2, 3, 4, 5, 6, 7]
print(is_consecutive(numbers))

# each example give achieves the same goal of checking if all numbers
#in the list are consecutive. they compare each element with the previous element
#in different ways to determine if they form a consecutive sequence.