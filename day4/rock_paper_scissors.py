import random
rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''
paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''
scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''
moves = [rock,paper,scissors] # this is the list of moves
user_move_string = input("what is your move? rock,paper or scissors:")
if user_move_string == 'rock':
    print('your move')
    print(rock)
    user_move = rock
elif user_move_string =='paper':
    print('your move')
    print(paper)
    user_move = paper
elif user_move_string == 'scissors':
    print('your move')
    print(scissors)
    user_move = scissors
else:
    print('please enter a valid move')
    
computer_input = random.randint(0,2)
computer_move = moves[computer_input]
print("Computer's move")
print(computer_move)
if computer_move == user_move:
    print("It's a draw")
elif computer_move == rock and user_move == paper:
    print('you win')
elif computer_move == rock and user_move == scissors:
    print("you loose")
elif computer_move == paper and user_move == scissors:
    print('you win')
elif computer_move == scissors and user_move == paper:
    print('you loose')
elif computer_move == paper and user_move == rock:
    print('you loose')
elif computer_move == scissors and user_move == rock:
    print('you win')


