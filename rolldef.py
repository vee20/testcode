print("Weicome To Rolling Two Fair Dice Game!")
from random import randint

#User's Details!
user_name =input("Please, enter your name: ")
def permission():

    #Premission To Play Or Not Play
    Permission =input(" Do you want to play roll the dice game or exit the game?\n Type YES/NO to make your choice: ")
    Permission = Permission.upper()
    if Permission == "NO":
       print("Please, exit game")
       exit()
    elif Permission == "YES":  
       print(f" welcome {user_name}, you can proceed: ")
    else: 
       print("You entered an invalid statement.\n The game will now exit!")
       exit()
permission()
#Start Game!
print(f"{user_name}, to begin the game you need double six")


def rollDice():
    print("Rolling dice")

#The outcome!
count = 3
rollDice()  
while count > 0:
    
    die_roll_1 = randint(1,6)
    die_roll_2 = randint(1,6)
    print(f"You rolled{die_roll_1} and {die_roll_2}")
    count = count - 1
    if die_roll_1 ==6 and die_roll_2 ==6:
      print(f" Thumbs up!{user_name}, you rolled double six\n You can proceed")
      exit()
    else:
      if count == 0:
        print("We are sorry! You cannot proceed!")
        

   
