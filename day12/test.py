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
print(lives)    
