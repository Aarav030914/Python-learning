# Importing necessary modules
import os
from art import logo
from art import vs
from game_data import data
import random
#decide a score
score = 0

### use a while loop for this task
correct_guess = True
while correct_guess:

    ## Select two random people
    compair_people = random.sample(data,2)

    # Print the initials of the game
    print(logo)
    print(f"Your current score is {score}")
    print(f"A:{compair_people[0]['name']} is a {compair_people[0]['description']} from {compair_people[0]['country']}")
    print(vs)
    print(f"B:{compair_people[1]['name']} is a {compair_people[1]['description']} from {compair_people[1]['country']}")

    #decide the winner
    winner = max(compair_people[0]['follower_count'], compair_people[1]['follower_count'])

    # take the guess from the user
    valid_input = True
    while valid_input:
        user_option = input("What is your guess A or B?")
        if user_option == 'A':
            user_guess = compair_people[0]
            valid_input = False
        elif user_option == 'B':
            user_guess = compair_people[1]
            valid_input = False
        else:
            print("Give a valid input")

        
                
    # Compare their followers
    # if correct then give the user a point and if incorrect stop the programm
    if winner == user_guess['follower_count']:        
        score += 1
        os.system('cls')
        print("You are correct")
    else:
        print("You are wrong")
        print(f"your final score is {score}")
        correct_guess = False



