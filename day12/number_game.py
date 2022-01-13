#Print the ASCII Art logo
import asciiart
print(asciiart.logo)
#Choose the random number between 1 and 100
import random
random_number = random.randint(1,100)
#Ask the user for easy, medium, hard level
difficulty = input("Choose the difficulty HARD, MEDIUM or EASY:").lower()
#hard = 5, medium = 7, easy = 10
if difficulty == 'hard':
    lives = 5
elif difficulty == 'medium':
    lives = 7
elif difficulty == 'easy':
    lives = 10
else:
    print("Write a valid difficulty")
    exit(0)            
#create a function which takes care of the guesses. Whether the guess is too high or too low.
guess = False
while lives > 0 and guess == False:
    print(f"You have {lives} lives remaining to guess the number")
    user_guess = int(input("Guess the number:"))
    if user_guess < random_number:
        print("Too low")
        lives -= 1
    elif user_guess > random_number:
        print("Too High")
        lives -= 1
    elif user_guess == random_number:
        print("You got it!")
        guess = True
if lives == 0:
    print("You loose")
    print(f"The number is {random_number}")                