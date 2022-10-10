#Labration1
import random
def choose_option(The_name):
    prop_answer= False 
    while prop_answer== False : 
        print(The_name,",what is your choice?")
        user_choice= input("ROCK(1), PAPER(2), (SCISSORS(3), or end game(q or quit)")
        if user_choice== "1":
            user_choice= 1
            prop_answer= True
        elif user_choice== "2":
            user_choice= 2
            prop_answer= True
        elif user_choice== "3":
            user_choice= 3
            prop_answer= True
        elif user_choice== "q" or user_choice== "quit" :
            print("Goodbye, thank you for playing!")
            prop_answer= True  
        else :
            print("Wrong input! Please try again!")
    return user_choice

print("Welcome to the game 'ROCK-PAPER-SCISSORS'")
player_name= input("Enter your name, please: ")
playing= True
while playing== True:
    user_choice = choose_option(player_name)
    comp_choice = random.randint(1,3)
    # 1= Rock, 2= PAPER, 3= SCISSORS
    if user_choice == 1 :
        if comp_choice== 1 :
            print("None is the winner of the game! ")
            print("Computer has ROCK")
        elif comp_choice== 2 :
            print(" Computer is the winner of the game!")
            print("Computer has PAPER")
        elif comp_choice== 3 :
            print(player_name,"is the winner of the game!")
            print("Computer has SCISSORS")
    elif user_choice== 2 :
        if comp_choice== 1:
            print( player_name, "is the winner of the game!")
            print("Computer has ROCK")
        elif comp_choice== 2:
            print("None is the winner of the game! ")
            print("Computer has PAPER")
        else :
            print("Computer is the winner of the game!")
            print("Computer has SCISSORS")
    elif user_choice== 3 :
        if comp_choice== 1 :
            print("Computer is the winner of the game!")
            print("Computer has ROCK")
        elif comp_choice== 2 :
            print(player_name, "is the winner of the game!")
            print("Computer has PAPER")
        else :
            print("None is the winner of the game!")
            print("Computer has SCISSORS")
    elif user_choice== "quit" or user_choice== "q":
        playing= False