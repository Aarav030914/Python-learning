alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

# Adding the cipher function    
def cipher():
    # taking inputs from the user
    directn = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
    message = input("Type your message:\n").lower()
    raw_shift = int(input("Type the shift number:\n"))
    letter_shift = raw_shift % 26
    if directn == 'encode':
        new_alphabet = []
        new_alphabet += alphabet
        del new_alphabet[0:letter_shift]
        new_alphabet+=alphabet[0:letter_shift]
        # replacing the list elements in the message_list with our set of "new_alphabets"         
        message_list = list(message)
        for i in range(0,len(message_list)):
            if message_list[i] in alphabet:
                letter_index = alphabet.index(message_list[i])
                message_list[i] = new_alphabet[letter_index]
            else:
                pass    
        # printing the encrypted message
        cipher_text = ""
        print(cipher_text.join(message_list))
    elif directn == 'decode':
        message_list = list(message)
        cipher_text = ""
        for letter in message_list:
            if letter in alphabet:
                position = alphabet.index(letter)
                new_position = position - letter_shift
                cipher_text += alphabet[new_position]
            else:
                cipher_text += letter     
        print(cipher_text)
# calling the function

restart = "yes"
while restart == 'yes':
    cipher()
    restart = input("Do you want to restart the program?(yes or no)\n")
    
