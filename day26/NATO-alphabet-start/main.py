import pandas

data = pandas.read_csv("./day26/NATO-alphabet-start/nato_phonetic_alphabet.csv")
phonetics = {item.letter:item.code for (index, item) in data.iterrows()}

user_word = input("Enter your word:").upper()

result = {letter:phonetics[letter] for letter in list(user_word)}
print(result)
