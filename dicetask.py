print("**Welcome To Number Gussing Game**")
#Import the needed classes!
from random import randint

#Activate user input!
user_name= input(" Please enter your name: ")
user_number= input("Please enter a number betwee 1 and 6: ")
user_number= int(user_number)
random_number= randint(1,6)
list_of_numbers=[1,2,3,4,5,6]

#Check if user input is valid
if user_number in list_of_numbers:
    print("Thank you!")
    print(f"The number the computer chose is {random_number}")
#Check if the user guessed correctly
while user_number != random_number:
    print("Try again!")
    user_number= input(f"{user_name}, please enter a number between 1 and 6: ")
    user_number= int(user_number)
    continue
print(f"Congratulations {user_name}")

