import random
#all the characters listed down
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

nr_letters=  random.randint(2, 5)
nr_symbols = random.randint(2, 5)
nr_numbers = random.randint(2, 5)
def generate():
    password = []

    #choosing letters
    for i in range(1,nr_letters+1):
        random_int = random.randint(0,len(letters)-1)
        password.append(letters[random_int])

    #choosing symbols        
    for i in range(1,nr_symbols+1):
        random_int = random.randint(0,len(symbols)-1)
        password.append(symbols[random_int])

    #choosing numbers        
    for i in range(1,nr_numbers+1):
        random_int = random.randint(0,len(numbers)-1)
        password.append(numbers[random_int])

    #reshuffling the obtained password 
    random.shuffle(password)
    new_tuple = tuple(password)
    return "".join(new_tuple)   
