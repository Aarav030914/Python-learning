#This is a love calculator
name1 = input("Your name:").lower()
name2 = input("Their name:").lower()
#TRUE
name = name1 +name2
tens_digit = str(name.count('t')+name.count('r')+name.count('u')+name.count('e'))
ones_digit = str(name.count('l')+name.count('o')+name.count('v')+name.count('e'))
score = int(tens_digit+ones_digit)
if score <10 or score> 90:
    print(f"Your score is {score},you go together like coke and mentos.")
elif 40 <= score <= 50:
    print(f"Your score is {score}, you are alright together.")
else:
    print(f"Your score is {score},you both should seperate out" )
        





