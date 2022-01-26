#TODO: Create a letter using starting_letter.txt 
#for each name in invited_names.txt
#Replace the [name] placeholder with the actual name.
#Save the letters in the folder "ReadyToSend".
    
#Hint1: This method will help you: https://www.w3schools.com/python/ref_file_readlines.asp
    #Hint2: This method will also help you: https://www.w3schools.com/python/ref_string_replace.asp
        #Hint3: THis method will help you: https://www.w3schools.com/python/ref_string_strip.asp
import os
os.chdir("./day23")


with open("./Mail Merge Project Start/Input/Names/invited_names.txt") as names:
    contents = names.read()
    contents_list = contents.split()


with open("./Mail Merge Project Start/Input/Letters/starting_letter.txt") as letter_format:
    letter_content = letter_format.read()

for name in contents_list:
    with open(f"./Mail Merge Project Start/Output/ReadyToSend/letter_for_{name}.txt", mode="w") as letter:
        
        place_holder = "[name]"
        replace_with = f"{name}"
        letter_content1 = letter_content.replace(place_holder, replace_with)
        letter.write(letter_content1)



        
