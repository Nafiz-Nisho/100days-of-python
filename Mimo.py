
# colon : is call indented line/blocks 

# What is argument?
# example: 
# def info(age , roll):
#   return age + roll

# how to call argument for example
# print(info("18" ,"122743" [This called Argument > ] ))


# password = 980790
# old_password = "8lk29"

# print(str(password) == old_password)

# print(type(password))
# print(type(old_password))
# my_number = 44.44
# print(int(my_number))

# memeber = 13
# co_member = 12

# print(bool(memeber))
# print(co_member)

# detail = ""
# response = bool(detail)
# print(response)

# how to use F string.

# Ullapara_sceince_collage = 1997
# student = 2500
# EINN = 17747

# print(f" institute: {Ullapara_sceince_collage} Ability {student} Licence {EINN} ")


# names = "NAFIZ"
# age = 19

# print(f" {names} + {age}")

# movie = "Vertigo"
# display = f"Airing tonight : {movie}"
# print(display)


# id_name = "jubayer ahmed shimanto"
# enter_id = "jubayer ahmed shimanto"
# result = id_name ==  enter_id
# print(result)

# Conditional Statement
# exam = False
# if exam:
#     print("Thank for help Me")

# Quiz APP in if statement

# What is Name Capital in Bangladesh

# Answare = "Dhaka"
# if Answare == "Dhaka":
#     print(Answare + " is currect!")
 

# conditional statment

# NowTime = 17
# time = NowTime
# if time < 9:
#     print("Good morning")
# elif time < 12:
#     print("Good Afternoon")
# elif time > 12:
#     print("Good Night")

# NowTime = 9
# time = NowTime
# if time <9:
#     print("Good Morning")
# elif time <12:
#     print("Good Afternoon")

# while Loop

# while True:
#     print("try again")

# My_ID = True

# while My_ID:
#     print("Acesses done!")
#     # how stop looping
#     My_ID = False


# controling while loop

# counter = 1
# while counter < 10:
#     counter += 1
#     print(counter)

# FOR LOOP

# for loop esier then while loop

# for name in range(4):
#     print("select your name")


# # How to stop the Loop in infinity

# distant_LastPlace_univers = True
# while distant_LastPlace_univers:
#     print("we are going!")
#     distant_LastPlace_univers = False


# For loop Project
# password chacking for any company!

# password_length = 6
# counter = 1
# permutations = 1
# while counter <= password_length:
#   permutations *= counter 
#   counter += 1
# print(f"The possible combination of a {password_length}-character password is: {permutations}")
# attempts = 5
# max_lock = permutations/attempts
# max_lock = int(max_lock)
# print(f"The maximum number of times the account might be locked is {max_lock} times.")
# locks = 0
# total_lock_time = 0
# lock_time_multiplier = 5
# for i in range (max_lock):
#     locks += 1
#     total_lock_time += lock_time_multiplier * locks
#     print(f"Your account is locked for {lock_time_multiplier*locks} minutes")
    
# print(f"Assuming the hacker only got the password right with the last possible combination, your account would have been locked for {total_lock_time} minutes in total.")

# Listing & Updating List : 

# # Make list
# food = ["orange" , "apple" , "mango"]
# print(food)

# # output: orange', 'apple', 'mango'

# # Add list
# food = ["orange" , "apple" , "mango"]
# food.append("cherry")
# print(food)

# # output : 'orange', 'apple', 'mango', 'cherry'

# # Insert 
# food = ["orange" , "apple" , "mango"]
# food.insert(0, "banana")
# print(food)

# # output: 'banana', 'orange', 'apple', 'mango'

# # Pop "Remove elements"
# food = ["orange" , "apple" , "mango"]
# food.pop(0)
# print(food)

# output: 'apple', 'mango

# deciding in list

# how to chacking length in python
# words = ["a ", "b", "c" ]
# words = len(words)
# print(words)

# # output = 3

# # using condition

# words = ["a ", "b", "c" ]
# if len(words) > 2:
#     print("3")

# LIST: CHALLENGE

# food = ["chicken" , "egg and bret"]
# print(f"Breakfast : {food[1]}")
# # Output : egg and bret
# # but
# # Change food in list
# food[1] = "biriyani"
# print(f"Breakfast : {food[1]}")


# LIST : CHALLENGE 2
# shopping_list = ["dish soap", "kleenex", "batteries", "aluminum foil", "pet food", "toothpaste", "lightbulbs"]
# for item in shopping_list:
#  print(f"Don't forget to buy {item}!")


 # for burger shop

# person_name = "nafiz ahmed nisho"
# food = "burger"
# value2 = 9

# nafiz_with_value = person_name + str(value2)

# print(f"shop name : {nafiz_with_value}")

# # for length
# print(f"length of name : {len(nafiz_with_value)}")


# finding extreme data

# To find the bigger Number in max()

# scores = [3, 6, 1, 12]
# print(max(scores))
# output = 12

# To find the smallest number in min()
# scores = [27 , 123 , 1]
# print(min(scores))
# # output = 1

# Sorted lists 
# scores = [3, 6, 1, 12]
# scores.sort()
# print(scores)
# output = [1, 3, 6, 12]

# summing data

