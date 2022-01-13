#all modules

import random
#all the characters listed down
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']
#the console part
print("Welcome to the PyPassword Generator!")
nr_letters= int(input("How many letters would you like in your password?\n")) 
nr_symbols = int(input("How many symbols would you like?\n"))
nr_numbers = int(input("How many numbers would you like?\n"))
password = ""
#choosing letters
for i in range(1,nr_letters+1):
    random_int = random.randint(0,len(letters)-1)
    password += letters[random_int]
#choosing symbols        
for i in range(1,nr_symbols+1):
    random_int = random.randint(0,len(symbols)-1)
    password += symbols[random_int]
#choosing numbers        
for i in range(1,nr_numbers+1):
    random_int = random.randint(0,len(numbers)-1)
    password += numbers[random_int]
#reshuffling the obtained password 
print(''.join(random.sample(password,len(password))))    
