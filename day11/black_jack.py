# distributed cards to user and computer
import random
cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
your_cards = random.sample(cards, 2)
your_total = your_cards[0] + your_cards[1]
computer_card = random.sample(cards, 1)
computer_total = computer_card[0]

# Whoever get the blackjack wins the game
def check_blackjack():
    if computer_total == 21:
        print("Computer wins the game")
    else:
        if your_total == 21:
            print("You win")
            exit(0)
            
        else:
            pass

def current_info():
    print(f"your cards:{your_cards}, current score:{your_total}")
    print(f"Computer's hand: {computer_card}")

def choose_a_card(user_card, user_total):
    hit = input("Whether you want to choose another card or not?(y/n)")
    if hit == 'y':
        hit_choice = random.choice(cards)
        if hit_choice == 11 and user_total > 10:
            hit_choice -= 10
        user_total += hit_choice
        user_card.append(hit_choice)
        current_info()

    else:
        pass

def check_total(user_total):
    if user_total > 21:
        print(f"{user_total} lost")
        exit(0)

current_info()
check_blackjack()
check_total(your_total)
choose_a_card(your_cards, your_total)

while computer_total < 16:
    computer_choice = random.choice(cards)
    computer_card.append(computer_choice)
    computer_total += computer_choice    
check_total(your_total)
check_total(computer_total)
if your_total < computer_total:
    print("you lose")
elif your_total == computer_total:
    print("Draw")
else:
    print("You Win")     