# To calculate the total of a list, in sum()

# Jun_users = [10 , 20 , 40]
# total = sum(Jun_users)
# print(total)
# # output = 70

# Joing List
# To join 2 datasets in + operator.

# dataset_1 = [1, 2, 3]
# dataset_2 = [4, 5]
# print(dataset_1 + dataset_2)
# output = [1, 2, 3, 4, 5]

# Counting Elements in count()
# answers = ["yes", "no", "sometimes", "yes", "no"]
# print(answers.count("yes"))
# output = 2

# keyword for in
# grocery = ["apple" , "orange" , "banana"]
# matching_food = "cherry" in grocery
# print(matching_food)
# Output = False

# PROJECT : Plant Growth Analysis

# growth = [3, 1, 2, 4, 2, 3, 2]
# growth.sort()
# smallest_growth = growth[0]
# print(f'The smallest growth in the week is: {smallest_growth}cm')
# biggest_growth = growth[len(growth) - 1]
# print(f'The biggest growth in the week is: {biggest_growth}cm')
# average_growth = sum(growth) / len(growth)
# print(f'The average growth in the week is: {average_growth}cm')
# new_growth = [2, 0, 3, 2, 4, 5, 4]
# joined_growth = growth + new_growth 

# joined_smallest_growth = min(joined_growth)
# print(f'The smallest growth in these 2 weeks is: {joined_smallest_growth}cm')
# joined_biggest_growth = max(joined_growth)
# print(f'The biggest growth in these 2 weeks is: {joined_biggest_growth}cm')
# joined_average_growth = sum(joined_growth) / len(joined_growth)
# print(f'The average growth in these 2 weeks is: {joined_average_growth}cm')

# joined_smallest_growth_count = joined_growth.count(joined_smallest_growth)
# print(f'The smallest growth happened {joined_smallest_growth_count} times in these 2 weeks')

# joined_biggest_growth_count = joined_growth.count(joined_biggest_growth)
# print(f'The biggest growth happened {joined_biggest_growth_count} times in these 2 weeks')

# Slitting String in split()

# # Example = 1
# url = "facebook.com/nafiz.nisho19"
# MakeSplit = url.split("/")
# print(MakeSplit)
# # output : 'facebook.com', 'nafiz.nisho19

# # Updating Strings in replace()

# # Example : 1
# monthly = "Monthly reduction is 25%"
# monthly = monthly.replace("25%","15%")
# print(monthly)
# # output : Monthly reduction is 15%

# # Example = 2
# tags = ".code .today"
# hash_tag = tags.replace(".", "#")
# print(hash_tag)
# # output : #code #today

# # Using Strings 

# # Example : 1

# names = "Sorry??"
# update = names.replace("Sorry??" , "Sorry!!")
# print(update)
# # output : Sorry!!

# Project : Electroincs store

# data = "14inch l@ptop,699|16inch l@ptop,999|sm@rtphone,1099|t@blet,499|g@ming pc,1999"

# device_list = data.split("|")
# formatted_list = []
# for device in device_list:
#  device_info_list = device.split(",")
#  name = device_info_list[0]
#  price = int(device_info_list[1])
#  new_price = int(price * 1.1);
#  formatted_device = f"Device Name: {name}, Device Price: ${price}"
#  corrected_formatted_device = formatted_device.replace("@" , "a")
#  formatted_list.append(corrected_formatted_device)
#  print(formatted_list)

# FUNCTION 

# Reusing Code with Functions
def Al_nsser():
    print("Live Now")
Al_nsser()
# output: Live Now

# Creating Parameters

# structure
def greet(name):
  print(f"Hello, {name}")
# func call
greet("Nisho")
# output: Hello Nisho

# example : 2
def user_status():
  username = "habib"
  status = "active"
  print(f" {username} is {status}")
user_status()

# # Returning Values

def age_label(age):
  label = "User age: " + age
  return label
print(age_label("22"))
# user age 22

# # Using Multiple Parameters
def display(first,last):
  print(first + " " + last)
display("Alex", "Morgan")

# Understanding Functions
def get_final_price(price , tax , discount):
  return price + tax - discount

Apex_shoes = get_final_price(10 , 5 , 3)
print(f" Price : {Apex_shoes}")
# output : 12

# function and scope

def apply_discount(price):
  discount = 20
# this is called scope
  discount = 10
  return price - discount

final_price = apply_discount(50)
print(final_price)
# output = 40

# Functions and Variable Scope

# Gloabal scope >
avarage_age = 100
def future_age(less):
  # Local scope >
  accident_age = 10
  return avarage_age - less - accident_age
find_age = future_age(30)
print(find_age)
# output = 60


# Deciding with Functions
def total_cart(cart):
  if cart < 100:
    gift_card = 20
    return cart + gift_card
  else:
    print("not available")
  
My_shopping_cart = 50
gift_With_card = total_cart(My_shopping_cart)
print(gift_With_card)
# output = 70

# function with list

# using index[] in function
# example : 1 
def get_winner(top_players):
  winner = top_players[0]
  print(f"Game winner: {winner}")

top_players = ["Jay", "Meg", "Cy"]
get_winner(top_players)
# output: Game winner: Jay
