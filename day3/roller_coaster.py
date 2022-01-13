# It will ask you your height 
# And then it will ask you wetherr you want a picture of you or not
print("Welcome to the roller coaster ride")
height = int(input("What is your height(cm)?:\n"))
age = int(input("What is your age?:\n"))

total_price = 0
if height >= 120:
    print("you can ride the roller coaster")
    if age <= 12:
        total_price += 5
    elif 12< age <= 18:
        total_price += 7
    elif 45 <=age <= 55:
        total_price += 0 
    else:
        print("Sorry, you cannot ride the roller coaster")      
drinks = input("Do you want a drink?(type 'yes' or 'no')\n")
if drinks == "yes":
    total_price += 3

else:
    print("You cannot ride the roller coaster")
print(f"Your ticket price is {total_price}$")                
        