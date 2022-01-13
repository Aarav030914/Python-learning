import random
import hangman_art
import hangman_words

#choosing a random word
choosen_word = random.choice(hangman_words.word_list)

#hangman logo
print(hangman_art.logo)

#remove this code later
print(choosen_word)

#This is what the user will see
display = []
for i in range(0,len(choosen_word)):
    display.append("_")
print(display)    

lives = 6
print(hangman_art.stages[lives])

#will prompt the user to keep typing the letters until no blank "Underscore is left"
while "_" in display:
    
    #checking whether the choosen_word contains the guessed letter
    user_guess = input("Guess a letter in the word:").lower()
    choosen_word_list = list(choosen_word)
    
    # checking whether the word has already been guessed
    if user_guess in display:
      print(f"you have already guessed {user_guess}")
    else:

      
      if user_guess in choosen_word_list:
          print("Right")
          for position in range(len(choosen_word_list)):
              
              #ammending the display
              if choosen_word_list[position] == user_guess:
                  display[position] = user_guess
              else:
                  pass                
      
      else:
          print("wrong")
          lives -= 1
          print(f"You have {lives} live(s) remaining.")
          # completing the hangman picture
          print(hangman_art.stages[lives])        
          if lives == 0:
              print("Game Over")
              exit(0)
      print(display)





