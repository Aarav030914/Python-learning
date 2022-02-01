import pandas

data = pandas.read_csv("./day26/NATO-alphabet-start/nato_phonetic_alphabet.csv")
phonetics = {item.letter:item.code for (index, item) in data.iterrows()}


go_ahead = True
while go_ahead:
    try:
        user_word = input("Enter your word:").upper()
        word_l = list(user_word)
        result = [phonetics[key] for key in word_l]
        print(result)
        go_ahead = False
    
    except KeyError:
        print("Please enter only letters")
        continue
