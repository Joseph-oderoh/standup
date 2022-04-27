#!if statements
# height = 74 # The unit is inches
# if height > 70 :
#     print("You are really tall")


# height = 68 # inches
# if height > 70 :
#     print("You are really tall")
# elif height > 60:
#     print("You are avarage height ")
# else:
#     print("You are really short")

# name = ""
# list_a = [1,12]

# if list_a:
#     print("I will not run")
# else:
#         print("I am Empty")
#!loops
# numbers = [1,2,3,4,5,6]
# for number in numbers:
#   print(number)

# list_b = list(range(0,10))
# print(list_b)

# for i in range(0,8):
#     print("I would like " + str(i) + "cookies")


# numbers = [1,2,3,4,5]
# for i in numbers:
#     if i  % 2 == 0:
#         print(i)
#! while loops run untill a certian condition is met
# players = 5

# while players >= 5 :
#     print("The remaining players are",players)
#     players -= 1
#! breack statement  = The break statement allows code to jump out of a loop whenever a certain condition has been met.


# number = 0
# while True:
#     print("I love candy " + str(number))
#     number +=1
#     if number == 7 :
#         break
# '''
# in a team of members 20, some numbers are taken
# and want to display the numbers that are not taken
# so others don't pick the picked numbers
# '''

# # taken numbers
# numTaken = [3,5,7,11,13]

# print("Available numbers")

# # loop
# for i in range(1,21):
#     if i in numTaken:
#         continue
#     print(i)

# print = ("What is your name?")
# name = input("Joseph")

# print("How old are you?")
# age = int(input(22))
# print(name)
# print(age)

# import sys
# name = sys.argv[1]
# print("How old are you?")
# age = int(input(22))
# print(name)
# print(age)
#!listing in lists
# list_a = ["a","b","c","d"] # list of strings
# list_b = [1,2,3,4,5,6] # list of numbers
# list_c = [1,"west",34,"longitude"] # mixed list
# print(list_a)
# print(list_b)
# print(list_c)
#!extending into an list
# list_a = ["a","b","c","d"]
# list_b = [1,2,3,4,5,6]

# # Joining list_b to list_a

# list_a.extend(list_b)

# print(list_a) # this will print ["a","b","c","d",1,2,3,4,5,6]
# print(list_b) # this will print [1,2,3,4,5,6]
# #!appeend
# list_a = ["a","b","c","d"]

# print(list_a)  # ["a","b","c","d"]

# list_a.append("e")

# print(list_a) # ["a","b","c","d","e"]

# #!reverc
# list_a = ["a","b","c","d"]
# list_a.reverse()

# print(list_a) # ['d', 'c', 'b', '

# #!
# print("Enter a string")

# input_string = input()

# characters = {}
# print("Enter a string")

# input_string = input()

# characters = {}

# for character in input_string:
#     characters.setdefault(character,0)

# print("Enter a string")

# input_string = input()

# characters = {}

# for character in input_string:
#  characters.setdefault(character,0)
# characters[character] = characters[character] + 1

# print(characters)

# name = "James"
# age = 19

# print(f"My name is {name} and I am {age} years old")

# print(r'Beyonce\'s lemonade stand')


#! Is x string methods
# ?isalpha() - returns True if the string consists of letters only and is not blank
# *isalnum() - returns True if the string consists of numbers and letters and is not blank
# TODO isdecimal() - returns True if the string contains only numeric characters
# !isspace() - returns True if the string contains only space,tabs or new lines
# ?istitle() - returns True if the string contains words that start with uppercase letters

# alpha = "Ilikeoldmusic"
# password = "K34jndnks"
# number_string = "12345"
# tabbs = "       "
# titles = "I Love Cups"
# false_titles = "I love Cups"

# print( alpha.isalpha() )
# print( password.isalnum() )
# print( number_string.isdecimal() )
# print( tabbs.isspace() )
# print( titles.istitle() )
# print( false_titles.istitle())

# name = "James"
# age = 19
# weight = '79' # Kilograms

# age_weight_ratio = int(weight)/age

# print(age_weight_ratio)

# greetings = 'Hello, Moringa!'

# part_one = greetings[-8:-1]
# print(part_one)

# def fun_a ():
#     print("I have been callesd")
# fun_a()

# def get_age():
#     print("How old are you ")
#     try:
#         age = int(input())
#         return age
#     except ValueError:
#         return "That was not a valid input"

# for fizbuzz in range(1,100):
#     if fizbuzz % 15 == 0:
#         print("FizBuzz")
#         continue

#     elif fizbuzz % 3 == 0:    
#         print("Fizz")
#         continue
#     elif fizbuzz % 5 == 0:
#         print("Buzz") 
#         continue
#     print(fizbuzz)          
# txt = "Hello World"[::-2]   
# print(txt)          

# def function():
# 	print("               ____                         _____  _                               ")
# 	print("              |  _ \                       / ____|| |                              ")
# 	print("              | |_) )  ____  ___   ___    / ____  | |__    _____  _ _  ____        ")
# 	print("              |  __/  / _  |/ __  / __    \___  \ |  __)  /  _  \| '_|/ __ \       ")
# 	print("              | |    / (_| |\__ \ \__ \    ___  / | |___ (  (_)  ) | |  ___/       ")
# 	print("              |_|    \_____| ___/  ___/   |____/  |_____) \_____/|_|  \____        ")
# function()

# from unittest import result


numbers = [1, 2, 3, 4, 5, 6, -3, -7, -29]

# def numberThing(numbers):
positives = 0
sums = 0
result = []
for i in numbers:
        if i > 0:
            positives += 1

        elif i < 0:
            sums += i

    # result.append(positives)
    # result.append(sums)
print(result)   